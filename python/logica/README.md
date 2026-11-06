<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# Python, nível 2: Condições e loops

*Python, level 2: Conditions and loops*

[Voltar ao README principal / Back to the main README](../../README.md)

- [11. Calculadora completa](11-calculadora-completa.py)
- [12. Ano bissexto](12-ano-bissexto.py)
- [13. Contador](13-contador.py)
- [14. Tabuada](14-tabuada.py)
- [15. Soma até N](15-soma-ate-n.py)
- [16. Fatorial](16-fatorial.py)
- [17. Jogo de adivinhação](17-jogo-adivinhacao.py)
- [18. Sistema de login](18-sistema-login.py)
- [19. Palíndromo](19-palindromo.py)
- [20. Contador de vogais](20-contador-vogais.py)

## 11. Calculadora completa / Full calculator

**Problema:** Implementar soma, subtração, multiplicação e divisão, tratando divisão por zero.  
**Problem:** Add, subtract, multiply and divide, handling division by zero.

**Objetivo:** Trocar uma cadeia de `if` por um dicionário de funções.  
**Goal:** Replace an `if` chain with a dictionary of functions.

**Conceitos / Concepts:** dicionários, módulo `operator`, `ZeroDivisionError`

**Arquivo / File:** [`11-calculadora-completa.py`](./11-calculadora-completa.py)

**Como executar / How to run**

```bash
python python/logica/11-calculadora-completa.py
```

**Entradas do exemplo / Example input:** `8` · `/` · `2`

**Exemplo de execução / Example run**

```text
Primeiro número: Operação (+ - * /): Segundo número: 8 / 2 = 4
```

**Resultado esperado:** O resultado da conta, ou um aviso na divisão por zero.  
**Expected result:** The result, or a warning on division by zero.

<details><summary>Código completo / Full code: <code>11-calculadora-completa.py</code></summary>

```python
"""11. Calculadora completa: soma, subtração, multiplicação e divisão."""

import math
import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(first: float, symbol: str, second: float) -> float:
    if symbol not in OPERATIONS:
        raise ValueError(f"Operação desconhecida: {symbol}")
    return OPERATIONS[symbol](first, second)


def read_number(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(number):
            return number
        print("O número precisa ser finito.")


def read_operation() -> str:
    while True:
        symbol = input("Operação (+ - * /): ").strip()
        if symbol in OPERATIONS:
            return symbol
        print("Operação inválida.")


def main() -> None:
    first = read_number("Primeiro número: ")
    symbol = read_operation()
    second = read_number("Segundo número: ")
    try:
        print(f"{first:g} {symbol} {second:g} = {calculate(first, symbol, second):g}")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")


if __name__ == "__main__":
    main()
```

</details>

## 12. Ano bissexto / Leap year

**Problema:** Identificar se um ano é bissexto.  
**Problem:** Tell whether a year is a leap year.

**Objetivo:** Combinar condições lógicas.  
**Goal:** Combine logical conditions.

**Conceitos / Concepts:** `and`, `or`, operador `%`

**Arquivo / File:** [`12-ano-bissexto.py`](./12-ano-bissexto.py)

**Como executar / How to run**

```bash
python python/logica/12-ano-bissexto.py
```

**Entradas do exemplo / Example input:** `2024`

**Exemplo de execução / Example run**

```text
Ano: 2024 é bissexto.
```

**Resultado esperado:** Informa se o ano é bissexto. 1900 não é; 2000 é.  
**Expected result:** Says if the year is a leap year. 1900 is not; 2000 is.

<details><summary>Código completo / Full code: <code>12-ano-bissexto.py</code></summary>

```python
"""12. Ano bissexto: aplica as regras do calendário gregoriano."""


def is_leap_year(year: int) -> bool:
    if year <= 0:
        raise ValueError("O ano precisa ser positivo.")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def read_year() -> int:
    while True:
        try:
            year = int(input("Ano: ").strip())
            is_leap_year(year)
            return year
        except ValueError:
            print("Valor inválido. Digite um ano inteiro e positivo.")


def main() -> None:
    year = read_year()
    verdict = "é" if is_leap_year(year) else "não é"
    print(f"{year} {verdict} bissexto.")


if __name__ == "__main__":
    main()
```

</details>

## 13. Contador / Counter

**Problema:** Contar de 1 até 100 utilizando repetição.  
**Problem:** Count from 1 to 100 with a loop.

**Objetivo:** Controlar um laço `while`.  
**Goal:** Control a `while` loop.

**Conceitos / Concepts:** `while`, `range`, fatiamento

**Arquivo / File:** [`13-contador.py`](./13-contador.py)

**Como executar / How to run**

```bash
python python/logica/13-contador.py
```

**Exemplo de execução / Example run**

```text
  1   2   3   4   5   6   7   8   9  10
 11  12  13  14  15  16  17  18  19  20
 21  22  23  24  25  26  27  28  29  30
 31  32  33  34  35  36  37  38  39  40
 41  42  43  44  45  46  47  48  49  50
 51  52  53  54  55  56  57  58  59  60
 61  62  63  64  65  66  67  68  69  70
 71  72  73  74  75  76  77  78  79  80
 81  82  83  84  85  86  87  88  89  90
 91  92  93  94  95  96  97  98  99 100
```

