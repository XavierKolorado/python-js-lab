# Guia de APIs / API guide

[Voltar ao README / Back to the README](../README.md)

Todas as APIs abaixo são públicas e **não exigem chave**. Nenhuma credencial é usada neste repositório.
*All APIs below are public and **need no key**. This repository uses no credentials.*

| API | Endpoint | Python | JavaScript | Observações / Notes |
|---|---|---|---|---|
| [ViaCEP](https://viacep.com.br/) | `viacep.com.br/ws/{cep}/json/` | 41, 44 | 44 | CEP inexistente devolve HTTP 200 com `erro`. / *Unknown ZIP returns HTTP 200 with `erro`.* |
| [Open-Meteo](https://open-meteo.com/) | `geocoding-api.open-meteo.com/v1/search`, `api.open-meteo.com/v1/forecast` | 42 | 45 | Uso não comercial gratuito. / *Free for non-commercial use.* |
| [Rick and Morty API](https://rickandmortyapi.com/) | `rickandmortyapi.com/api/character/` | 43 | 50 | Busca vazia devolve HTTP 404. / *Empty search returns HTTP 404.* |
| [Frankfurter](https://frankfurter.dev/) | `api.frankfurter.dev/v1/latest` | 45 | | Taxas de referência diárias, não cotação em tempo real. / *Daily reference rates, not live quotes.* |
| [is.gd](https://is.gd/developers.php) | `is.gd/create.php` | 46 | | Cada URL nova cria um link público e permanente. / *Each new URL creates a public, permanent link.* |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | `jsonplaceholder.typicode.com/todos`, `/users` | 47, 49 | 43 | Escritas são simuladas e nada é salvo. / *Writes are simulated and nothing is saved.* |
| [httpbin](https://httpbin.org/) | `httpbin.org/get`, `/post` | 48 | | Devolve o que recebeu; útil para testes. / *Echoes what it receives; useful for tests.* |
| [Studio Ghibli API](https://ghibliapi.vercel.app/) | `ghibliapi.vercel.app/films` | | 46 | Catálogo fixo, mantido pela comunidade. Pôsteres vêm de um servidor externo. / *Fixed, community-run catalog. Posters come from an external server.* |
| [DummyJSON](https://dummyjson.com/) | `dummyjson.com/products` | | 47 | Dados fictícios. / *Fictional data.* |

Por que a Studio Ghibli API no exercício 46? As APIs de filmes mais conhecidas exigem chave, e este repositório não usa credenciais.
*Why the Studio Ghibli API in exercise 46? The best-known movie APIs need a key, and this repository uses no credentials.*

## Conferir as APIs / Check the APIs

```bash
python tools/check_apis.py
```

O script não cria nada novo. APIs públicas podem mudar ou sair do ar sem aviso, então os exercícios tratam falhas de rede e mostram uma mensagem clara.
*The script creates nothing new. Public APIs can change or go down without notice, so the exercises handle network failures and show a clear message.*

## Boas práticas usadas / Practices used

- Tempo limite em toda requisição. / *A timeout on every request.*
- Conferência do status antes de ler o corpo. / *Status check before reading the body.*
- Validação da entrada antes de chamar a rede. / *Input validation before calling the network.*
- Mensagens de erro claras, sem expor um stack trace. / *Clear error messages, with no stack trace.*
- Nada de chaves no código. Se uma API exigir chave, use variável de ambiente e nunca faça commit dela. / *No keys in code. If an API needs a key, use an environment variable and never commit it.*
