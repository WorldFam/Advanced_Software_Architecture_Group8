# # main.py
# from fastapi import FastAPI, APIRouter

# from controller.base_controller import BaseController
# from service.base_production_line_service import BaseProductionLineService

# app = FastAPI()


# packaging_ctrl = BaseController(APIRouter(), BaseProductionLineService("Packaging"))
# packaging_ctrl.add_routes()

# production_ctrl = BaseController(APIRouter(), BaseProductionLineService("Production"))
# production_ctrl.add_routes()

# app.include_router(packaging_ctrl.router, prefix="/packaging-line")
# app.include_router(production_ctrl.router, prefix="/production-line")

from channel.kafka_consumer import KafkaConsumer
from models.models import Order
from service.base_production_line_service import BaseProductionLineService


# consumer = KafkaConsumer(broker="kafka:9092", 
#                          topic="scheduler-topic")
production = BaseProductionLineService("Packaging")

order = Order("1", "order", "64")
production.start_production_line(order=order)
# consumer.consume_messages(production)