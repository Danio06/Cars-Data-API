from carparser import detect_model, detect_fuel, detect_intent
import sqlite3

def ask(query):
    model_input = detect_model(query)
    fuel = detect_fuel(query)
    intent = detect_intent(query)

    if not model_input:
        return {
            "status": "error",
            "message": "Please provide model (e.g. E90, F30, X5)"
        }

    with sqlite3.connect("cars.db") as conn:
        cursor = conn.cursor()

        search_term = f"%{model_input}%"
        cursor.execute("SELECT DISTINCT model FROM engines WHERE model LIKE ? OR series LIKE ?", (search_term, search_term))
        
        found_models = [row[0] for row in cursor.fetchall()]

        if not found_models:
            return {
                "status": "error",
                "message": f"Model '{model_input}' not found."
            }
        results_by_generation = {}

        for gen_model in found_models:
            if fuel:
                cursor.execute("SELECT name, engine_code, power FROM engines WHERE model = ? AND fuel = ?", (gen_model, fuel))
            else:
                cursor.execute("SELECT name, engine_code, power FROM engines WHERE model = ?", (gen_model,))
            
            eng_rows = cursor.fetchall()
            engines = [{"model": r[0], "engine": r[1], "power": r[2]} for r in eng_rows]

            cursor.execute("SELECT transmission_type, speeds, name FROM transmissions WHERE model = ?", (gen_model,))
            trans_rows = cursor.fetchall()
            transmissions = {}
            for r in trans_rows:
                t_type = r[0]
                if t_type not in transmissions:
                    transmissions[t_type] = []
                transmissions[t_type].append({"speeds": r[1], "type": r[2]})

            best_info = None
            if intent == "best":
                if fuel:
                    cursor.execute("SELECT name, reason FROM best_engines WHERE model = ? AND fuel = ?", (gen_model, fuel))
                    b_row = cursor.fetchone()
                    if b_row:
                        best_info = {"model": b_row[0], "reason": b_row[1]}
                else:
                    cursor.execute("SELECT fuel, name, reason FROM best_engines WHERE model = ?", (gen_model,))
                    b_rows = cursor.fetchall()
                    best_info = {r[0]: {"model": r[1], "reason": r[2]} for r in b_rows}

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