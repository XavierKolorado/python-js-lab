<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 47. Painel de dados / Data dashboard

**Problema:** Criar um dashboard que apresenta informações de uma API REST.  
**Problem:** Build a dashboard with data from a REST API.

**Objetivo:** Agregar dados e desenhar barras com CSS.  
**Goal:** Aggregate data and draw bars with CSS.

**Conceitos / Concepts:** `reduce`, `Map`, `Intl`, DummyJSON

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/47-painel-dados/`

**Resultado esperado:** Indicadores, gráfico por categoria e ranking.  
**Expected result:** Metrics, a category chart and a ranking.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>47. Painel de dados</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card card--wide stack">
      <h1>Painel de produtos</h1>
      <p class="muted">Dados de exemplo da DummyJSON.</p>
      <p id="status" class="status" role="status"></p>
      <section id="metrics" class="metrics" aria-label="Indicadores"></section>
      <section>
        <h2>Categorias com mais produtos</h2>
        <div id="category-chart" class="bars"></div>
      </section>
      <section>
        <h2>Melhor avaliados</h2>
        <table class="table">
          <thead><tr><th>Produto</th><th>Categoria</th><th>Nota</th><th>Preço</th></tr></thead>
          <tbody id="top-products"></tbody>
        </table>
      </section>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const PRODUCTS_URL =
  "https://dummyjson.com/products?limit=100&select=title,price,rating,stock,category";
const TIMEOUT_MS = 10000;
const TOP_CATEGORIES = 6;
const TOP_PRODUCTS = 5;

const statusMessage = document.querySelector("#status");
const metrics = document.querySelector("#metrics");
const categoryChart = document.querySelector("#category-chart");
const topProducts = document.querySelector("#top-products");

const currency = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" });

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function averageOf(products, field) {
  return products.reduce((total, product) => total + product[field], 0) / products.length;
}

function summarize(products) {
  return [
    ["Produtos", products.length],
    ["Unidades em estoque", products.reduce((total, { stock }) => total + stock, 0)],
    ["Preço médio", currency.format(averageOf(products, "price"))],
    ["Nota média", averageOf(products, "rating").toFixed(2)],
  ];
}

function countByCategory(products) {
  const counts = new Map();
  products.forEach(({ category }) => counts.set(category, (counts.get(category) ?? 0) + 1));
  return [...counts].sort((first, second) => second[1] - first[1]).slice(0, TOP_CATEGORIES);
}

function renderMetrics(products) {
  metrics.replaceChildren(
    ...summarize(products).map(([label, value]) => {
      const metric = document.createElement("div");
      metric.className = "metric";
      const number = document.createElement("strong");
      number.textContent = value;
      const caption = document.createElement("span");
      caption.className = "muted";
      caption.textContent = label;
      metric.append(number, caption);
      return metric;
    }),
  );
}

function renderChart(products) {
  const categories = countByCategory(products);
  const largest = categories[0]?.[1] ?? 1;
  categoryChart.replaceChildren(
    ...categories.map(([category, amount]) => {
      const row = document.createElement("div");
      row.className = "bar";
      const label = document.createElement("span");
      label.textContent = category;
      const track = document.createElement("span");
      track.className = "bar-track";
      const fill = document.createElement("span");
      fill.className = "bar-fill";
      fill.style.width = `${(amount / largest) * 100}%`;
      track.append(fill);
      const value = document.createElement("span");
      value.textContent = amount;
      row.append(label, track, value);
      return row;
    }),
  );
}

function renderTable(products) {
  const ranked = [...products].sort((first, second) => second.rating - first.rating);
  topProducts.replaceChildren(
    ...ranked.slice(0, TOP_PRODUCTS).map(({ title, category, rating, price }) => {
      const row = document.createElement("tr");
      [title, category, rating.toFixed(2), currency.format(price)].forEach((text) => {
        const cell = document.createElement("td");
        cell.textContent = text;
        row.append(cell);
      });
      return row;
    }),
  );
}

async function loadDashboard() {
  setStatus("Carregando dados...");
  try {
    const response = await fetch(PRODUCTS_URL, { signal: AbortSignal.timeout(TIMEOUT_MS) });
    if (!response.ok) {
      throw new Error(`A API respondeu com status ${response.status}.`);
    }
    const { products } = await response.json();
    if (products.length === 0) {
      setStatus("A API não retornou produtos.");
      return;
    }
    renderMetrics(products);
    renderChart(products);
    renderTable(products);
    setStatus("");
  } catch (error) {
    setStatus(`Falha ao carregar: ${error.message}`, true);
  }
}

loadDashboard();
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
