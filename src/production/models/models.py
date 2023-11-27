from pydantic import BaseModel

class Order(BaseModel):
    uuid: str
    size: str
    amount: str