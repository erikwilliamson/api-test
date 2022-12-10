from app.lib.crud.base import CRUDBase
from app.lib.models import Company, CompanyUpdate


class CRUDCompany(CRUDBase[Company, CompanyUpdate]):
    def get_by_name(self) -> Company:
        pass


company = CRUDCompany(Company)
