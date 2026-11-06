"""28. Frequência de palavras: conta as ocorrências de cada palavra."""

import re
from collections import Counter

WORD_PATTERN = re.compile(r"[^\W\d_]+(?:-[^\W\d_]+)*")


def word_frequency(text: str) -> Counter:
    return Counter(WORD_PATTERN.findall(text.casefold()))


def main() -> None:
    frequencies = word_frequency(input("Texto: "))
    if not frequencies:
        print("Nenhuma palavra encontrada.")
        return
    for word, amount in frequencies.most_common():
        print(f"{word}: {amount}")


if __name__ == "__main__":
    main()
