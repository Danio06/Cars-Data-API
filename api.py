from fastapi import FastAPI
from service import ask

app = FastAPI()

@app.get("/search")
async def search(q: str):
    result = ask(q)
    return result