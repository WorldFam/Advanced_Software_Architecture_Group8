from fastapi import APIRouter

from models.models import Configurations
from service.base_production_line_service import BaseProductionLineService


class BaseController:
    def __init__(self, router: APIRouter, service: BaseProductionLineService):
        self.router = router
        self.service = service

    def get_status(self):
        return self.service.get_status()

    def start(self, config: Configurations):
        return self.service.start_production_line(config)

    def stop(self):
        return self.service.stop_production_line()

    def pause(self):
        return self.service.pause_production_line()

    def resume(self):
        return self.service.resume_production_line()

    def add_routes(self):
        @self.router.get("/status")
        async def get_status():
            return self.get_status()

        @self.router.post("/start")
        async def start_process(config: Configurations):
            return self.start(config)

        @self.router.post("/stop")
        async def stop_process():
            return self.stop()

        @self.router.post("/pause")
        async def pause_process():
            return self.pause()

        @self.router.post("/resume")
        async def resume_process():
            return self.resume()