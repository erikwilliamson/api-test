from fastapi import APIRouter

from app.api.api_v1.endpoints import company, car

api_router = APIRouter()
api_router.include_router(company.router, prefix="/company", tags=["Company"])
api_router.include_router(car.router, prefix="/car", tags=["Car"])
