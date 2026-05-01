from db import get_conn

def find_models(conn, search_term):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT model FROM engines
        WHERE model ILIKE %s OR series ILIKE %s
    """, (search_term, search_term))
    return [r[0] for r in cursor.fetchall()]

def get_engines(conn, model, fuel=None):
    cursor = conn.cursor()
    if fuel:
        cursor.execute("""
            SELECT name, engine_code, power FROM engines
            WHERE model = %s AND fuel = %s
        """, (model, fuel))
    else:
        cursor.execute("""
            SELECT name, engine_code, power FROM engines
            WHERE model = %s
        """, (model,))
    return [{"model": r[0], "engine": r[1], "power": r[2]} for r in cursor.fetchall()]

def get_transmissions(conn, model):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT transmission_type, speeds, name FROM transmissions
        WHERE model = %s
    """, (model,))
    transmissions = {}
    for t_type, speeds, name in cursor.fetchall():
        transmissions.setdefault(t_type, []).append({"speeds": speeds, "type": name})
    return transmissions

def get_best_engines(conn, model):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT fuel, name, reason FROM best_engines
        WHERE model = %s
    """, (model,))
    return cursor.fetchall()