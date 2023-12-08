import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("mosquitto", 1883, 60)

def publish_message(topic, message):
    try:
        serialized_message = json.dumps(message.__dict__).encode('utf-8')
        client.publish(topic, serialized_message)
        print(f"Message sent to topic '{topic}': {message}")
    except Exception as e:
        print(f"Failed to send message to topic '{topic}': {str(e)}")