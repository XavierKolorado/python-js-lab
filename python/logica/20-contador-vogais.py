"""20. Contador de vogais: conta vogais, inclusive as acentuadas."""

import unicodedata

VOWELS = "aeiou"


def count_vowels(text: str) -> dict[str, int]:
    decomposed = unicodedata.normalize("NFD", text.casefold())
    counts = dict.fromkeys(VOWELS, 0)
    for char in decomposed:
        if char in counts:
            counts[char] += 1
    return counts


def main() -> None:
    counts = count_vowels(input("Frase: "))
    print(f"Total de vogais: {sum(counts.values())}")
    for vowel, amount in counts.items():
        print(f"  {vowel}: {amount}")


if __name__ == "__main__":
    main()
