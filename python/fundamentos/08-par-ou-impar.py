"""08. Par ou ímpar: identifica a paridade de um número inteiro."""


def parity(number: int) -> str:
    return "par" if number % 2 == 0 else "ímpar"


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    number = read_integer("Digite um número inteiro: ")
    print(f"{number} é {parity(number)}.")


if __name__ == "__main__":
    main()
