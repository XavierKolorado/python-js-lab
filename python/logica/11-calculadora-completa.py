"""11. Calculadora completa: soma, subtração, multiplicação e divisão."""

import math
import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(first: float, symbol: str, second: float) -> float:
    if symbol not in OPERATIONS:
        raise ValueError(f"Operação desconhecida: {symbol}")
    return OPERATIONS[symbol](first, second)


def read_number(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(number):
            return number
        print("O número precisa ser finito.")


def read_operation() -> str:
    while True:
        symbol = input("Operação (+ - * /): ").strip()
        if symbol in OPERATIONS:
            return symbol
        print("Operação inválida.")


def main() -> None:
    first = read_number("Primeiro número: ")
    symbol = read_operation()
    second = read_number("Segundo número: ")
    try:
        print(f"{first:g} {symbol} {second:g} = {calculate(first, symbol, second):g}")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")


if __name__ == "__main__":
    main()
