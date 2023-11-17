import os
from dotenv import load_dotenv
from confluent_kafka import Producer
from confluent_kafka import Producer

load_dotenv()

config = {
    'bootstrap.servers': 'kafka:9092',  
}

# Create a Kafka producer
producer = Producer(config)

# Function to publish a message to the Kafka topic
def publish_message(topic, message):
    try:
        producer.produce(topic, key=None, value=message)
        producer.flush()
        print(f"Message sent to topic '{topic}': {message}")
    except Exception as e:
        print(f"Failed to send message to topic '{topic}': {str(e)}")