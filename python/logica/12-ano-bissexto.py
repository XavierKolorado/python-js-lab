"""12. Ano bissexto: aplica as regras do calendário gregoriano."""


def is_leap_year(year: int) -> bool:
    if year <= 0:
        raise ValueError("O ano precisa ser positivo.")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def read_year() -> int:
    while True:
        try:
            year = int(input("Ano: ").strip())
            is_leap_year(year)
            return year
        except ValueError:
            print("Valor inválido. Digite um ano inteiro e positivo.")


def main() -> None:
    year = read_year()
    verdict = "é" if is_leap_year(year) else "não é"
    print(f"{year} {verdict} bissexto.")


if __name__ == "__main__":
    main()
