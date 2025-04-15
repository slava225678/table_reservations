from typing import List

from sqlalchemy.orm import Session

from app.models.tables import Table


def create_table(
        db: Session,
        table_name: str,
        seats: int,
        location: str
) -> Table:
    '''Создание нового столика.'''
    new_table = Table(name=table_name, seats=seats, location=location)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


def get_tables(
    db: Session
) -> List[Table]:
    '''Получение всех столиков.'''
    return db.query(Table).all()


def delete_table(
        db: Session,
        table_id: int
) -> None:
    '''Удаление столика по ID.'''
    table = db.query(Table).filter(Table.id == table_id).first()
    if table:
        db.delete(table)
        db.commit()
