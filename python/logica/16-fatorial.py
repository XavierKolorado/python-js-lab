"""16. Fatorial: calcula n! de forma iterativa."""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def read_non_negative_integer() -> int:
    while True:
        try:
            number = int(input("Número: ").strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if number >= 0:
            return number
        print("O número não pode ser negativo.")


def main() -> None:
    number = read_non_negative_integer()
    print(f"{number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
