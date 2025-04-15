from app.models.tables import Table
from app.services.base import CRUDBase


class CRUDTable(CRUDBase):
    pass


table_crud = CRUDTable(Table)
