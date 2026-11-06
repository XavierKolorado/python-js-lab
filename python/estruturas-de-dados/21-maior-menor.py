"""21. Maior e menor: percorre uma lista uma única vez."""

import math


def parse_numbers(raw_numbers: str) -> list[float]:
    try:
        numbers = [float(item.replace(",", ".")) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números separados por espaço.") from error
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("use apenas números finitos.")
    return numbers


def find_min_max(numbers: list[float]) -> tuple[float, float]:
    if not numbers:
        raise ValueError("A lista está vazia.")
    smallest = largest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return smallest, largest


def main() -> None:
    try:
        numbers = parse_numbers(input("Números separados por espaço: "))
        smallest, largest = find_min_max(numbers)
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return
    print(f"Menor: {smallest:g}")
    print(f"Maior: {largest:g}")


if __name__ == "__main__":
    main()
