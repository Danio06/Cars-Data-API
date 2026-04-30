from carparser import detect_model, detect_fuel, detect_intent
from db import get_conn

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

    try:
        cursor = conn.cursor()

        search_term = f"%{model_input}%"

        cursor.execute("""
            SELECT DISTINCT model
            FROM engines
            WHERE model ILIKE %s OR series ILIKE %s
        """, (search_term, search_term))

        found_models = [r[0] for r in cursor.fetchall()]

        if not found_models:
            return {
                "status": "error",
                "message": f"Model '{model_input}' not found."
            }

        results_by_generation = {}

        for gen_model in found_models:

            # ENGINES
            if fuel:
                cursor.execute("""
                    SELECT name, engine_code, power
                    FROM engines
                    WHERE model = %s AND fuel = %s
                """, (gen_model, fuel))
            else:
                cursor.execute("""
                    SELECT name, engine_code, power
                    FROM engines
                    WHERE model = %s
                """, (gen_model,))

            engines = [
                {"model": r[0], "engine": r[1], "power": r[2]}
                for r in cursor.fetchall()
            ]

            # TRANSMISSIONS
            cursor.execute("""
                SELECT transmission_type, speeds, name
                FROM transmissions
                WHERE model = %s
            """, (gen_model,))

            transmissions = {}
            for t_type, speeds, name in cursor.fetchall():
                transmissions.setdefault(t_type, []).append({
                    "speeds": speeds,
                    "type": name
                })

            # BEST ENGINE
            best_info = None

            if intent == "best":
                cursor.execute("""
                    SELECT fuel, name, reason
                    FROM best_engines
                    WHERE model = %s
                """, (gen_model,))

                rows = cursor.fetchall()

                if fuel:
                    for r in rows:
                        if r[0] == fuel:
                            best_info = {"model": r[1], "reason": r[2]}
                else:
                    best_info = {
                        r[0]: {"model": r[1], "reason": r[2]}
                        for r in rows
                    }

            results_by_generation[gen_model] = {
                "engines": engines,
                "transmission": transmissions,
                "best_engine": best_info
            }

        return {
            "status": "ok",
            "search_query": model_input,
            "generations": results_by_generation
        }

    finally:
        conn.close()