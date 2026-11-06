"""14. Tabuada: exibe a tabuada de um número informado."""


def multiplication_table(number: int, last_factor: int = 10) -> list[str]:
    return [
        f"{number} x {factor:2d} = {number * factor}"
        for factor in range(1, last_factor + 1)
    ]


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    number = read_integer("Tabuada de: ")
    print("\n".join(multiplication_table(number)))


if __name__ == "__main__":
    main()
