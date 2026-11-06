"""37. Validador de e-mails: confere o formato, não a existência da caixa postal."""

import re

MAX_EMAIL_LENGTH = 254
EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}"
)


def is_valid_email(email: str) -> bool:
    candidate = email.strip()
    if len(candidate) > MAX_EMAIL_LENGTH or ".." in candidate:
        return False
    local_part = candidate.split("@")[0]
    if local_part.startswith(".") or local_part.endswith("."):
        return False
    return EMAIL_PATTERN.fullmatch(candidate) is not None


def main() -> None:
    email = input("E-mail: ")
    print("Formato válido." if is_valid_email(email) else "Formato inválido.")


if __name__ == "__main__":
    main()
