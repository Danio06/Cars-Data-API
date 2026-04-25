import re

def clean_query(query):
    return query.upper().strip()

def detect_model(query):
    query = clean_query(query)

    patterns = {
        "E21": r"E\s*21",
        "E30": r"E\s*30",
        "E36": r"E\s*36",
        "E46": r"E\s*46",
        "E90": r"E\s*90",
        "F30": r"F\s*30",
        "G20": r"G\s*20"
    }

    for model, pattern in patterns.items():
        if re.search(pattern, query):
            return model

    return None

def detect_fuel(query):
    query = query.upper()

    if re.search(r"\bDIESEL\b", query):
        return "diesel"

    if re.search(r"\bPETROL\b", query):
        return "petrol"

    return None

def detect_intent(query):
    query = query.upper()

    if re.search(r"\bBEST\b", query):
        return "best"

    if re.search(r"\bENGINE\b", query):
        return "engine"

    return "general"