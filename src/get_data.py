import json

import requests

from src.constants import API_URL, SAVE_DIR
from src.utils import is_internet_connection


def load_currencies_from_api() -> list[dict]:
    response = requests.get(API_URL)
    raw_currencies = response.json()
    return raw_currencies[0]["rates"]


def process_raw_currencies(raw_currencies) -> dict:
    currencies = {}
    for currency in raw_currencies:
        code = currency["code"]
        name = currency["currency"]
        rate = currency["mid"]
        currencies[code] = {"name": name, "rate": rate}
    currencies["PLN"] = {"name": "Złoty polski", "rate": 1.0}
    return currencies


def save_currencies_to_file(currencies) -> None:
    with open(SAVE_DIR, "w") as f:
        json.dump(currencies, f)


def load_currencies_from_file() -> dict:
    with open(SAVE_DIR, "r") as f:
        currencies = json.load(f)
    return currencies


def get_currencies_data() -> dict:
    if is_internet_connection():
        currencies = load_currencies_from_api()
        currencies = process_raw_currencies(currencies)
        save_currencies_to_file(currencies)
    else:
        currencies = load_currencies_from_file()
    return currencies
