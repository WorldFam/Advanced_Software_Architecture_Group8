# from confluent_kafka import Producer
# from model import Order
# import time
# import json


# # Kafka producer configuration
# producer_config = {
#     'bootstrap.servers': 'kafka:9092',  # Replace with your Kafka broker(s)
#     'client.id': 'scheduler-app'
# }

# # Create a Kafka producer instance
# producer = Producer(producer_config)

# # Function to publish a message to the Kafka topic
# def publish_message(topic, message):
#     try:
#         producer.produce(topic, key=None, value=message)
#         producer.flush()
#         print(f"Message sent to topic '{topic}': {message}")
#     except Exception as e:
#         print(f"Failed to send message to topic '{topic}': {str(e)}")

# # Your scheduling logic here
# def schedule_task():
#     # Replace this with your scheduling logic
#     order = Order(int(time.time()), 'Water Bottle', '64')
#     return json.dumps(order.__dict__)

# # Main loop for scheduling tasks and publishing messages
# if __name__ == "__main__":
#     kafka_topic = 'scheduler-topic'  # Replace with your desired Kafka topic

#     try:
#         while True:
#             message = schedule_task()
#             publish_message(kafka_topic, message)
#             time.sleep(1)  # Adjust the interval as needed (in seconds)
#     except KeyboardInterrupt:
#         print("Scheduler stopped.")

from fastapi import FastAPI

app = FastAPI()

from controller.controller import router as controller_router
app.include_router(controller_router, prefix="/v1")