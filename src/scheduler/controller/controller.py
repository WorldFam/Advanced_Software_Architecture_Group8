from fastapi import APIRouter, HTTPException

from model.order import Order
from producer.producer import publish_message

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/order")
async def schedule_order(order: Order):
    try:
        publish_message('scheduler-topic', order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e), response_model=None)

