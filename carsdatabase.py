import sqlite3
import json

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS engines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    series TEXT,
    model TEXT,
    fuel TEXT,
    name TEXT,
    engine_code TEXT,
    power INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS best_engines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    fuel TEXT,
    name TEXT,
    reason TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transmissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    transmission_type TEXT,
    speeds INTEGER,
    name TEXT
)
""")

cursor.execute("DELETE FROM engines")
cursor.execute("DELETE FROM best_engines")
cursor.execute("DELETE FROM transmissions")

with open("datacars.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for brand_name, brand_data in data.items():
    for series_name, series_data in brand_data.items():
        for model, model_data in series_data.items():

            engines = model_data.get("engines", {})
            for fuel, engine_list in engines.items():
                for engine in engine_list:
                    cursor.execute("""
                    INSERT INTO engines (series, model, fuel, name, engine_code, power)
                    VALUES (?, ?, ?, ?, ?, ?)
                     """, (series_name, model, fuel, engine["model"], engine["engine"], engine["power"]))

            best = model_data.get("best_engine", {})
            for fuel, engine in best.items():
                if isinstance(engine, dict) and engine.get("model") is not None:
                    cursor.execute("""
                    INSERT INTO best_engines (model, fuel, name, reason)
                    VALUES (?, ?, ?, ?)
                    """, (model, fuel, engine.get("model"), engine.get("reason")))
                else:
                    print(f"Skipping best engine for {model} {fuel} - no data available.")

            transmissions = model_data.get("transmission", {})
            for trans_type, trans_list in transmissions.items():
                for trans in trans_list:
                    cursor.execute("""
                    INSERT INTO transmissions (model, transmission_type, speeds, name)
                    VALUES (?, ?, ?, ?)
                    """, (model, trans_type, trans["speeds"], trans["type"]))

conn.commit()
conn.close()
print("ETL Process finished: Database is now fully populated.")