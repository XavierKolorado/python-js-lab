"""04. Média de notas: lê três notas de 0 a 10 e calcula a média."""

MIN_GRADE = 0.0
MAX_GRADE = 10.0
GRADE_COUNT = 3


def parse_grade(raw_grade: str) -> float:
    grade = float(raw_grade.strip().replace(",", "."))
    if not MIN_GRADE <= grade <= MAX_GRADE:
        raise ValueError("A nota está fora do intervalo.")
    return grade


def calculate_average(grades: list[float]) -> float:
    if not grades:
        raise ValueError("Informe ao menos uma nota.")
    return sum(grades) / len(grades)


def read_grade(position: int) -> float:
    while True:
        try:
            return parse_grade(input(f"Nota {position}: "))
        except ValueError:
            print(f"Nota inválida. Digite um valor de {MIN_GRADE:g} a {MAX_GRADE:g}.")


def main() -> None:
    grades = [read_grade(position) for position in range(1, GRADE_COUNT + 1)]
    print(f"Média: {calculate_average(grades):.2f}")


if __name__ == "__main__":
    main()
