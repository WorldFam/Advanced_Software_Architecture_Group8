from confluent_kafka import Consumer, KafkaError

# Configure the consumer
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

# Subscribe to a topic
consumer.subscribe(['topic_name'])

# Poll for messages
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print('Error while polling:', msg.error())
    else:
        print('Received message: ', msg.value())
