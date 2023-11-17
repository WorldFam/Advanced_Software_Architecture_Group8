from pydantic import BaseModel

class Order(BaseModel):
    id: str
    name: str
    amount: str