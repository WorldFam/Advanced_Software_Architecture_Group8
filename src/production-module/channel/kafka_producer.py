from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, broker, topic):
        self.producer = Producer({"bootstrap.servers": broker})
        self.topic = topic

    def send_log(self, log_message):
        self.producer.produce(self.topic, value=log_message)
        self.producer.flush()
