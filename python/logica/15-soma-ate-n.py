"""15. Soma até N: soma todos os inteiros de 1 até o limite informado."""


def sum_up_to(limit: int) -> int:
    if limit < 1:
        raise ValueError("O limite precisa ser maior ou igual a 1.")
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


def read_limit() -> int:
    while True:
        try:
            limit = int(input("Somar de 1 até: ").strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if limit >= 1:
            return limit
        print("O limite precisa ser maior ou igual a 1.")


def main() -> None:
    limit = read_limit()
    print(f"A soma de 1 até {limit} é {sum_up_to(limit)}.")


if __name__ == "__main__":
    main()
