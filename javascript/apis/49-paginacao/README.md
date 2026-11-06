<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 49. Paginação / Pagination

**Problema:** Criar paginação para uma lista de dados.  
**Problem:** Build pagination for a data list.

**Objetivo:** Calcular páginas e limites com uma função pura.  
**Goal:** Compute pages and bounds with a pure function.

**Conceitos / Concepts:** `slice`, `Math.ceil`, `aria-current`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/49-paginacao/`

**Resultado esperado:** Navegação por páginas com tamanho configurável.  
**Expected result:** Page navigation with a configurable page size.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>49. Paginação</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Paginação</h1>
      <label class="page-size">Itens por página
        <select id="page-size">
          <option>5</option>
          <option selected>10</option>
          <option>20</option>
        </select>
      </label>
      <ol id="item-list" class="item-list"></ol>
      <nav class="row pagination" aria-label="Paginação">
        <button id="previous-page" class="btn btn--ghost" type="button">Anterior</button>
        <span id="page-buttons" class="row"></span>
        <button id="next-page" class="btn btn--ghost" type="button">Próxima</button>
      </nav>
      <p id="page-info" class="muted" role="status"></p>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const TOTAL_ITEMS = 53;
const ITEMS = Array.from({ length: TOTAL_ITEMS }, (_, index) => `Registro ${index + 1}`);

const pageSizeSelect = document.querySelector("#page-size");
const itemList = document.querySelector("#item-list");
const pageButtons = document.querySelector("#page-buttons");
const previousButton = document.querySelector("#previous-page");
const nextButton = document.querySelector("#next-page");
const pageInfo = document.querySelector("#page-info");

let currentPage = 1;

function paginate(items, page, pageSize) {
  const totalPages = Math.max(1, Math.ceil(items.length / pageSize));
  const safePage = Math.min(Math.max(page, 1), totalPages);
  const start = (safePage - 1) * pageSize;
  return { page: safePage, totalPages, start, pageItems: items.slice(start, start + pageSize) };
}

function createPageButton(pageNumber, isCurrent) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "btn btn--ghost";
  button.textContent = pageNumber;
  if (isCurrent) {
    button.setAttribute("aria-current", "page");
  }
  button.addEventListener("click", () => goToPage(pageNumber));
  return button;
}

function goToPage(page) {
  currentPage = page;
  render();
}

function render() {
  const pageSize = Number(pageSizeSelect.value);
  const { page, totalPages, start, pageItems } = paginate(ITEMS, currentPage, pageSize);
  currentPage = page;
  itemList.replaceChildren(
    ...pageItems.map((text) => {
      const item = document.createElement("li");
      item.textContent = text;
      return item;
    }),
  );
  pageButtons.replaceChildren(
    ...Array.from({ length: totalPages }, (_, index) => createPageButton(index + 1, index + 1 === page)),
  );
  previousButton.disabled = page === 1;
  nextButton.disabled = page === totalPages;
  pageInfo.textContent = `Exibindo ${start + 1} a ${start + pageItems.length} de ${ITEMS.length}`;
}

previousButton.addEventListener("click", () => goToPage(currentPage - 1));
nextButton.addEventListener("click", () => goToPage(currentPage + 1));
pageSizeSelect.addEventListener("change", () => goToPage(1));

render();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
