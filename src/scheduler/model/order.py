from pydantic import BaseModel

class Order(BaseModel):
    id: str
    customer: str
    size: str
    amount: str
    timestamp: str