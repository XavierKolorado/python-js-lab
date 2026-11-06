"""39. Sistema de biblioteca: cadastra livros, empréstimos e devoluções.

Uso: python 39-sistema-biblioteca.py [arquivo.json]
"""

import json
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "biblioteca.json"
MENU = """
1. Cadastrar livro
2. Listar livros
3. Emprestar livro
4. Devolver livro
0. Sair"""


class Library:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.books: list[dict] = []
        if path.exists():
            try:
                self.books = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise ValueError(f"{path.name} contém JSON inválido.") from error

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        content = json.dumps(self.books, ensure_ascii=False, indent=2)
        self.path.write_text(content, encoding="utf-8")

    def _find(self, title: str) -> dict:
        needle = title.strip().casefold()
        for book in self.books:
            if book["title"].casefold() == needle:
                return book
        raise KeyError(f"Livro não encontrado: {title.strip()}")

    def add_book(self, title: str, author: str) -> None:
        clean_title, clean_author = title.strip(), author.strip()
        if not clean_title or not clean_author:
            raise ValueError("Título e autoria são obrigatórios.")
        if any(book["title"].casefold() == clean_title.casefold() for book in self.books):
            raise ValueError("Livro já cadastrado.")
        self.books.append({"title": clean_title, "author": clean_author, "borrower": None})
        self._save()

    def lend(self, title: str, borrower: str) -> None:
        book = self._find(title)
        clean_borrower = borrower.strip()
        if not clean_borrower:
            raise ValueError("Informe quem está pegando o livro.")
        if book["borrower"]:
            raise ValueError(f"Livro já emprestado para {book['borrower']}.")
        book["borrower"] = clean_borrower
        self._save()

    def give_back(self, title: str) -> None:
        book = self._find(title)
        if not book["borrower"]:
            raise ValueError("Este livro não está emprestado.")
        book["borrower"] = None
        self._save()


def print_books(books: list[dict]) -> None:
    if not books:
        print("Nenhum livro cadastrado.")
    for book in books:
        status = f"emprestado para {book['borrower']}" if book["borrower"] else "disponível"
        print(f"- {book['title']} ({book['author']}): {status}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        library = Library(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                library.add_book(input("Título: "), input("Autoria: "))
                print("Livro cadastrado.")
            elif option == "2":
                print_books(library.books)
            elif option == "3":
                library.lend(input("Título: "), input("Pessoa: "))
                print("Empréstimo registrado.")
            elif option == "4":
                library.give_back(input("Título: "))
                print("Devolução registrada.")
            elif option == "0":
                print("Até logo!")
                return 0
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    sys.exit(main())
