"""29. Agenda de contatos: cadastra, lista, pesquisa e exclui contatos."""

MENU = """
1. Cadastrar
2. Listar
3. Pesquisar
4. Excluir
0. Sair"""


class ContactBook:
    def __init__(self) -> None:
        self._contacts: dict[str, dict[str, str]] = {}

    def add(self, name: str, phone: str) -> None:
        clean_name, clean_phone = name.strip(), phone.strip()
        if not clean_name or not clean_phone:
            raise ValueError("Nome e telefone são obrigatórios.")
        key = clean_name.casefold()
        if key in self._contacts:
            raise ValueError(f"{clean_name} já está na agenda.")
        self._contacts[key] = {"name": clean_name, "phone": clean_phone}

    def list_all(self) -> list[dict[str, str]]:
        return sorted(self._contacts.values(), key=lambda contact: contact["name"].casefold())

    def search(self, term: str) -> list[dict[str, str]]:
        needle = term.strip().casefold()
        return [contact for contact in self.list_all() if needle in contact["name"].casefold()]

    def delete(self, name: str) -> None:
        if self._contacts.pop(name.strip().casefold(), None) is None:
            raise KeyError(f"{name.strip()} não está na agenda.")


def print_contacts(contacts: list[dict[str, str]]) -> None:
    if not contacts:
        print("Nenhum contato encontrado.")
    for contact in contacts:
        print(f"- {contact['name']}: {contact['phone']}")


def main() -> None:
    book = ContactBook()
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                book.add(input("Nome: "), input("Telefone: "))
                print("Contato cadastrado.")
            elif option == "2":
                print_contacts(book.list_all())
            elif option == "3":
                print_contacts(book.search(input("Buscar por: ")))
            elif option == "4":
                book.delete(input("Nome para excluir: "))
                print("Contato excluído.")
            elif option == "0":
                print("Até logo!")
                return
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    main()
