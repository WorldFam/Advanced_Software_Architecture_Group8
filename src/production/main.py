from subscriber.mqtt_subscriber import MQTTSubscriber
import asyncio

# MQTT configuration
mqtt_broker_address = "mosquitto"
mqtt_topic = "order-topic"

if __name__ == "__main__":
    mqtt_subscriber = MQTTSubscriber(mqtt_broker_address, mqtt_topic)
    asyncio.run(mqtt_subscriber.subscribe())