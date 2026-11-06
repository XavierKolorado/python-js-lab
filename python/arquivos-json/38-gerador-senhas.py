"""38. Gerador de senhas: usa secrets, próprio para valores sensíveis.

Uso: python 38-gerador-senhas.py --tamanho 20 --sem-simbolos
"""

import argparse
import secrets
import string

MIN_LENGTH = 8
SYMBOLS = "!@#$%&*?-_=+"


def build_character_groups(digits: bool, uppercase: bool, symbols: bool) -> list[str]:
    groups = [string.ascii_lowercase]
    if uppercase:
        groups.append(string.ascii_uppercase)
    if digits:
        groups.append(string.digits)
    if symbols:
        groups.append(SYMBOLS)
    return groups


def generate_password(length: int, groups: list[str]) -> str:
    if length < MIN_LENGTH:
        raise ValueError(f"O tamanho mínimo é {MIN_LENGTH}.")
    # Um caractere de cada grupo garante que todo tipo escolhido apareça.
    characters = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    characters += [secrets.choice(alphabet) for _ in range(length - len(characters))]
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera senhas aleatórias.")
    parser.add_argument("--tamanho", type=int, default=16)
    parser.add_argument("--sem-numeros", action="store_true")
    parser.add_argument("--sem-maiusculas", action="store_true")
    parser.add_argument("--sem-simbolos", action="store_true")
    options = parser.parse_args()
    groups = build_character_groups(
        digits=not options.sem_numeros,
        uppercase=not options.sem_maiusculas,
        symbols=not options.sem_simbolos,
    )
    try:
        print(generate_password(options.tamanho, groups))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
