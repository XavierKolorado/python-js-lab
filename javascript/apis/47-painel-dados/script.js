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
