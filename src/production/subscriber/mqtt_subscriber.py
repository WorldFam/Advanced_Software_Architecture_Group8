import json
from asyncio_mqtt import Client, MqttError
from service.production_line import BaseProductionLineService

filling = BaseProductionLineService("Filling")
labeling = BaseProductionLineService("Labeling")
packaging = BaseProductionLineService("Packaging")
from service.websocket import send_message
from model.log import Log

class MQTTSubscriber:
    def __init__(self, broker_address, topic):
        self.broker_address = broker_address
        self.topic = topic

    async def on_message(self, client, topic, message):
        try:
            order = json.loads(message.payload.decode('utf-8'))
            await filling.start_production_line(order)
            await labeling.start_production_line(order)
            await packaging.start_production_line(order)
            await send_message(Log(orderId=order.get('id'), process="Order completed"))

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    async def subscribe(self):
        async with Client(self.broker_address) as client:
            try:
                async with client.messages() as messages:
                    await client.subscribe(self.topic)
                    async for message in messages:
                        await self.on_message(client, message.topic, message)

            except MqttError as e:
                print(f"MQTT error: {e}")