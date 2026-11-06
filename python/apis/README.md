<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# Python, nível 5: APIs e projetos intermediários

*Python, level 5: APIs and intermediate projects*

[Voltar ao README principal / Back to the main README](../../README.md)

- [41. Consulta de CEP](41-consulta-cep.py)
- [42. Consulta de clima](42-consulta-clima.py)
- [43. Consulta de personagens](43-consulta-personagens.py)
- [44. Buscador de endereço](44-buscador-endereco.py)
- [45. Conversor de moedas com API](45-conversor-moedas-api.py)
- [46. Encurtador de URLs](46-encurtador-urls.py)
- [47. Gerenciador de tarefas com API](47-tarefas-api.py)
- [48. Cliente HTTP](48-cliente-http.py)
- [49. Exportador de dados](49-exportador-dados.py)
- [50. Sistema CLI completo](50-sistema-cli.py)

## 41. Consulta de CEP / ZIP code lookup

**Problema:** Consultar CEP utilizando a API ViaCEP.  
**Problem:** Look up a Brazilian ZIP code with the ViaCEP API.

**Objetivo:** Fazer uma requisição GET e tratar respostas.  
**Goal:** Make a GET request and handle responses.

**Conceitos / Concepts:** `requests`, JSON, timeout, regex

**Arquivo / File:** [`41-consulta-cep.py`](./41-consulta-cep.py)

**Como executar / How to run**

```bash
python python/apis/41-consulta-cep.py 01001-000
```

**Exemplo de execução / Example run**

```text
Praça da Sé, Sé
São Paulo/SP - 01001-000
```

**Resultado esperado:** O endereço do CEP. CEP inválido ou inexistente gera erro claro.  
**Expected result:** The address. An invalid or unknown ZIP gives a clear error.

<details><summary>Código completo / Full code: <code>41-consulta-cep.py</code></summary>

```python
"""41. Consulta de CEP: consulta a API ViaCEP.

Uso: python 41-consulta-cep.py 01001-000
"""

import re
import sys

import requests

VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"
TIMEOUT_SECONDS = 10


def normalize_cep(raw_cep: str) -> str:
    digits = re.sub(r"\D", "", raw_cep)
    if len(digits) != 8:
        raise ValueError("O CEP precisa ter 8 dígitos.")
    return digits


def fetch_cep(cep: str) -> dict:
    response = requests.get(VIACEP_URL.format(cep=normalize_cep(cep)), timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    # A ViaCEP responde 200 com {"erro": "true"} quando o CEP não existe.
    if data.get("erro"):
        raise LookupError("CEP não encontrado.")
    return data


def main() -> int:
    raw_cep = sys.argv[1] if len(sys.argv) > 1 else input("CEP: ")
    try:
        address = fetch_cep(raw_cep)
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a ViaCEP: {error}")
        return 1
    print(f"{address['logradouro']}, {address['bairro']}")
    print(f"{address['localidade']}/{address['uf']} - {address['cep']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 42. Consulta de clima / Weather lookup

**Problema:** Consultar informações meteorológicas utilizando uma API pública.  
**Problem:** Fetch weather data from a public API.

**Objetivo:** Encadear duas chamadas: geocodificação e previsão.  
**Goal:** Chain two calls: geocoding and forecast.

**Conceitos / Concepts:** `requests`, parâmetros de URL, Open-Meteo

**Arquivo / File:** [`42-consulta-clima.py`](./42-consulta-clima.py)

**Como executar / How to run**

```bash
python python/apis/42-consulta-clima.py Curitiba
```

**Exemplo de execução / Example run**

```text
Curitiba, Brasil
Condição: garoa fraca
Temperatura: 18.3 °C
Umidade: 98%
Vento: 8.0 km/h
```

**Resultado esperado:** Condição, temperatura, umidade e vento atuais. Os valores mudam.  
**Expected result:** Current condition, temperature, humidity and wind. Values change.

<details><summary>Código completo / Full code: <code>42-consulta-clima.py</code></summary>

```python
"""42. Consulta de clima: usa as APIs de geocodificação e previsão da Open-Meteo.

Uso: python 42-consulta-clima.py "São Paulo"
"""

