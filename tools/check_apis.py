"""Check that every public API used by the exercises still answers as expected.

Usage: python tools/check_apis.py
This script creates nothing new: is.gd reuses the existing link for a known URL.
"""

import sys

import requests

TIMEOUT_SECONDS = 15
ENDPOINTS = [
    ("ViaCEP", "https://viacep.com.br/ws/01001000/json/", "logradouro"),
    ("Open-Meteo Geocoding", "https://geocoding-api.open-meteo.com/v1/search?name=Curitiba&count=1", "results"),
    ("Open-Meteo Forecast", "https://api.open-meteo.com/v1/forecast?latitude=-25.4&longitude=-49.2&current=temperature_2m", "current"),
    ("Rick and Morty API", "https://rickandmortyapi.com/api/character/?name=rick", "results"),
    ("Frankfurter", "https://api.frankfurter.dev/v1/latest?base=USD&symbols=BRL", "rates"),
    ("JSONPlaceholder", "https://jsonplaceholder.typicode.com/todos/1", "title"),
    ("httpbin", "https://httpbin.org/get", "url"),
    ("Studio Ghibli API", "https://ghibliapi.vercel.app/films?limit=1", None),
    ("DummyJSON", "https://dummyjson.com/products?limit=1", "products"),
    # is.gd returns the same link for a known URL, so this call creates nothing new.
    ("is.gd", "https://is.gd/create.php?format=json&url=https://www.python.org/", "shorturl"),
]


def check_json(url: str, expected_key: str | None) -> str:
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    if expected_key is not None and expected_key not in data:
        raise ValueError(f"missing key {expected_key}")
    return f"HTTP {response.status_code}"


def main() -> int:
    failures = 0
    for name, url, expected_key in ENDPOINTS:
        try:
            print(f"[ok]   {name}: {check_json(url, expected_key)}")
        except (requests.RequestException, ValueError) as error:
            failures += 1
            print(f"[fail] {name}: {error}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
