"""26. Verificador de números primos: testa divisores até a raiz quadrada."""

import math


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    return all(number % divisor for divisor in range(3, math.isqrt(number) + 1, 2))


def main() -> None:
    try:
        number = int(input("Número inteiro: ").strip())
    except ValueError:
        print("Entrada inválida: digite um número inteiro.")
        return
    verdict = "é" if is_prime(number) else "não é"
    print(f"{number} {verdict} primo.")


if __name__ == "__main__":
    main()
