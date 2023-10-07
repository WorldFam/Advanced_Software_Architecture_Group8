from confluent_kafka import Producer
import time
import json

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'kafka:9092',  # Replace with your Kafka broker(s)
    'client.id': 'scheduler-app'
}

# Create a Kafka producer instance
producer = Producer(producer_config)

# Function to publish a message to the Kafka topic
def publish_message(topic, message):
    try:
        producer.produce(topic, key=None, value=message)
        producer.flush()
        print(f"Message sent to topic '{topic}': {message}")
    except Exception as e:
        print(f"Failed to send message to topic '{topic}': {str(e)}")

# Your scheduling logic here
def schedule_task():
    # Replace this with your scheduling logic
    task = {
        'task_id': 1,
        'task_name': 'Sample Task',
        'timestamp': int(time.time())
    }
    return json.dumps(task)

# Main loop for scheduling tasks and publishing messages
if __name__ == "__main__":
    kafka_topic = 'scheduler-topic'  # Replace with your desired Kafka topic

    try:
        while True:
            message = schedule_task()
            publish_message(kafka_topic, message)
            time.sleep(1)  # Adjust the interval as needed (in seconds)
    except KeyboardInterrupt:
        print("Scheduler stopped.")