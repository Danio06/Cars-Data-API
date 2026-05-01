from fastapi import APIRouter, Query
from service import ask

router = APIRouter()

@router.get("/search")
def search(q: str = Query(..., min_length=1)):
    return ask(q)