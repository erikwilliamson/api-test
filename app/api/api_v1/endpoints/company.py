import logging
from typing import List

from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId

from app.lib.core.config import settings
from app.lib.models.company import Company, CompanyUpdate
from app.lib.exceptions import CrudException
from app.lib import crud

router = APIRouter()
logger = logging.getLogger(settings.LOGGER_NAME)


@router.post("", response_model=Company)
async def create(company: Company):
    """
    Create a company
    """
    try:
        return await crud.company.create(obj_in=company)
    except CrudException as exc:
        raise HTTPException(status_code=exc.http_return_code, detail=exc.message)


@router.get("", response_model=List[Company])
async def read_all(skip: int = 0, limit: int = 100):
    """
    Retrieve the list of companies
    """
    try:
        return await crud.company.read_multi(skip=skip, limit=limit)
    except CrudException as exc:
        raise HTTPException(status_code=exc.http_return_code, detail=exc.message)


@router.get("/{object_id}", status_code=status.HTTP_200_OK, response_model=Company)
async def read_one(object_id: PydanticObjectId):
    """
    Get Company by ID
    """

    try:
        return await crud.company.read(object_id=object_id)
    except CrudException as exc:
        raise HTTPException(status_code=exc.http_return_code, detail=exc.message)


@router.patch("/{object_id", response_model=Company)
async def update(object_id: PydanticObjectId, req: CompanyUpdate):
    """
    Updates a company
    """
    try:
        return await crud.company.update(object_id=object_id, obj_in=req)
    except CrudException as exc:
        raise HTTPException(status_code=exc.http_return_code, detail=exc.message)


@router.delete("/{object_id}", response_model=Company)
async def delete(object_id: PydanticObjectId):
    """
    Deletes a Company
    """
    try:
        company = await crud.company.delete(object_id=object_id)
    except CrudException as exc:
        raise HTTPException(status_code=exc.http_return_code, detail=exc.message)

    return company
