import paho.mqtt.client as mqtt
import json

class MQTTSubscriber:
    def __init__(self, broker, topic, callback_function):
        self.client = mqtt.Client()
        self.broker = broker
        self.topic = topic
        self.callback_function = callback_function

    def on_message(self, client, userdata, msg):
        try:
            # Process the message
            order = json.loads(msg.payload.decode('utf-8'))
            print(f"Received message: {order}")
            self.callback_function(order)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def consume_messages(self):
        try:
            # Set up the connection to the MQTT broker
            self.client.connect(self.broker, 1883, 300)
            self.client.on_message = self.on_message
            self.client.subscribe(self.topic)
            
            # Start the MQTT loop to listen for messages
            self.client.loop_forever()

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        finally:
            # Disconnect from the MQTT broker
            self.client.disconnect()
