from model.order import Order
from producer.producer import publish_message
import requests

from service.websocket import send_message
from model.log import Log
class OrderPlacementError(Exception):
    pass

async def make_supply_request(url, order):
    payload = {
        "size": order.size,
        "amount": order.amount
    }
    print(payload)
    try:
        await send_message(Log(orderId=order.id, process=f"Requesting supplies {payload}"))
        return requests.patch(url + "/supply", json=payload)
    except requests.RequestException as e:
        await send_message(Log(orderId=order.id, process=f"Error making supply request: {e}"))

        raise OrderPlacementError(f"Failed to place order: {e}")

async def place_order(order: Order):
    supply_url = "http://supply:9093"

    try:
        await send_message(Log(orderId=order.id, process="Starting request for resources from supply"))
        response = await make_supply_request(supply_url, order)

        if response.status_code == 200:
            await send_message(Log(orderId=order.id, process="Enough supplies proceeding with the order"))
            await publish_message('order-topic', order)
            await send_message(Log(orderId=order.id, process="Order sent to production successfully"))

        else: 
            await send_message(Log(orderId=order.id, process=f"Error senting order to production. Status code: {response.status_code}, Response: {response.text}"))
            raise OrderPlacementError(f"Failed to place order. Status code: {response.status_code}")

    except OrderPlacementError as e:
        await send_message(Log(orderId=order.id, process=f"Order placement failed: {e}"))


    except Exception as e:
        await send_message(Log(orderId=order.id, process=f"Unexpected error: {e}"))
