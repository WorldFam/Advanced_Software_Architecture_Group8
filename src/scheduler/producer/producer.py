import json
from asyncio_mqtt import Client, MqttError

async def publish_message(topic, message):
    try:
        async with Client('mosquitto') as client:
            serialized_message = message.json().encode('utf-8')
            await client.publish(topic, payload=serialized_message)
            print(f"Message sent to topic '{topic}': {message}")
    except MqttError as e:
        print(f"Failed to communicate with MQTT broker: {str(e)}")
        raise