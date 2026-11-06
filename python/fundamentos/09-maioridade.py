"""09. Maioridade: verifica se uma pessoa tem 18 anos ou mais."""

LEGAL_AGE = 18
MAX_AGE = 130


def is_adult(age: int) -> bool:
    if not 0 <= age <= MAX_AGE:
        raise ValueError(f"A idade deve estar entre 0 e {MAX_AGE}.")
    return age >= LEGAL_AGE


def read_age() -> int:
    while True:
        try:
            age = int(input("Idade: ").strip())
            is_adult(age)
            return age
        except ValueError:
            print(f"Idade inválida. Digite um inteiro entre 0 e {MAX_AGE}.")


def main() -> None:
    age = read_age()
    if is_adult(age):
        print("Maior de idade.")
    else:
        print(f"Menor de idade. Faltam {LEGAL_AGE - age} ano(s) para os {LEGAL_AGE}.")


if __name__ == "__main__":
    main()
