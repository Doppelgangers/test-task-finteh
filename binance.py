import requests


def fetch_exchange_rates(pairs: list[str]) -> dict[str, float]:
    """
    Получает информацию по валютным парам
    :param pairs: ['BTCUSD', 'ETHUSDT'] # Валюты которые нужно вывести
    :return: {'BTCUSDT': 70000.0} # Возвращает валютные пары
    """
    if pairs is None:
        pairs = ['BTCUSD', 'ETHUSDT']

    url = "https://api.binance.com/api/v3/ticker/price"

    response = requests.get(url)
    data = response.json()
    rates = {item['symbol']: float(item['price']) for item in data if item['symbol'] in pairs}
    return rates
