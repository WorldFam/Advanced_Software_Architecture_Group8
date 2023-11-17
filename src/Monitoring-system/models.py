from typing import Optional
from pydantic import BaseModel, Field

class LogIn(BaseModel):
    programName: str = Field(...)
    log: str = Field(...)

class LogOut(BaseModel):
    id: str = Field(...)
    programName: str = Field(...)
    log: str = Field(...)


m