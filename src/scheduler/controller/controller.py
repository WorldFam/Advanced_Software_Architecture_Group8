from fastapi import APIRouter, HTTPException
from model.order import Order
from model.log import Log 
from service.websocket import send_message 
from service.scheduler import place_order

router = APIRouter()

@router.post("/order")
async def schedule_order(order: Order):
    try:
        print(f"Order {order.id} received")
        await send_message(Log(orderId=order.id, process="Received order being scheduled"))
        await place_order(order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))