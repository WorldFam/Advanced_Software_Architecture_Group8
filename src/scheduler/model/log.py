from pydantic import BaseModel, Field
from datetime import datetime

class Log(BaseModel):
    orderId: str
    timestamp: str = Field(default_factory=lambda: str(datetime.now().isoformat()))
    process: str
    system: str = "Scheduler"

    