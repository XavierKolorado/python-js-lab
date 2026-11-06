"""13. Contador: conta de 1 até 100 usando repetição."""

LIMIT = 100
NUMBERS_PER_LINE = 10


def count_up_to(limit: int) -> list[int]:
    numbers = []
    current = 1
    while current <= limit:
        numbers.append(current)
        current += 1
    return numbers


def main() -> None:
    numbers = count_up_to(LIMIT)
    for start in range(0, len(numbers), NUMBERS_PER_LINE):
        line = numbers[start : start + NUMBERS_PER_LINE]
        print(" ".join(f"{number:3d}" for number in line))


if __name__ == "__main__":
    main()
