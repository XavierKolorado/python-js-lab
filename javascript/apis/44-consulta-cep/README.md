<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 44. Consulta de CEP / ZIP code lookup

**Problema:** Consultar CEP utilizando ViaCEP.  
**Problem:** Look up a ZIP code with ViaCEP.

**Objetivo:** Validar antes do `fetch` e tratar o erro no corpo.  
**Goal:** Validate before `fetch` and handle errors in the body.

**Conceitos / Concepts:** `fetch`, regex, `dl`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/44-consulta-cep/`

**Resultado esperado:** O endereço, ou uma mensagem clara de erro.  
**Expected result:** The address, or a clear error message.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>44. Consulta de CEP</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Consulta de CEP</h1>
      <form id="cep-form" class="search-form" novalidate>
        <input id="cep-input" aria-label="CEP" placeholder="01001-000" inputmode="numeric" maxlength="9" />
        <button class="btn" type="submit">Buscar</button>
      </form>
      <p id="status" class="status" role="status"></p>
      <dl id="address" class="address" hidden></dl>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const TIMEOUT_MS = 10000;
const ADDRESS_FIELDS = [
  ["CEP", "cep"],
  ["Logradouro", "logradouro"],
  ["Bairro", "bairro"],
  ["Cidade", "localidade"],
  ["Estado", "uf"],
  ["DDD", "ddd"],
];

const cepForm = document.querySelector("#cep-form");
const cepInput = document.querySelector("#cep-input");
const statusMessage = document.querySelector("#status");
const addressList = document.querySelector("#address");

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function normalizeCep(rawCep) {
  const digits = rawCep.replace(/\D/g, "");
  if (digits.length !== 8) {
    throw new Error("O CEP precisa ter 8 dígitos.");
  }
  return digits;
}

async function fetchAddress(cep) {
  const url = `https://viacep.com.br/ws/${cep}/json/`;
  const response = await fetch(url, { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  const data = await response.json();
  // A ViaCEP responde 200 com { erro: "true" } quando o CEP não existe.
  if (data.erro) {
    throw new Error("CEP não encontrado.");
  }
  return data;
}

function renderAddress(address) {
  const rows = ADDRESS_FIELDS.filter(([, key]) => address[key]).flatMap(([label, key]) => {
    const term = document.createElement("dt");
    const value = document.createElement("dd");
    term.textContent = label;
    value.textContent = address[key];
    return [term, value];
  });
  addressList.replaceChildren(...rows);
  addressList.hidden = false;
}

cepForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  addressList.hidden = true;
  setStatus("Buscando...");
  try {
    renderAddress(await fetchAddress(normalizeCep(cepInput.value)));
    setStatus("");
  } catch (error) {
    setStatus(error.message, true);
  }
});
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
