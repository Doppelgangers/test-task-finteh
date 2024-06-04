import datetime

import uvicorn
from fastapi import FastAPI, HTTPException

from binance import fetch_exchange_rates
from controllers.exchange_rates import create_exchange_rates
from model import core
from model.database import engine
from fastapi import Depends
from sqlalchemy.orm import Session
from model.database import get_db
from model.schemas import ExchangeRate

core.Base.metadata.create_all(bind=engine)

app = FastAPI()
pairs = ['BTCUSDT', 'ETHUSDT']


@app.get('/exchange_rates/')
def get_exchange_rates(db: Session = Depends(get_db)) -> dict[str, float]:
    exchange_rates = fetch_exchange_rates(pairs)
    for pair_name, rate in exchange_rates.items():
        data = ExchangeRate(pair=pair_name, rate=rate, timestamp=datetime.datetime.now())
        create_exchange_rates(db=db, data=data)
    return exchange_rates


@app.get('/exchange_rates/{name}')
def get_exchange_rates(name: str, db: Session = Depends(get_db)):
    pair: str = name + 'USDT'
    exchange_rates = fetch_exchange_rates(pairs)
    for pair_name, rate in exchange_rates.items():
        data = ExchangeRate(pair=pair_name, rate=rate, timestamp=datetime.datetime.now())
        create_exchange_rates(db=db, data=data)
    course: float | None = exchange_rates.get(pair)

    if course is None:
        raise HTTPException(status_code=404, detail=f"Exchange rates '{name}' not found")

    return {pair: course}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