import sys

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT_SECONDS = 10
WEATHER_DESCRIPTIONS = {
    0: "céu limpo",
    1: "predomínio de sol",
    2: "parcialmente nublado",
    3: "nublado",
    45: "neblina",
    48: "neblina com geada",
    51: "garoa fraca",
    53: "garoa moderada",
    55: "garoa intensa",
    61: "chuva fraca",
    63: "chuva moderada",
    65: "chuva forte",
    71: "neve fraca",
    73: "neve moderada",
    75: "neve forte",
    80: "pancadas de chuva fracas",
    81: "pancadas de chuva moderadas",
    82: "pancadas de chuva fortes",
    95: "trovoada",
    96: "trovoada com granizo",
    99: "trovoada forte com granizo",
}


def describe_weather(code: int) -> str:
    return WEATHER_DESCRIPTIONS.get(code, f"condição desconhecida ({code})")


def find_city(name: str) -> dict:
    if not name.strip():
        raise ValueError("Informe o nome de uma cidade.")
    parameters = {"name": name.strip(), "count": 1, "language": "pt"}
    response = requests.get(GEOCODING_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        raise LookupError(f"Cidade não encontrada: {name.strip()}")
    return results[0]


def fetch_current_weather(latitude: float, longitude: float) -> dict:
    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "auto",
    }
    response = requests.get(FORECAST_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()["current"]


def main() -> int:
    city_name = sys.argv[1] if len(sys.argv) > 1 else input("Cidade: ")
    try:
        city = find_city(city_name)
        weather = fetch_current_weather(city["latitude"], city["longitude"])
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a Open-Meteo: {error}")
        return 1
    print(f"{city['name']}, {city.get('country', '')}")
    print(f"Condição: {describe_weather(weather['weather_code'])}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Umidade: {weather['relative_humidity_2m']}%")
    print(f"Vento: {weather['wind_speed_10m']} km/h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 43. Consulta de personagens / Character lookup

**Problema:** Consumir uma API pública de personagens e listar resultados.  
**Problem:** Consume a public character API and list results.

**Objetivo:** Tratar um 404 que significa busca vazia.  
**Goal:** Handle a 404 that means an empty search.

**Conceitos / Concepts:** `requests`, paginação, Rick and Morty API

**Arquivo / File:** [`43-consulta-personagens.py`](./43-consulta-personagens.py)

**Como executar / How to run**

```bash
python python/apis/43-consulta-personagens.py rick
```

**Exemplo de execução / Example run**

```text
107 resultado(s). Primeiros 10:
- Rick Sanchez (Human, Alive)
- Adjudicator Rick (Human, Dead)
- Alien Rick (Alien, unknown)
- Antenna Rick (Human, unknown)
- Aqua Rick (Humanoid, unknown)
- Black Rick (Human, Alive)
- Bootleg Portal Chemist Rick (Human, Dead)
- Commander Rick (Human, Dead)
- Cool Rick (Human, Alive)
- Cop Rick (Human, Alive)
```

**Resultado esperado:** Total de resultados e até dez personagens.  
**Expected result:** The result total and up to ten characters.

<details><summary>Código completo / Full code: <code>43-consulta-personagens.py</code></summary>

```python
"""43. Consulta de personagens: usa a Rick and Morty API.

Uso: python 43-consulta-personagens.py rick
"""

import sys

import requests

CHARACTERS_URL = "https://rickandmortyapi.com/api/character/"
TIMEOUT_SECONDS = 10
MAX_RESULTS = 10


def search_characters(name: str) -> tuple[int, list[dict]]:
    if not name.strip():
        raise ValueError("Informe parte do nome de um personagem.")
    response = requests.get(CHARACTERS_URL, params={"name": name.strip()}, timeout=TIMEOUT_SECONDS)
    # Esta API usa o status 404 para buscas sem resultado.
    if response.status_code == 404:
        return 0, []
    response.raise_for_status()
    data = response.json()
    return data["info"]["count"], data["results"]


def format_character(character: dict) -> str:
    return f"{character['name']} ({character['species']}, {character['status']})"


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else input("Nome do personagem: ")
    try:
        total, characters = search_characters(name)
    except ValueError as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a API: {error}")
        return 1
    if not characters:
        print("Nenhum personagem encontrado.")
        return 0
    print(f"{total} resultado(s). Primeiros {min(MAX_RESULTS, len(characters))}:")
    for character in characters[:MAX_RESULTS]:
        print(f"- {format_character(character)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 44. Buscador de endereço / Address finder

**Problema:** Buscar endereço por CEP e exibir os dados organizadamente.  
**Problem:** Find an address by ZIP code and show it neatly.

**Objetivo:** Processar vários itens sem parar no primeiro erro.  
**Goal:** Process many items without stopping at the first error.

**Conceitos / Concepts:** `requests`, alinhamento de texto, código de saída

**Arquivo / File:** [`44-buscador-endereco.py`](./44-buscador-endereco.py)

**Como executar / How to run**

```bash
python python/apis/44-buscador-endereco.py 01001-000 20040-020
```

**Exemplo de execução / Example run**

```text
CEP         : 01001-000
Logradouro  : Praça da Sé
Complemento : lado ímpar
Bairro      : Sé
Cidade      : São Paulo
Estado      : São Paulo
Região      : Sudeste
DDD         : 11

CEP         : 20040-020
Logradouro  : Praça Pio X
Complemento : lado ímpar
Bairro      : Centro
Cidade      : Rio de Janeiro
Estado      : Rio de Janeiro
Região      : Sudeste
DDD         : 21
```

**Resultado esperado:** Um cartão por CEP, omitindo campos vazios.  
**Expected result:** One card per ZIP code, skipping empty fields.

<details><summary>Código completo / Full code: <code>44-buscador-endereco.py</code></summary>

```python
"""44. Buscador de endereço: exibe um cartão organizado para cada CEP informado.

Uso: python 44-buscador-endereco.py 01001-000 20040-020
"""

import re
import sys

import requests

VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"
TIMEOUT_SECONDS = 10
ADDRESS_FIELDS = (
    ("CEP", "cep"),
    ("Logradouro", "logradouro"),
    ("Complemento", "complemento"),
    ("Bairro", "bairro"),
    ("Cidade", "localidade"),
    ("Estado", "estado"),
    ("Região", "regiao"),
    ("DDD", "ddd"),
)


def fetch_address(raw_cep: str) -> dict:
    digits = re.sub(r"\D", "", raw_cep)
    if len(digits) != 8:
        raise ValueError(f"CEP inválido: {raw_cep}")
    response = requests.get(VIACEP_URL.format(cep=digits), timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    if data.get("erro"):
        raise LookupError(f"CEP não encontrado: {raw_cep}")
    return data


def format_address(address: dict) -> str:
    width = max(len(label) for label, _ in ADDRESS_FIELDS)
    lines = [
        f"{label:<{width}} : {address[key]}"
        for label, key in ADDRESS_FIELDS
        if address.get(key)
    ]
    return "\n".join(lines)


def main() -> int:
    ceps = sys.argv[1:] or input("CEPs separados por espaço: ").split()
    if not ceps:
        print("Erro: informe ao menos um CEP.")
        return 1
    exit_code = 0
    for cep in ceps:
        try:
            print(format_address(fetch_address(cep)))
        except (ValueError, LookupError) as error:
            print(f"Erro: {error}")
            exit_code = 1
        except requests.RequestException as error:
            print(f"Erro de rede ao consultar a ViaCEP: {error}")
            exit_code = 1
        print()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 45. Conversor de moedas com API / Currency converter with API

**Problema:** Consultar taxas de câmbio através de uma API pública.  
**Problem:** Fetch exchange rates from a public API.

**Objetivo:** Validar antes de chamar a rede.  
**Goal:** Validate before calling the network.

**Conceitos / Concepts:** `requests`, Frankfurter API

**Arquivo / File:** [`45-conversor-moedas-api.py`](./45-conversor-moedas-api.py)

**Como executar / How to run**

```bash
python python/apis/45-conversor-moedas-api.py 100 USD BRL
```

**Exemplo de execução / Example run**

```text
100.00 USD = 546.64 BRL
Taxa: 5.4664 (referência de 2026-11-05)
```

**Resultado esperado:** O valor convertido, a taxa e a data de referência.  
**Expected result:** The converted amount, the rate and its date.

<details><summary>Código completo / Full code: <code>45-conversor-moedas-api.py</code></summary>

```python
"""45. Conversor de moedas com API: consulta taxas na Frankfurter.

Uso: python 45-conversor-moedas-api.py 100 USD BRL
"""

import math
import sys

import requests

RATES_URL = "https://api.frankfurter.dev/v1/latest"
TIMEOUT_SECONDS = 10


def validate_currency(code: str) -> str:
    clean_code = code.strip().upper()
    if len(clean_code) != 3 or not clean_code.isalpha():
        raise ValueError(f"Código de moeda inválido: {code}")
    return clean_code


def fetch_rate(source: str, target: str) -> tuple[float, str]:
    parameters = {"base": source, "symbols": target}
    response = requests.get(RATES_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    # A Frankfurter usa 404 ou 422 para moedas que ela não conhece.
    if response.status_code in (404, 422):
        raise LookupError("Moeda não suportada pela API.")
    response.raise_for_status()
    data = response.json()
    return data["rates"][target], data["date"]


def convert(amount: float, source: str, target: str) -> tuple[float, float, str]:
    if not (math.isfinite(amount) and amount >= 0):
        raise ValueError("Informe um valor positivo.")
    source, target = validate_currency(source), validate_currency(target)
    if source == target:
        raise ValueError("Escolha duas moedas diferentes.")
    rate, date = fetch_rate(source, target)
    return amount * rate, rate, date


def main() -> int:
    if len(sys.argv) != 4:
        print("Uso: python 45-conversor-moedas-api.py VALOR ORIGEM DESTINO")
        return 1
    try:
        amount = float(sys.argv[1].replace(",", "."))
        result, rate, date = convert(amount, sys.argv[2], sys.argv[3])
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a API: {error}")
        return 1
    print(f"{amount:.2f} {sys.argv[2].upper()} = {result:.2f} {sys.argv[3].upper()}")
    print(f"Taxa: {rate} (referência de {date})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 46. Encurtador de URLs / URL shortener

**Problema:** Utilizar uma API pública para encurtar links.  
**Problem:** Shorten links with a public API.

**Objetivo:** Ler erros devolvidos no corpo da resposta.  
**Goal:** Read errors returned in the response body.

**Conceitos / Concepts:** `requests`, `urllib.parse`, is.gd

**Arquivo / File:** [`46-encurtador-urls.py`](./46-encurtador-urls.py)

**Como executar / How to run**

```bash
python python/apis/46-encurtador-urls.py https://www.python.org/
```

**Exemplo de execução / Example run**

```text
URL curta: https://is.gd/RXuRZx
```

**Resultado esperado:** A URL curta. Cada URL nova cria um link público e permanente.  
**Expected result:** The short URL. Each new URL creates a public, permanent link.

<details><summary>Código completo / Full code: <code>46-encurtador-urls.py</code></summary>

```python
"""46. Encurtador de URLs: usa a API pública do is.gd.

Uso: python 46-encurtador-urls.py https://www.python.org/
Atenção: cada URL nova cria um link público e permanente no serviço.
"""

import sys
from urllib.parse import urlparse

import requests

SHORTENER_URL = "https://is.gd/create.php"
TIMEOUT_SECONDS = 10


def validate_url(url: str) -> str:
    clean_url = url.strip()
    parsed = urlparse(clean_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("Informe uma URL completa, iniciada por http:// ou https://.")
    return clean_url


def shorten_url(url: str) -> str:
    parameters = {"format": "json", "url": validate_url(url)}
    response = requests.get(SHORTENER_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    if "shorturl" not in data:
        raise LookupError(data.get("errormessage", "O serviço recusou a URL."))
    return data["shorturl"]


def main() -> int:
    url = sys.argv[1] if len(sys.argv) > 1 else input("URL: ")
    try:
        print(f"URL curta: {shorten_url(url)}")
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar o is.gd: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 47. Gerenciador de tarefas com API / Task manager with API

**Problema:** Criar um cliente que consome uma API REST para gerenciar tarefas.  
**Problem:** Build a client that manages tasks through a REST API.

**Objetivo:** Usar os verbos HTTP e subcomandos de terminal.  
**Goal:** Use HTTP verbs and terminal subcommands.

**Conceitos / Concepts:** `requests.Session`, `argparse`, REST, JSONPlaceholder

**Arquivo / File:** [`47-tarefas-api.py`](./47-tarefas-api.py)

**Como executar / How to run**

```bash
python python/apis/47-tarefas-api.py listar --usuario 1
```

**Exemplo de execução / Example run**

```text
20 tarefa(s). Primeiras 5:
[ ] 1. delectus aut autem
[ ] 2. quis ut nam facilis et officia qui
[ ] 3. fugiat veniam minus
[x] 4. et porro tempora
[ ] 5. laboriosam mollitia et enim quasi adipisci quia provident illum
```

**Resultado esperado:** Listagem real. Criar, concluir e excluir são simulados pela API.  
**Expected result:** Real listing. Create, complete and delete are simulated by the API.

<details><summary>Código completo / Full code: <code>47-tarefas-api.py</code></summary>

```python
"""47. Gerenciador de tarefas com API: cliente REST para a JSONPlaceholder.

Uso:
  python 47-tarefas-api.py listar --usuario 1
  python 47-tarefas-api.py criar "Estudar HTTP"
  python 47-tarefas-api.py concluir 5
  python 47-tarefas-api.py excluir 5

A JSONPlaceholder responde como uma API real, mas não grava alterações.
"""

import argparse
import sys

import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"
TIMEOUT_SECONDS = 10
LIST_LIMIT = 5


class TaskApiClient:
    def __init__(self, base_url: str = BASE_URL) -> None:
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method: str, url: str, **options) -> requests.Response:
        response = self.session.request(method, url, timeout=TIMEOUT_SECONDS, **options)
        response.raise_for_status()
        return response

    def list_tasks(self, user_id: int) -> list[dict]:
        return self._request("GET", self.base_url, params={"userId": user_id}).json()

    def create_task(self, title: str, user_id: int = 1) -> dict:
        if not title.strip():
            raise ValueError("O título é obrigatório.")
        payload = {"title": title.strip(), "completed": False, "userId": user_id}
        return self._request("POST", self.base_url, json=payload).json()

    def complete_task(self, task_id: int) -> dict:
        url = f"{self.base_url}/{task_id}"
        return self._request("PATCH", url, json={"completed": True}).json()

    def delete_task(self, task_id: int) -> None:
        self._request("DELETE", f"{self.base_url}/{task_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Cliente REST de tarefas.")
    commands = parser.add_subparsers(dest="command", required=True)
    list_command = commands.add_parser("listar")
    list_command.add_argument("--usuario", type=int, default=1)
    commands.add_parser("criar").add_argument("titulo")
    commands.add_parser("concluir").add_argument("id", type=int)
    commands.add_parser("excluir").add_argument("id", type=int)
    return parser


def run_command(client: TaskApiClient, options: argparse.Namespace) -> None:
    if options.command == "listar":
        tasks = client.list_tasks(options.usuario)
        print(f"{len(tasks)} tarefa(s). Primeiras {LIST_LIMIT}:")
        for task in tasks[:LIST_LIMIT]:
            mark = "x" if task["completed"] else " "
            print(f"[{mark}] {task['id']}. {task['title']}")
    elif options.command == "criar":
        task = client.create_task(options.titulo)
        print(f"Tarefa simulada com id {task['id']}: {task['title']}")
    elif options.command == "concluir":
        task = client.complete_task(options.id)
        print(f"Tarefa {task['id']} concluída (simulação).")
    else:
        client.delete_task(options.id)
        print(f"Tarefa {options.id} excluída (simulação).")


def main() -> int:
    options = build_parser().parse_args()
    try:
        run_command(TaskApiClient(), options)
    except ValueError as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro ao chamar a API: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 48. Cliente HTTP / HTTP client

**Problema:** Criar um programa capaz de realizar requisições GET e POST.  
**Problem:** Build a program that sends GET and POST requests.

**Objetivo:** Entender status, cabeçalhos e corpo.  
**Goal:** Understand status, headers and body.

**Conceitos / Concepts:** `requests`, `argparse`, JSON

**Arquivo / File:** [`48-cliente-http.py`](./48-cliente-http.py)

**Como executar / How to run**

```bash
python python/apis/48-cliente-http.py POST https://httpbin.org/post --json '{"nome": "Lab"}'
```

**Exemplo de execução / Example run**

```text
Status: 200 OK
Tipo: application/json

{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, zstd",
    "Content-Length": "15",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.34.2"
  },
  "method": "POST",
  "origin": "179.190.113.229",
  "url": "https://httpbin.org/post",
  "data": "{\"nome\": \"Lab\"}",
  "files": {},
  "form": {},
  "json": {
    "nome": "Lab"
  }
}
```

**Resultado esperado:** Status, tipo de conteúdo e corpo resumido da resposta.  
**Expected result:** The response status, content type and a short body.

<details><summary>Código completo / Full code: <code>48-cliente-http.py</code></summary>

```python
"""48. Cliente HTTP: realiza requisições GET e POST pelo terminal.

Uso:
  python 48-cliente-http.py GET https://httpbin.org/get
  python 48-cliente-http.py POST https://httpbin.org/post --json '{"nome": "Lab"}'
"""

import argparse
import json
import sys

import requests

TIMEOUT_SECONDS = 15
MAX_BODY_LENGTH = 600


def send_request(method: str, url: str, raw_json: str | None = None) -> requests.Response:
    if method == "GET" and raw_json is not None:
        raise ValueError("--json só pode ser usado com POST.")
    try:
        payload = None if raw_json is None else json.loads(raw_json)
    except json.JSONDecodeError as error:
        raise ValueError(f"Corpo JSON inválido: {error.msg}") from error
    return requests.request(method, url, json=payload, timeout=TIMEOUT_SECONDS)


def format_response(response: requests.Response) -> str:
    content_type = response.headers.get("Content-Type", "desconhecido")
    body = response.text
    if len(body) > MAX_BODY_LENGTH:
        body = f"{body[:MAX_BODY_LENGTH]}... ({len(response.text)} caracteres no total)"
    return f"Status: {response.status_code} {response.reason}\nTipo: {content_type}\n\n{body}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Cliente HTTP simples.")
    parser.add_argument("method", type=str.upper, choices=["GET", "POST"])
    parser.add_argument("url")
    parser.add_argument("--json", dest="raw_json", help="corpo JSON de um POST")
    options = parser.parse_args()
    try:
        response = send_request(options.method, options.url, options.raw_json)
    except ValueError as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede: {error}")
        return 1
    print(format_response(response))
    return 0 if response.ok else 1


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 49. Exportador de dados / Data exporter

**Problema:** Consultar uma API e salvar os resultados em JSON.  
**Problem:** Query an API and save the results as JSON.

**Objetivo:** Transformar dados antes de gravar.  
**Goal:** Transform data before saving.

**Conceitos / Concepts:** `requests`, `json`, `datetime`

**Arquivo / File:** [`49-exportador-dados.py`](./49-exportador-dados.py)

**Como executar / How to run**

```bash
python python/apis/49-exportador-dados.py
```

**Exemplo de execução / Example run**

```text
10 registro(s) exportado(s) para usuarios-exportados.json.
```

**Resultado esperado:** Um arquivo JSON com metadados e registros simplificados.  
**Expected result:** A JSON file with metadata and simplified records.

<details><summary>Código completo / Full code: <code>49-exportador-dados.py</code></summary>

```python
"""49. Exportador de dados: consulta uma API e salva o resultado em JSON.

Uso: python 49-exportador-dados.py [arquivo.json]
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

SOURCE_URL = "https://jsonplaceholder.typicode.com/users"
DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "usuarios-exportados.json"
TIMEOUT_SECONDS = 10


def fetch_records(url: str = SOURCE_URL) -> list[dict]:
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def simplify_record(record: dict) -> dict:
    return {
        "id": record["id"],
        "name": record["name"],
        "email": record["email"],
        "city": record["address"]["city"],
        "company": record["company"]["name"],
    }


def build_export(records: list[dict]) -> dict:
    return {
        "source": SOURCE_URL,
        "exported_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total": len(records),
        "records": [simplify_record(record) for record in records],
    }


def save_export(path: Path, export: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(export, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        export = build_export(fetch_records())
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar a API: {error}")
        return 1
    except (KeyError, TypeError):
        print("Erro: a API respondeu em um formato inesperado.")
        return 1
    save_export(path, export)
    print(f"{export['total']} registro(s) exportado(s) para {path.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>

## 50. Sistema CLI completo / Complete CLI system

**Problema:** Criar uma aplicação de terminal reunindo cadastro, autenticação demonstrativa e gerenciamento de dados.  
**Problem:** Build a terminal app with registration, demo authentication and data management.

**Objetivo:** Integrar persistência, hash de senha e menus. Não usa rede.  
**Goal:** Combine persistence, password hashing and menus. It uses no network.

**Conceitos / Concepts:** classes, PBKDF2, `json`, `getpass`

**Arquivo / File:** [`50-sistema-cli.py`](./50-sistema-cli.py)

**Como executar / How to run**

```bash
python python/apis/50-sistema-cli.py
```

**Entradas do exemplo / Example input:** `1` · `ana` · `senha-de-teste` · `2` · `ana` · `senha-de-teste` · `1` · `Primeira nota` · `2` · `4` · `0`

**Exemplo de execução / Example run**

```text

1. Criar conta
2. Entrar
0. Sair
Opção: Usuário: Senha: Conta criada.

1. Criar conta
2. Entrar
0. Sair
Opção: Usuário: Senha: Bem-vindo(a), ana!

1. Adicionar nota
2. Listar notas
3. Excluir nota
4. Sair da conta
Opção: Nota: Nota salva.

1. Adicionar nota
2. Listar notas
3. Excluir nota
4. Sair da conta
Opção: 1. Primeira nota

1. Adicionar nota
2. Listar notas
3. Excluir nota
4. Sair da conta
Opção: 
1. Criar conta
2. Entrar
... (2 linhas omitidas)
```

**Resultado esperado:** Contas com hash e salt, e notas separadas por pessoa.  
**Expected result:** Accounts with salted hashes and notes per person.

<details><summary>Código completo / Full code: <code>50-sistema-cli.py</code></summary>

```python
"""50. Sistema CLI completo: cadastro, login demonstrativo e notas por usuário.

Uso: python 50-sistema-cli.py [arquivo.json]

Senhas são gravadas como hash PBKDF2 com salt individual. Isso protege contra a
leitura direta do arquivo, mas o projeto continua didático: um sistema real
precisa de controle de sessão, limite de tentativas e armazenamento protegido.
"""

import getpass
import hashlib
import hmac
import json
import os
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "dados" / "sistema.json"
PBKDF2_ITERATIONS = 200_000
MIN_PASSWORD_LENGTH = 8
GUEST_MENU = """
1. Criar conta
2. Entrar
0. Sair"""
USER_MENU = """
1. Adicionar nota
2. Listar notas
3. Excluir nota
4. Sair da conta"""


def hash_password(password: str, salt: bytes) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ITERATIONS).hex()


class AppStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.users: dict[str, dict] = {}
        if path.exists():
            try:
                self.users = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise ValueError(f"{path.name} contém JSON inválido.") from error

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.users, ensure_ascii=False, indent=2), encoding="utf-8")

    def register(self, username: str, password: str) -> None:
        clean_username = username.strip().lower()
        if not clean_username.isalnum():
            raise ValueError("O usuário deve conter apenas letras e números.")
        if clean_username in self.users:
            raise ValueError("Usuário já existe.")
        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValueError(f"A senha precisa de ao menos {MIN_PASSWORD_LENGTH} caracteres.")
        salt = os.urandom(16)
        self.users[clean_username] = {
            "salt": salt.hex(),
            "password_hash": hash_password(password, salt),
            "notes": [],
        }
        self.save()

    def authenticate(self, username: str, password: str) -> str | None:
        clean_username = username.strip().lower()
        user = self.users.get(clean_username)
        if user is None:
            return None
        candidate = hash_password(password, bytes.fromhex(user["salt"]))
        return clean_username if hmac.compare_digest(candidate, user["password_hash"]) else None

    def add_note(self, username: str, text: str) -> None:
        if not text.strip():
            raise ValueError("A nota não pode ficar vazia.")
        self.users[username]["notes"].append(text.strip())
        self.save()

    def notes_of(self, username: str) -> list[str]:
        return self.users[username]["notes"]

    def delete_note(self, username: str, position: int) -> None:
        notes = self.notes_of(username)
        if not 1 <= position <= len(notes):
            raise ValueError("Nota inexistente.")
        notes.pop(position - 1)
        self.save()


