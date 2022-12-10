from typing import Optional
from beanie import Document
from pydantic import BaseModel


class Car(Document):
    name: str

    class Settings:
        name = "car"

    class Config:
        schema_extra = {
            "example": {
                "name": "audi"
            }
        }

    async def __json__(self):
        return {
            "name": self.name
        }

    async def listing(self):
        return self.name


class CarUpdate(BaseModel):
    name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Nissan"
            }
        }


class CarCreate(BaseModel):
    name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Lotus"
            }
        }
