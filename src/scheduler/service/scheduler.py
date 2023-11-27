from model.order import Order
from producer.producer import publish_message
import requests

url = "http://supply:9093"

def place_order(order: Order):
    response = requests.patch(url + "/supply",json={
                "size": order.size,
                "amount": order.amount
            })
    if response.status_code == 200:
        publish_message('order-topic', order)
    else:
        print(f"Error: {response.status_code} - {response.text}")