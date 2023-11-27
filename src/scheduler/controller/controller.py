from fastapi import APIRouter, HTTPException

from model.order import Order
from service.scheduler import place_order

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/order")
def schedule_order(order: Order):
    try:
        place_order(order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

