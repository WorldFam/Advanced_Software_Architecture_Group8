from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as log_router
from confluent_kafka import Consumer, KafkaError

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}
    

consumer = Consumer(conf)

# Subscribe to a topic
consumer.subscribe(['quickstart-events'])
print('kafka on')

    

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(log_router, tags=["logs"], prefix="/logs")


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


#LocalHost:80/docs access the swagger

