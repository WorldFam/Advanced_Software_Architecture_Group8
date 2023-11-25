from confluent_kafka import Consumer, KafkaError

class KafkaConsumer:
    def __init__(self, broker, topic):
        self.consumer = Consumer({
            'bootstrap.servers': broker,
            'group.id': 'console-consumer-20477',
            'client.id': 'console-consumer',
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': True,
            'auto.offset.reset': 'earliest'  # Start reading from the beginning of the topic if no offset is stored for the consumer group.
        })
        self.topic = topic

    def consume_messages(self, production):
        self.consumer.subscribe([self.topic])

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
                    print(f"Received message: {msg.value().decode('utf-8')}")
                    production.start_production_line(msg.value().decode('utf-8'))
                    # return msg.value().decode('utf-8')

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()
