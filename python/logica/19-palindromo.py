"""19. Palíndromo: ignora acentos, espaços, pontuação e maiúsculas."""

import unicodedata


def normalize_text(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text.casefold())
    return "".join(char for char in decomposed if char.isalnum())


def is_palindrome(text: str) -> bool:
    normalized = normalize_text(text)
    if not normalized:
        raise ValueError("Informe ao menos uma letra ou número.")
    return normalized == normalized[::-1]


def main() -> None:
    text = input("Palavra ou frase: ")
    try:
        verdict = "é" if is_palindrome(text) else "não é"
        print(f'"{text.strip()}" {verdict} um palíndromo.')
    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()
