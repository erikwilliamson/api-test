from typing import Optional
from beanie import Document
from pydantic import BaseModel


class Pet(Document):
    name: str

    class Settings:
        name = "pet"

    class Config:
        schema_extra = {
            "example": {
                "name": "Sadie"
            }
        }

    async def __json__(self):
        return {
            "name": self.name
        }

    async def listing(self):
        return self.name


class PetUpdate(BaseModel):
    name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Agnes"
            }
        }
