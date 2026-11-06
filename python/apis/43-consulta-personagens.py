"""43. Consulta de personagens: usa a Rick and Morty API.

Uso: python 43-consulta-personagens.py rick
"""

import sys

import requests

CHARACTERS_URL = "https://rickandmortyapi.com/api/character/"
TIMEOUT_SECONDS = 10
MAX_RESULTS = 10


def search_characters(name: str) -> tuple[int, list[dict]]:
    if not name.strip():
        raise ValueError("Informe parte do nome de um personagem.")
    response = requests.get(CHARACTERS_URL, params={"name": name.strip()}, timeout=TIMEOUT_SECONDS)
    # Esta API usa o status 404 para buscas sem resultado.
    if response.status_code == 404:
        return 0, []
    response.raise_for_status()
    data = response.json()
    return data["info"]["count"], data["results"]


def format_character(character: dict) -> str:
    return f"{character['name']} ({character['species']}, {character['status']})"


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else input("Nome do personagem: ")
    try:
        total, characters = search_characters(name)
    except ValueError as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a API: {error}")
        return 1
    if not characters:
        print("Nenhum personagem encontrado.")
        return 0
    print(f"{total} resultado(s). Primeiros {min(MAX_RESULTS, len(characters))}:")
    for character in characters[:MAX_RESULTS]:
        print(f"- {format_character(character)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
