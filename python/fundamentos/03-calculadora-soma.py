"""03. Calculadora de soma: lê dois números e apresenta a soma."""

import math


def parse_number(raw_value: str) -> float:
    number = float(raw_value.strip().replace(",", "."))
    if not math.isfinite(number):
        raise ValueError("O número precisa ser finito.")
    return number


def read_number(prompt: str) -> float:
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError:
            print("Valor inválido. Digite um número, como 10 ou 2,5.")


def add(first: float, second: float) -> float:
    return first + second


def main() -> None:
    first = read_number("Primeiro número: ")
    second = read_number("Segundo número: ")
    print(f"{first:g} + {second:g} = {add(first, second):g}")


if __name__ == "__main__":
    main()
