from cars import cars
from carparser import detect_model, detect_fuel, detect_best

def ask(query):
    model = detect_model(query)
    fuel = detect_fuel(query)
    best = detect_best(query)
#if user didnt provide series or model we give back everything
    if not model:
        return cars["BMW"]
    data = cars ["BMW"]["3_series"][model]
#if user wants only best engine we return only best ones from our data
    if best:
        if fuel:
            return {
                "best_engine": data["best_engine"][fuel],
                "transmission": data["transmission"]
            }
        return {
            "best_engine": data["best_engine"],
            "transmission": data["transmission"]
        }
#if user does not want best - we give back everything
    if fuel:
        return {
            "engines": data["engines"][fuel] if isinstance(data["engines", dict]) else data["engines"],
            "transmission": data["transmission"]
        } 
    return {
        "engines": data["engines"],
        "transmission": data["transmission"]
    }      
#if user for example asks "celica"
    if model not in cars["BMW"]["3_series"]:
        return "Model not found"  