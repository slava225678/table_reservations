from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.tables import TableCreate, TableRead
from app.services.crud_tables import create_table, delete_table, get_tables
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
    return create_table(db, table.name, table.seats, table.location)


@router.get(
        "/",
        response_model=List[TableRead]
)
def get_tables_api(db: Session = Depends(get_db)) -> List[TableRead]:
    '''Получение списка всех столиков.'''
    return get_tables(db)  # type: ignore


@router.delete(
        "/{table_id}",
        status_code=204
)
def delete_table_api(
    table_id: int, db: Session = Depends(get_db)
) -> None:
    '''Удаление столика по ID.'''
    check_table_exists(db, table_id)
    delete_table(db, table_id)
