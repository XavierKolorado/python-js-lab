// 26. Ordenação de produtos: uso `node 26-ordenacao-produtos.js [asc|desc]`.
"use strict";

const PRODUCTS = [
  { name: "Monitor", price: 900 },
  { name: "Mouse", price: 80 },
  { name: "Teclado", price: 150 },
  { name: "Headset", price: 220 },
];

function sortByPrice(products, direction = "asc") {
  if (direction !== "asc" && direction !== "desc") {
    throw new Error('A direção deve ser "asc" ou "desc".');
  }
  const multiplier = direction === "asc" ? 1 : -1;
  // A cópia evita alterar o array recebido, pois sort() muda o original.
  return [...products].sort((first, second) => (first.price - second.price) * multiplier);
}

function main() {
  try {
    for (const { name, price } of sortByPrice(PRODUCTS, process.argv[2])) {
      console.log(`${name}: R$ ${price.toFixed(2)}`);
    }
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { sortByPrice };
