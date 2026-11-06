"""42. Consulta de clima: usa as APIs de geocodificação e previsão da Open-Meteo.

Uso: python 42-consulta-clima.py "São Paulo"
"""

import sys

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT_SECONDS = 10
WEATHER_DESCRIPTIONS = {
    0: "céu limpo",
    1: "predomínio de sol",
    2: "parcialmente nublado",
    3: "nublado",
    45: "neblina",
    48: "neblina com geada",
    51: "garoa fraca",
    53: "garoa moderada",
    55: "garoa intensa",
    61: "chuva fraca",
    63: "chuva moderada",
    65: "chuva forte",
    71: "neve fraca",
    73: "neve moderada",
    75: "neve forte",
    80: "pancadas de chuva fracas",
    81: "pancadas de chuva moderadas",
    82: "pancadas de chuva fortes",
    95: "trovoada",
    96: "trovoada com granizo",
    99: "trovoada forte com granizo",
}


def describe_weather(code: int) -> str:
    return WEATHER_DESCRIPTIONS.get(code, f"condição desconhecida ({code})")


def find_city(name: str) -> dict:
    if not name.strip():
        raise ValueError("Informe o nome de uma cidade.")
    parameters = {"name": name.strip(), "count": 1, "language": "pt"}
    response = requests.get(GEOCODING_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        raise LookupError(f"Cidade não encontrada: {name.strip()}")
    return results[0]


def fetch_current_weather(latitude: float, longitude: float) -> dict:
    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "auto",
    }
    response = requests.get(FORECAST_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()["current"]


def main() -> int:
    city_name = sys.argv[1] if len(sys.argv) > 1 else input("Cidade: ")
    try:
        city = find_city(city_name)
        weather = fetch_current_weather(city["latitude"], city["longitude"])
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a Open-Meteo: {error}")
        return 1
    print(f"{city['name']}, {city.get('country', '')}")
    print(f"Condição: {describe_weather(weather['weather_code'])}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Umidade: {weather['relative_humidity_2m']}%")
    print(f"Vento: {weather['wind_speed_10m']} km/h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
