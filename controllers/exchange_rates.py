from sqlalchemy.orm import Session

from model import core
from model.schemas import ExchangeRate


def create_exchange_rates(data: ExchangeRate, db: Session):
    exchange_rates = core.ExchangeRate(
        pair=data.pair,
        rate=data.rate,
        timestamp=data.timestamp
    )
    try:
        db.add(exchange_rates)
        db.commit()
        db.refresh(exchange_rates)
    except Exception as e:
        print(e)
