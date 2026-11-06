"""35. Controle financeiro: registra entradas e saídas e calcula o saldo.

Uso: python 35-controle-financeiro.py [arquivo.json]
Valores usam Decimal porque float acumula erros de arredondamento em dinheiro.
"""

import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "financas.json"
INCOME, EXPENSE = "entrada", "saida"
MENU = """
1. Registrar entrada
2. Registrar saída
3. Ver extrato
0. Sair"""


def parse_amount(raw_amount: str) -> Decimal:
    try:
        amount = Decimal(raw_amount.strip().replace(",", "."))
    except InvalidOperation as error:
        raise ValueError("Valor inválido.") from error
    if not amount.is_finite() or amount <= 0:
        raise ValueError("O valor precisa ser maior que zero.")
    return amount.quantize(Decimal("0.01"))


def add_transaction(transactions: list[dict], kind: str, description: str, amount: Decimal) -> None:
    if kind not in (INCOME, EXPENSE):
        raise ValueError("Tipo de lançamento desconhecido.")
    clean_description = description.strip()
    if not clean_description:
        raise ValueError("A descrição é obrigatória.")
    transactions.append({"kind": kind, "description": clean_description, "amount": str(amount)})


def calculate_balance(transactions: list[dict]) -> Decimal:
    balance = Decimal("0.00")
    for transaction in transactions:
        amount = Decimal(transaction["amount"])
        balance += amount if transaction["kind"] == INCOME else -amount
    return balance


def load_transactions(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} contém JSON inválido.") from error


def save_transactions(path: Path, transactions: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(transactions, ensure_ascii=False, indent=2), encoding="utf-8")


def print_statement(transactions: list[dict]) -> None:
    for transaction in transactions:
        sign = "+" if transaction["kind"] == INCOME else "-"
        print(f"{sign} R$ {transaction['amount']:>10}  {transaction['description']}")
    print(f"Saldo: R$ {calculate_balance(transactions)}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        transactions = load_transactions(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    kinds = {"1": INCOME, "2": EXPENSE}
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        if option in kinds:
            try:
                description = input("Descrição: ")
                add_transaction(transactions, kinds[option], description, parse_amount(input("Valor: ")))
                save_transactions(path, transactions)
                print("Lançamento salvo.")
            except ValueError as error:
                print(f"Erro: {error}")
        elif option == "3":
            print_statement(transactions)
        elif option == "0":
            print("Até logo!")
            return 0
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    sys.exit(main())
