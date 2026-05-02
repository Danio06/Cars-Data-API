from db import get_conn

def get_all_series(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT series FROM engines WHERE series IS NOT NULL")
    return [r[0].upper() for r in cursor.fetchall()]

def get_all_models(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT model FROM engines WHERE model IS NOT NULL")
    return [r[0].upper() for r in cursor.fetchall()]

def get_engines(conn, series=None, model=None, fuel=None):
    cursor = conn.cursor()
    query = "SELECT series, model, fuel, name, engine_code, power FROM engines WHERE 1=1"
    params = []
    if series:
        query += " AND series ILIKE %s"
        params.append(series)
    if model:
        query += " AND model ILIKE %s"
        params.append(model)
    if fuel:
        query += " AND fuel = %s"
        params.append(fuel)
    cursor.execute(query, params)
    columns = [desc[0] for desc in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def get_transmissions(conn, series=None, model=None):
    cursor = conn.cursor()
    query = "SELECT model, transmission_type, speeds, name FROM transmissions WHERE 1=1"
    params = []
    if series:
        query += " AND model IN (SELECT DISTINCT model FROM engines WHERE series ILIKE %s)"
        params.append(series)
    if model:
        query += " AND model ILIKE %s"
        params.append(model)
    cursor.execute(query, params)
    result = {}
    for row in cursor.fetchall():
        m, t_type, speeds, name = row
        result.setdefault(m, {}).setdefault(t_type, []).append({"speeds": speeds, "type": name})
    return result

def get_best_engines(conn, series=None, model=None, fuel=None):
    cursor = conn.cursor()
    query = "SELECT model, fuel, name, reason FROM best_engines WHERE 1=1"
    params = []
    if series:
        query += " AND model IN (SELECT DISTINCT model FROM engines WHERE series ILIKE %s)"
        params.append(series)
    if model:
        query += " AND model ILIKE %s"
        params.append(model)
    if fuel:
        query += " AND fuel = %s"
        params.append(fuel)
    cursor.execute(query, params)
    result = {}
    for row in cursor.fetchall():
        m, f, name, reason = row
        result.setdefault(m, {})[f] = {"model": name, "reason": reason}
    return result