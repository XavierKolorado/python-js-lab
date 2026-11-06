"""17. Jogo de adivinhação: tenta acertar um número aleatório de 1 a 100.

Uso: python 17-jogo-adivinhacao.py [semente]
A semente opcional repete o mesmo número, o que ajuda em testes e demonstrações.
"""

import random
import sys

LOWEST = 1
HIGHEST = 100


def evaluate_guess(guess: int, secret: int) -> str:
    if guess < secret:
        return "maior"
    if guess > secret:
        return "menor"
    return "acertou"


def read_guess() -> int:
    while True:
        try:
            guess = int(input(f"Palpite ({LOWEST}-{HIGHEST}): ").strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if LOWEST <= guess <= HIGHEST:
            return guess
        print(f"O palpite deve estar entre {LOWEST} e {HIGHEST}.")


def play(secret: int) -> int:
    attempts = 0
    while True:
        attempts += 1
        result = evaluate_guess(read_guess(), secret)
        if result == "acertou":
            return attempts
        print(f"O número secreto é {result}.")


def main() -> None:
    generator = random.Random(sys.argv[1]) if len(sys.argv) > 1 else random.Random()
    attempts = play(generator.randint(LOWEST, HIGHEST))
    print(f"Parabéns! Você acertou em {attempts} tentativa(s).")


if __name__ == "__main__":
    main()
