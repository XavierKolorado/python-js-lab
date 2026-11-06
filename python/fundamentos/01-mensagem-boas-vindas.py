"""01. Mensagem de boas-vindas: exibe uma saudação personalizada no terminal."""

DEFAULT_NAME = "visitante"


def build_welcome_message(name: str) -> str:
    clean_name = name.strip() or DEFAULT_NAME
    return f"Olá, {clean_name}! Boas-vindas ao Python & JavaScript Lab."


def main() -> None:
    name = input("Como você se chama? ")
    print(build_welcome_message(name))


if __name__ == "__main__":
    main()
