<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# Python, nível 1: Fundamentos

*Python, level 1: Fundamentals*

[Voltar ao README principal / Back to the main README](../../README.md)

- [01. Mensagem de boas-vindas](01-mensagem-boas-vindas.py)
- [02. Cadastro básico](02-cadastro-basico.py)
- [03. Calculadora de soma](03-calculadora-soma.py)
- [04. Média de notas](04-media-notas.py)
- [05. Conversor Celsius para Fahrenheit](05-celsius-fahrenheit.py)
- [06. Conversor de moedas](06-conversor-moedas.py)
- [07. Área e perímetro](07-area-perimetro.py)
- [08. Par ou ímpar](08-par-ou-impar.py)
- [09. Maioridade](09-maioridade.py)
- [10. Maior número](10-maior-numero.py)

## 01. Mensagem de boas-vindas / Welcome message

**Problema:** Exibir uma mensagem personalizada no terminal.  
**Problem:** Show a personalized message in the terminal.

**Objetivo:** Ler uma entrada e montar um texto com ela.  
**Goal:** Read input and build text from it.

**Conceitos / Concepts:** `input`, `print`, f-strings, funções

**Arquivo / File:** [`01-mensagem-boas-vindas.py`](./01-mensagem-boas-vindas.py)

**Como executar / How to run**

```bash
python python/fundamentos/01-mensagem-boas-vindas.py
```

**Entradas do exemplo / Example input:** `Ana`

**Exemplo de execução / Example run**

```text
Como você se chama? Olá, Ana! Boas-vindas ao Python & JavaScript Lab.
```

**Resultado esperado:** Saudação com o nome informado, ou com "visitante" se ele ficar em branco.  
**Expected result:** A greeting with the given name, or "visitante" when it is blank.

<details><summary>Código completo / Full code: <code>01-mensagem-boas-vindas.py</code></summary>

```python
"""01. Mensagem de boas-vindas: exibe uma saudação personalizada no terminal."""

DEFAULT_NAME = "visitante"


def build_welcome_message(name: str) -> str:
    clean_name = name.strip() or DEFAULT_NAME
    return f"Olá, {clean_name}! Boas-vindas ao Python & JavaScript Lab."


def main() -> None:
    name = input("Como você se chama? ")
    print(build_welcome_message(name))


if __name__ == "__main__":
    main()
```

</details>

## 02. Cadastro básico / Basic registration

**Problema:** Pedir nome e idade e apresentar os dados organizadamente.  
**Problem:** Ask for name and age and show them neatly.

**Objetivo:** Validar entradas e formatar saídas.  
**Goal:** Validate input and format output.

**Conceitos / Concepts:** `while`, `try/except`, conversão de tipos

**Arquivo / File:** [`02-cadastro-basico.py`](./02-cadastro-basico.py)

**Como executar / How to run**

```bash
python python/fundamentos/02-cadastro-basico.py
```

**Entradas do exemplo / Example input:** `Ana` · `29`

**Exemplo de execução / Example run**

```text
Nome: Idade: --- Cadastro ---
Nome : Ana
Idade: 29 anos
```

**Resultado esperado:** Ficha com nome e idade. Entradas inválidas são pedidas de novo.  
**Expected result:** A profile with name and age. Invalid input is requested again.

<details><summary>Código completo / Full code: <code>02-cadastro-basico.py</code></summary>

```python
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
```

</details>

## 03. Calculadora de soma / Sum calculator

**Problema:** Receber dois números e apresentar a soma.  
**Problem:** Read two numbers and show their sum.

**Objetivo:** Converter texto em número com segurança.  
**Goal:** Convert text to numbers safely.

**Conceitos / Concepts:** `float`, funções, validação

**Arquivo / File:** [`03-calculadora-soma.py`](./03-calculadora-soma.py)

**Como executar / How to run**

```bash
python python/fundamentos/03-calculadora-soma.py
```

**Entradas do exemplo / Example input:** `10` · `2,5`

**Exemplo de execução / Example run**

