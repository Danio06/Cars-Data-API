from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router
from carsdatabase import load_json_to_db

app = FastAPI(title="Cars Data API", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    try:
        print("API starting...")
        load_json_to_db()
        print("Database ready")
    except Exception as e:
        print("Startup error:", e)

@app.get("/")
def root():
    return {"status": "online", "usage": "/search?q=..."}

@app.get("/healthz")
def health():
    return {"status": "ok"}

app.include_router(router)