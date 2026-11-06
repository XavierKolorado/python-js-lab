"""30. Gerenciador de estoque: cadastra produtos e controla quantidades."""

MENU = """
1. Cadastrar produto
2. Atualizar quantidade
3. Consultar produto
4. Listar estoque
0. Sair"""


class Inventory:
    def __init__(self) -> None:
        self._products: dict[str, int] = {}

    def add_product(self, name: str, quantity: int) -> None:
        key = name.strip().casefold()
        if not key:
            raise ValueError("O nome do produto é obrigatório.")
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if key in self._products:
            raise ValueError("Produto já cadastrado.")
        self._products[key] = quantity

    def adjust_quantity(self, name: str, delta: int) -> int:
        key = self._existing_key(name)
        new_quantity = self._products[key] + delta
        if new_quantity < 0:
            raise ValueError(f"Estoque insuficiente: há {self._products[key]} unidade(s).")
        self._products[key] = new_quantity
        return new_quantity

    def quantity_of(self, name: str) -> int:
        return self._products[self._existing_key(name)]

    def items(self) -> list[tuple[str, int]]:
        return sorted(self._products.items())

    def _existing_key(self, name: str) -> str:
        key = name.strip().casefold()
        if key not in self._products:
            raise KeyError(f"Produto não encontrado: {name.strip()}")
        return key


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    inventory = Inventory()
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                inventory.add_product(input("Produto: "), read_integer("Quantidade: "))
                print("Produto cadastrado.")
            elif option == "2":
                name = input("Produto: ")
                total = inventory.adjust_quantity(name, read_integer("Entrada (+) ou saída (-): "))
                print(f"Novo saldo: {total}")
            elif option == "3":
                print(f"Quantidade: {inventory.quantity_of(input('Produto: '))}")
            elif option == "4":
                for name, quantity in inventory.items():
                    print(f"- {name}: {quantity}")
                if not inventory.items():
                    print("Estoque vazio.")
            elif option == "0":
                print("Até logo!")
                return
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    main()
