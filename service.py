from carparser import detect_model, detect_fuel, detect_intent
import psycopg2
import os

def get_conn():
    return psycopg2.connect(os.environ["DATABASE_URL"])


def ask(query):
    model_input = detect_model(query)
    fuel = detect_fuel(query)
    intent = detect_intent(query)

    if not model_input:
        return {
            "status": "error",
            "message": "Please provide model (e.g. E90, F30, X5)"
        }

    conn = get_conn()
    cursor = conn.cursor()

    search_term = f"%{model_input}%"

    cursor.execute(
        "SELECT DISTINCT model FROM engines WHERE model ILIKE %s OR series ILIKE %s",
        (search_term, search_term)
    )

    found_models = [row[0] for row in cursor.fetchall()]

    if not found_models:
        conn.close()
        return {
            "status": "error",
            "message": f"Model '{model_input}' not found."
        }

    results_by_generation = {}

    for gen_model in found_models:

        if fuel:
            cursor.execute(
                "SELECT name, engine_code, power FROM engines WHERE model = %s AND fuel = %s",
                (gen_model, fuel)
            )
        else:
            cursor.execute(
                "SELECT name, engine_code, power FROM engines WHERE model = %s",
                (gen_model,)
            )

        engines = [
            {"model": r[0], "engine": r[1], "power": r[2]}
            for r in cursor.fetchall()
        ]

        cursor.execute(
            "SELECT transmission_type, speeds, name FROM transmissions WHERE model = %s",
            (gen_model,)
        )

        transmissions = {}
        for t_type, speeds, name in cursor.fetchall():
            transmissions.setdefault(t_type, []).append({
                "speeds": speeds,
                "type": name
            })

        best_info = None

        if intent == "best":
            if fuel:
                cursor.execute(
                    "SELECT name, reason FROM best_engines WHERE model = %s AND fuel = %s",
                    (gen_model, fuel)
                )
                row = cursor.fetchone()
                if row:
                    best_info = {"model": row[0], "reason": row[1]}
            else:
                cursor.execute(
                    "SELECT fuel, name, reason FROM best_engines WHERE model = %s",
                    (gen_model,)
                )
                rows = cursor.fetchall()
                best_info = {
                    r[0]: {"model": r[1], "reason": r[2]}
                    for r in rows
                }

        results_by_generation[gen_model] = {
            "engines": engines,
            "transmission": transmissions,
            "best_engine": best_info
        }

    conn.close()

    return {
        "status": "ok",
        "search_query": model_input,
        "generations": results_by_generation
    }