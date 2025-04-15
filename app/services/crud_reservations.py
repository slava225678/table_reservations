from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.reservations import Reservation
from app.schemas.reservations import ReservationCreate
from app.services.validators import validate_reservation_time


def create_reservation(
    db: Session,
    table_id: int,
    reservation: ReservationCreate
) -> Reservation:
    '''Создание новой брони с проверкой на пересечение времени.'''
    if validate_reservation_time(
        db,
        table_id,
        reservation.reservation_time,
        reservation.duration_minutes
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The table is already reserved for this time slot."
        )

    new_reservation = Reservation(
        customer_name=reservation.customer_name,
        table_id=table_id,
        reservation_time=reservation.reservation_time,
        duration_minutes=reservation.duration_minutes
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


def get_reservations(
        db: Session,
        skip: int = 0,
        limit: int = 100
) -> List[Reservation]:
    '''Получение списка бронирований.'''
    return db.query(
        Reservation
    ).offset(
        skip
    ).limit(
        limit
    ).all()


def delete_reservation(
        db: Session,
        reservation_id: int
) -> None:
    '''Получение бронирования по ID.'''
    reservaton = db.query(
        Reservation
    ).filter(
        Reservation.id == reservation_id
    ).first()
    if reservaton:
        db.delete(reservaton)
        db.commit()
