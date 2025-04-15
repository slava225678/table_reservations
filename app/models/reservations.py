from sqlalchemy import (CheckConstraint, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Reservation(Base):
    '''
    Модель бронирования столиков.
    Содержит информацию о клиенте,
    столике и времени брони.
    '''
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)
    table_id = Column(Integer, ForeignKey(
        "tables.id", ondelete="CASCADE"
    ), nullable=False)
    reservation_time = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, default=10, nullable=False)

    table = relationship("Table", back_populates="reservations")

    __table_args__ = (
        CheckConstraint(
            'duration_minutes > 9',
            name='check_seats_positive'
        ),
    )
