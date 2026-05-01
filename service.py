from db import get_conn
from repository.engine_repo import (
    get_all_models, get_all_series,
    get_engines, get_transmissions, get_best_engines
)
from parser.parser import parse_query

def ask(query):
    conn = get_conn()
    try:
        available_models = get_all_models(conn)
        available_series = get_all_series(conn)
        parsed = parse_query(query, available_models, available_series)

        scope = parsed["scope"]
        fuel = parsed["fuel"]
        intent = parsed["intent"]

        series = scope["value"] if scope["type"] == "series" else None
        model = scope["value"] if scope["type"] == "model" else None

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