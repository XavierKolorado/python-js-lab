<div align="center">

# Python & JavaScript Lab

**{{TOTAL}} exercícios resolvidos, testados e documentados, do primeiro `print` a aplicações com APIs reais.**

*{{TOTAL}} solved, tested and documented exercises, from the first `print` to apps using real APIs.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES2022-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-XavierKolorado-181717?logo=github&logoColor=white)](https://github.com/XavierKolorado)
[![CI](https://github.com/XavierKolorado/python-js-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/XavierKolorado/python-js-lab/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Português](#português) · [English](#english) · [Exercícios / Exercises](#lista-de-exercícios--exercise-list) · [Progresso / Progress](#checklist-de-progresso--progress-checklist)

</div>

---

## Progresso / Progress

| Linguagem / Language | Exercícios / Exercises | Resolvidos / Solved |
|---|---:|---:|
| Python | {{PY_TOTAL}} | {{PY_SOLVED}} |
| JavaScript | {{JS_TOTAL}} | {{JS_SOLVED}} |
| **Total** | **{{TOTAL}}** | **{{SOLVED}}** |

Esta tabela é gerada a partir dos arquivos do repositório. / *This table is generated from the repository files.*

---

## Português

### Sobre o laboratório

Este repositório é um laboratório de estudos e um portfólio de programação. Ele reúne {{PY_TOTAL}} exercícios de Python e {{JS_TOTAL}} de JavaScript, organizados em cinco níveis por linguagem. Todos têm solução completa, documentação, exemplo de execução e instruções.

### Objetivos de aprendizagem

- Dominar variáveis, condições, laços e funções nas duas linguagens.
- Trabalhar com listas, objetos, strings e algoritmos clássicos.
- Persistir dados em arquivos, JSON e `localStorage`.
- Tratar erros e validar entradas em vez de confiar no usuário.
- Manipular o DOM e criar interfaces acessíveis.
- Consumir APIs REST reais com tempo limite e tratamento de falhas.
- Escrever testes automatizados.

### Organização

| Nível | Python | JavaScript |
|---:|---|---|
| 1 | [Fundamentos](python/fundamentos/README.md) | [Fundamentos](javascript/fundamentos/README.md) |
| 2 | [Condições e loops](python/logica/README.md) | [Condições, loops e funções](javascript/logica/README.md) |
| 3 | [Listas, strings e funções](python/estruturas-de-dados/README.md) | [Arrays e objetos](javascript/arrays-objetos/README.md) |
| 4 | [Arquivos, JSON e erros](python/arquivos-json/README.md) | [DOM e páginas](javascript/dom/README.md) |
| 5 | [APIs e projetos](python/apis/README.md) | [Armazenamento, APIs e projetos](javascript/apis/README.md) |

Cada pasta de nível tem um `README.md` com problema, objetivo, conceitos, código, exemplo real de execução e resultado esperado de cada exercício.

Guias: [Python](docs/python-guide.md) · [JavaScript](docs/javascript-guide.md) · [APIs](docs/api-guide.md)

### Tecnologias e bibliotecas

| Item | Uso |
|---|---|
| Python 3.10+ | Exercícios de terminal. Só a biblioteca padrão, exceto nos exercícios 41 a 49 |
| [`requests`](https://requests.readthedocs.io/) | Chamadas HTTP nos exercícios Python 41 a 49 |
| [`pytest`](https://docs.pytest.org/) | Testes de Python (desenvolvimento) |
| Node.js 22+ | Exercícios JavaScript 01 a 30 e testes, sem dependências |
| HTML, CSS e JavaScript puros | Projetos 31 a 50, sem frameworks |
| [`playwright-core`](https://playwright.dev/) | Testes em navegador real (desenvolvimento) |

### Instalação

```bash
git clone https://github.com/XavierKolorado/python-js-lab.git
```

```bash
cd python-js-lab
```

```bash
python -m venv .venv
```

Ative o ambiente com `source .venv/bin/activate`, ou `.venv\Scripts\activate` no Windows. Depois instale as dependências:

```bash
pip install -r requirements-dev.txt
```

```bash
npm install
```

### Como executar

Execute os comandos a partir da raiz do repositório.

```bash
python python/logica/19-palindromo.py
```

```bash
node javascript/logica/15-palindromo.js "Ame a ema"
```

Para os projetos de navegador, inicie um servidor local e abra o endereço do exercício:

```bash
python -m http.server 8000
```

Exemplo: `http://localhost:8000/javascript/dom/36-calculadora-visual/`

### Como executar os testes

```bash
python -m pytest
```

```bash
npm test
```

```bash
npm run test:e2e
```

```bash
python tools/run_examples.py
```

```bash
python tools/check_apis.py
```

Os testes de navegador usam o Google Chrome instalado na máquina.

### Exemplos de utilização

```text
$ python python/apis/41-consulta-cep.py 01001-000
Praça da Sé, Sé
São Paulo/SP - 01001-000

$ node javascript/logica/13-fatorial.js 25
25! = 15511210043330985984000000
```

### Sobre segurança

Os exercícios de login são demonstrações didáticas. Python 18 e 50 usam hash PBKDF2 com salt, e JavaScript 42 avisa na própria página que não oferece segurança real. Não use esses códigos em produção. Nenhuma chave de API ou credencial privada faz parte do repositório.

### Contribuições

Sugestões e correções são bem-vindas. Abra uma [issue](https://github.com/XavierKolorado/python-js-lab/issues) ou um pull request.

1. Mantenha cada exercício executável de forma independente.
2. Adicione ou atualize os testes.
3. Atualize `tools/catalog.py` e rode `python tools/build_docs.py`, pois os READMEs são gerados.
4. Confirme que `python -m pytest` e `npm test` passam.

---

## English

### About the lab

This repository is a study lab and programming portfolio. It holds {{PY_TOTAL}} Python and {{JS_TOTAL}} JavaScript exercises, organized in five levels per language. Each one has a complete solution, documentation, a sample run and instructions. Program output is in Portuguese.

### Learning goals

- Master variables, conditions, loops and functions in both languages.
- Work with lists, objects, strings and classic algorithms.
- Persist data in files, JSON and `localStorage`.
- Handle errors and validate input instead of trusting the user.
- Manipulate the DOM and build accessible interfaces.
- Consume real REST APIs with timeouts and failure handling.
- Write automated tests.

### Structure

| Level | Python | JavaScript |
|---:|---|---|
| 1 | [Fundamentals](python/fundamentos/README.md) | [Fundamentals](javascript/fundamentos/README.md) |
| 2 | [Conditions and loops](python/logica/README.md) | [Conditions, loops and functions](javascript/logica/README.md) |
| 3 | [Lists, strings and functions](python/estruturas-de-dados/README.md) | [Arrays and objects](javascript/arrays-objetos/README.md) |
| 4 | [Files, JSON and errors](python/arquivos-json/README.md) | [DOM and pages](javascript/dom/README.md) |
| 5 | [APIs and projects](python/apis/README.md) | [Storage, APIs and projects](javascript/apis/README.md) |

Guides: [Python](docs/python-guide.md) · [JavaScript](docs/javascript-guide.md) · [APIs](docs/api-guide.md)

### Technologies

Python 3.10+ with the standard library, plus [`requests`](https://requests.readthedocs.io/) for exercises 41 to 49. Node.js 22+ with no runtime dependencies. Plain HTML, CSS and JavaScript for projects 31 to 50. Development tools: [`pytest`](https://docs.pytest.org/) and [`playwright-core`](https://playwright.dev/).

### Install

Clone the repository, create a virtual environment, then run:

```bash
pip install -r requirements-dev.txt
```

```bash
npm install
```

### Run

Run commands from the repository root.

```bash
python python/logica/19-palindromo.py
```

```bash
node javascript/logica/15-palindromo.js "Ame a ema"
```

For browser projects, run `python -m http.server 8000` and open the exercise, such as `http://localhost:8000/javascript/dom/36-calculadora-visual/`.

### Test

```bash
python -m pytest
```

```bash
npm test
```

```bash
npm run test:e2e
```

Browser tests use the Google Chrome installed on the machine.

### Security

The login exercises are teaching demos. Python 18 and 50 use salted PBKDF2 hashes, and JavaScript 42 warns on the page that it offers no real security. Do not use this code in production. The repository contains no API keys or private credentials.

### Contributing

Suggestions and fixes are welcome through [issues](https://github.com/XavierKolorado/python-js-lab/issues) and pull requests. Keep each exercise independently runnable, add tests, and edit `tools/catalog.py` before running `python tools/build_docs.py`, because the READMEs are generated.

---

## Lista de exercícios / Exercise list

## Python

{{PY_TABLE}}

## JavaScript

{{JS_TABLE}}

---

## Checklist de progresso / Progress checklist

<details>
<summary><strong>Python: {{PY_SOLVED}} de {{PY_TOTAL}}</strong></summary>

{{PY_CHECKLIST}}

</details>

<details>
<summary><strong>JavaScript: {{JS_SOLVED}} de {{JS_TOTAL}}</strong></summary>

{{JS_CHECKLIST}}

</details>

---

## Licença / License

Distribuído sob a [licença MIT](LICENSE). / *Released under the [MIT License](LICENSE).*
