// 27. Catálogo de produtos: uso `node 27-catalogo-produtos.js [categoria]`.
"use strict";

const CATALOG = [
  { id: 1, name: "Notebook", category: "informática", price: 3500, stock: 4 },
  { id: 2, name: "Mouse", category: "informática", price: 80, stock: 30 },
  { id: 3, name: "Cadeira", category: "móveis", price: 750, stock: 0 },
  { id: 4, name: "Mesa", category: "móveis", price: 1200, stock: 6 },
];

function listCategories(catalog) {
  return [...new Set(catalog.map((product) => product.category))];
}

function filterByCategory(catalog, category) {
  return catalog.filter((product) => product.category === category);
}

function findProduct(catalog, id) {
  return catalog.find((product) => product.id === id) ?? null;
}

function formatProduct({ name, price, stock }) {
  const availability = stock > 0 ? `${stock} em estoque` : "esgotado";
  return `${name} - R$ ${price.toFixed(2)} (${availability})`;
}

function main() {
  const category = process.argv[2];
  const products = category ? filterByCategory(CATALOG, category) : CATALOG;
  if (products.length === 0) {
    console.log(`Categoria sem produtos. Opções: ${listCategories(CATALOG).join(", ")}`);
    return;
  }
  console.log(products.map(formatProduct).join("\n"));
}

if (require.main === module) {
  main();
}

module.exports = { CATALOG, listCategories, filterByCategory, findProduct, formatProduct };
