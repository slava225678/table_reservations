from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.reservations import Reservation
from app.models.tables import Table


def validate_reservation_time(
    db: Session,
    table_id: int,
    reservation_time: datetime,
    duration_minutes: int
) -> bool:
    '''Проверка на пересечение временных слотов столика.'''

    new_start = reservation_time
    new_end = reservation_time + timedelta(minutes=duration_minutes)

    existing_reservations = db.query(Reservation).filter(
        Reservation.table_id == table_id
    ).all()

    for reservation in existing_reservations:
        existing_start = reservation.reservation_time
        existing_end = existing_start + timedelta(
            minutes=reservation.duration_minutes
        )

        if not (
            new_end <= existing_start or new_start >= existing_end
        ):
            return True

    return False


def check_reservation_conflict(
    db: Session,
    table_id: int,
    reservation_time: datetime,
    duration_minutes: int
) -> None:
    """Бросает ошибку, если бронирование конфликтует с уже существующим."""

    has_conflict = validate_reservation_time(
        db, table_id, reservation_time, duration_minutes
    )
    if has_conflict:
        raise HTTPException(
            status_code=400,
            detail="Столик уже забронирован в указанное время."
        )


def check_table_name_duplicate(db: Session, name: str) -> None:
    if db.query(Table).filter(Table.name == name).first():
        raise HTTPException(
            status_code=422,
            detail='Столик с таким именем уже существует.'
        )


def check_table_exists(db: Session, table_id: int) -> Table:
    table = db.query(Table).filter(Table.id == table_id).first()
    if table is None:
        raise HTTPException(
            status_code=404,
            detail='Столик не найден.'
        )
    return table


def check_reservation_exists(
        db: Session,
        reservation_id: int
) -> Reservation:
    reservation = db.query(
        Reservation
    ).filter(Reservation.id == reservation_id).first()
    if reservation is None:
        raise HTTPException(
            status_code=404,
            detail='Бронирование не найдено.'
        )
    return reservation
