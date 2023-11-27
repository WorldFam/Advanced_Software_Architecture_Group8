from confluent_kafka import Consumer, KafkaError
import json

from models.models import Order
class KafkaConsumer:
    def __init__(self, broker, topic, callback_function):
        self.consumer = Consumer({
            'bootstrap.servers': broker,
            'group.id': 'console-consumer-20477',
            'client.id': 'console-consumer',
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': True,
            'auto.offset.reset': 'earliest'  # Start reading from the beginning of the topic if no offset is stored for the consumer group.
        })
        self.topic = topic
        self.callback_function = callback_function
        self.consumer.subscribe([self.topic])

    def consume_messages(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)  # Timeout in seconds

                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event (not an error)
                        print(f"Reached end of partition {msg.partition()}")
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
