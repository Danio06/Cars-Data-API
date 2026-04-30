import re
import psycopg2
import os

def get_conn():
    return psycopg2.connect(os.environ["DATABASE_URL"])


def clean_query(query):
    return query.upper().strip()


def get_all_models_from_db():
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT model FROM engines
            UNION
            SELECT DISTINCT series FROM engines
        """)

        models = [row[0].upper() for row in cursor.fetchall() if row[0]]

        conn.close()
        return models

    except Exception as e:
        print("Parser DB error:", e)
        return []


def detect_model(query):
    query = clean_query(query)
    normalized_query = query.replace(" ", "")

    series_match = re.search(r'SERIES(\d)', normalized_query)
    if series_match:
        query = query + " " + f"{series_match.group(1)}_SERIES"

    available_entities = get_all_models_from_db()

    found_entity = None
    for entity in available_entities:
        clean_entity = entity.replace("_", "")

        if entity in query or clean_entity in normalized_query:
            if not found_entity or len(entity) > len(found_entity):
                found_entity = entity

    return found_entity


def detect_fuel(query):
    query = query.upper()
    if re.search(r"\bDIESEL\b", query): return "diesel"
    if re.search(r"\bPETROL\b", query): return "petrol"
    if re.search(r"\bELECTRIC\b", query): return "electric"
    return None


def detect_intent(query):
    query = query.upper()
    if re.search(r"\bBEST\b", query): return "best"
    if re.search(r"\bENGINE\b", query): return "engine"
    return "general"