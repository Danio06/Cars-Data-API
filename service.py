from db import get_conn
from repository.cars_rep import find_models, get_engines, get_transmissions, get_best_engines
from carparser import detect_model, detect_fuel, detect_intent

def ask(query):
    conn = get_conn()

    try:
        model_input = detect_model(query)
        fuel = detect_fuel(query)
        intent = detect_intent(query)

        if not model_input:
            return {"status": "error", "message": "Please provide model (e.g. E90, F30, X5)"}

        found_models = find_models(conn, f"%{model_input}%")

        if not found_models:
            return {"status": "error", "message": f"Model '{model_input}' not found."}

        results_by_generation = {}

        for gen_model in found_models:
            engines = get_engines(conn, gen_model, fuel)
            transmissions = get_transmissions(conn, gen_model)

            best_info = None
            if intent == "best":
                rows = get_best_engines(conn, gen_model)
                if fuel:
                    for r in rows:
                        if r[0] == fuel:
                            best_info = {"model": r[1], "reason": r[2]}
                else:
                    best_info = {r[0]: {"model": r[1], "reason": r[2]} for r in rows}

            results_by_generation[gen_model] = {
                "engines": engines,
                "transmission": transmissions,
                "best_engine": best_info
            }

        return {"status": "ok", "search_query": model_input, "generations": results_by_generation}

    finally:
        conn.close()