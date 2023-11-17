from fastapi import FastAPI

app = FastAPI()

from controller.controller import router as controller_router
app.include_router(controller_router, prefix="/v1")