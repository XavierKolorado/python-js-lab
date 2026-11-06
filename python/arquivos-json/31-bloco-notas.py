"""31. Bloco de notas: salva e lê textos em arquivos .txt.

Uso: python 31-bloco-notas.py [pasta]
"""

import re
import sys
from pathlib import Path

DEFAULT_DIRECTORY = Path(__file__).resolve().parent / "dados" / "notas"
NOTE_NAME_PATTERN = re.compile(r"[\w -]+")
MENU = """
1. Escrever nota
2. Ler nota
3. Listar notas
0. Sair"""


def note_path(directory: Path, name: str) -> Path:
    clean_name = name.strip()
    # A lista de caracteres aceitos impede nomes como ../../segredo.
    if not NOTE_NAME_PATTERN.fullmatch(clean_name):
        raise ValueError("Use apenas letras, números, espaços, - e _ no nome.")
    return directory / f"{clean_name}.txt"


def save_note(directory: Path, name: str, text: str) -> Path:
    path = note_path(directory, name)
    directory.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as note_file:
        note_file.write(text + "\n")
    return path


def read_note(directory: Path, name: str) -> str:
    return note_path(directory, name).read_text(encoding="utf-8")


def list_notes(directory: Path) -> list[str]:
    return sorted(path.stem for path in directory.glob("*.txt"))


def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIRECTORY
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                path = save_note(directory, input("Nome da nota: "), input("Texto: "))
                print(f"Nota salva em {path.name}.")
            elif option == "2":
                print(read_note(directory, input("Nome da nota: ")), end="")
            elif option == "3":
                print("\n".join(list_notes(directory)) or "Nenhuma nota salva.")
            elif option == "0":
                print("Até logo!")
                return
            else:
                print("Opção inválida.")
        except ValueError as error:
            print(f"Erro: {error}")
        except FileNotFoundError:
            print("Erro: essa nota não existe.")


if __name__ == "__main__":
    main()
