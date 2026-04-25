from carparser import detect_model, detect_fuel, detect_intent
from cars import cars

def ask(query):

    model = detect_model(query)
    fuel = detect_fuel(query)
    intent = detect_intent(query)


    series = cars["BMW"]["3_series"]


    if not model:
        return {
            "status": "ok",
            "data": series
        }

 
    if model not in series:
        return {
            "status": "error",
            "message": "Model not found",
            "available_models": list(series.keys())
        }


    data = series[model]


    if intent == "best":
        if fuel:
            return {
                "status": "ok",
                "model": model,
                "best_engine": data["best_engine"].get(fuel)
            }

        return {
            "status": "ok",
            "model": model,
            "best_engine": data["best_engine"]
        }


    if fuel:
        return {
            "status": "ok",
            "model": model,
            "engines": data["engines"].get(fuel, data["engines"]),
            "transmission": data["transmission"]
        }

    return {
        "status": "ok",
        "model": model,
        "engines": data["engines"],
        "transmission": data["transmission"]
    }