```text
Primeiro número: Segundo número: 10 + 2.5 = 12.5
```

**Resultado esperado:** A soma dos dois números. Vírgula decimal é aceita.  
**Expected result:** The sum of both numbers. A decimal comma is accepted.

<details><summary>Código completo / Full code: <code>03-calculadora-soma.py</code></summary>

```python
"""03. Calculadora de soma: lê dois números e apresenta a soma."""

import math


def parse_number(raw_value: str) -> float:
    number = float(raw_value.strip().replace(",", "."))
    if not math.isfinite(number):
        raise ValueError("O número precisa ser finito.")
    return number


def read_number(prompt: str) -> float:
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError:
            print("Valor inválido. Digite um número, como 10 ou 2,5.")


def add(first: float, second: float) -> float:
    return first + second


def main() -> None:
    first = read_number("Primeiro número: ")
    second = read_number("Segundo número: ")
    print(f"{first:g} + {second:g} = {add(first, second):g}")


if __name__ == "__main__":
    main()
```

</details>

## 04. Média de notas / Grade average

**Problema:** Receber três notas e calcular a média.  
**Problem:** Read three grades and compute the average.

**Objetivo:** Trabalhar com listas e intervalos válidos.  
**Goal:** Work with lists and valid ranges.

**Conceitos / Concepts:** listas, `sum`, `len`, constantes

**Arquivo / File:** [`04-media-notas.py`](./04-media-notas.py)

**Como executar / How to run**

```bash
python python/fundamentos/04-media-notas.py
```

**Entradas do exemplo / Example input:** `7` · `8,5` · `9`

**Exemplo de execução / Example run**

```text
Nota 1: Nota 2: Nota 3: Média: 8.17
```

**Resultado esperado:** A média com duas casas decimais.  
**Expected result:** The average with two decimal places.

<details><summary>Código completo / Full code: <code>04-media-notas.py</code></summary>

```python
"""04. Média de notas: lê três notas de 0 a 10 e calcula a média."""

MIN_GRADE = 0.0
MAX_GRADE = 10.0
GRADE_COUNT = 3


def parse_grade(raw_grade: str) -> float:
    grade = float(raw_grade.strip().replace(",", "."))
    if not MIN_GRADE <= grade <= MAX_GRADE:
        raise ValueError("A nota está fora do intervalo.")
    return grade


def calculate_average(grades: list[float]) -> float:
    if not grades:
        raise ValueError("Informe ao menos uma nota.")
    return sum(grades) / len(grades)


def read_grade(position: int) -> float:
    while True:
        try:
            return parse_grade(input(f"Nota {position}: "))
        except ValueError:
            print(f"Nota inválida. Digite um valor de {MIN_GRADE:g} a {MAX_GRADE:g}.")


def main() -> None:
    grades = [read_grade(position) for position in range(1, GRADE_COUNT + 1)]
    print(f"Média: {calculate_average(grades):.2f}")


if __name__ == "__main__":
    main()
```

</details>

## 05. Conversor Celsius para Fahrenheit / Celsius to Fahrenheit converter

**Problema:** Converter temperaturas utilizando a fórmula correta.  
**Problem:** Convert temperatures with the correct formula.

**Objetivo:** Aplicar uma fórmula e um limite físico.  
**Goal:** Apply a formula and a physical limit.

**Conceitos / Concepts:** expressões, exceções, `math.isfinite`

**Arquivo / File:** [`05-celsius-fahrenheit.py`](./05-celsius-fahrenheit.py)

**Como executar / How to run**

```bash
python python/fundamentos/05-celsius-fahrenheit.py
```

**Entradas do exemplo / Example input:** `25`

**Exemplo de execução / Example run**

```text
Temperatura em °C: 25.0 °C = 77.0 °F
```

**Resultado esperado:** A temperatura em °F. Valores abaixo do zero absoluto são recusados.  
**Expected result:** The temperature in °F. Values below absolute zero are rejected.

<details><summary>Código completo / Full code: <code>05-celsius-fahrenheit.py</code></summary>

