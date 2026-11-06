"""25. Separador de números: divide uma lista em pares e ímpares."""


def parse_integers(raw_numbers: str) -> list[int]:
    try:
        return [int(item) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números inteiros separados por espaço.") from error


def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 != 0]
    return even_numbers, odd_numbers


def main() -> None:
    try:
        numbers = parse_integers(input("Inteiros separados por espaço: "))
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return
    even_numbers, odd_numbers = split_even_odd(numbers)
    print(f"Pares: {even_numbers}")
    print(f"Ímpares: {odd_numbers}")


if __name__ == "__main__":
    main()
