"""41. Consulta de CEP: consulta a API ViaCEP.

Uso: python 41-consulta-cep.py 01001-000
"""

import re
import sys

import requests

VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"
TIMEOUT_SECONDS = 10


def normalize_cep(raw_cep: str) -> str:
    digits = re.sub(r"\D", "", raw_cep)
    if len(digits) != 8:
        raise ValueError("O CEP precisa ter 8 dígitos.")
    return digits


def fetch_cep(cep: str) -> dict:
    response = requests.get(VIACEP_URL.format(cep=normalize_cep(cep)), timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    # A ViaCEP responde 200 com {"erro": "true"} quando o CEP não existe.
    if data.get("erro"):
        raise LookupError("CEP não encontrado.")
    return data


def main() -> int:
    raw_cep = sys.argv[1] if len(sys.argv) > 1 else input("CEP: ")
    try:
        address = fetch_cep(raw_cep)
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a ViaCEP: {error}")
        return 1
    print(f"{address['logradouro']}, {address['bairro']}")
    print(f"{address['localidade']}/{address['uf']} - {address['cep']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
