import requests


def is_internet_connection() -> bool:
    try:
        _ = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def convert_currency(amount: float | int, from_rate: float, to_rate: float) -> float:
    return amount * from_rate / to_rate
