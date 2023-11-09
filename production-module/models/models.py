from pydantic import BaseModel


class Configurations(BaseModel):
    id: int | None
    name: str
    amount: int
