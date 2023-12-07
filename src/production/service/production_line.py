import threading
from threading import Thread
import time

from model.model import Order
SERVICE="Production"

# Production line
class BaseProductionLineService:
    def __init__(self, name):
        self.countdown_thread: Thread | None = None
        self.paused = False
        self.stopped = threading.Event()
        self.current_number = 0
        self.operationName = name

    def start_production_line(self, order: Order):
        if self.countdown_thread is None or not self.countdown_thread.is_alive():
            start_number = int(order.get('amount'))
            print("%s has been started. The amount remained: %i" % (self.operationName, start_number))
            self.countdown_thread = threading.Thread(target=self.countdown, args=(start_number,self.operationName))
            self.stopped.clear()
            self.paused = False
            self.countdown_thread.start()
            return {'message': f'Countdown started from {start_number}.'}
        else:
            return {'message': 'Countdown is already running.'}

    def get_status(self):
        return {'current_number': self.current_number, 'paused': self.paused, 'stopped': self.stopped.is_set()}

    def countdown(self, start_number, name):
        self.current_number = start_number
        while self.current_number > 0:
            if self.stopped.is_set():
                print("%s has been stopped at %ith bootle." % (name, self.current_number))
                break
            if not self.paused:
                self.current_number -= 1
                time.sleep(1)
            if self.paused:
                print("%s has been paused at %ith bootle." % (name, self.current_number))
            print("Remaining bottles at %s: %i" % (name, self.current_number))
