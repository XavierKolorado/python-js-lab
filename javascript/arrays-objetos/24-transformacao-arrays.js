// 24. Transformação de arrays: aplica map() para criar novos arrays.
"use strict";

const PRODUCTS = [
  { name: "Teclado", price: 150 },
  { name: "Mouse", price: 80 },
  { name: "Monitor", price: 900 },
];

function doubleValues(numbers) {
  return numbers.map((number) => number * 2);
}

function applyIncrease(products, percentage) {
  const factor = 1 + percentage / 100;
  return products.map((product) => ({ ...product, price: product.price * factor }));
}

function toLabels(products) {
  return products.map(({ name, price }) => `${name}: R$ ${price.toFixed(2)}`);
}

function main() {
  console.log("Dobro:", doubleValues([1, 2, 3]));
  console.log("Com 10% de aumento:", toLabels(applyIncrease(PRODUCTS, 10)));
}

if (require.main === module) {
  main();
}

module.exports = { doubleValues, applyIncrease, toLabels };
