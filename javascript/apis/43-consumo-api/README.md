<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 43. Consumo de API / API consumption

**Problema:** Consumir uma API utilizando `fetch()` e tratar respostas.  
**Problem:** Consume an API with `fetch()` and handle responses.

**Objetivo:** Tratar os estados de carregamento, sucesso e erro.  
**Goal:** Handle loading, success and error states.

**Conceitos / Concepts:** `fetch`, `async/await`, `AbortSignal.timeout`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/43-consumo-api/`

**Resultado esperado:** Lista de usuários, ou mensagem de erro com o botão ativo.  
**Expected result:** A user list, or an error message with the button enabled.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>43. Consumo de API</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Consumo de API</h1>
      <p class="muted">Usuários de exemplo da JSONPlaceholder.</p>
      <button id="load-users" class="btn" type="button">Carregar usuários</button>
      <p id="status" class="status" role="status"></p>
      <ul id="user-list" class="user-list"></ul>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const USERS_URL = "https://jsonplaceholder.typicode.com/users";
const TIMEOUT_MS = 10000;

const loadButton = document.querySelector("#load-users");
const statusMessage = document.querySelector("#status");
const userList = document.querySelector("#user-list");

async function fetchJson(url) {
  const response = await fetch(url, { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  return response.json();
}

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function createUserItem({ name, email, address }) {
  const item = document.createElement("li");
  const title = document.createElement("strong");
  title.textContent = name;
  const details = document.createElement("div");
  details.className = "muted";
  details.textContent = `${email} · ${address.city}`;
  item.append(title, details);
  return item;
}

async function loadUsers() {
  loadButton.disabled = true;
  userList.replaceChildren();
  setStatus("Carregando...");
  try {
    const users = await fetchJson(USERS_URL);
    userList.replaceChildren(...users.map(createUserItem));
    setStatus(`${users.length} usuário(s) carregado(s).`);
  } catch (error) {
    setStatus(`Falha ao carregar: ${error.message}`, true);
  } finally {
    loadButton.disabled = false;
  }
}

loadButton.addEventListener("click", loadUsers);
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
