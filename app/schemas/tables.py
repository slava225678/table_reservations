from pydantic import BaseModel, field_validator

from app.schemas.enums import TableLocation, TableName


class TableCreate(BaseModel):
    '''
    Схема для создания столика.
    Ожидает название, количество мест и местоположение.
    '''
    name: TableName
    seats: int = 1
    location: TableLocation

    @field_validator("seats")
    def validate_seats(cls, value):
        if value < 1:
            raise ValueError("Количество мест должно быть больше нуля")
        return value


class TableRead(BaseModel):
    '''Схема для чтения столика. Включает поле id.'''
    id: int
    name: str
    seats: int = 1
    location: str

    class Config:
        orm_mode = True
