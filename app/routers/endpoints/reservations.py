from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.reservations import ReservationCreate, ReservationRead
from app.services.crud_reservations import crud_reservations
from app.services.validators import (check_reservation_conflict,
                                     check_reservation_exists,
                                     check_table_exists)

router = APIRouter()


@router.get("/", response_model=List[ReservationRead])
def get_reservations_api(
    db: Session = Depends(get_db)
) -> List[ReservationRead]:
    '''Получение списка всех броней.'''
    return crud_reservations.get_multi(db)  # type: ignore


@router.post("/", response_model=ReservationRead)
def create_reservation_api(
    table_id: int,
    reservation: ReservationCreate,
    db: Session = Depends(get_db)
) -> ReservationRead:
    '''
    Создание новой брони.
    Проверка на пересечение временных слотов столика.
    '''
    check_table_exists(db, table_id)
    check_reservation_conflict(
        db,
        table_id,
        reservation.reservation_time,
        reservation.duration_minutes
    )
    return crud_reservations.create_reservation(db, table_id, reservation)


@router.delete("/{reservation_id}", status_code=204)
def delete_reservation_api(
    reservation_id: int, db: Session = Depends(get_db)
) -> None:
    '''Удаление брони по ID.'''
    check_reservation_exists(db, reservation_id)
    reservation = crud_reservations.get(reservation_id, db)
    crud_reservations.remove(reservation, db)
