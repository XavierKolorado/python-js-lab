<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# JavaScript, nível 5: Armazenamento, APIs e projetos

*JavaScript, level 5: Storage, APIs and projects*

[Voltar ao README principal / Back to the main README](../../README.md)

- [41. Preferências com localStorage](41-preferencias-localstorage/)
- [42. Login demonstrativo](42-login-demonstrativo/)
- [43. Consumo de API](43-consumo-api/)
- [44. Consulta de CEP](44-consulta-cep/)
- [45. Aplicação de clima](45-aplicacao-clima/)
- [46. Buscador de filmes](46-buscador-filmes/)
- [47. Painel de dados](47-painel-dados/)
- [48. CRUD de produtos](48-crud-produtos/)
- [49. Paginação](49-paginacao/)
- [50. Aplicação de favoritos](50-aplicacao-favoritos/)

## 41. Preferências com localStorage / Preferences with localStorage

**Problema:** Salvar e recuperar preferências do usuário.  
**Problem:** Save and restore user preferences.

**Objetivo:** Persistir no navegador e tolerar dados corrompidos.  
**Goal:** Persist in the browser and tolerate corrupted data.

**Conceitos / Concepts:** `localStorage`, `JSON`, formulários

**Arquivo / File:** [`41-preferencias-localstorage`](./41-preferencias-localstorage)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/41-preferencias-localstorage/`

**Resultado esperado:** Nome, fonte e destaque voltam ao recarregar.  
**Expected result:** Name, font and highlight return after reload.

## 42. Login demonstrativo / Demo login

**Problema:** Criar uma interface de login com validação local, sem apresentá-la como segurança real.  
**Problem:** Build a login interface with local validation, without presenting it as real security.

**Objetivo:** Entender por que autenticação não pode depender do navegador.  
**Goal:** Understand why authentication cannot rely on the browser.

**Conceitos / Concepts:** `sessionStorage`, formulários, segurança

**Arquivo / File:** [`42-login-demonstrativo`](./42-login-demonstrativo)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/42-login-demonstrativo/`

**Resultado esperado:** Sessão de demonstração com aviso visível. A senha não é salva.  
**Expected result:** A demo session with a visible warning. The password is not stored.

## 43. Consumo de API / API consumption

**Problema:** Consumir uma API utilizando `fetch()` e tratar respostas.  
**Problem:** Consume an API with `fetch()` and handle responses.

**Objetivo:** Tratar os estados de carregamento, sucesso e erro.  
**Goal:** Handle loading, success and error states.

**Conceitos / Concepts:** `fetch`, `async/await`, `AbortSignal.timeout`

**Arquivo / File:** [`43-consumo-api`](./43-consumo-api)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/43-consumo-api/`

**Resultado esperado:** Lista de usuários, ou mensagem de erro com o botão ativo.  
**Expected result:** A user list, or an error message with the button enabled.

## 44. Consulta de CEP / ZIP code lookup

**Problema:** Consultar CEP utilizando ViaCEP.  
**Problem:** Look up a ZIP code with ViaCEP.

**Objetivo:** Validar antes do `fetch` e tratar o erro no corpo.  
**Goal:** Validate before `fetch` and handle errors in the body.

**Conceitos / Concepts:** `fetch`, regex, `dl`

**Arquivo / File:** [`44-consulta-cep`](./44-consulta-cep)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/44-consulta-cep/`

**Resultado esperado:** O endereço, ou uma mensagem clara de erro.  
**Expected result:** The address, or a clear error message.

## 45. Aplicação de clima / Weather app

**Problema:** Criar uma aplicação que apresenta informações meteorológicas de uma API pública.  
**Problem:** Build an app that shows weather data from a public API.

**Objetivo:** Encadear requisições dependentes.  
**Goal:** Chain dependent requests.

**Conceitos / Concepts:** `fetch`, `URLSearchParams`, Open-Meteo

**Arquivo / File:** [`45-aplicacao-clima`](./45-aplicacao-clima)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/45-aplicacao-clima/`

**Resultado esperado:** Temperatura, condição, umidade e vento da cidade.  
**Expected result:** The city's temperature, condition, humidity and wind.

## 46. Buscador de filmes / Movie finder

**Problema:** Consumir uma API de filmes e apresentar resultados.  
**Problem:** Consume a movie API and show results.

**Objetivo:** Carregar uma vez e filtrar no cliente.  
**Goal:** Load once and filter on the client.

**Conceitos / Concepts:** `fetch`, `filter`, CSS Grid, Studio Ghibli API

**Arquivo / File:** [`46-buscador-filmes`](./46-buscador-filmes)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/46-buscador-filmes/`

**Resultado esperado:** Cartões de filmes filtrados por título, direção ou ano.  
**Expected result:** Movie cards filtered by title, director or year.

## 47. Painel de dados / Data dashboard

**Problema:** Criar um dashboard que apresenta informações de uma API REST.  
**Problem:** Build a dashboard with data from a REST API.

**Objetivo:** Agregar dados e desenhar barras com CSS.  
**Goal:** Aggregate data and draw bars with CSS.

**Conceitos / Concepts:** `reduce`, `Map`, `Intl`, DummyJSON

**Arquivo / File:** [`47-painel-dados`](./47-painel-dados)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/47-painel-dados/`

**Resultado esperado:** Indicadores, gráfico por categoria e ranking.  
**Expected result:** Metrics, a category chart and a ranking.

## 48. CRUD de produtos / Product CRUD

**Problema:** Cadastrar, listar, editar e excluir produtos com armazenamento local.  
**Problem:** Create, list, edit and delete products with local storage.

**Objetivo:** Integrar formulário, tabela e persistência.  
**Goal:** Combine a form, a table and persistence.

**Conceitos / Concepts:** `localStorage`, `crypto.randomUUID`, `confirm`

**Arquivo / File:** [`48-crud-produtos`](./48-crud-produtos)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/48-crud-produtos/`

**Resultado esperado:** Produtos mantidos ao recarregar, com validação e confirmação de exclusão.  
**Expected result:** Products kept after reload, with validation and delete confirmation.

## 49. Paginação / Pagination

**Problema:** Criar paginação para uma lista de dados.  
**Problem:** Build pagination for a data list.

**Objetivo:** Calcular páginas e limites com uma função pura.  
**Goal:** Compute pages and bounds with a pure function.

**Conceitos / Concepts:** `slice`, `Math.ceil`, `aria-current`

**Arquivo / File:** [`49-paginacao`](./49-paginacao)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/49-paginacao/`

**Resultado esperado:** Navegação por páginas com tamanho configurável.  
**Expected result:** Page navigation with a configurable page size.

## 50. Aplicação de favoritos / Favorites app

**Problema:** Consumir uma API, filtrar resultados e permitir salvar favoritos.  
**Problem:** Consume an API, filter results and save favorites.

**Objetivo:** Unir dados remotos e estado local.  
**Goal:** Combine remote data and local state.

**Conceitos / Concepts:** `fetch`, `localStorage`, Rick and Morty API

**Arquivo / File:** [`50-aplicacao-favoritos`](./50-aplicacao-favoritos)

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/50-aplicacao-favoritos/`

**Resultado esperado:** Busca por nome e status, e favoritos mantidos ao recarregar.  
**Expected result:** Search by name and status, with favorites kept after reload.
