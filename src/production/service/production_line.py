from model.order import Order
from model.log import Log
from service.websocket import send_message
import asyncio
class BaseProductionLineService:
    def __init__(self, name):
        self.task = None
        self.current_number = 0
        self.operation_name = name

    async def start_production_line(self, order: Order):
            start_number = int(order.get('amount'))
            self.task = await self.countdown(start_number, self.operation_name, order)
            return {'message': f'Countdown started from {start_number}.'}

    async def countdown(self, start_number, name, order):
        self.current_number = start_number
        print(f"Remaining bottles at {name}: {self.current_number}")
        await self.send_log(order, name)

        while self.current_number > 0:
                self.current_number -= 1
                await asyncio.sleep(1)
                if self.current_number > 0: 
                    print(f"Remaining bottles at {name}: {self.current_number}")
                    await self.send_log(order, name)

    async def send_log(self, order, name):
        await send_message(Log(orderId=order.get('id'), process=f"Remaining bottles at {name}: {self.current_number}"))
