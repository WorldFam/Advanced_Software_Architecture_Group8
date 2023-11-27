from pydantic import BaseModel

class Order(BaseModel):
    uuid: str
    name: str
    size: str
    amount: str