from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from http import HTTPStatus
from pydantic import BaseModel
from beanie import PydanticObjectId, Document
from beanie.exceptions import CollectionWasNotInitialized
from pymongo.errors import DuplicateKeyError
from app.lib.exceptions import CrudException

ModelType = TypeVar("ModelType", bound=Document)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        """
        self.model = model

    @property
    def collection_name(self) -> str:
        return self.model.get_collection_name()

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        try:
            created_object = await obj_in.create()
        except CollectionWasNotInitialized:
            raise CrudException(
                http_return_code=HTTPStatus.NOT_FOUND,
                message=f"Collection '{self.collection_name}' does not exist"
            )
        except DuplicateKeyError:
            raise CrudException(
                http_return_code=HTTPStatus.BAD_REQUEST,
                message=f"a similar '{self.collection_name}' already exists"
            )

        return created_object

    async def read(self, object_id: PydanticObjectId) -> ModelType:
        try:
            target_object = await self.model.find_one(self.model.id == object_id)
        except CollectionWasNotInitialized:
            raise CrudException(
                http_return_code=HTTPStatus.NOT_FOUND,
                message=f"Collection '{self.collection_name}' does not exist"
            )

        if target_object is None:
            raise CrudException(
                http_return_code=HTTPStatus.NOT_FOUND,
                message=f"{self.collection_name} with ID '{object_id}' does not exist"
            )

        return target_object

    async def read_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        try:
            return await self.model.find_all().skip(skip).limit(limit).to_list()
        except CollectionWasNotInitialized:
            raise CrudException(
                http_return_code=HTTPStatus.NOT_FOUND,
                message=f"Collection '{self.collection_name}' does not exist"
            )

    async def update(self, object_id: PydanticObjectId, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        target_object = await self.model.find_one(self.model.id == object_id)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        update_query = {
            "$set": {
                field: value for field, value in update_data.items()
            }
        }

        await target_object.update(update_query)
        return target_object

    async def delete(self, object_id: PydanticObjectId) -> ModelType:
        target_object = await self.read(object_id=object_id)

        await target_object.delete()
        return target_object

    async def delete_all(self) -> None:
        await self.model.delete_all()
        return
