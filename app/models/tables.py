from sqlalchemy import CheckConstraint, Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Table(Base):
    '''
    Модель столиков ресторана.
    Описывает столик с его названием,
    количеством мест и местоположением.
    '''
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    seats = Column(Integer, nullable=False)
    location = Column(String(100))

    reservations = relationship(
        "Reservation",
        back_populates="table",
        cascade="all, delete-orphan"
    )
    __table_args__ = (
        CheckConstraint('seats > 0', name='check_seats_positive'),
    )
