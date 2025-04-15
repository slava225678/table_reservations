from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.tables import TableCreate, TableRead
from app.services.crud_tables import table_crud
from app.services.validators import (check_table_exists,
                                     check_table_name_duplicate)

router = APIRouter()


@router.post(
        "/",
        response_model=TableRead
)
def create_table_api(
    table: TableCreate,
    db: Session = Depends(get_db)
) -> TableRead:
    '''Создание нового столика в ресторане.'''
    check_table_name_duplicate(db, table.name)
    return table_crud.create(table, db)


@router.get(
        "/",
        response_model=List[TableRead]
)
def get_tables_api(db: Session = Depends(get_db)) -> List[TableRead]:
    '''Получение списка всех столиков.'''
    return table_crud.get_multi(db)  # type: ignore


@router.delete(
        "/{table_id}",
        status_code=204
)
def delete_table_api(
    table_id: int, db: Session = Depends(get_db)
) -> None:
    '''Удаление столика по ID.'''
    check_table_exists(db, table_id)
    table = table_crud.get(table_id, db)
    table_crud.remove(table, db)