def read_password() -> str:
    return getpass.getpass("Senha: ") if sys.stdin.isatty() else input("Senha: ")


def user_session(store: AppStore, username: str) -> None:
    while True:
        print(USER_MENU)
        option = input("Opção: ").strip()
        try:
            if option == "1":
                store.add_note(username, input("Nota: "))
                print("Nota salva.")
            elif option == "2":
                for position, note in enumerate(store.notes_of(username), start=1):
                    print(f"{position}. {note}")
                if not store.notes_of(username):
                    print("Nenhuma nota.")
            elif option == "3":
                raw_position = input("Número da nota: ").strip()
                if not raw_position.isdigit():
                    raise ValueError("Digite um número válido.")
                store.delete_note(username, int(raw_position))
                print("Nota excluída.")
            elif option == "4":
                return
            else:
                print("Opção inválida.")
        except ValueError as error:
            print(f"Erro: {error}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    try:
        store = AppStore(path)
    except ValueError as error:
        print(f"Erro: {error} Corrija ou remova o arquivo.")
        return 1
    while True:
        print(GUEST_MENU)
        option = input("Opção: ").strip()
        if option == "1":
            try:
                store.register(input("Usuário: "), read_password())
                print("Conta criada.")
            except ValueError as error:
                print(f"Erro: {error}")
        elif option == "2":
            username = store.authenticate(input("Usuário: "), read_password())
            if username is None:
                print("Usuário ou senha incorretos.")
            else:
                print(f"Bem-vindo(a), {username}!")
                user_session(store, username)
        elif option == "0":
            print("Até logo!")
            return 0
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    sys.exit(main())
```

</details>
