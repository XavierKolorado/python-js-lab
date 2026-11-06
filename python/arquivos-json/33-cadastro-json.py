"""33. Cadastro com JSON: cadastra usuários e persiste os dados.

Uso: python 33-cadastro-json.py [arquivo.json]
"""

import json
import re
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "usuarios.json"
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
MENU = """
1. Cadastrar usuário
2. Listar usuários
0. Sair"""


def load_users(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} contém JSON inválido.") from error


def save_users(path: Path, users: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")


def add_user(users: list[dict], name: str, email: str) -> dict:
    clean_name, clean_email = name.strip(), email.strip().lower()
    if not clean_name:
        raise ValueError("O nome é obrigatório.")
    if not EMAIL_PATTERN.fullmatch(clean_email):
        raise ValueError("E-mail inválido.")
    if any(user["email"] == clean_email for user in users):
        raise ValueError("E-mail já cadastrado.")
    user = {"name": clean_name, "email": clean_email}
    users.append(user)
    return user


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        users = load_users(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        if option == "1":
            try:
                add_user(users, input("Nome: "), input("E-mail: "))
                save_users(path, users)
                print("Usuário salvo.")
            except ValueError as error:
                print(f"Erro: {error}")
        elif option == "2":
            for user in users:
                print(f"- {user['name']} <{user['email']}>")
            if not users:
                print("Nenhum usuário cadastrado.")
        elif option == "0":
            print("Até logo!")
            return 0
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    sys.exit(main())
