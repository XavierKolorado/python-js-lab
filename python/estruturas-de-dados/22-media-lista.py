"""22. Média de uma lista: calcula a média dos valores informados."""

import math


def parse_numbers(raw_numbers: str) -> list[float]:
    try:
        numbers = [float(item.replace(",", ".")) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números separados por espaço.") from error
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("use apenas números finitos.")
    return numbers


def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("A lista está vazia.")
    return sum(numbers) / len(numbers)


def main() -> None:
    try:
        numbers = parse_numbers(input("Números separados por espaço: "))
        print(f"Média de {len(numbers)} valor(es): {average(numbers):.2f}")
    except ValueError as error:
        print(f"Entrada inválida: {error}")


if __name__ == "__main__":
    main()
