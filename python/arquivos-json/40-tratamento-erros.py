"""40. Tratamento de erros: entrada inválida, arquivo inexistente e JSON inválido."""

import json
from pathlib import Path


def parse_age(raw_age: str) -> int:
    try:
        age = int(raw_age)
    except ValueError as error:
        raise ValueError(f"'{raw_age}' não é um número inteiro.") from error
    if age < 0:
        raise ValueError("A idade não pode ser negativa.")
    return age


def read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise ValueError(f"Arquivo não encontrado: {path.name}") from error


def parse_json(raw_json: str) -> object:
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON inválido na linha {error.lineno}, coluna {error.colno}.") from error


def demonstrate(label: str, action, *arguments) -> None:
    try:
        print(f"[ok]   {label}: {action(*arguments)}")
    except ValueError as error:
        print(f"[erro] {label}: {error}")


def main() -> None:
    demonstrate("idade válida", parse_age, "30")
    demonstrate("idade com texto", parse_age, "trinta")
    demonstrate("idade negativa", parse_age, "-1")
    demonstrate("arquivo inexistente", read_text_file, Path("nao-existe.txt"))
    demonstrate("JSON válido", parse_json, '{"linguagem": "Python"}')
    demonstrate("JSON inválido", parse_json, '{"linguagem": }')


if __name__ == "__main__":
    main()