**Resultado esperado:** Os números de 1 a 100, dez por linha.  
**Expected result:** Numbers 1 to 100, ten per line.

<details><summary>Código completo / Full code: <code>13-contador.py</code></summary>

```python
"""13. Contador: conta de 1 até 100 usando repetição."""

LIMIT = 100
NUMBERS_PER_LINE = 10


def count_up_to(limit: int) -> list[int]:
    numbers = []
    current = 1
    while current <= limit:
        numbers.append(current)
        current += 1
    return numbers


def main() -> None:
    numbers = count_up_to(LIMIT)
    for start in range(0, len(numbers), NUMBERS_PER_LINE):
        line = numbers[start : start + NUMBERS_PER_LINE]
        print(" ".join(f"{number:3d}" for number in line))


if __name__ == "__main__":
    main()
```

</details>

## 14. Tabuada / Multiplication table

**Problema:** Exibir a tabuada de um número informado.  
**Problem:** Show the multiplication table of a number.

**Objetivo:** Gerar linhas com um laço.  
**Goal:** Generate lines with a loop.

**Conceitos / Concepts:** list comprehension, `range`, formatação

**Arquivo / File:** [`14-tabuada.py`](./14-tabuada.py)

**Como executar / How to run**

```bash
python python/logica/14-tabuada.py
```

**Entradas do exemplo / Example input:** `7`

**Exemplo de execução / Example run**

```text
Tabuada de: 7 x  1 = 7
7 x  2 = 14
7 x  3 = 21
7 x  4 = 28
7 x  5 = 35
7 x  6 = 42
7 x  7 = 49
7 x  8 = 56
7 x  9 = 63
7 x 10 = 70
```

**Resultado esperado:** Dez linhas de multiplicação.  
**Expected result:** Ten multiplication lines.

<details><summary>Código completo / Full code: <code>14-tabuada.py</code></summary>

```python
"""14. Tabuada: exibe a tabuada de um número informado."""


def multiplication_table(number: int, last_factor: int = 10) -> list[str]:
    return [
        f"{number} x {factor:2d} = {number * factor}"
        for factor in range(1, last_factor + 1)
    ]


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    number = read_integer("Tabuada de: ")
    print("\n".join(multiplication_table(number)))


if __name__ == "__main__":
    main()
```

</details>

## 15. Soma até N / Sum up to N

**Problema:** Somar todos os números de 1 até um limite informado.  
**Problem:** Add all numbers from 1 to a given limit.

**Objetivo:** Usar um acumulador.  
**Goal:** Use an accumulator.

**Conceitos / Concepts:** `for`, acumulador, validação

**Arquivo / File:** [`15-soma-ate-n.py`](./15-soma-ate-n.py)

**Como executar / How to run**

```bash
python python/logica/15-soma-ate-n.py
```

**Entradas do exemplo / Example input:** `100`

**Exemplo de execução / Example run**

```text
Somar de 1 até: A soma de 1 até 100 é 5050.
```

**Resultado esperado:** A soma de 1 até o limite.  
**Expected result:** The sum from 1 to the limit.

<details><summary>Código completo / Full code: <code>15-soma-ate-n.py</code></summary>

```python
"""15. Soma até N: soma todos os inteiros de 1 até o limite informado."""


def sum_up_to(limit: int) -> int:
    if limit < 1:
        raise ValueError("O limite precisa ser maior ou igual a 1.")
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


def read_limit() -> int:
    while True:
        try:
            limit = int(input("Somar de 1 até: ").strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if limit >= 1:
            return limit
        print("O limite precisa ser maior ou igual a 1.")


def main() -> None:
    limit = read_limit()
    print(f"A soma de 1 até {limit} é {sum_up_to(limit)}.")


if __name__ == "__main__":
    main()
```

</details>

## 16. Fatorial / Factorial

**Problema:** Calcular o fatorial de um número.  
**Problem:** Compute a number's factorial.

**Objetivo:** Tratar casos de borda como 0! e negativos.  
**Goal:** Handle edge cases like 0! and negatives.

**Conceitos / Concepts:** `for`, inteiros grandes, `ValueError`

**Arquivo / File:** [`16-fatorial.py`](./16-fatorial.py)

**Como executar / How to run**

```bash
python python/logica/16-fatorial.py
```

**Entradas do exemplo / Example input:** `5`

**Exemplo de execução / Example run**

```text
Número: 5! = 120
```

**Resultado esperado:** O valor de n!.  
**Expected result:** The value of n!.

<details><summary>Código completo / Full code: <code>16-fatorial.py</code></summary>

```python
"""16. Fatorial: calcula n! de forma iterativa."""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def read_non_negative_integer() -> int:
    while True:
        try:
            number = int(input("Número: ").strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if number >= 0:
            return number
        print("O número não pode ser negativo.")


def main() -> None:
    number = read_non_negative_integer()
    print(f"{number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
```

</details>

