<div align="center">

# Python & JavaScript Lab

**100 exercícios resolvidos, testados e documentados, do primeiro `print` a aplicações com APIs reais.**

*100 solved, tested and documented exercises, from the first `print` to apps using real APIs.*

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
| Python | 50 | 50 |
| JavaScript | 50 | 50 |
| **Total** | **100** | **100** |

Esta tabela é gerada a partir dos arquivos do repositório. / *This table is generated from the repository files.*

---

## Português

### Sobre o laboratório

Este repositório é um laboratório de estudos e um portfólio de programação. Ele reúne 50 exercícios de Python e 50 de JavaScript, organizados em cinco níveis por linguagem. Todos têm solução completa, documentação, exemplo de execução e instruções.

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

This repository is a study lab and programming portfolio. It holds 50 Python and 50 JavaScript exercises, organized in five levels per language. Each one has a complete solution, documentation, a sample run and instructions. Program output is in Portuguese.

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

### Nível 1: Fundamentos · *Fundamentals*

[Documentação do nível / Level docs](python/fundamentos/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 01 | [Mensagem de boas-vindas](python/fundamentos/01-mensagem-boas-vindas.py) | Welcome message | `input`, `print`, f-strings, funções |
| 02 | [Cadastro básico](python/fundamentos/02-cadastro-basico.py) | Basic registration | `while`, `try/except`, conversão de tipos |
| 03 | [Calculadora de soma](python/fundamentos/03-calculadora-soma.py) | Sum calculator | `float`, funções, validação |
| 04 | [Média de notas](python/fundamentos/04-media-notas.py) | Grade average | listas, `sum`, `len`, constantes |
| 05 | [Conversor Celsius para Fahrenheit](python/fundamentos/05-celsius-fahrenheit.py) | Celsius to Fahrenheit converter | expressões, exceções, `math.isfinite` |
| 06 | [Conversor de moedas](python/fundamentos/06-conversor-moedas.py) | Currency converter | funções, formatação numérica, validação |
| 07 | [Área e perímetro](python/fundamentos/07-area-perimetro.py) | Area and perimeter | tuplas, desempacotamento |
| 08 | [Par ou ímpar](python/fundamentos/08-par-ou-impar.py) | Even or odd | operador `%`, expressão condicional |
| 09 | [Maioridade](python/fundamentos/09-maioridade.py) | Legal age | `if/else`, constantes, booleanos |
| 10 | [Maior número](python/fundamentos/10-maior-numero.py) | Largest number | `if`, comparação, list comprehension |

### Nível 2: Condições e loops · *Conditions and loops*

[Documentação do nível / Level docs](python/logica/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 11 | [Calculadora completa](python/logica/11-calculadora-completa.py) | Full calculator | dicionários, módulo `operator`, `ZeroDivisionError` |
| 12 | [Ano bissexto](python/logica/12-ano-bissexto.py) | Leap year | `and`, `or`, operador `%` |
| 13 | [Contador](python/logica/13-contador.py) | Counter | `while`, `range`, fatiamento |
| 14 | [Tabuada](python/logica/14-tabuada.py) | Multiplication table | list comprehension, `range`, formatação |
| 15 | [Soma até N](python/logica/15-soma-ate-n.py) | Sum up to N | `for`, acumulador, validação |
| 16 | [Fatorial](python/logica/16-fatorial.py) | Factorial | `for`, inteiros grandes, `ValueError` |
| 17 | [Jogo de adivinhação](python/logica/17-jogo-adivinhacao.py) | Guessing game | `random`, `while`, `sys.argv` |
| 18 | [Sistema de login](python/logica/18-sistema-login.py) | Login system | `hashlib.pbkdf2_hmac`, `hmac.compare_digest`, `getpass` |
| 19 | [Palíndromo](python/logica/19-palindromo.py) | Palindrome | `unicodedata`, fatiamento, `casefold` |
| 20 | [Contador de vogais](python/logica/20-contador-vogais.py) | Vowel counter | `unicodedata`, `dict.fromkeys`, `for` |

### Nível 3: Listas, strings e funções · *Lists, strings and functions*

[Documentação do nível / Level docs](python/estruturas-de-dados/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 21 | [Maior e menor](python/estruturas-de-dados/21-maior-menor.py) | Largest and smallest | listas, `split`, tuplas |
| 22 | [Média de uma lista](python/estruturas-de-dados/22-media-lista.py) | List average | `sum`, `len`, exceções |
| 23 | [Remover duplicados](python/estruturas-de-dados/23-remover-duplicados.py) | Remove duplicates | `set`, listas, complexidade |
| 24 | [Ordenação manual](python/estruturas-de-dados/24-ordenacao-manual.py) | Manual sorting | algoritmos, índices, cópia de listas |
| 25 | [Separador de números](python/estruturas-de-dados/25-separador-numeros.py) | Number splitter | list comprehension, tuplas |
| 26 | [Verificador de números primos](python/estruturas-de-dados/26-numeros-primos.py) | Prime checker | `math.isqrt`, `all`, geradores |
| 27 | [Inversor de texto](python/estruturas-de-dados/27-inversor-texto.py) | Text reverser | fatiamento, strings |
| 28 | [Frequência de palavras](python/estruturas-de-dados/28-frequencia-palavras.py) | Word frequency | `re`, `collections.Counter` |
| 29 | [Agenda de contatos](python/estruturas-de-dados/29-agenda-contatos.py) | Contact book | classes, dicionários, menu |
| 30 | [Gerenciador de estoque](python/estruturas-de-dados/30-gerenciador-estoque.py) | Inventory manager | classes, exceções, dicionários |

### Nível 4: Arquivos, JSON e tratamento de erros · *Files, JSON and error handling*

[Documentação do nível / Level docs](python/arquivos-json/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 31 | [Bloco de notas](python/arquivos-json/31-bloco-notas.py) | Notepad | `pathlib`, `open`, regex, modos de arquivo |
| 32 | [Analisador de arquivos](python/arquivos-json/32-analisador-arquivos.py) | File analyzer | `pathlib`, `sys.argv`, exceções |
| 33 | [Cadastro com JSON](python/arquivos-json/33-cadastro-json.py) | JSON registration | `json`, regex, `pathlib` |
| 34 | [Gerenciador de tarefas](python/arquivos-json/34-gerenciador-tarefas.py) | Task manager | classes, `json`, identificadores |
| 35 | [Controle financeiro](python/arquivos-json/35-controle-financeiro.py) | Personal finance | `decimal`, `json` |
| 36 | [Histórico de calculadora](python/arquivos-json/36-historico-calculadora.py) | Calculator history | modo `a`, `pathlib`, `split` |
| 37 | [Validador de e-mails](python/arquivos-json/37-validador-emails.py) | Email validator | `re.fullmatch`, strings |
| 38 | [Gerador de senhas](python/arquivos-json/38-gerador-senhas.py) | Password generator | `secrets`, `argparse`, `string` |
| 39 | [Sistema de biblioteca](python/arquivos-json/39-sistema-biblioteca.py) | Library system | classes, `json`, exceções |
| 40 | [Tratamento de erros](python/arquivos-json/40-tratamento-erros.py) | Error handling | `try/except`, `raise ... from`, `json` |

### Nível 5: APIs e projetos intermediários · *APIs and intermediate projects*

[Documentação do nível / Level docs](python/apis/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 41 | [Consulta de CEP](python/apis/41-consulta-cep.py) | ZIP code lookup | `requests`, JSON, timeout, regex |
| 42 | [Consulta de clima](python/apis/42-consulta-clima.py) | Weather lookup | `requests`, parâmetros de URL, Open-Meteo |
| 43 | [Consulta de personagens](python/apis/43-consulta-personagens.py) | Character lookup | `requests`, paginação, Rick and Morty API |
| 44 | [Buscador de endereço](python/apis/44-buscador-endereco.py) | Address finder | `requests`, alinhamento de texto, código de saída |
| 45 | [Conversor de moedas com API](python/apis/45-conversor-moedas-api.py) | Currency converter with API | `requests`, Frankfurter API |
| 46 | [Encurtador de URLs](python/apis/46-encurtador-urls.py) | URL shortener | `requests`, `urllib.parse`, is.gd |
| 47 | [Gerenciador de tarefas com API](python/apis/47-tarefas-api.py) | Task manager with API | `requests.Session`, `argparse`, REST, JSONPlaceholder |
| 48 | [Cliente HTTP](python/apis/48-cliente-http.py) | HTTP client | `requests`, `argparse`, JSON |
| 49 | [Exportador de dados](python/apis/49-exportador-dados.py) | Data exporter | `requests`, `json`, `datetime` |
| 50 | [Sistema CLI completo](python/apis/50-sistema-cli.py) | Complete CLI system | classes, PBKDF2, `json`, `getpass` |

## JavaScript

### Nível 1: Fundamentos · *Fundamentals*

[Documentação do nível / Level docs](javascript/fundamentos/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 01 | [Mensagem no console](javascript/fundamentos/01-mensagem-console.js) | Console message | `console.log`, template strings, `process.argv` |
| 02 | [Variáveis](javascript/fundamentos/02-variaveis.js) | Variables | `let`, `const`, escopo, `TypeError` |
| 03 | [Calculadora](javascript/fundamentos/03-calculadora.js) | Calculator | objetos, arrow functions, `process.exitCode` |
| 04 | [Média de notas](javascript/fundamentos/04-media-notas.js) | Grade average | `reduce`, `Number.isFinite`, `toFixed` |
| 05 | [Conversor de temperatura](javascript/fundamentos/05-conversor-temperatura.js) | Temperature converter | funções, `toFixed`, `??` |
| 06 | [Par ou ímpar](javascript/fundamentos/06-par-ou-impar.js) | Even or odd | `%`, ternário, `Number.isInteger` |
| 07 | [Maior número](javascript/fundamentos/07-maior-numero.js) | Largest number | `if`, desestruturação, `every` |
| 08 | [Maioridade](javascript/fundamentos/08-maioridade.js) | Legal age | constantes, booleanos, exceções |
| 09 | [Classificação de notas](javascript/fundamentos/09-classificacao-notas.js) | Grade classification | `find`, desestruturação, arrays de objetos |
| 10 | [Calculadora de desconto](javascript/fundamentos/10-calculadora-desconto.js) | Discount calculator | `Intl.NumberFormat`, objetos |

### Nível 2: Condições, loops e funções · *Conditions, loops and functions*

[Documentação do nível / Level docs](javascript/logica/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 11 | [Tabuada](javascript/logica/11-tabuada.js) | Multiplication table | `for`, `padStart`, `join` |
| 12 | [Soma até N](javascript/logica/12-soma-ate-n.js) | Sum up to N | `for`, validação |
| 13 | [Fatorial](javascript/logica/13-fatorial.js) | Factorial | `BigInt`, `for` |
| 14 | [Jogo de adivinhação](javascript/logica/14-jogo-adivinhacao.js) | Guessing game | `Math.random`, `readline`, `for await` |
| 15 | [Palíndromo](javascript/logica/15-palindromo.js) | Palindrome | `normalize`, regex Unicode, espalhamento |
| 16 | [Contador de vogais](javascript/logica/16-contador-vogais.js) | Vowel counter | `for...of`, `Object.fromEntries`, `normalize` |
| 17 | [Números primos](javascript/logica/17-numeros-primos.js) | Prime numbers | `for`, `%`, casos de borda |
| 18 | [Maior valor de array](javascript/logica/18-maior-valor-array.js) | Largest array value | `for...of`, `every`, exceções |
| 19 | [Inversor de strings](javascript/logica/19-inversor-strings.js) | String reverser | espalhamento, `reverse`, `join` |
| 20 | [Contador regressivo](javascript/logica/20-contador-regressivo.js) | Countdown | `setInterval`, `clearInterval`, callbacks |

### Nível 3: Arrays e objetos · *Arrays and objects*

[Documentação do nível / Level docs](javascript/arrays-objetos/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 21 | [Maior e menor](javascript/arrays-objetos/21-maior-menor.js) | Largest and smallest | `reduce`, `Math.min`, `Math.max` |
| 22 | [Remover duplicados](javascript/arrays-objetos/22-remover-duplicados.js) | Remove duplicates | `Set`, espalhamento |
| 23 | [Filtro de pares](javascript/arrays-objetos/23-filtro-pares.js) | Even filter | `filter`, arrow functions |
| 24 | [Transformação de arrays](javascript/arrays-objetos/24-transformacao-arrays.js) | Array transformation | `map`, espalhamento de objetos |
| 25 | [Soma com reduce](javascript/arrays-objetos/25-soma-reduce.js) | Sum with reduce | `reduce` |
| 26 | [Ordenação de produtos](javascript/arrays-objetos/26-ordenacao-produtos.js) | Product sorting | `sort`, cópia de arrays |
| 27 | [Catálogo de produtos](javascript/arrays-objetos/27-catalogo-produtos.js) | Product catalog | `filter`, `find`, `Set`, `??` |
| 28 | [Busca de usuários](javascript/arrays-objetos/28-busca-usuarios.js) | User search | `includes`, `normalize`, `filter` |
| 29 | [Agrupamento por idade](javascript/arrays-objetos/29-agrupamento-idade.js) | Grouping by age | `reduce`, `Object.entries` |
| 30 | [Carrinho de compras](javascript/arrays-objetos/30-carrinho-compras.js) | Shopping cart | classes, campos privados, `Map`, getters |

### Nível 4: DOM e interação com páginas · *DOM and page interaction*

[Documentação do nível / Level docs](javascript/dom/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 31 | [Contador interativo](javascript/dom/31-contador-interativo) | Interactive counter | `querySelector`, `addEventListener`, `textContent` |
| 32 | [Lista de tarefas](javascript/dom/32-lista-tarefas) | To-do list | `createElement`, `replaceChildren`, formulários |
| 33 | [Formulário validado](javascript/dom/33-formulario-validado) | Validated form | `FormData`, regex, `aria-invalid` |
| 34 | [Menu responsivo](javascript/dom/34-menu-responsivo) | Responsive menu | `@media`, `aria-expanded`, teclado |
| 35 | [Tema claro e escuro](javascript/dom/35-tema-claro-escuro) | Light and dark theme | variáveis CSS, `matchMedia`, `localStorage` |
| 36 | [Calculadora visual](javascript/dom/36-calculadora-visual) | Visual calculator | CSS Grid, delegação de eventos, teclado |
| 37 | [Modal](javascript/dom/37-modal) | Modal | `dialog`, `showModal`, `::backdrop` |
| 38 | [Galeria de imagens](javascript/dom/38-galeria-imagens) | Image gallery | CSS Grid, `dialog`, SVG, aritmética modular |
| 39 | [Pesquisa em tempo real](javascript/dom/39-pesquisa-tempo-real) | Live search | `input`, `normalize`, `DocumentFragment` |
| 40 | [Cronômetro](javascript/dom/40-cronometro) | Stopwatch | `performance.now`, `setInterval`, estado |

### Nível 5: Armazenamento, APIs e projetos · *Storage, APIs and projects*

[Documentação do nível / Level docs](javascript/apis/README.md)

| # | Exercício | Exercise | Conceitos / Concepts |
|---:|---|---|---|
| 41 | [Preferências com localStorage](javascript/apis/41-preferencias-localstorage) | Preferences with localStorage | `localStorage`, `JSON`, formulários |
| 42 | [Login demonstrativo](javascript/apis/42-login-demonstrativo) | Demo login | `sessionStorage`, formulários, segurança |
| 43 | [Consumo de API](javascript/apis/43-consumo-api) | API consumption | `fetch`, `async/await`, `AbortSignal.timeout` |
| 44 | [Consulta de CEP](javascript/apis/44-consulta-cep) | ZIP code lookup | `fetch`, regex, `dl` |
| 45 | [Aplicação de clima](javascript/apis/45-aplicacao-clima) | Weather app | `fetch`, `URLSearchParams`, Open-Meteo |
| 46 | [Buscador de filmes](javascript/apis/46-buscador-filmes) | Movie finder | `fetch`, `filter`, CSS Grid, Studio Ghibli API |
| 47 | [Painel de dados](javascript/apis/47-painel-dados) | Data dashboard | `reduce`, `Map`, `Intl`, DummyJSON |
| 48 | [CRUD de produtos](javascript/apis/48-crud-produtos) | Product CRUD | `localStorage`, `crypto.randomUUID`, `confirm` |
| 49 | [Paginação](javascript/apis/49-paginacao) | Pagination | `slice`, `Math.ceil`, `aria-current` |
| 50 | [Aplicação de favoritos](javascript/apis/50-aplicacao-favoritos) | Favorites app | `fetch`, `localStorage`, Rick and Morty API |

---

## Checklist de progresso / Progress checklist

<details>
<summary><strong>Python: 50 de 50</strong></summary>

- [x] 01. Mensagem de boas-vindas
- [x] 02. Cadastro básico
- [x] 03. Calculadora de soma
- [x] 04. Média de notas
- [x] 05. Conversor Celsius para Fahrenheit
- [x] 06. Conversor de moedas
- [x] 07. Área e perímetro
- [x] 08. Par ou ímpar
- [x] 09. Maioridade
- [x] 10. Maior número
- [x] 11. Calculadora completa
- [x] 12. Ano bissexto
- [x] 13. Contador
- [x] 14. Tabuada
- [x] 15. Soma até N
- [x] 16. Fatorial
- [x] 17. Jogo de adivinhação
- [x] 18. Sistema de login
- [x] 19. Palíndromo
- [x] 20. Contador de vogais
- [x] 21. Maior e menor
- [x] 22. Média de uma lista
- [x] 23. Remover duplicados
- [x] 24. Ordenação manual
- [x] 25. Separador de números
- [x] 26. Verificador de números primos
- [x] 27. Inversor de texto
- [x] 28. Frequência de palavras
- [x] 29. Agenda de contatos
- [x] 30. Gerenciador de estoque
- [x] 31. Bloco de notas
- [x] 32. Analisador de arquivos
- [x] 33. Cadastro com JSON
- [x] 34. Gerenciador de tarefas
- [x] 35. Controle financeiro
- [x] 36. Histórico de calculadora
- [x] 37. Validador de e-mails
- [x] 38. Gerador de senhas
- [x] 39. Sistema de biblioteca
- [x] 40. Tratamento de erros
- [x] 41. Consulta de CEP
- [x] 42. Consulta de clima
- [x] 43. Consulta de personagens
- [x] 44. Buscador de endereço
- [x] 45. Conversor de moedas com API
- [x] 46. Encurtador de URLs
- [x] 47. Gerenciador de tarefas com API
- [x] 48. Cliente HTTP
- [x] 49. Exportador de dados
- [x] 50. Sistema CLI completo

</details>

<details>
<summary><strong>JavaScript: 50 de 50</strong></summary>

- [x] 01. Mensagem no console
- [x] 02. Variáveis
- [x] 03. Calculadora
- [x] 04. Média de notas
- [x] 05. Conversor de temperatura
- [x] 06. Par ou ímpar
- [x] 07. Maior número
- [x] 08. Maioridade
- [x] 09. Classificação de notas
- [x] 10. Calculadora de desconto
- [x] 11. Tabuada
- [x] 12. Soma até N
- [x] 13. Fatorial
- [x] 14. Jogo de adivinhação
- [x] 15. Palíndromo
- [x] 16. Contador de vogais
- [x] 17. Números primos
- [x] 18. Maior valor de array
- [x] 19. Inversor de strings
- [x] 20. Contador regressivo
- [x] 21. Maior e menor
- [x] 22. Remover duplicados
- [x] 23. Filtro de pares
- [x] 24. Transformação de arrays
- [x] 25. Soma com reduce
- [x] 26. Ordenação de produtos
- [x] 27. Catálogo de produtos
- [x] 28. Busca de usuários
- [x] 29. Agrupamento por idade
- [x] 30. Carrinho de compras
- [x] 31. Contador interativo
- [x] 32. Lista de tarefas
- [x] 33. Formulário validado
- [x] 34. Menu responsivo
- [x] 35. Tema claro e escuro
- [x] 36. Calculadora visual
- [x] 37. Modal
- [x] 38. Galeria de imagens
- [x] 39. Pesquisa em tempo real
- [x] 40. Cronômetro
- [x] 41. Preferências com localStorage
- [x] 42. Login demonstrativo
- [x] 43. Consumo de API
- [x] 44. Consulta de CEP
- [x] 45. Aplicação de clima
- [x] 46. Buscador de filmes
- [x] 47. Painel de dados
- [x] 48. CRUD de produtos
- [x] 49. Paginação
- [x] 50. Aplicação de favoritos

</details>

---

## Licença / License

Distribuído sob a [licença MIT](LICENSE). / *Released under the [MIT License](LICENSE).*
