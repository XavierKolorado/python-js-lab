"""44. Buscador de endereço: exibe um cartão organizado para cada CEP informado.

Uso: python 44-buscador-endereco.py 01001-000 20040-020
"""

import re
import sys

import requests

VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"
TIMEOUT_SECONDS = 10
ADDRESS_FIELDS = (
    ("CEP", "cep"),
    ("Logradouro", "logradouro"),
    ("Complemento", "complemento"),
    ("Bairro", "bairro"),
    ("Cidade", "localidade"),
    ("Estado", "estado"),
    ("Região", "regiao"),
    ("DDD", "ddd"),
)


def fetch_address(raw_cep: str) -> dict:
    digits = re.sub(r"\D", "", raw_cep)
    if len(digits) != 8:
        raise ValueError(f"CEP inválido: {raw_cep}")
    response = requests.get(VIACEP_URL.format(cep=digits), timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    if data.get("erro"):
        raise LookupError(f"CEP não encontrado: {raw_cep}")
    return data


def format_address(address: dict) -> str:
    width = max(len(label) for label, _ in ADDRESS_FIELDS)
    lines = [
        f"{label:<{width}} : {address[key]}"
        for label, key in ADDRESS_FIELDS
        if address.get(key)
    ]
    return "\n".join(lines)


def main() -> int:
    ceps = sys.argv[1:] or input("CEPs separados por espaço: ").split()
    if not ceps:
        print("Erro: informe ao menos um CEP.")
        return 1
    exit_code = 0
    for cep in ceps:
        try:
            print(format_address(fetch_address(cep)))
        except (ValueError, LookupError) as error:
            print(f"Erro: {error}")
            exit_code = 1
        except requests.RequestException as error:
            print(f"Erro de rede ao consultar a ViaCEP: {error}")
            exit_code = 1
        print()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
