from model.order import Order
from producer.producer import publish_message
import requests

# Change with supply managament URL!!!
api_url = "http://api.example.com/data"

def schedule_order(order: Order):
    response = requests.post(api_url, json=order)
    if response.status_code == 200:
        publish_message('order-topic', order)
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")