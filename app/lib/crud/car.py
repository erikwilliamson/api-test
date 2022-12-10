from app.lib.crud.base import CRUDBase
from app.lib.models import Car, CarUpdate


class CRUDCar(CRUDBase[Car, CarUpdate]):
    def get_by_name(self) -> Car:
        pass


car = CRUDCar(Car)
