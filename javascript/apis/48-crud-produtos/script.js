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
