<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# Python, nível 4: Arquivos, JSON e tratamento de erros

*Python, level 4: Files, JSON and error handling*

[Voltar ao README principal / Back to the main README](../../README.md)

- [31. Bloco de notas](31-bloco-notas.py)
- [32. Analisador de arquivos](32-analisador-arquivos.py)
- [33. Cadastro com JSON](33-cadastro-json.py)
- [34. Gerenciador de tarefas](34-gerenciador-tarefas.py)
- [35. Controle financeiro](35-controle-financeiro.py)
- [36. Histórico de calculadora](36-historico-calculadora.py)
- [37. Validador de e-mails](37-validador-emails.py)
- [38. Gerador de senhas](38-gerador-senhas.py)
- [39. Sistema de biblioteca](39-sistema-biblioteca.py)
- [40. Tratamento de erros](40-tratamento-erros.py)

## 31. Bloco de notas / Notepad

**Problema:** Criar um programa que salva e lê textos em arquivos `.txt`.  
**Problem:** Save and read texts in `.txt` files.

**Objetivo:** Ler e gravar arquivos com segurança.  
**Goal:** Read and write files safely.

**Conceitos / Concepts:** `pathlib`, `open`, regex, modos de arquivo

**Arquivo / File:** [`31-bloco-notas.py`](./31-bloco-notas.py)

**Como executar / How to run**

```bash
python python/arquivos-json/31-bloco-notas.py
```

**Entradas do exemplo / Example input:** `1` · `ideias` · `Estudar Python` · `3` · `2` · `ideias` · `0`

**Exemplo de execução / Example run**

```text

1. Escrever nota
2. Ler nota
3. Listar notas
0. Sair
Opção: Nome da nota: Texto: Nota salva em ideias.txt.

1. Escrever nota
2. Ler nota
3. Listar notas
0. Sair
Opção: ideias

1. Escrever nota
2. Ler nota
3. Listar notas
0. Sair
Opção: Nome da nota: Estudar Python

1. Escrever nota
2. Ler nota
3. Listar notas
0. Sair
Opção: Até logo!
```

**Resultado esperado:** Notas salvas em `dados/notas/`. Nomes com `../` são recusados.  
**Expected result:** Notes saved in `dados/notas/`. Names with `../` are rejected.

<details><summary>Código completo / Full code: <code>31-bloco-notas.py</code></summary>

```python
"""31. Bloco de notas: salva e lê textos em arquivos .txt.

Uso: python 31-bloco-notas.py [pasta]
"""

import re
import sys
from pathlib import Path

DEFAULT_DIRECTORY = Path(__file__).resolve().parent / "dados" / "notas"
NOTE_NAME_PATTERN = re.compile(r"[\w -]+")
MENU = """
1. Escrever nota
2. Ler nota
3. Listar notas
0. Sair"""


def note_path(directory: Path, name: str) -> Path:
    clean_name = name.strip()
    # A lista de caracteres aceitos impede nomes como ../../segredo.
    if not NOTE_NAME_PATTERN.fullmatch(clean_name):
        raise ValueError("Use apenas letras, números, espaços, - e _ no nome.")
    return directory / f"{clean_name}.txt"


def save_note(directory: Path, name: str, text: str) -> Path:
    path = note_path(directory, name)
    directory.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as note_file:
        note_file.write(text + "\n")
    return path


def read_note(directory: Path, name: str) -> str:
    return note_path(directory, name).read_text(encoding="utf-8")


def list_notes(directory: Path) -> list[str]:
    return sorted(path.stem for path in directory.glob("*.txt"))


def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIRECTORY
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                path = save_note(directory, input("Nome da nota: "), input("Texto: "))
                print(f"Nota salva em {path.name}.")
            elif option == "2":
                print(read_note(directory, input("Nome da nota: ")), end="")
            elif option == "3":
                print("\n".join(list_notes(directory)) or "Nenhuma nota salva.")
            elif option == "0":
                print("Até logo!")
                return
            else:
                print("Opção inválida.")
        except ValueError as error:
            print(f"Erro: {error}")
        except FileNotFoundError:
            print("Erro: essa nota não existe.")


if __name__ == "__main__":
    main()
```

</details>

## 32. Analisador de arquivos / File analyzer

