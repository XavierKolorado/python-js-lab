"""27. Inversor de texto: inverte uma string usando fatiamento."""


def reverse_text(text: str) -> str:
    return text[::-1]


def main() -> None:
    text = input("Texto: ")
    print(f"Invertido: {reverse_text(text)}")


if __name__ == "__main__":
    main()
