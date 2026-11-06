// 25. Soma com reduce: uso `node 25-soma-reduce.js 10 20 30`.
"use strict";

function sumValues(numbers) {
  return numbers.reduce((total, number) => total + number, 0);
}

function main() {
  const numbers = process.argv.slice(2).map(Number);
  if (!numbers.every(Number.isFinite)) {
    console.error("Erro: informe apenas números.");
    process.exitCode = 1;
    return;
  }
  console.log(`Soma: ${sumValues(numbers)}`);
}

if (require.main === module) {
  main();
}

module.exports = { sumValues };
