from fastapi import APIRouter, HTTPException

from model.order import Order
# from service.scheduler import place_order
import json
import websockets
import asyncio
from datetime import datetime

router = APIRouter()

async def send_message(message):
    async with websockets.connect("ws://logging:8765") as websocket:
        await websocket.send(message)

@router.post("/order")
async def schedule_order(order: Order):
    try:
        log =  {
            "orderId": order.id,
            "timestamp": str(datetime.now().isoformat()),
            "process": "Received order being scheduled",
            "system": "Scheduler"
        }
        log_json = json.dumps(log)
        await send_message(log_json)
        # place_order(order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))