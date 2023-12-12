import time
import json
from locust import task, TaskSet
from locust.user.wait_time import between
from locust_plugins.users.mqtt import MqttUser

class MyUser(MqttUser):
    host = "mosquitto"
    port = 1883
    wait_time = between(0.01, 0.1)

    @task
    class MyTasks(TaskSet):
        def on_start(self):
            time.sleep(5)

        @task
        def say_hello(self):
            test_order = {
                 "id" : "65723b0fa452744e29ca6a3a",
                 "customer" : "Sdu",
                 "size" : "2L",
                 "amount" : "10",
                 "timestamp" : "2023-12-07T21:37:19.674Z"
            }
            serialized_message = json.dumps(test_order)
            self.client.publish("order-topic",serialized_message)