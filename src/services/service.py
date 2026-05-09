from src.core.db import get_conn
from src.repository.cars_rep import (
    get_all_models, get_all_series,
    get_engines, get_transmissions, get_best_engines
)
from src.parsers.carparser import parse_query

def ask(query):
    conn = get_conn()
    try:
        available_models = get_all_models(conn)
        available_series = get_all_series(conn)
        parsed = parse_query(query, available_models, available_series)

        if "error" in parsed:
            return {
                "status": "error",
                "message": parsed["error"]
            }

        scope = parsed["scope"]
        fuel = parsed["fuel"]
        intent = parsed["intent"]

        if scope["type"] == "model":
            series = None
            model = scope["value"]
        elif scope["type"] == "series":
            series = scope["value"]
            model = None
        elif scope["type"] == "family":
            series = scope["value"] + "%"
            model = None
        else:
            series = None
            model = None

        engines = get_engines(conn, series=series, model=model, fuel=fuel)

        if not engines:
            return {
                "status": "error",
                "message": f"No results found for: {query}",
                "parsed": parsed
            }

        transmissions = get_transmissions(conn, series=series, model=model)

        best = None
        if intent == "best":
            best = get_best_engines(conn, series=series, model=model, fuel=fuel)

        grouped = {}
        for e in engines:
            m = e["model"]
            if m not in grouped:
                grouped[m] = {"engines": [], "transmission": transmissions.get(m, {}), "best_engine": None}
            grouped[m]["engines"].append({
                "model": e["name"],
                "engine": e["engine_code"],
                "power": e["power"],
                "fuel": e["fuel"]
            })
            if best and m in best:
                grouped[m]["best_engine"] = best[m].get(fuel) if fuel else best[m]

        return {
            "status": "ok",
            "search_query": query,
            "parsed": parsed,
            "generations": grouped
        }

    finally:
        conn.close()