**Problema:** Contar linhas, palavras e caracteres de um arquivo.  
**Problem:** Count a file's lines, words and characters.

**Objetivo:** Tratar falhas comuns de leitura.  
**Goal:** Handle common read failures.

**Conceitos / Concepts:** `pathlib`, `sys.argv`, exceções

**Arquivo / File:** [`32-analisador-arquivos.py`](./32-analisador-arquivos.py)

**Como executar / How to run**

```bash
python python/arquivos-json/32-analisador-arquivos.py
```

**Exemplo de execução / Example run**

```text
Arquivo: 32-analisador-arquivos.py
Linhas: 43
Palavras: 117
Caracteres: 1170
```

**Resultado esperado:** Estatísticas do arquivo. Sem argumento, analisa o próprio código.  
**Expected result:** File statistics. With no argument, it reads its own code.

<details><summary>Código completo / Full code: <code>32-analisador-arquivos.py</code></summary>

```python
"""32. Analisador de arquivos: conta linhas, palavras e caracteres.

Uso: python 32-analisador-arquivos.py [arquivo]
Sem argumento, o programa analisa o próprio código-fonte.
"""

import sys
from pathlib import Path


def analyze_text(text: str) -> dict[str, int]:
    return {
        "linhas": len(text.splitlines()),
        "palavras": len(text.split()),
        "caracteres": len(text),
    }


def analyze_file(path: Path) -> dict[str, int]:
    return analyze_text(path.read_text(encoding="utf-8"))


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__)
    try:
        statistics = analyze_file(path)
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado: {path}")
        return 1
    except (IsADirectoryError, PermissionError):
        print(f"Erro: não foi possível abrir {path}")
        return 1
    except UnicodeDecodeError:
        print(f"Erro: {path} não é um arquivo de texto UTF-8.")
        return 1
    print(f"Arquivo: {path.name}")
    for label, value in statistics.items():
        print(f"{label.capitalize()}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 33. Cadastro com JSON / JSON registration

**Problema:** Cadastrar usuários e persistir os dados em JSON.  
**Problem:** Register users and persist them as JSON.

**Objetivo:** Serializar dados e preservar arquivos corrompidos.  
**Goal:** Serialize data and leave corrupted files untouched.

**Conceitos / Concepts:** `json`, regex, `pathlib`

**Arquivo / File:** [`33-cadastro-json.py`](./33-cadastro-json.py)

**Como executar / How to run**

```bash
python python/arquivos-json/33-cadastro-json.py
```

**Entradas do exemplo / Example input:** `1` · `Ana` · `ana@example.com` · `2` · `0`

**Exemplo de execução / Example run**

```text

1. Cadastrar usuário
2. Listar usuários
0. Sair
Opção: Nome: E-mail: Usuário salvo.

1. Cadastrar usuário
2. Listar usuários
0. Sair
Opção: - Ana <ana@example.com>

1. Cadastrar usuário
2. Listar usuários
0. Sair
Opção: Até logo!
```

**Resultado esperado:** Usuários salvos em `dados/usuarios.json`.  
**Expected result:** Users saved in `dados/usuarios.json`.

<details><summary>Código completo / Full code: <code>33-cadastro-json.py</code></summary>

```python
"""33. Cadastro com JSON: cadastra usuários e persiste os dados.

Uso: python 33-cadastro-json.py [arquivo.json]
"""

import json
import re
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "usuarios.json"
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
MENU = """
1. Cadastrar usuário
2. Listar usuários
0. Sair"""


def load_users(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} contém JSON inválido.") from error