## 17. Jogo de adivinhação / Guessing game

**Problema:** Gerar um número aleatório e permitir tentativas até acertar.  
**Problem:** Draw a random number and allow guesses until it is found.

**Objetivo:** Usar `random` e tornar o código testável com uma semente.  
**Goal:** Use `random` and keep code testable with a seed.

**Conceitos / Concepts:** `random`, `while`, `sys.argv`

**Arquivo / File:** [`17-jogo-adivinhacao.py`](./17-jogo-adivinhacao.py)

**Como executar / How to run**

```bash
python python/logica/17-jogo-adivinhacao.py 42
```

**Entradas do exemplo / Example input:** `50` · `75` · `61`

**Exemplo de execução / Example run**

```text
Palpite (1-100): O número secreto é maior.
Palpite (1-100): O número secreto é menor.
Palpite (1-100): Parabéns! Você acertou em 3 tentativa(s).
```

**Resultado esperado:** Dicas de maior ou menor até o acerto, com o total de tentativas.  
**Expected result:** Higher or lower hints until the hit, with the attempt count.

<details><summary>Código completo / Full code: <code>17-jogo-adivinhacao.py</code></summary>

```python
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
```

</details>

## 18. Sistema de login / Login system

**Problema:** Criar um login demonstrativo com limite de tentativas.  
**Problem:** Build a demo login with an attempt limit.

**Objetivo:** Conhecer hash com salt e comparação em tempo constante. É didático, não é autenticação real.  
**Goal:** Learn salted hashing and constant-time comparison. It is a lesson, not real authentication.

**Conceitos / Concepts:** `hashlib.pbkdf2_hmac`, `hmac.compare_digest`, `getpass`

**Arquivo / File:** [`18-sistema-login.py`](./18-sistema-login.py)

**Como executar / How to run**

```bash
python python/logica/18-sistema-login.py
```

**Entradas do exemplo / Example input:** `aluno` · `errada` · `aluno` · `lab-demo`

**Exemplo de execução / Example run**

```text
Login demonstrativo: aluno / lab-demo
Usuário: Senha: Credenciais inválidas. Tentativa 1 de 3.
Usuário: Senha: Acesso liberado. Olá, aluno!
```

**Resultado esperado:** Acesso liberado, ou bloqueio após três erros.  
**Expected result:** Access granted, or a block after three errors.

<details><summary>Código completo / Full code: <code>18-sistema-login.py</code></summary>

```python
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
```

</details>

## 19. Palíndromo / Palindrome

**Problema:** Verificar se uma palavra ou frase é um palíndromo.  
**Problem:** Check whether a word or phrase is a palindrome.

**Objetivo:** Normalizar texto antes de comparar.  
**Goal:** Normalize text before comparing.

**Conceitos / Concepts:** `unicodedata`, fatiamento, `casefold`

**Arquivo / File:** [`19-palindromo.py`](./19-palindromo.py)

**Como executar / How to run**

```bash
python python/logica/19-palindromo.py
```

**Entradas do exemplo / Example input:** `Socorram-me, subi no ônibus em Marrocos`

**Exemplo de execução / Example run**

```text
Palavra ou frase: "Socorram-me, subi no ônibus em Marrocos" é um palíndromo.
```

**Resultado esperado:** Informa se o texto é um palíndromo.  
**Expected result:** Says whether the text is a palindrome.

<details><summary>Código completo / Full code: <code>19-palindromo.py</code></summary>

```python
"""19. Palíndromo: ignora acentos, espaços, pontuação e maiúsculas."""

import unicodedata


def normalize_text(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text.casefold())
    return "".join(char for char in decomposed if char.isalnum())


def is_palindrome(text: str) -> bool:
    normalized = normalize_text(text)
    if not normalized:
        raise ValueError("Informe ao menos uma letra ou número.")
    return normalized == normalized[::-1]


def main() -> None:
    text = input("Palavra ou frase: ")
    try:
        verdict = "é" if is_palindrome(text) else "não é"
        print(f'"{text.strip()}" {verdict} um palíndromo.')
    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()
```

</details>

## 20. Contador de vogais / Vowel counter

**Problema:** Contar quantas vogais existem em uma frase.  
**Problem:** Count the vowels in a sentence.

**Objetivo:** Percorrer strings e usar dicionários como contadores.  
**Goal:** Walk strings and use dictionaries as counters.

**Conceitos / Concepts:** `unicodedata`, `dict.fromkeys`, `for`

**Arquivo / File:** [`20-contador-vogais.py`](./20-contador-vogais.py)

**Como executar / How to run**

```bash
python python/logica/20-contador-vogais.py
```

**Entradas do exemplo / Example input:** `Programação é prática`

**Exemplo de execução / Example run**

```text
Frase: Total de vogais: 9
  a: 5
  e: 1
  i: 1
  o: 2
  u: 0
```

**Resultado esperado:** O total de vogais e a contagem de cada uma.  
**Expected result:** The vowel total and a count for each.

<details><summary>Código completo / Full code: <code>20-contador-vogais.py</code></summary>

```python
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
```

</details>
