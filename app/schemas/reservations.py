from datetime import datetime

from pydantic import BaseModel, field_validator


class ReservationCreate(BaseModel):
    '''
    Схема для создания брони.
    Ожидает данные клиента, столика,
    времени и продолжительности бронирования.
    '''
    customer_name: str
    reservation_time: datetime
    duration_minutes: int = 10

    @field_validator("duration_minutes")
    def validate_seats(cls, value):
        if value < 10:
            raise ValueError(
                "Минимальная длительность бронирования должна быть 10 минут"
            )
        return value


class ReservationRead(BaseModel):
    '''Схема для чтения брони. Включает поле id.'''
    id: int
    customer_name: str
    reservation_time: datetime
    duration_minutes: int

    class Config:
        orm_mode = True