def save_users(path: Path, users: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")


def add_user(users: list[dict], name: str, email: str) -> dict:
    clean_name, clean_email = name.strip(), email.strip().lower()
    if not clean_name:
        raise ValueError("O nome é obrigatório.")
    if not EMAIL_PATTERN.fullmatch(clean_email):
        raise ValueError("E-mail inválido.")
    if any(user["email"] == clean_email for user in users):
        raise ValueError("E-mail já cadastrado.")
    user = {"name": clean_name, "email": clean_email}
    users.append(user)
    return user


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        users = load_users(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        if option == "1":
            try:
                add_user(users, input("Nome: "), input("E-mail: "))
                save_users(path, users)
                print("Usuário salvo.")
            except ValueError as error:
                print(f"Erro: {error}")
        elif option == "2":
            for user in users:
                print(f"- {user['name']} <{user['email']}>")
            if not users:
                print("Nenhum usuário cadastrado.")
        elif option == "0":
            print("Até logo!")
            return 0
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 34. Gerenciador de tarefas / Task manager

**Problema:** Implementar um CRUD de tarefas com persistência em JSON.  
**Problem:** Build a task CRUD persisted as JSON.

**Objetivo:** Aplicar as quatro operações de um CRUD.  
**Goal:** Apply the four CRUD operations.

**Conceitos / Concepts:** classes, `json`, identificadores

**Arquivo / File:** [`34-gerenciador-tarefas.py`](./34-gerenciador-tarefas.py)

**Como executar / How to run**

```bash
python python/arquivos-json/34-gerenciador-tarefas.py
```

**Entradas do exemplo / Example input:** `1` · `Estudar JSON` · `1` · `Praticar` · `4` · `1` · `5` · `2` · `2` · `0`

**Exemplo de execução / Example run**

```text

1. Criar tarefa
2. Listar tarefas
3. Editar tarefa
4. Concluir tarefa
5. Excluir tarefa
0. Sair
Opção: Título: Tarefa 1 criada.

1. Criar tarefa
2. Listar tarefas
3. Editar tarefa
4. Concluir tarefa
5. Excluir tarefa
0. Sair
Opção: Título: Tarefa 2 criada.

1. Criar tarefa
2. Listar tarefas
3. Editar tarefa
4. Concluir tarefa
5. Excluir tarefa
0. Sair
Opção: Número da tarefa: Tarefa concluída.

1. Criar tarefa
2. Listar tarefas
3. Editar tarefa
4. Concluir tarefa
5. Excluir tarefa
... (18 linhas omitidas)
```

**Resultado esperado:** Tarefas criadas, editadas, concluídas e excluídas, mantidas entre execuções.  
**Expected result:** Tasks created, edited, completed and deleted, kept between runs.

<details><summary>Código completo / Full code: <code>34-gerenciador-tarefas.py</code></summary>

```python
"""34. Gerenciador de tarefas: CRUD com persistência em JSON.

Uso: python 34-gerenciador-tarefas.py [arquivo.json]
"""

import json
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "tarefas.json"
MENU = """
1. Criar tarefa
2. Listar tarefas
3. Editar tarefa
4. Concluir tarefa
5. Excluir tarefa
0. Sair"""


class TaskStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.tasks: list[dict] = self._load()

    def _load(self) -> list[dict]:
        if not self.path.exists():
            return []
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ValueError(f"{self.path.name} contém JSON inválido.") from error

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        content = json.dumps(self.tasks, ensure_ascii=False, indent=2)
        self.path.write_text(content, encoding="utf-8")

    def _find(self, task_id: int) -> dict:
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise KeyError(f"Tarefa {task_id} não encontrada.")

    @staticmethod
    def _clean_title(title: str) -> str:
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("O título é obrigatório.")
        return clean_title

    def create(self, title: str) -> dict:
        next_id = max((task["id"] for task in self.tasks), default=0) + 1
        task = {"id": next_id, "title": self._clean_title(title), "done": False}
        self.tasks.append(task)
        self._save()
        return task

    def update(self, task_id: int, title: str) -> dict:
        task = self._find(task_id)
        task["title"] = self._clean_title(title)
        self._save()
        return task

    def complete(self, task_id: int) -> dict:
        task = self._find(task_id)
        task["done"] = True
        self._save()
        return task

    def delete(self, task_id: int) -> None:
        self.tasks.remove(self._find(task_id))
        self._save()


def print_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['id']}. {task['title']}")


def read_task_id() -> int:
    raw_id = input("Número da tarefa: ").strip()
    if not raw_id.isdigit():
        raise ValueError("Digite um número válido.")
    return int(raw_id)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        store = TaskStore(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                print(f"Tarefa {store.create(input('Título: '))['id']} criada.")
            elif option == "2":
                print_tasks(store.tasks)
            elif option == "3":
                store.update(read_task_id(), input("Novo título: "))
                print("Tarefa atualizada.")
            elif option == "4":
                store.complete(read_task_id())
                print("Tarefa concluída.")
            elif option == "5":
                store.delete(read_task_id())
                print("Tarefa excluída.")
            elif option == "0":
                print("Até logo!")
                return 0
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 35. Controle financeiro / Personal finance

**Problema:** Registrar entradas e saídas e calcular o saldo.  
**Problem:** Record income and expenses and compute the balance.

**Objetivo:** Usar `Decimal` para dinheiro.  
**Goal:** Use `Decimal` for money.

**Conceitos / Concepts:** `decimal`, `json`

**Arquivo / File:** [`35-controle-financeiro.py`](./35-controle-financeiro.py)

**Como executar / How to run**

```bash
python python/arquivos-json/35-controle-financeiro.py
```

**Entradas do exemplo / Example input:** `1` · `Salário` · `1500,50` · `2` · `Mercado` · `320,10` · `3` · `0`

**Exemplo de execução / Example run**

```text

1. Registrar entrada
2. Registrar saída
3. Ver extrato
0. Sair
Opção: Descrição: Valor: Lançamento salvo.

1. Registrar entrada
2. Registrar saída
3. Ver extrato
0. Sair
Opção: Descrição: Valor: Lançamento salvo.

1. Registrar entrada
2. Registrar saída
3. Ver extrato
0. Sair
Opção: + R$    1500.50  Salário
- R$     320.10  Mercado
Saldo: R$ 1180.40

1. Registrar entrada
2. Registrar saída
3. Ver extrato
0. Sair
Opção: Até logo!
```

**Resultado esperado:** Extrato com saldo exato, sem erro de ponto flutuante.  
**Expected result:** A statement with an exact balance, free of float errors.

<details><summary>Código completo / Full code: <code>35-controle-financeiro.py</code></summary>

```python
"""35. Controle financeiro: registra entradas e saídas e calcula o saldo.

Uso: python 35-controle-financeiro.py [arquivo.json]
Valores usam Decimal porque float acumula erros de arredondamento em dinheiro.
"""

import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "financas.json"
INCOME, EXPENSE = "entrada", "saida"
MENU = """
1. Registrar entrada
2. Registrar saída
3. Ver extrato
0. Sair"""


def parse_amount(raw_amount: str) -> Decimal:
    try:
        amount = Decimal(raw_amount.strip().replace(",", "."))
    except InvalidOperation as error:
        raise ValueError("Valor inválido.") from error
    if not amount.is_finite() or amount <= 0:
        raise ValueError("O valor precisa ser maior que zero.")
    return amount.quantize(Decimal("0.01"))


def add_transaction(transactions: list[dict], kind: str, description: str, amount: Decimal) -> None:
    if kind not in (INCOME, EXPENSE):
        raise ValueError("Tipo de lançamento desconhecido.")
    clean_description = description.strip()
    if not clean_description:
        raise ValueError("A descrição é obrigatória.")
    transactions.append({"kind": kind, "description": clean_description, "amount": str(amount)})


def calculate_balance(transactions: list[dict]) -> Decimal:
    balance = Decimal("0.00")
    for transaction in transactions:
        amount = Decimal(transaction["amount"])
        balance += amount if transaction["kind"] == INCOME else -amount
    return balance


def load_transactions(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} contém JSON inválido.") from error


def save_transactions(path: Path, transactions: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(transactions, ensure_ascii=False, indent=2), encoding="utf-8")


def print_statement(transactions: list[dict]) -> None:
    for transaction in transactions:
        sign = "+" if transaction["kind"] == INCOME else "-"
        print(f"{sign} R$ {transaction['amount']:>10}  {transaction['description']}")
    print(f"Saldo: R$ {calculate_balance(transactions)}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        transactions = load_transactions(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    kinds = {"1": INCOME, "2": EXPENSE}
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        if option in kinds:
            try:
                description = input("Descrição: ")
                add_transaction(transactions, kinds[option], description, parse_amount(input("Valor: ")))
                save_transactions(path, transactions)
                print("Lançamento salvo.")
            except ValueError as error:
                print(f"Erro: {error}")
        elif option == "3":
            print_statement(transactions)
        elif option == "0":
            print("Até logo!")
            return 0
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 36. Histórico de calculadora / Calculator history

**Problema:** Salvar operações realizadas em um arquivo.  
**Problem:** Save performed operations to a file.

**Objetivo:** Acrescentar linhas a um arquivo.  
**Goal:** Append lines to a file.

**Conceitos / Concepts:** modo `a`, `pathlib`, `split`

**Arquivo / File:** [`36-historico-calculadora.py`](./36-historico-calculadora.py)

**Como executar / How to run**

```bash
python python/arquivos-json/36-historico-calculadora.py
```

**Entradas do exemplo / Example input:** `8 * 2` · `1 / 0` · `historico` · `sair`

**Exemplo de execução / Example run**

```text
Digite uma expressão, ou: historico, limpar, sair.
> 8 * 2 = 16
> Erro: não é possível dividir por zero.
> 8 * 2 = 16
> Até logo!
```

**Resultado esperado:** Contas válidas ficam no histórico. Erros não são gravados.  
**Expected result:** Valid operations go to history. Errors are not saved.

<details><summary>Código completo / Full code: <code>36-historico-calculadora.py</code></summary>

```python
"""36. Histórico de calculadora: salva as operações realizadas em um arquivo.

Uso: python 36-historico-calculadora.py [arquivo.txt]
Digite expressões como 8 * 2. Comandos: historico, limpar, sair.
"""

import operator
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "historico.txt"
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def evaluate(expression: str) -> str:
    parts = expression.replace(",", ".").split()
    if len(parts) != 3 or parts[1] not in OPERATIONS:
        raise ValueError("Use o formato: número operador número.")
    try:
        first, symbol, second = float(parts[0]), parts[1], float(parts[2])
    except ValueError as error:
        raise ValueError("Use o formato: número operador número.") from error
    result = OPERATIONS[symbol](first, second)
    return f"{first:g} {symbol} {second:g} = {result:g}"


def append_history(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as history_file:
        history_file.write(line + "\n")


def read_history(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    print("Digite uma expressão, ou: historico, limpar, sair.")
    while True:
        command = input("> ").strip()
        if command == "sair":
            print("Até logo!")
            return
        if command == "historico":
            print("\n".join(read_history(path)) or "Histórico vazio.")
        elif command == "limpar":
            path.unlink(missing_ok=True)
            print("Histórico apagado.")
        else:
            try:
                line = evaluate(command)
                append_history(path, line)
                print(line)
            except ZeroDivisionError:
                print("Erro: não é possível dividir por zero.")
            except ValueError as error:
                print(f"Erro: {error}")


if __name__ == "__main__":
    main()
```

</details>

## 37. Validador de e-mails / Email validator

**Problema:** Verificar se um endereço de e-mail possui formato válido.  
**Problem:** Check whether an email address has a valid format.

**Objetivo:** Escrever uma regex e conhecer seus limites.  
**Goal:** Write a regex and know its limits.

**Conceitos / Concepts:** `re.fullmatch`, strings

**Arquivo / File:** [`37-validador-emails.py`](./37-validador-emails.py)

**Como executar / How to run**

```bash
python python/arquivos-json/37-validador-emails.py
```

**Entradas do exemplo / Example input:** `ana@example.com`

**Exemplo de execução / Example run**

```text
E-mail: Formato válido.
```

**Resultado esperado:** Formato válido ou inválido. A existência da caixa postal não é verificada.  
**Expected result:** Valid or invalid format. The mailbox itself is not checked.

<details><summary>Código completo / Full code: <code>37-validador-emails.py</code></summary>

```python
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
```

</details>

## 38. Gerador de senhas / Password generator

**Problema:** Gerar senhas aleatórias com tamanho e caracteres configuráveis.  
**Problem:** Generate random passwords with configurable length and characters.

**Objetivo:** Usar `secrets`, próprio para valores sensíveis, em vez de `random`.  
**Goal:** Use `secrets`, built for sensitive values, instead of `random`.

**Conceitos / Concepts:** `secrets`, `argparse`, `string`

**Arquivo / File:** [`38-gerador-senhas.py`](./38-gerador-senhas.py)

**Como executar / How to run**

```bash
python python/arquivos-json/38-gerador-senhas.py --tamanho 20
```

**Exemplo de execução / Example run**

```text
%+@hGkRadIOBCIlEZk0-
```

**Resultado esperado:** Uma senha com ao menos um caractere de cada tipo escolhido. A saída muda a cada execução.  
**Expected result:** A password with at least one character of each chosen type. Output changes on every run.

<details><summary>Código completo / Full code: <code>38-gerador-senhas.py</code></summary>

```python
"""38. Gerador de senhas: usa secrets, próprio para valores sensíveis.

Uso: python 38-gerador-senhas.py --tamanho 20 --sem-simbolos
"""

import argparse
import secrets
import string

MIN_LENGTH = 8
SYMBOLS = "!@#$%&*?-_=+"


def build_character_groups(digits: bool, uppercase: bool, symbols: bool) -> list[str]:
    groups = [string.ascii_lowercase]
    if uppercase:
        groups.append(string.ascii_uppercase)
    if digits:
        groups.append(string.digits)
    if symbols:
        groups.append(SYMBOLS)
    return groups


def generate_password(length: int, groups: list[str]) -> str:
    if length < MIN_LENGTH:
        raise ValueError(f"O tamanho mínimo é {MIN_LENGTH}.")
    # Um caractere de cada grupo garante que todo tipo escolhido apareça.
    characters = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    characters += [secrets.choice(alphabet) for _ in range(length - len(characters))]
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera senhas aleatórias.")
    parser.add_argument("--tamanho", type=int, default=16)
    parser.add_argument("--sem-numeros", action="store_true")
    parser.add_argument("--sem-maiusculas", action="store_true")
    parser.add_argument("--sem-simbolos", action="store_true")
    options = parser.parse_args()
    groups = build_character_groups(
        digits=not options.sem_numeros,
        uppercase=not options.sem_maiusculas,
        symbols=not options.sem_simbolos,
    )
    try:
        print(generate_password(options.tamanho, groups))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
```

</details>

## 39. Sistema de biblioteca / Library system

**Problema:** Cadastrar livros, registrar empréstimos e devoluções.  
**Problem:** Add books and record loans and returns.

**Objetivo:** Modelar estados e impedir transições inválidas.  
**Goal:** Model states and block invalid transitions.

**Conceitos / Concepts:** classes, `json`, exceções

**Arquivo / File:** [`39-sistema-biblioteca.py`](./39-sistema-biblioteca.py)

**Como executar / How to run**

```bash
python python/arquivos-json/39-sistema-biblioteca.py
```

**Entradas do exemplo / Example input:** `1` · `Dom Casmurro` · `Machado de Assis` · `3` · `Dom Casmurro` · `Ana` · `2` · `4` · `Dom Casmurro` · `2` · `0`

**Exemplo de execução / Example run**

```text

1. Cadastrar livro
2. Listar livros
3. Emprestar livro
4. Devolver livro
0. Sair
Opção: Título: Autoria: Livro cadastrado.

1. Cadastrar livro
2. Listar livros
3. Emprestar livro
4. Devolver livro
0. Sair
Opção: Título: Pessoa: Empréstimo registrado.

1. Cadastrar livro
2. Listar livros
3. Emprestar livro
4. Devolver livro
0. Sair
Opção: - Dom Casmurro (Machado de Assis): emprestado para Ana

1. Cadastrar livro
2. Listar livros
3. Emprestar livro
4. Devolver livro
0. Sair
Opção: Título: Devolução registrada.

1. Cadastrar livro
... (12 linhas omitidas)
```

**Resultado esperado:** Status de cada livro. Um livro emprestado não pode sair de novo.  
**Expected result:** Each book's status. A lent book cannot be lent again.

<details><summary>Código completo / Full code: <code>39-sistema-biblioteca.py</code></summary>

```python
"""39. Sistema de biblioteca: cadastra livros, empréstimos e devoluções.

Uso: python 39-sistema-biblioteca.py [arquivo.json]
"""

import json
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "biblioteca.json"
MENU = """
1. Cadastrar livro
2. Listar livros
3. Emprestar livro
4. Devolver livro
0. Sair"""


class Library:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.books: list[dict] = []
        if path.exists():
            try:
                self.books = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise ValueError(f"{path.name} contém JSON inválido.") from error

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        content = json.dumps(self.books, ensure_ascii=False, indent=2)
        self.path.write_text(content, encoding="utf-8")

    def _find(self, title: str) -> dict:
        needle = title.strip().casefold()
        for book in self.books:
            if book["title"].casefold() == needle:
                return book
        raise KeyError(f"Livro não encontrado: {title.strip()}")

    def add_book(self, title: str, author: str) -> None:
        clean_title, clean_author = title.strip(), author.strip()
        if not clean_title or not clean_author:
            raise ValueError("Título e autoria são obrigatórios.")
        if any(book["title"].casefold() == clean_title.casefold() for book in self.books):
            raise ValueError("Livro já cadastrado.")
        self.books.append({"title": clean_title, "author": clean_author, "borrower": None})
        self._save()

    def lend(self, title: str, borrower: str) -> None:
        book = self._find(title)
        clean_borrower = borrower.strip()
        if not clean_borrower:
            raise ValueError("Informe quem está pegando o livro.")
        if book["borrower"]:
            raise ValueError(f"Livro já emprestado para {book['borrower']}.")
        book["borrower"] = clean_borrower
        self._save()

    def give_back(self, title: str) -> None:
        book = self._find(title)
        if not book["borrower"]:
            raise ValueError("Este livro não está emprestado.")
        book["borrower"] = None
        self._save()


def print_books(books: list[dict]) -> None:
    if not books:
        print("Nenhum livro cadastrado.")
    for book in books:
        status = f"emprestado para {book['borrower']}" if book["borrower"] else "disponível"
        print(f"- {book['title']} ({book['author']}): {status}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        library = Library(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                library.add_book(input("Título: "), input("Autoria: "))
                print("Livro cadastrado.")
            elif option == "2":
                print_books(library.books)
            elif option == "3":
                library.lend(input("Título: "), input("Pessoa: "))
                print("Empréstimo registrado.")
            elif option == "4":
                library.give_back(input("Título: "))
                print("Devolução registrada.")
            elif option == "0":
                print("Até logo!")
                return 0
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as error:
            print(f"Erro: {error.args[0]}")


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 40. Tratamento de erros / Error handling

**Problema:** Demonstrar tratamento de erros de entrada, arquivos inexistentes e JSON inválido.  
**Problem:** Show handling of bad input, missing files and invalid JSON.

**Objetivo:** Capturar exceções específicas e encadeá-las.  
**Goal:** Catch specific exceptions and chain them.

**Conceitos / Concepts:** `try/except`, `raise ... from`, `json`

**Arquivo / File:** [`40-tratamento-erros.py`](./40-tratamento-erros.py)

**Como executar / How to run**

```bash
python python/arquivos-json/40-tratamento-erros.py
```

**Exemplo de execução / Example run**

```text
[ok]   idade válida: 30
[erro] idade com texto: 'trinta' não é um número inteiro.
[erro] idade negativa: A idade não pode ser negativa.
[erro] arquivo inexistente: Arquivo não encontrado: nao-existe.txt
[ok]   JSON válido: {'linguagem': 'Python'}
[erro] JSON inválido: JSON inválido na linha 1, coluna 15.
```

**Resultado esperado:** Linhas `[ok]` e `[erro]` para cada caso, sem encerrar o programa.  
**Expected result:** `[ok]` and `[erro]` lines for each case, without crashing.

<details><summary>Código completo / Full code: <code>40-tratamento-erros.py</code></summary>

```python
"""40. Tratamento de erros: entrada inválida, arquivo inexistente e JSON inválido."""

import json
from pathlib import Path


def parse_age(raw_age: str) -> int:
    try:
        age = int(raw_age)
    except ValueError as error:
        raise ValueError(f"'{raw_age}' não é um número inteiro.") from error
    if age < 0:
        raise ValueError("A idade não pode ser negativa.")
    return age


def read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise ValueError(f"Arquivo não encontrado: {path.name}") from error


def parse_json(raw_json: str) -> object:
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON inválido na linha {error.lineno}, coluna {error.colno}.") from error


def demonstrate(label: str, action, *arguments) -> None:
    try:
        print(f"[ok]   {label}: {action(*arguments)}")
    except ValueError as error:
        print(f"[erro] {label}: {error}")


def main() -> None:
    demonstrate("idade válida", parse_age, "30")
    demonstrate("idade com texto", parse_age, "trinta")
    demonstrate("idade negativa", parse_age, "-1")
    demonstrate("arquivo inexistente", read_text_file, Path("nao-existe.txt"))
    demonstrate("JSON válido", parse_json, '{"linguagem": "Python"}')
    demonstrate("JSON inválido", parse_json, '{"linguagem": }')


if __name__ == "__main__":
    main()
```

</details>
