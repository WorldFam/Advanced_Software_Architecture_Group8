from fastapi import APIRouter, HTTPException

from model.order import Order
from service.scheduler import place_order

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/order")
async def schedule_order(order: Order):
    try:
        print(f"Order {order.__dict__} being scheduled")
        place_order(order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