```python
"""05. Conversor Celsius para Fahrenheit: aplica F = C * 9/5 + 32."""

import math

ABSOLUTE_ZERO_CELSIUS = -273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("A temperatura está abaixo do zero absoluto.")
    return celsius * 9 / 5 + 32


def read_celsius() -> float:
    while True:
        try:
            celsius = float(input("Temperatura em °C: ").strip().replace(",", "."))
            if not math.isfinite(celsius):
                raise ValueError("A temperatura precisa ser finita.")
            celsius_to_fahrenheit(celsius)
            return celsius
        except ValueError:
            print(f"Valor inválido. Digite um número a partir de {ABSOLUTE_ZERO_CELSIUS}.")


def main() -> None:
    celsius = read_celsius()
    print(f"{celsius:.1f} °C = {celsius_to_fahrenheit(celsius):.1f} °F")


if __name__ == "__main__":
    main()
```

</details>

## 06. Conversor de moedas / Currency converter

**Problema:** Converter reais para dólares usando uma cotação informada pelo usuário.  
**Problem:** Convert reais to dollars with a rate given by the user.

**Objetivo:** Separar cálculo e interação.  
**Goal:** Separate calculation from interaction.

**Conceitos / Concepts:** funções, formatação numérica, validação

**Arquivo / File:** [`06-conversor-moedas.py`](./06-conversor-moedas.py)

**Como executar / How to run**

```bash
python python/fundamentos/06-conversor-moedas.py
```

**Entradas do exemplo / Example input:** `100` · `5,25`

**Exemplo de execução / Example run**

```text
Valor em reais (R$): Cotação do dólar (R$ por US$ 1): R$ 100.00 = US$ 19.05 (cotação 5.2500)
```

**Resultado esperado:** O valor em dólares com a cotação usada.  
**Expected result:** The dollar amount with the rate used.

<details><summary>Código completo / Full code: <code>06-conversor-moedas.py</code></summary>

```python
"""06. Conversor de moedas: converte reais para dólares com a cotação informada."""

import math


def convert_brl_to_usd(amount_brl: float, usd_rate: float) -> float:
    if amount_brl < 0:
        raise ValueError("O valor em reais não pode ser negativo.")
    if usd_rate <= 0:
        raise ValueError("A cotação precisa ser maior que zero.")
    return amount_brl / usd_rate


def read_positive_number(prompt: str, allow_zero: bool) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(value) and (value > 0 or (allow_zero and value == 0)):
            return value
        print("O número precisa ser positivo.")


def main() -> None:
    amount_brl = read_positive_number("Valor em reais (R$): ", allow_zero=True)
    usd_rate = read_positive_number("Cotação do dólar (R$ por US$ 1): ", allow_zero=False)
    amount_usd = convert_brl_to_usd(amount_brl, usd_rate)
    print(f"R$ {amount_brl:.2f} = US$ {amount_usd:.2f} (cotação {usd_rate:.4f})")


if __name__ == "__main__":
    main()
```

</details>

## 07. Área e perímetro / Area and perimeter

**Problema:** Calcular a área e o perímetro de um retângulo.  
**Problem:** Compute a rectangle's area and perimeter.

**Objetivo:** Retornar mais de um valor de uma função.  
**Goal:** Return more than one value from a function.

**Conceitos / Concepts:** tuplas, desempacotamento

**Arquivo / File:** [`07-area-perimetro.py`](./07-area-perimetro.py)

**Como executar / How to run**

```bash
python python/fundamentos/07-area-perimetro.py
```

**Entradas do exemplo / Example input:** `3` · `4`

**Exemplo de execução / Example run**

```text
Largura: Altura: Área: 12
Perímetro: 14
```

**Resultado esperado:** Área e perímetro do retângulo.  
**Expected result:** The rectangle's area and perimeter.

<details><summary>Código completo / Full code: <code>07-area-perimetro.py</code></summary>

