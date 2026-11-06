<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# Python, nível 3: Listas, strings e funções

*Python, level 3: Lists, strings and functions*

[Voltar ao README principal / Back to the main README](../../README.md)

- [21. Maior e menor](21-maior-menor.py)
- [22. Média de uma lista](22-media-lista.py)
- [23. Remover duplicados](23-remover-duplicados.py)
- [24. Ordenação manual](24-ordenacao-manual.py)
- [25. Separador de números](25-separador-numeros.py)
- [26. Verificador de números primos](26-numeros-primos.py)
- [27. Inversor de texto](27-inversor-texto.py)
- [28. Frequência de palavras](28-frequencia-palavras.py)
- [29. Agenda de contatos](29-agenda-contatos.py)
- [30. Gerenciador de estoque](30-gerenciador-estoque.py)

## 21. Maior e menor / Largest and smallest

**Problema:** Encontrar o maior e o menor número de uma lista.  
**Problem:** Find a list's largest and smallest numbers.

**Objetivo:** Percorrer uma lista uma única vez.  
**Goal:** Walk a list only once.

**Conceitos / Concepts:** listas, `split`, tuplas

**Arquivo / File:** [`21-maior-menor.py`](./21-maior-menor.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/21-maior-menor.py
```

**Entradas do exemplo / Example input:** `8 3 15 -2`

**Exemplo de execução / Example run**

```text
Números separados por espaço: Menor: -2
Maior: 15
```

**Resultado esperado:** O menor e o maior valor. Lista vazia gera aviso.  
**Expected result:** Smallest and largest. An empty list gives a warning.

<details><summary>Código completo / Full code: <code>21-maior-menor.py</code></summary>

```python
"""21. Maior e menor: percorre uma lista uma única vez."""

import math


def parse_numbers(raw_numbers: str) -> list[float]:
    try:
        numbers = [float(item.replace(",", ".")) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números separados por espaço.") from error
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("use apenas números finitos.")
    return numbers


def find_min_max(numbers: list[float]) -> tuple[float, float]:
    if not numbers:
        raise ValueError("A lista está vazia.")
    smallest = largest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return smallest, largest


def main() -> None:
    try:
        numbers = parse_numbers(input("Números separados por espaço: "))
        smallest, largest = find_min_max(numbers)
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return
    print(f"Menor: {smallest:g}")
    print(f"Maior: {largest:g}")


if __name__ == "__main__":
    main()
```

</details>

## 22. Média de uma lista / List average

**Problema:** Calcular a média dos valores de uma lista.  
**Problem:** Compute the average of a list.

**Objetivo:** Evitar divisão por zero em listas vazias.  
**Goal:** Avoid division by zero on empty lists.

**Conceitos / Concepts:** `sum`, `len`, exceções

**Arquivo / File:** [`22-media-lista.py`](./22-media-lista.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/22-media-lista.py
```

**Entradas do exemplo / Example input:** `7 8 9 10`

**Exemplo de execução / Example run**

```text
Números separados por espaço: Média de 4 valor(es): 8.50
```

**Resultado esperado:** A média dos valores.  
**Expected result:** The average of the values.

<details><summary>Código completo / Full code: <code>22-media-lista.py</code></summary>

```python
"""22. Média de uma lista: calcula a média dos valores informados."""

import math


def parse_numbers(raw_numbers: str) -> list[float]:
    try:
        numbers = [float(item.replace(",", ".")) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números separados por espaço.") from error
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("use apenas números finitos.")
    return numbers


def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("A lista está vazia.")
    return sum(numbers) / len(numbers)


def main() -> None:
    try:
        numbers = parse_numbers(input("Números separados por espaço: "))
        print(f"Média de {len(numbers)} valor(es): {average(numbers):.2f}")
    except ValueError as error:
        print(f"Entrada inválida: {error}")


if __name__ == "__main__":
    main()
```

</details>

## 23. Remover duplicados / Remove duplicates

**Problema:** Remover elementos repetidos de uma lista.  
**Problem:** Remove repeated items from a list.

**Objetivo:** Usar `set` para consultas rápidas sem perder a ordem.  
**Goal:** Use `set` for fast lookups while keeping order.

**Conceitos / Concepts:** `set`, listas, complexidade

**Arquivo / File:** [`23-remover-duplicados.py`](./23-remover-duplicados.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/23-remover-duplicados.py
```

**Entradas do exemplo / Example input:** `a b a c b`

**Exemplo de execução / Example run**

```text
Itens separados por espaço: Sem duplicados: a b c
Removidos: 2
```

**Resultado esperado:** A lista sem repetições e quantos itens saíram.  
**Expected result:** The list without repeats and how many left.

<details><summary>Código completo / Full code: <code>23-remover-duplicados.py</code></summary>

```python
"""23. Remover duplicados: mantém a primeira ocorrência e a ordem original."""


def remove_duplicates(items: list) -> list:
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items


def main() -> None:
    items = input("Itens separados por espaço: ").split()
    unique_items = remove_duplicates(items)
    print(f"Sem duplicados: {' '.join(unique_items) or '(lista vazia)'}")
    print(f"Removidos: {len(items) - len(unique_items)}")


if __name__ == "__main__":
    main()
```

</details>

## 24. Ordenação manual / Manual sorting

**Problema:** Ordenar uma lista sem utilizar `sort()` ou `sorted()`.  
**Problem:** Sort a list without `sort()` or `sorted()`.

**Objetivo:** Entender o insertion sort.  
**Goal:** Understand insertion sort.

**Conceitos / Concepts:** algoritmos, índices, cópia de listas

**Arquivo / File:** [`24-ordenacao-manual.py`](./24-ordenacao-manual.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/24-ordenacao-manual.py
```

**Entradas do exemplo / Example input:** `5 2 9 1`

**Exemplo de execução / Example run**

```text
Números separados por espaço: Ordenados: 1 2 5 9
```

**Resultado esperado:** Os números em ordem crescente.  
**Expected result:** The numbers in ascending order.

<details><summary>Código completo / Full code: <code>24-ordenacao-manual.py</code></summary>

```python
"""24. Ordenação manual: insertion sort, sem sort() nem sorted()."""

import math


def parse_numbers(raw_numbers: str) -> list[float]:
    try:
        numbers = [float(item.replace(",", ".")) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números separados por espaço.") from error
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("use apenas números finitos.")
    return numbers


def insertion_sort(numbers: list[float]) -> list[float]:
    ordered = numbers.copy()
    for index in range(1, len(ordered)):
        current = ordered[index]
        position = index - 1
        while position >= 0 and ordered[position] > current:
            ordered[position + 1] = ordered[position]
            position -= 1
        ordered[position + 1] = current
    return ordered


def main() -> None:
    try:
        numbers = parse_numbers(input("Números separados por espaço: "))
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return
    if not numbers:
        print("A lista está vazia: nada a ordenar.")
        return
    print("Ordenados:", " ".join(f"{number:g}" for number in insertion_sort(numbers)))


if __name__ == "__main__":
    main()
```

</details>

## 25. Separador de números / Number splitter

**Problema:** Separar números pares e ímpares.  
**Problem:** Split even and odd numbers.

**Objetivo:** Filtrar com list comprehensions.  
**Goal:** Filter with list comprehensions.

**Conceitos / Concepts:** list comprehension, tuplas

**Arquivo / File:** [`25-separador-numeros.py`](./25-separador-numeros.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/25-separador-numeros.py
```

**Entradas do exemplo / Example input:** `1 2 3 4 5 6`

**Exemplo de execução / Example run**

```text
Inteiros separados por espaço: Pares: [2, 4, 6]
Ímpares: [1, 3, 5]
```

**Resultado esperado:** Duas listas: pares e ímpares.  
**Expected result:** Two lists: even and odd.

<details><summary>Código completo / Full code: <code>25-separador-numeros.py</code></summary>

```python
"""25. Separador de números: divide uma lista em pares e ímpares."""


def parse_integers(raw_numbers: str) -> list[int]:
    try:
        return [int(item) for item in raw_numbers.split()]
    except ValueError as error:
        raise ValueError("use apenas números inteiros separados por espaço.") from error


def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 != 0]
    return even_numbers, odd_numbers


def main() -> None:
    try:
        numbers = parse_integers(input("Inteiros separados por espaço: "))
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return
    even_numbers, odd_numbers = split_even_odd(numbers)
    print(f"Pares: {even_numbers}")
    print(f"Ímpares: {odd_numbers}")


if __name__ == "__main__":
    main()
```

</details>

## 26. Verificador de números primos / Prime checker

**Problema:** Criar uma função que identifica números primos.  
**Problem:** Write a function that detects primes.

**Objetivo:** Reduzir trabalho testando até a raiz quadrada.  
**Goal:** Save work by testing up to the square root.

**Conceitos / Concepts:** `math.isqrt`, `all`, geradores

**Arquivo / File:** [`26-numeros-primos.py`](./26-numeros-primos.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/26-numeros-primos.py
```

**Entradas do exemplo / Example input:** `97`

**Exemplo de execução / Example run**

```text
Número inteiro: 97 é primo.
```

**Resultado esperado:** Informa se o número é primo.  
**Expected result:** Says whether the number is prime.

<details><summary>Código completo / Full code: <code>26-numeros-primos.py</code></summary>

```python
"""26. Verificador de números primos: testa divisores até a raiz quadrada."""

import math


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    return all(number % divisor for divisor in range(3, math.isqrt(number) + 1, 2))


def main() -> None:
    try:
        number = int(input("Número inteiro: ").strip())
    except ValueError:
        print("Entrada inválida: digite um número inteiro.")
        return
    verdict = "é" if is_prime(number) else "não é"
    print(f"{number} {verdict} primo.")


if __name__ == "__main__":
    main()
```

</details>

## 27. Inversor de texto / Text reverser

**Problema:** Criar uma função que inverte uma string.  
**Problem:** Write a function that reverses a string.

**Objetivo:** Usar fatiamento com passo negativo.  
**Goal:** Use slicing with a negative step.

**Conceitos / Concepts:** fatiamento, strings

**Arquivo / File:** [`27-inversor-texto.py`](./27-inversor-texto.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/27-inversor-texto.py
```

**Entradas do exemplo / Example input:** `Python`

**Exemplo de execução / Example run**

```text
Texto: Invertido: nohtyP
```

**Resultado esperado:** O texto de trás para frente.  
**Expected result:** The text backwards.

<details><summary>Código completo / Full code: <code>27-inversor-texto.py</code></summary>

```python
"""27. Inversor de texto: inverte uma string usando fatiamento."""


def reverse_text(text: str) -> str:
    return text[::-1]


def main() -> None:
    text = input("Texto: ")
    print(f"Invertido: {reverse_text(text)}")


if __name__ == "__main__":
    main()
```

</details>

## 28. Frequência de palavras / Word frequency

**Problema:** Contar quantas vezes cada palavra aparece em um texto.  
**Problem:** Count how often each word appears.

**Objetivo:** Extrair palavras com regex e contar com `Counter`.  
**Goal:** Extract words with regex and count with `Counter`.

**Conceitos / Concepts:** `re`, `collections.Counter`

**Arquivo / File:** [`28-frequencia-palavras.py`](./28-frequencia-palavras.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/28-frequencia-palavras.py
```

**Entradas do exemplo / Example input:** `o rato roeu a roupa e o rato fugiu`

**Exemplo de execução / Example run**

```text
Texto: o: 2
rato: 2
roeu: 1
a: 1
roupa: 1
e: 1
fugiu: 1
```

**Resultado esperado:** Cada palavra com sua contagem, da mais frequente à menos frequente.  
**Expected result:** Each word with its count, most frequent first.

<details><summary>Código completo / Full code: <code>28-frequencia-palavras.py</code></summary>

```python
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
```

</details>

## 29. Agenda de contatos / Contact book

**Problema:** Cadastrar, listar, pesquisar e excluir contatos.  
**Problem:** Add, list, search and delete contacts.

**Objetivo:** Organizar estado em uma classe e separar a interface.  
**Goal:** Keep state in a class and separate the interface.

**Conceitos / Concepts:** classes, dicionários, menu

**Arquivo / File:** [`29-agenda-contatos.py`](./29-agenda-contatos.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/29-agenda-contatos.py
```

**Entradas do exemplo / Example input:** `1` · `Ana` · `1111-2222` · `3` · `an` · `4` · `Ana` · `2` · `0`

**Exemplo de execução / Example run**

```text

1. Cadastrar
2. Listar
3. Pesquisar
4. Excluir
0. Sair
Opção: Nome: Telefone: Contato cadastrado.

1. Cadastrar
2. Listar
3. Pesquisar
4. Excluir
0. Sair
Opção: Buscar por: - Ana: 1111-2222

1. Cadastrar
2. Listar
3. Pesquisar
4. Excluir
0. Sair
Opção: Nome para excluir: Contato excluído.

1. Cadastrar
2. Listar
3. Pesquisar
4. Excluir
0. Sair
Opção: Nenhum contato encontrado.

1. Cadastrar
... (5 linhas omitidas)
```

**Resultado esperado:** Menu funcional. Os contatos ficam só na memória.  
**Expected result:** A working menu. Contacts stay in memory only.

<details><summary>Código completo / Full code: <code>29-agenda-contatos.py</code></summary>

```python
"""29. Agenda de contatos: cadastra, lista, pesquisa e exclui contatos."""

MENU = """
1. Cadastrar
2. Listar
3. Pesquisar
4. Excluir
0. Sair"""


class ContactBook:
    def __init__(self) -> None:
        self._contacts: dict[str, dict[str, str]] = {}

    def add(self, name: str, phone: str) -> None:
        clean_name, clean_phone = name.strip(), phone.strip()
        if not clean_name or not clean_phone:
            raise ValueError("Nome e telefone são obrigatórios.")
        key = clean_name.casefold()
        if key in self._contacts:
            raise ValueError(f"{clean_name} já está na agenda.")
        self._contacts[key] = {"name": clean_name, "phone": clean_phone}

    def list_all(self) -> list[dict[str, str]]:
        return sorted(self._contacts.values(), key=lambda contact: contact["name"].casefold())

    def search(self, term: str) -> list[dict[str, str]]:
        needle = term.strip().casefold()
        return [contact for contact in self.list_all() if needle in contact["name"].casefold()]

    def delete(self, name: str) -> None:
        if self._contacts.pop(name.strip().casefold(), None) is None:
            raise KeyError(f"{name.strip()} não está na agenda.")


def print_contacts(contacts: list[dict[str, str]]) -> None:
    if not contacts:
        print("Nenhum contato encontrado.")
    for contact in contacts:
        print(f"- {contact['name']}: {contact['phone']}")


def main() -> None:
    book = ContactBook()
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                book.add(input("Nome: "), input("Telefone: "))
                print("Contato cadastrado.")
            elif option == "2":
                print_contacts(book.list_all())
            elif option == "3":
                print_contacts(book.search(input("Buscar por: ")))
            elif option == "4":
                book.delete(input("Nome para excluir: "))
                print("Contato excluído.")
            elif option == "0":
                print("Até logo!")
                return
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    main()
```

</details>

## 30. Gerenciador de estoque / Inventory manager

**Problema:** Cadastrar produtos, atualizar quantidades e consultar estoque.  
**Problem:** Add products, update quantities and query stock.

**Objetivo:** Proteger regras de negócio, como saldo negativo.  
**Goal:** Protect business rules such as negative stock.

**Conceitos / Concepts:** classes, exceções, dicionários

**Arquivo / File:** [`30-gerenciador-estoque.py`](./30-gerenciador-estoque.py)

**Como executar / How to run**

```bash
python python/estruturas-de-dados/30-gerenciador-estoque.py
```

**Entradas do exemplo / Example input:** `1` · `Caneta` · `10` · `2` · `caneta` · `-3` · `2` · `caneta` · `-30` · `4` · `0`

**Exemplo de execução / Example run**

```text

1. Cadastrar produto
2. Atualizar quantidade
3. Consultar produto
4. Listar estoque
0. Sair
Opção: Produto: Quantidade: Produto cadastrado.

1. Cadastrar produto
2. Atualizar quantidade
3. Consultar produto
4. Listar estoque
0. Sair
Opção: Produto: Entrada (+) ou saída (-): Novo saldo: 7

1. Cadastrar produto
2. Atualizar quantidade
3. Consultar produto
4. Listar estoque
0. Sair
Opção: Produto: Entrada (+) ou saída (-): Erro: Estoque insuficiente: há 7 unidade(s).

1. Cadastrar produto
2. Atualizar quantidade
3. Consultar produto
4. Listar estoque
0. Sair
Opção: - caneta: 7

1. Cadastrar produto
... (5 linhas omitidas)
```

**Resultado esperado:** Menu funcional que recusa saída maior que o saldo.  
**Expected result:** A working menu that refuses taking more than the stock.

<details><summary>Código completo / Full code: <code>30-gerenciador-estoque.py</code></summary>

```python
"""30. Gerenciador de estoque: cadastra produtos e controla quantidades."""

MENU = """
1. Cadastrar produto
2. Atualizar quantidade
3. Consultar produto
4. Listar estoque
0. Sair"""


class Inventory:
    def __init__(self) -> None:
        self._products: dict[str, int] = {}

    def add_product(self, name: str, quantity: int) -> None:
        key = name.strip().casefold()
        if not key:
            raise ValueError("O nome do produto é obrigatório.")
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if key in self._products:
            raise ValueError("Produto já cadastrado.")
        self._products[key] = quantity

    def adjust_quantity(self, name: str, delta: int) -> int:
        key = self._existing_key(name)
        new_quantity = self._products[key] + delta
        if new_quantity < 0:
            raise ValueError(f"Estoque insuficiente: há {self._products[key]} unidade(s).")
        self._products[key] = new_quantity
        return new_quantity

    def quantity_of(self, name: str) -> int:
        return self._products[self._existing_key(name)]

    def items(self) -> list[tuple[str, int]]:
        return sorted(self._products.items())

    def _existing_key(self, name: str) -> str:
        key = name.strip().casefold()
        if key not in self._products:
            raise KeyError(f"Produto não encontrado: {name.strip()}")
        return key


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    inventory = Inventory()
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                inventory.add_product(input("Produto: "), read_integer("Quantidade: "))
                print("Produto cadastrado.")
            elif option == "2":
                name = input("Produto: ")
                total = inventory.adjust_quantity(name, read_integer("Entrada (+) ou saída (-): "))
                print(f"Novo saldo: {total}")
            elif option == "3":
                print(f"Quantidade: {inventory.quantity_of(input('Produto: '))}")
            elif option == "4":
                for name, quantity in inventory.items():
                    print(f"- {name}: {quantity}")
                if not inventory.items():
                    print("Estoque vazio.")
            elif option == "0":
                print("Até logo!")
                return
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    main()
```

</details>
