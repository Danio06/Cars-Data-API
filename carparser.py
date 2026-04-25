def clean_query(query):
    return query.lower().strip()

def detect_model(query):
    query = clean_query(query)

    MODELS = ["E21", "E30", "E36", "E46", "E90", "F30", "G20"]

    for model in MODELS:
        if model.lower() in query:
            return model

        return None

def detect_fuel(query):
    query = clean_query(query)

    if "petrol" in query:
        return "petrol"

    if "diesel" in query:
        return "diesel"

    return None

def detect_best(query):
    query = clean_query(query)

    if "best" in query:
        return True
    
    return False