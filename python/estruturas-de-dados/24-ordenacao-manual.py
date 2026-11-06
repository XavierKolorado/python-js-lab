"""24. Ordenação manual: insertion sort, sem sort() nem sorted()."""

import math


def parse_numbers(raw_numbers: str) -> list[float]:
    try:
        numbers = [float(item.replace(",", ".")) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números separados por espaço.") from error
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("use apenas números finitos.")
    return numbers


def insertion_sort(numbers: list[float]) -> list[float]:
    ordered = numbers.copy()
    for index in range(1, len(ordered)):
        current = ordered[index]
        position = index - 1
        while position >= 0 and ordered[position] > current:
            ordered[position + 1] = ordered[position]
            position -= 1
        ordered[position + 1] = current
    return ordered


def main() -> None:
    try:
        numbers = parse_numbers(input("Números separados por espaço: "))
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return
    if not numbers:
        print("A lista está vazia: nada a ordenar.")
        return
    print("Ordenados:", " ".join(f"{number:g}" for number in insertion_sort(numbers)))


if __name__ == "__main__":
    main()
