"""10. Maior número: encontra o maior entre três números usando condições."""

import math


def largest_of_three(first: float, second: float, third: float) -> float:
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest


def read_number(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(number):
            return number
        print("O número precisa ser finito.")


def main() -> None:
    numbers = [read_number(f"Número {position}: ") for position in (1, 2, 3)]
    print(f"Maior número: {largest_of_three(*numbers):g}")


if __name__ == "__main__":
    main()
