// 23. Filtro de pares: uso `node 23-filtro-pares.js 1 2 3 4`.
"use strict";

const DEFAULT_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function filterEven(numbers) {
  return numbers.filter((number) => number % 2 === 0);
}

function main() {
  const args = process.argv.slice(2).map(Number);
  const numbers = args.length > 0 ? args : DEFAULT_NUMBERS;
  if (!numbers.every(Number.isInteger)) {
    console.error("Erro: informe apenas números inteiros.");
    process.exitCode = 1;
    return;
  }
  console.log("Pares:", filterEven(numbers));
}

if (require.main === module) {
  main();
}

module.exports = { filterEven };
