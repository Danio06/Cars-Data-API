from carparser import detect_model, detect_fuel, detect_intent
import sqlite3


def ask(query):

    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()

    model = detect_model(query)
    fuel = detect_fuel(query)
    intent = detect_intent(query)

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

    if intent == "best":

        if fuel:
            cursor.execute("""
            SELECT name, reason
            FROM best_engines
            WHERE model = ? AND fuel = ?
            """, (model, fuel))

            row = cursor.fetchone()

            return {
                "status": "ok",
                "model": model,
                "best_engine": {
                    "model": row[0],
                    "reason": row[1]
                } if row else None
            }

        else:
            cursor.execute("""
            SELECT fuel, name, reason
            FROM best_engines
            WHERE model = ?
            """, (model,))

            rows = cursor.fetchall()

            best = {}
            for r in rows:
                best[r[0]] = {
                    "model": r[1],
                    "reason": r[2]
                }

            return {
                "status": "ok",
                "model": model,
                "best_engine": best
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

    cursor.execute("""
    SELECT transmission_type, speeds, name
    FROM transmissions
    WHERE model = ?
    """, (model.upper(),))

    rows = cursor.fetchall()

    transmissions = {}

    for row in rows:
        t_type = row[0]

        if t_type not in transmissions:
            transmissions[t_type] = []

        transmissions[t_type].append({
            "speeds": row[1],
            "type": row[2]
        })

    conn.close()

    return {
        "status": "ok",
        "model": model,
        "engines": engines,
        "transmission": transmissions
    }