import sqlite3
import json

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM engines")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='engines'")

cursor.execute("""
CREATE TABLE IF NOT EXISTS engines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    fuel TEXT,
    name TEXT,
    engine_code TEXT,
    power INTEGER
)
""")

with open("datacars.json", "r", encoding="utf-8") as f:
    data = json.load(f)

series = data["BMW"]["3_series"]

for model, model_data in series.items():
    engines = model_data["engines"]

    for fuel, engine_list in engines.items():
        for engine in engine_list:
            cursor.execute("""
            INSERT OR IGNORE INTO engines (model, fuel, name, engine_code, power)
            VALUES (?, ?, ?, ?, ?)
            """, (
                model,
                fuel,
                engine["model"],
                engine["engine"],
                engine["power"]
            ))

cursor.execute("SELECT model, name FROM engines")
print(cursor.fetchall())

conn.commit()
conn.close()