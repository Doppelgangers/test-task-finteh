from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from .database import Base


class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'

    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, index=True)
    rate = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
