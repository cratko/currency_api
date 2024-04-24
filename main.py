from typing import List, Dict
import requests

API_URL = "https://api.freecurrencyapi.com/v1/latest"
API_KEY = "fca_live_Wz0JsuY5r0eBjzy1Hz94n9jvzk8pvNDYJ3JWaVDF"


def get_currencies(base_currency: str) -> Dict:
    payload = {
        "apikey": API_KEY,
        "base_currency": base_currency

    }
    r = requests.get(API_URL, payload)
    return r.json()['data']


def print_currencies(data: Dict) -> None:
    for currency_name, value in data.items():
        print(currency_name, value)


cur = "USD"
while cur != "0":
    print("Rates relative to the " + cur + ": \n")
    print_currencies(get_currencies("USD"))

    cur = input("\nChoose relative currency (0 - to EXIT): ").replace(" ", "")
