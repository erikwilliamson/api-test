from app.lib.crud.base import CRUDBase
from app.lib.models import Pet, PetUpdate


class CRUDPet(CRUDBase[Pet, PetUpdate]):
    def get_by_name(self) -> Pet:
        pass


pet = CRUDPet(Pet)
