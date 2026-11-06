<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 39. Pesquisa em tempo real / Live search

**Problema:** Filtrar elementos conforme o usuário digita.  
**Problem:** Filter items as the user types.

**Objetivo:** Reagir ao evento `input` e destacar sem `innerHTML`.  
**Goal:** React to `input` and highlight without `innerHTML`.

**Conceitos / Concepts:** `input`, `normalize`, `DocumentFragment`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/39-pesquisa-tempo-real/`

**Resultado esperado:** A lista diminui a cada tecla e o termo fica destacado.  
**Expected result:** The list narrows on each key and the term is highlighted.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>39. Pesquisa em tempo real</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Pesquisa em tempo real</h1>
      <input id="search-input" type="search" aria-label="Pesquisar capital" placeholder="Digite uma capital ou estado" />
      <p id="result-count" class="muted" role="status"></p>
      <ul id="result-list" class="result-list"></ul>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const CAPITALS = [
  ["Belém", "Pará"], ["Belo Horizonte", "Minas Gerais"], ["Brasília", "Distrito Federal"],
  ["Curitiba", "Paraná"], ["Florianópolis", "Santa Catarina"], ["Fortaleza", "Ceará"],
  ["Goiânia", "Goiás"], ["João Pessoa", "Paraíba"], ["Maceió", "Alagoas"],
  ["Manaus", "Amazonas"], ["Natal", "Rio Grande do Norte"], ["Porto Alegre", "Rio Grande do Sul"],
  ["Recife", "Pernambuco"], ["Rio de Janeiro", "Rio de Janeiro"], ["Salvador", "Bahia"],
  ["São Luís", "Maranhão"], ["São Paulo", "São Paulo"], ["Teresina", "Piauí"], ["Vitória", "Espírito Santo"],
].map(([city, state]) => ({ city, state }));

const searchInput = document.querySelector("#search-input");
const resultCount = document.querySelector("#result-count");
const resultList = document.querySelector("#result-list");

function removeAccents(text) {
  return text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
}

function highlightMatch(text, term) {
  const fragment = document.createDocumentFragment();
  // Sem acentos, cada letra mantém a posição, então o índice vale para o original.
  const start = term ? removeAccents(text).indexOf(term) : -1;
  if (start < 0) {
    fragment.append(text);
    return fragment;
  }
  const mark = document.createElement("mark");
  mark.textContent = text.slice(start, start + term.length);
  fragment.append(text.slice(0, start), mark, text.slice(start + term.length));
  return fragment;
}

function render() {
  const term = removeAccents(searchInput.value.trim());
  const matches = CAPITALS.filter(({ city, state }) =>
    removeAccents(`${city} ${state}`).includes(term),
  );
  resultCount.textContent = matches.length
    ? `${matches.length} resultado(s)`
    : "Nenhum resultado encontrado.";
  resultList.replaceChildren(
    ...matches.map(({ city, state }) => {
      const item = document.createElement("li");
      const cityName = document.createElement("span");
      const stateName = document.createElement("span");
      cityName.append(highlightMatch(city, term));
      stateName.className = "muted";
      stateName.append(highlightMatch(state, term));
      item.append(cityName, stateName);
      return item;
    }),
  );
}

searchInput.addEventListener("input", render);
render();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
