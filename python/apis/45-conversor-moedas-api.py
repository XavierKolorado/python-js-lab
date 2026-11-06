"""45. Conversor de moedas com API: consulta taxas na Frankfurter.

Uso: python 45-conversor-moedas-api.py 100 USD BRL
"""

import math
import sys

import requests

RATES_URL = "https://api.frankfurter.dev/v1/latest"
TIMEOUT_SECONDS = 10


def validate_currency(code: str) -> str:
    clean_code = code.strip().upper()
    if len(clean_code) != 3 or not clean_code.isalpha():
        raise ValueError(f"Código de moeda inválido: {code}")
    return clean_code


def fetch_rate(source: str, target: str) -> tuple[float, str]:
    parameters = {"base": source, "symbols": target}
    response = requests.get(RATES_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    # A Frankfurter usa 404 ou 422 para moedas que ela não conhece.
    if response.status_code in (404, 422):
        raise LookupError("Moeda não suportada pela API.")
    response.raise_for_status()
    data = response.json()
    return data["rates"][target], data["date"]


def convert(amount: float, source: str, target: str) -> tuple[float, float, str]:
    if not (math.isfinite(amount) and amount >= 0):
        raise ValueError("Informe um valor positivo.")
    source, target = validate_currency(source), validate_currency(target)
    if source == target:
        raise ValueError("Escolha duas moedas diferentes.")
    rate, date = fetch_rate(source, target)
    return amount * rate, rate, date


def main() -> int:
    if len(sys.argv) != 4:
        print("Uso: python 45-conversor-moedas-api.py VALOR ORIGEM DESTINO")
        return 1
    try:
        amount = float(sys.argv[1].replace(",", "."))
        result, rate, date = convert(amount, sys.argv[2], sys.argv[3])
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a API: {error}")
        return 1
    print(f"{amount:.2f} {sys.argv[2].upper()} = {result:.2f} {sys.argv[3].upper()}")
    print(f"Taxa: {rate} (referência de {date})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
