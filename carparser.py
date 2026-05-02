import re

INTENT_TO_SERIES = {
    "suv": {"type": "family", "value": "X"},
    "x":   {"type": "family", "value": "X"},
    "coupe": {"type": "series", "value": "4_series"},
    "sedan": {"type": "series", "value": "3_series"},
    "compact": {"type": "series", "value": "1_series"},
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
}

def clean(query):
    return query.upper().strip()

def detect_scope(query, available_models, available_series):
    q = clean(query)
    q_lower = query.lower().strip()

    for keyword, scope in INTENT_TO_SERIES.items():
        if keyword in q_lower:
            return scope

    for model in available_models:
        if model in q or model in q.replace(" ", ""):
            return {"type": "model", "value": model}

    x_match = re.search(r"\bX([1-7])\b", q)
    if x_match:
        return {"type": "series", "value": f"X{x_match.group(1)}"}

    if re.search(r"\bX\b", q):
        return {"type": "family", "value": "X"}

    if re.search(r"\bM\b", q):
        return {"type": "series", "value": "M_models"}

    if re.search(r"\bZ\b", q):
        return {"type": "series", "value": "Z_series"}

    series_match = re.search(r"\b([1-8])\s*(?:SERIES|_SERIES)?\b", q)
    if series_match:
        num = series_match.group(1)
        return {"type": "series", "value": SERIES_ALIASES.get(num, f"{num}_series")}

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