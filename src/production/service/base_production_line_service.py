import os
import threading
from threading import Thread
import time

from channel.kafka_consumer import KafkaConsumer
from channel.kafka_producer import KafkaProducer
from models.models import Order


# Production line
class BaseProductionLineService:
    def __init__(self, name):
        self.countdown_thread: Thread | None = None
        self.paused = False
        self.stopped = threading.Event()
        self.current_number = 0
        self.operationName = name
    
        # Initialize the Kafka producer with your Kafka broker address and topic
        # self.producer = KafkaProducer(broker="kafka:9092", topic="production-topic")

    def start_production_line(self, order: Order):
        if self.countdown_thread is None or not self.countdown_thread.is_alive():
            print(order.get('amount'))
            start_number = int(order.get('amount'))
            self.producer.send_log("%s has been started. The amount remained: %i" % (self.operationName, start_number))
            self.countdown_thread = threading.Thread(target=self.countdown, args=(start_number,self.operationName))
            self.stopped.clear()
            self.paused = False
            self.countdown_thread.start()
            return {'message': f'Countdown started from {start_number}.'}
        else:
            return {'message': 'Countdown is already running.'}

    def pause_production_line(self):
        if self.countdown_thread and self.countdown_thread.is_alive():
            self.paused = True
            return {'message': 'Countdown paused.'}
        else:
            return {'message': 'No countdown running to pause.'}

    def resume_production_line(self):
        if self.countdown_thread and self.countdown_thread.is_alive():
            self.paused = False
            return {'message': 'Countdown resumed.'}
        else:
            return {'message': 'No countdown running to resume.'}

    def stop_production_line(self):
        if self.countdown_thread and self.countdown_thread.is_alive():
            self.stopped.set()
            self.countdown_thread.join()
            return {'message': 'Countdown stopped.'}
        else:
            return {'message': 'No countdown running to stop.'}

    def get_status(self):
        return {'current_number': self.current_number, 'paused': self.paused, 'stopped': self.stopped.is_set()}

    def countdown(self, start_number, name):
        self.current_number = start_number
        while self.current_number > 0:
            if self.stopped.is_set():
                self.producer.send_log("%s has been stopped at %ith bootle." % (name, self.current_number))
                break
            if not self.paused:
                self.current_number -= 1
                time.sleep(1)
            if self.paused:
                self.producer.send_log("%s has been paused at %ith bootle." % (name, self.current_number))
            self.producer.send_log("Remaining bottles at %s: %i" % (name, self.current_number))
