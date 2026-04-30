from fastapi import FastAPI
from service import ask
from fastapi.middleware.cors import CORSMiddleware
from carsdatabase import load_json_to_db, is_db_empty


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    if is_db_empty():
        print("Seeding DB...")
        load_json_to_db()


@app.get("/")
def read_root():
    return {
        "message": "Welcome to BMW Technical Data API",
        "usage": "Go to /search?q=... to query data or /docs for documentation",
        "status": "online"
    }

@app.get("/search")
async def search(q: str):
    result = ask(q)
    return result