import re

INTENT_TO_SERIES = {
    "suv":      "x",
    "x":        "x",
    "coupe":    "4_series",
    "sedan":    "3_series",
    "compact":  "1_series",
}

SERIES_ALIASES = {
    "1": "1_series",
    "2": "2_series",
    "3": "3_series",
    "4": "4_series",
    "5": "5_series",
    "6": "6_series",
    "7": "7_series",
    "8": "8_series",
    "x": "x",
    "z": "z_series",
}

def clean(q):
    return q.upper().strip()

def detect_scope(query, available_models, available_series):
    q = clean(query)
    q_lower = query.lower().strip()

    for keyword, series in INTENT_TO_SERIES.items():
        if keyword in q_lower:
            return {"type": "series", "value": series}

    for model in available_models:
        if model in q or model in q.replace(" ", ""):
            return {"type": "model", "value": model}

    series_match = re.search(r"\b([1-8])\s*(?:SERIES|_SERIES)?\b", q)
    if series_match:
        num = series_match.group(1)
        return {"type": "series", "value": SERIES_ALIASES.get(num, f"{num}_series")}

    for letter in ["X", "M", "Z"]:
        if re.search(rf"\b{letter}\b", q):
            return {"type": "family", "value": letter}

    return {"type": "all", "value": None}

def detect_fuel(query):
    q = clean(query)
    if "DIESEL" in q: return "diesel"
    if "PETROL" in q: return "petrol"
    if "ELECTRIC" in q or "EV" in q: return "electric"
    if "HYBRID" in q: return "hybrid"
    return None

def detect_intent(query):
    q = clean(query)
    if "BEST" in q: return "best"
    return "list"

def parse_query(query, available_models, available_series):
    return {
        "scope": detect_scope(query, available_models, available_series),
        "fuel": detect_fuel(query),
        "intent": detect_intent(query),
        "raw": query
    }