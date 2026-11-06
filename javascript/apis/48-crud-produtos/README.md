<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 48. CRUD de produtos / Product CRUD

**Problema:** Cadastrar, listar, editar e excluir produtos com armazenamento local.  
**Problem:** Create, list, edit and delete products with local storage.

**Objetivo:** Integrar formulário, tabela e persistência.  
**Goal:** Combine a form, a table and persistence.

**Conceitos / Concepts:** `localStorage`, `crypto.randomUUID`, `confirm`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/48-crud-produtos/`

**Resultado esperado:** Produtos mantidos ao recarregar, com validação e confirmação de exclusão.  
**Expected result:** Products kept after reload, with validation and delete confirmation.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>48. CRUD de produtos</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card card--wide stack">
      <h1>CRUD de produtos</h1>
      <form id="product-form" class="product-form" novalidate>
        <label>Nome <input name="name" maxlength="60" /></label>
        <label>Preço (R$) <input name="price" inputmode="decimal" /></label>
        <label>Quantidade <input name="quantity" inputmode="numeric" /></label>
        <div class="row form-actions">
          <button id="save-product" class="btn" type="submit">Cadastrar</button>
          <button id="cancel-edit" class="btn btn--ghost" type="button" hidden>Cancelar</button>
        </div>
      </form>
      <p id="status" class="status" role="status"></p>
      <table class="table">
        <thead><tr><th>Produto</th><th>Preço</th><th>Qtd.</th><th>Ações</th></tr></thead>
        <tbody id="product-rows"></tbody>
      </table>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const STORAGE_KEY = "lab-products";

const form = document.querySelector("#product-form");
const saveButton = document.querySelector("#save-product");
const cancelButton = document.querySelector("#cancel-edit");
const statusMessage = document.querySelector("#status");
const productRows = document.querySelector("#product-rows");

const priceFormat = new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" });

let products = loadProducts();
let editingId = null;

function loadProducts() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return Array.isArray(saved) ? saved : [];
  } catch {
    return [];
  }
}

function persistProducts() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(products));
}

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function readProductForm() {
  const name = form.elements.name.value.trim();
  const price = Number(form.elements.price.value.replace(",", "."));
  const rawQuantity = form.elements.quantity.value.trim();
  const quantity = Number(rawQuantity);
  if (!name) {
    throw new Error("Informe o nome do produto.");
  }
  if (!form.elements.price.value.trim() || !Number.isFinite(price) || price < 0) {
    throw new Error("Informe um preço válido.");
  }
  if (rawQuantity === "" || !Number.isInteger(quantity) || quantity < 0) {
    throw new Error("Informe uma quantidade inteira.");
  }
  return { name, price, quantity };
}

function setEditing(product) {
  editingId = product?.id ?? null;
  saveButton.textContent = product ? "Salvar alterações" : "Cadastrar";
  cancelButton.hidden = !product;
  form.reset();
  if (product) {
    form.elements.name.value = product.name;
    form.elements.price.value = product.price;
    form.elements.quantity.value = product.quantity;
    form.elements.name.focus();
  }
}

function deleteProduct(product) {
  if (!confirm(`Excluir ${product.name}?`)) {
    return;
  }
  products = products.filter(({ id }) => id !== product.id);
  if (editingId === product.id) {
    setEditing(null);
  }
  persistProducts();
  setStatus("Produto excluído.");
  render();
}

function createActionButton(label, className, onClick) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = `btn ${className}`;
  button.textContent = label;
  button.addEventListener("click", onClick);
  return button;
}

function createRow(product) {
  const row = document.createElement("tr");
  [product.name, priceFormat.format(product.price), product.quantity].forEach((text) => {
    const cell = document.createElement("td");
    cell.textContent = text;
    row.append(cell);
  });
  const actions = document.createElement("td");
  actions.className = "row";
  actions.append(
    createActionButton("Editar", "btn--ghost", () => setEditing(product)),
    createActionButton("Excluir", "btn--danger", () => deleteProduct(product)),
  );
  row.append(actions);
  return row;
}

function render() {
  if (products.length === 0) {
    const row = document.createElement("tr");
    const cell = document.createElement("td");
    cell.colSpan = 4;
    cell.className = "muted";
    cell.textContent = "Nenhum produto cadastrado.";
    row.append(cell);
    productRows.replaceChildren(row);
    return;
  }
  productRows.replaceChildren(...products.map(createRow));
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  try {
    const data = readProductForm();
    if (editingId === null) {
      products.push({ id: crypto.randomUUID(), ...data });
      setStatus("Produto cadastrado.");
    } else {
      products = products.map((product) =>
        product.id === editingId ? { ...product, ...data } : product,
      );
      setStatus("Produto atualizado.");
    }
    persistProducts();
    setEditing(null);
    render();
  } catch (error) {
    setStatus(error.message, true);
  }
});

cancelButton.addEventListener("click", () => setEditing(null));

render();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
