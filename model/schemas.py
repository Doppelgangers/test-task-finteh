from datetime import datetime

from pydantic import BaseModel


class ExchangeRate(BaseModel):
    pair: str
    rate: float
    timestamp: datetime
