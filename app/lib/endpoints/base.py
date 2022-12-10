from __future__ import annotations
from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from beanie import Document
from app.lib.exceptions import CrudException
from app.lib.crud.base import CRUDBase
from app.lib.helpers import HTTPMethods
from fastapi import HTTPException, APIRouter, status
from pydantic.main import ModelMetaclass
ModelType = TypeVar("ModelType", bound=Document)
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
# UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

#
# READ THIS
#  https://stackoverflow.com/questions/63853813/how-to-create-routes-with-fastapi-within-a-class


class EndpointBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    async def create(self, obj_in: CreateSchemaType):
        """
        Create a document
        """
        try:
            return await self.crud.create(obj_in=obj_in)
        except CrudException as exc:
            raise HTTPException(status_code=exc.http_return_code, detail=exc.message)

    def __init__(self, model: Type[ModelType], router: APIRouter, crud: CRUDBase, path: str):
        """
        Endpoint object with default endpoints for Create, Read, Update, Delete.
        """
        self.model = model
        self.router = router
        self.crud = crud
        self.path = path

        self.router.add_api_route(
            path="",
            endpoint=self.create,
            methods=[HTTPMethods.POST],
            response_model=self.model,
            status_code=status.HTTP_201_CREATED
        )

    # async def create(self, obj_in: ModelType):
    #     """
    #     Create a document
    #     """
    #     try:
    #         return await self.crud.create(obj_in=obj_in)
    #     except CrudException as exc:
    #         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
    #
        # self.router.add_api_route(
        #     path="",
        #     endpoint=self.read_all,
        #     methods=[HTTPMethods.GET],
        #     response_model=List[self.model],
        #     status_code=status.HTTP_200_OK
        # )
        # self.router.add_api_route(
        #     path=f"/{{object_id}}",
        #     endpoint=self.read_one,
        #     methods=[HTTPMethods.GET],
        #     response_model=self.model,
        #     status_code=status.HTTP_200_OK
        # )

        # self.router.add_api_route(
        #     path=f"/{{object_id}}",
        #     endpoint=self.update,
        #     methods=[HTTPMethods.PUT],
        #     response_model=self.model,
        #     status_code=status.HTTP_200_OK
        # )
        # self.router.add_api_route(
        #     path=f"/{{object_id}}",
        #     endpoint=self.delete_one,
        #     methods=[HTTPMethods.DELETE],
        #     response_model=self.model,
        #     status_code=status.HTTP_200_OK
        # )
        # self.router.add_api_route(
        #     path="",
        #     endpoint=self.delete_all,
        #     methods=[HTTPMethods.DELETE],
        #     response_model=None,
        #     status_code=status.HTTP_204_NO_CONTENT
        # )

    # async def read_all(self, skip: int = 0, limit: int = 100):
    #     """
    #     Retrieve the list of documents
    #     """
    #     try:
    #         return await self.crud.read_multi(skip=skip, limit=limit)
    #     except CrudException as exc:
    #         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
    #
    # async def read_one(self, object_id: PydanticObjectId):
    #     """
    #     Get document by ID
    #     """
    #
    #     try:
    #         return await self.crud.read(object_id=object_id)
    #     except CrudException as exc:
    #         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
    #
    # async def update(self, object_id: PydanticObjectId, obj_in: UpdateSchemaType):
    #     """
    #     Updates a document
    #     """
    #     try:
    #         return await self.crud.update(object_id=object_id, obj_in=obj_in)
    #     except CrudException as exc:
    #         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
    #
    # async def delete_one(self, object_id: PydanticObjectId):
    #     """
    #     Deletes a document
    #     """
    #     try:
    #         company = await self.crud.delete(object_id=object_id)
    #     except CrudException as exc:
    #         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
    #
    #     return company
    #
    # async def delete_all(self):
    #     """
    #     Deletes all documents in a collection
    #     """
    #     try:
    #         company = await self.crud.delete_all()
    #     except CrudException as exc:
    #         raise HTTPException(status_code=exc.http_return_code, detail=exc.message)
    #
    #     return company
