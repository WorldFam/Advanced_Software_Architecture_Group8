# main.py
from fastapi import FastAPI, APIRouter

from controller.base_controller import BaseController
from service.base_production_line_service import BaseProductionLineService

app = FastAPI()


packaging_ctrl = BaseController(APIRouter(), BaseProductionLineService("Packaging"))
packaging_ctrl.add_routes()

production_ctrl = BaseController(APIRouter(), BaseProductionLineService("Production"))
production_ctrl.add_routes()

app.include_router(packaging_ctrl.router, prefix="/packaging-line")
app.include_router(production_ctrl.router, prefix="/production-line")
