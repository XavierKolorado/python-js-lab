"""18. Sistema de login: demonstração didática com limite de tentativas.

A credencial de exemplo (aluno / lab-demo) existe só para o exercício. O código
guarda um hash PBKDF2 com salt, nunca o texto puro. Isso não torna a demonstração
um sistema de autenticação real: faltam bloqueio persistente, auditoria e HTTPS.
"""

import getpass
import hashlib
import hmac
import os
import sys

MAX_ATTEMPTS = 3
PBKDF2_ITERATIONS = 200_000
DEMO_USERNAME = "aluno"
DEMO_PASSWORD = "lab-demo"


def hash_password(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ITERATIONS)


def create_account(username: str, password: str) -> dict:
    salt = os.urandom(16)
    return {"username": username, "salt": salt, "hash": hash_password(password, salt)}


def verify_login(account: dict, username: str, password: str) -> bool:
    candidate = hash_password(password, account["salt"])
    same_user = username == account["username"]
    return hmac.compare_digest(candidate, account["hash"]) and same_user


def read_password() -> str:
    # getpass exige um terminal real; com entrada redirecionada, input() é usado.
    return getpass.getpass("Senha: ") if sys.stdin.isatty() else input("Senha: ")


def run_login(account: dict, max_attempts: int = MAX_ATTEMPTS) -> bool:
    for attempt in range(1, max_attempts + 1):
        username = input("Usuário: ").strip()
        if verify_login(account, username, read_password()):
            return True
        print(f"Credenciais inválidas. Tentativa {attempt} de {max_attempts}.")
    return False


def main() -> None:
    account = create_account(DEMO_USERNAME, DEMO_PASSWORD)
    print(f"Login demonstrativo: {DEMO_USERNAME} / {DEMO_PASSWORD}")
    if run_login(account):
        print(f"Acesso liberado. Olá, {DEMO_USERNAME}!")
    else:
        print("Acesso bloqueado: limite de tentativas atingido.")


if __name__ == "__main__":
    main()