```python
"""07. Área e perímetro: calcula as medidas de um retângulo."""

import math


def rectangle_measures(width: float, height: float) -> tuple[float, float]:
    if width <= 0 or height <= 0:
        raise ValueError("Largura e altura precisam ser maiores que zero.")
    return width * height, 2 * (width + height)


def read_side(prompt: str) -> float:
    while True:
        try:
            side = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if math.isfinite(side) and side > 0:
            return side
        print("A medida precisa ser maior que zero.")


def main() -> None:
    width = read_side("Largura: ")
    height = read_side("Altura: ")
    area, perimeter = rectangle_measures(width, height)
    print(f"Área: {area:g}")
    print(f"Perímetro: {perimeter:g}")


if __name__ == "__main__":
    main()
```

</details>

## 08. Par ou ímpar / Even or odd

**Problema:** Identificar se um número é par ou ímpar.  
**Problem:** Tell whether a number is even or odd.

**Objetivo:** Usar o operador de resto.  
**Goal:** Use the remainder operator.

**Conceitos / Concepts:** operador `%`, expressão condicional

**Arquivo / File:** [`08-par-ou-impar.py`](./08-par-ou-impar.py)

**Como executar / How to run**

```bash
python python/fundamentos/08-par-ou-impar.py
```

**Entradas do exemplo / Example input:** `7`

**Exemplo de execução / Example run**

```text
Digite um número inteiro: 7 é ímpar.
```

**Resultado esperado:** Uma frase com a paridade do número.  
**Expected result:** A sentence with the number's parity.

<details><summary>Código completo / Full code: <code>08-par-ou-impar.py</code></summary>

```python
"""08. Par ou ímpar: identifica a paridade de um número inteiro."""


def parity(number: int) -> str:
    return "par" if number % 2 == 0 else "ímpar"


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    number = read_integer("Digite um número inteiro: ")
    print(f"{number} é {parity(number)}.")


if __name__ == "__main__":
    main()
```

</details>

## 09. Maioridade / Legal age

**Problema:** Verificar se uma pessoa é maior de idade.  
**Problem:** Check whether a person is an adult.

**Objetivo:** Escrever condições com constantes nomeadas.  
**Goal:** Write conditions with named constants.

**Conceitos / Concepts:** `if/else`, constantes, booleanos

**Arquivo / File:** [`09-maioridade.py`](./09-maioridade.py)

**Como executar / How to run**

```bash
python python/fundamentos/09-maioridade.py
```

**Entradas do exemplo / Example input:** `16`

**Exemplo de execução / Example run**

```text
Idade: Menor de idade. Faltam 2 ano(s) para os 18.
```

**Resultado esperado:** Maior ou menor de idade, com os anos que faltam.  
**Expected result:** Adult or minor, with the years left.

<details><summary>Código completo / Full code: <code>09-maioridade.py</code></summary>

```python
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
```

</details>

## 10. Maior número / Largest number

**Problema:** Encontrar o maior entre três números.  
**Problem:** Find the largest of three numbers.

**Objetivo:** Comparar valores com condições.  
**Goal:** Compare values with conditions.

**Conceitos / Concepts:** `if`, comparação, list comprehension

**Arquivo / File:** [`10-maior-numero.py`](./10-maior-numero.py)

**Como executar / How to run**

```bash
python python/fundamentos/10-maior-numero.py
```

**Entradas do exemplo / Example input:** `4` · `19` · `7`

**Exemplo de execução / Example run**

```text
Número 1: Número 2: Número 3: Maior número: 19
```

**Resultado esperado:** O maior número informado.  
**Expected result:** The largest number entered.

<details><summary>Código completo / Full code: <code>10-maior-numero.py</code></summary>

```python
"""10. Maior número: encontra o maior entre três números usando condições."""

import math


def largest_of_three(first: float, second: float, third: float) -> float:
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest


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


def main() -> None:
    numbers = [read_number(f"Número {position}: ") for position in (1, 2, 3)]
    print(f"Maior número: {largest_of_three(*numbers):g}")


if __name__ == "__main__":
    main()
```

</details>
