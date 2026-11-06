"""02. Cadastro básico: lê nome e idade e apresenta os dados organizados."""

MAX_AGE = 130


def parse_age(raw_age: str) -> int:
    age = int(raw_age.strip())
    if not 0 <= age <= MAX_AGE:
        raise ValueError(f"A idade deve estar entre 0 e {MAX_AGE}.")
    return age


def format_profile(name: str, age: int) -> str:
    plural_suffix = "" if age == 1 else "s"
    return "\n".join(
        [
            "--- Cadastro ---",
            f"Nome : {name}",
            f"Idade: {age} ano{plural_suffix}",
        ]
    )


def read_name() -> str:
    while True:
        name = input("Nome: ").strip()
        if name:
            return name
        print("O nome não pode ficar em branco.")


def read_age() -> int:
    while True:
        try:
            return parse_age(input("Idade: "))
        except ValueError:
            print(f"Idade inválida. Digite um inteiro entre 0 e {MAX_AGE}.")


def main() -> None:
    name = read_name()
    age = read_age()
    print(format_profile(name, age))


if __name__ == "__main__":
    main()
