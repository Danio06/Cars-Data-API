import os
import psycopg2

def get_conn():
    url = os.getenv("DATABASE_URL")

    if not url:
        raise RuntimeError("DATABASE_URL is missing")

    return psycopg2.connect(url)