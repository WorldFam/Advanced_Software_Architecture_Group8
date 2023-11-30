from confluent_kafka import Consumer, KafkaError
import json

from models.models import Order
class KafkaConsumer:
    def __init__(self, broker, topic, callback_function):
        self.consumer = Consumer({
            'bootstrap.servers': broker,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': True,
        })
        self.topic = topic
        self.callback_function = callback_function

    def consume_messages(self):
        try:
            self.consumer.subscribe([self.topic])
            while True:
                msg = self.consumer.poll(1.0)  # Timeout in seconds

                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event (not an error)
                        continue
                    else:
                        print(f"Error: {msg.error()}")
                else:
                    # Process the message
                    order = json.loads(msg.value().decode('utf-8'))
                    print(f"Received message: {order}")
                    self.callback_function(order)

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()
