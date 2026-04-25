from carparser import detect_model, detect_fuel, detect_intent
import sqlite3

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

def ask(query):

    model = detect_model(query)
    fuel = detect_fuel(query)

    if not model:
        return {
            "status": "error",
            "message": "Please provide model (e.g. E90, F30)"
        }

    cursor.execute("SELECT DISTINCT model FROM engines")
    models = [row[0] for row in cursor.fetchall()]

    if model not in models:
        return {
            "status": "error",
            "message": "Model not found",
            "available_models": models
        }

    if fuel:
        cursor.execute("""
        SELECT name, engine_code, power
        FROM engines
        WHERE model = ? AND fuel = ?
        """, (model, fuel))
    else:
        cursor.execute("""
        SELECT name, engine_code, power
        FROM engines
        WHERE model = ?
        """, (model,))

    rows = cursor.fetchall()

    engines = []
    for row in rows:
        engines.append({
            "model": row[0],
            "engine": row[1],
            "power": row[2]
        })

    return {
        "status": "ok",
        "model": model,
        "engines": engines
    }