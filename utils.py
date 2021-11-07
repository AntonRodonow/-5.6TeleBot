import requests
import json
from config import keys

class APIException(Exception):
    pass

class MoneyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f"Вы пытаетесь конвертировать одинаковые валюты {base}. Инструкция: /help")
        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}, возможно она не внесена в инструменты, см. /help')
        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}, возможно она не внесена в инструменты, см. /help')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f"http://data.fixer.io/api/latest?access_key=26820b9ce2581028a54f0b00ff269c2b&base={quote_tiker}&symbols={base_tiker}")
        total_base = (json.loads(r.content).get("rates")).get(keys[base])

        return total_base