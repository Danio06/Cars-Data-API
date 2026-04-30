from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from service import ask
from carsdatabase import load_json_to_db, is_db_empty, get_connection

app = FastAPI(
    title="Technical Data API",
    description="Query engines, transmissions and specs",
    version="2.0.3"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- STARTUP ---
@app.on_event("startup")
def startup():
    try:
        print("API starting...")

        conn = get_connection()
        conn.close()

        try:
            if is_db_empty():
                print("Seeding PostgreSQL database...")
                load_json_to_db()
            else:
                print("Database already seeded")
        except Exception as db_error:
            print("DB not ready yet, skipping seed:", db_error)

    except Exception as e:
        print("Startup error:", e)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Technical Data API",
        "usage": "Go to /search?q=... to query data or /docs for documentation",
        "status": "online"
    }

@app.get("/healthz")
def health():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()

        return {"status": "ok"}

    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/search")
async def search(q: str = Query(..., min_length=1)):
    try:
        result = ask(q)
        return result

    except Exception as e:
        return {
            "status": "error",
            "message": "Internal server error",
            "detail": str(e)
        }