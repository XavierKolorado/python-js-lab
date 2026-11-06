"""50. Sistema CLI completo: cadastro, login demonstrativo e notas por usuário.

Uso: python 50-sistema-cli.py [arquivo.json]

Senhas são gravadas como hash PBKDF2 com salt individual. Isso protege contra a
leitura direta do arquivo, mas o projeto continua didático: um sistema real
precisa de controle de sessão, limite de tentativas e armazenamento protegido.
"""

import getpass
import hashlib
import hmac
import json
import os
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "sistema.json"
PBKDF2_ITERATIONS = 200_000
MIN_PASSWORD_LENGTH = 8
GUEST_MENU = """
1. Criar conta
2. Entrar
0. Sair"""
USER_MENU = """
1. Adicionar nota
2. Listar notas
3. Excluir nota
4. Sair da conta"""


def hash_password(password: str, salt: bytes) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ITERATIONS).hex()


class AppStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.users: dict[str, dict] = {}
        if path.exists():
            try:
                self.users = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise ValueError(f"{path.name} contém JSON inválido.") from error

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.users, ensure_ascii=False, indent=2), encoding="utf-8")

    def register(self, username: str, password: str) -> None:
        clean_username = username.strip().lower()
        if not clean_username.isalnum():
            raise ValueError("O usuário deve conter apenas letras e números.")
        if clean_username in self.users:
            raise ValueError("Usuário já existe.")
        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValueError(f"A senha precisa de ao menos {MIN_PASSWORD_LENGTH} caracteres.")
        salt = os.urandom(16)
        self.users[clean_username] = {
            "salt": salt.hex(),
            "password_hash": hash_password(password, salt),
            "notes": [],
        }
        self.save()

    def authenticate(self, username: str, password: str) -> str | None:
        clean_username = username.strip().lower()
        user = self.users.get(clean_username)
        if user is None:
            return None
        candidate = hash_password(password, bytes.fromhex(user["salt"]))
        return clean_username if hmac.compare_digest(candidate, user["password_hash"]) else None

    def add_note(self, username: str, text: str) -> None:
        if not text.strip():
            raise ValueError("A nota não pode ficar vazia.")
        self.users[username]["notes"].append(text.strip())
        self.save()

    def notes_of(self, username: str) -> list[str]:
        return self.users[username]["notes"]

    def delete_note(self, username: str, position: int) -> None:
        notes = self.notes_of(username)
        if not 1 <= position <= len(notes):
            raise ValueError("Nota inexistente.")
        notes.pop(position - 1)
        self.save()


def read_password() -> str:
    return getpass.getpass("Senha: ") if sys.stdin.isatty() else input("Senha: ")


def user_session(store: AppStore, username: str) -> None:
    while True:
        print(USER_MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                store.add_note(username, input("Nota: "))
                print("Nota salva.")
            elif option == "2":
                for position, note in enumerate(store.notes_of(username), start=1):
                    print(f"{position}. {note}")
                if not store.notes_of(username):
                    print("Nenhuma nota.")
            elif option == "3":
                raw_position = input("Número da nota: ").strip()
                if not raw_position.isdigit():
                    raise ValueError("Digite um número válido.")
                store.delete_note(username, int(raw_position))
                print("Nota excluída.")
            elif option == "4":
                return
            else:
                print("Opção inválida.")
        except ValueError as error:
            print(f"Erro: {error}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        store = AppStore(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(GUEST_MENU)
        option = input("Opção: ").strip()
        if option == "1":
            try:
                store.register(input("Usuário: "), read_password())
                print("Conta criada.")
            except ValueError as error:
                print(f"Erro: {error}")
        elif option == "2":
            username = store.authenticate(input("Usuário: "), read_password())
            if username is None:
                print("Usuário ou senha incorretos.")
            else:
                print(f"Bem-vindo(a), {username}!")
                user_session(store, username)
        elif option == "0":
            print("Até logo!")
            return 0
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    sys.exit(main())
