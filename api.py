from fastapi import FastAPI
from service import ask

app = FastAPI()

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