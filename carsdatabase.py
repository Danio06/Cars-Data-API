import psycopg2
import json
import os

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def is_db_empty():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM engines")
    count = cursor.fetchone()[0]

    conn.close()
    return count == 0


def load_json_to_db():
    conn = get_connection()
    cursor = conn.cursor()

    # CREATE TABLES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS engines (
        id SERIAL PRIMARY KEY,
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
        id SERIAL PRIMARY KEY,
        model TEXT,
        fuel TEXT,
        name TEXT,
        reason TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transmissions (
        id SERIAL PRIMARY KEY,
        model TEXT,
        transmission_type TEXT,
        speeds INTEGER,
        name TEXT
    )
    """)

    # CLEAR OLD DATA
    cursor.execute("DELETE FROM engines")
    cursor.execute("DELETE FROM best_engines")
    cursor.execute("DELETE FROM transmissions")

    # LOAD JSON
    with open("datacars.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # INSERT DATA
    for brand_name, brand_data in data.items():
        for series_name, series_data in brand_data.items():
            for model, model_data in series_data.items():

                engines = model_data.get("engines", {})
                for fuel, engine_list in engines.items():
                    for engine in engine_list:
                        cursor.execute("""
                        INSERT INTO engines (series, model, fuel, name, engine_code, power)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """, (series_name, model, fuel, engine["model"], engine["engine"], engine["power"]))

                best = model_data.get("best_engine", {})
                for fuel, engine in best.items():
                    if isinstance(engine, dict) and engine.get("model") is not None:
                        cursor.execute("""
                        INSERT INTO best_engines (model, fuel, name, reason)
                        VALUES (%s, %s, %s, %s)
                        """, (model, fuel, engine.get("model"), engine.get("reason")))

                transmissions = model_data.get("transmission", {})
                for trans_type, trans_list in transmissions.items():
                    for trans in trans_list:
                        cursor.execute("""
                        INSERT INTO transmissions (model, transmission_type, speeds, name)
                        VALUES (%s, %s, %s, %s)
                        """, (model, trans_type, trans["speeds"], trans["type"]))

    conn.commit()
    conn.close()

    print("PostgreSQL DB seeded.")