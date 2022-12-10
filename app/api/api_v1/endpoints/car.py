import logging
from typing import List

from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId

from app.lib.core.config import settings
from app.lib.models.car import Car, CarUpdate, CarCreate
from app.lib.exceptions import CrudException
from app.lib import crud
from app.lib.helpers import HTTPMethods
from app.lib.endpoints.base import EndpointBase
router = APIRouter()
logger = logging.getLogger(settings.LOGGER_NAME)


# async def create(car: Car):
#     return await crud.car.create(obj_in=car)
#
# router.add_api_route(
#     path="",
#     endpoint=create,
#     methods=[HTTPMethods.POST],
#     response_model=Car,
#     status_code=status.HTTP_201_CREATED
# )
#


class EndpointCar(EndpointBase[Car, CarCreate, CarUpdate]):
    def get_by_name(self) -> Car:
        pass


car_endpoints = EndpointCar(model=Car, router=router, crud=crud.car, path="/car")







#
# @router.get("", response_model=List[Car])
# async def read_all(skip: int = 0, limit: int = 100):
#     """
#     Retrieve the list of companies
#     """
#     try:
#         return await crud.car.read_multi(skip=skip, limit=limit)
#     except CrudException as exc:
#         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
#
#
# @router.get("/{object_id}", status_code=status.HTTP_200_OK, response_model=Car)
# async def read_one(object_id: PydanticObjectId):
#     """
#     Get Car by ID
#     """
#
#     try:
#         return await crud.car.read(object_id=object_id)
#     except CrudException as exc:
#         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
#
#
# @router.patch("/{object_id", response_model=Car)
# async def update(object_id: PydanticObjectId, req: CarUpdate):
#     """
#     Updates a car
#     """
#     try:
#         return await crud.car.update(object_id=object_id, obj_in=req)
#     except CrudException as exc:
#         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
#
#
# @router.delete("/{object_id}", response_model=Car)
# async def delete(object_id: PydanticObjectId):
#     """
#     Deletes a Car
#     """
#     try:
#         car = await crud.car.delete(object_id=object_id)
#     except CrudException as exc:
#         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
#
#     return car
