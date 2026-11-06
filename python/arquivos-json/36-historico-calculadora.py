"""36. Histórico de calculadora: salva as operações realizadas em um arquivo.

Uso: python 36-historico-calculadora.py [arquivo.txt]
Digite expressões como 8 * 2. Comandos: historico, limpar, sair.
"""

import operator
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "historico.txt"
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def evaluate(expression: str) -> str:
    parts = expression.replace(",", ".").split()
    if len(parts) != 3 or parts[1] not in OPERATIONS:
        raise ValueError("Use o formato: número operador número.")
    try:
        first, symbol, second = float(parts[0]), parts[1], float(parts[2])
    except ValueError as error:
        raise ValueError("Use o formato: número operador número.") from error
    result = OPERATIONS[symbol](first, second)
    return f"{first:g} {symbol} {second:g} = {result:g}"


def append_history(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as history_file:
        history_file.write(line + "\n")


def read_history(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    print("Digite uma expressão, ou: historico, limpar, sair.")
    while True:
        command = input("> ").strip()
        if command == "sair":
            print("Até logo!")
            return
        if command == "historico":
            print("\n".join(read_history(path)) or "Histórico vazio.")
        elif command == "limpar":
            path.unlink(missing_ok=True)
            print("Histórico apagado.")
        else:
            try:
                line = evaluate(command)
                append_history(path, line)
                print(line)
            except ZeroDivisionError:
                print("Erro: não é possível dividir por zero.")
            except ValueError as error:
                print(f"Erro: {error}")


if __name__ == "__main__":
    main()
