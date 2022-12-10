from typing import Optional
from beanie import Document
from pydantic import BaseModel


class Company(Document):
    name: str

    class Settings:
        name = "company"

    class Config:
        schema_extra = {
            "example": {
                "name": "TechSanity, Inc."
            }
        }

    async def __json__(self):
        return {
            "name": self.name
        }

    async def listing(self):
        return self.name


class CompanyUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "TechSanity, Inc."
            }
        }
