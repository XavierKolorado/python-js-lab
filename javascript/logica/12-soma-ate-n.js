// 12. Soma até N: uso `node 12-soma-ate-n.js 100`.
"use strict";

function sumUpTo(limit) {
  if (!Number.isInteger(limit) || limit < 1) {
    throw new Error("O limite precisa ser um inteiro maior ou igual a 1.");
  }
  let total = 0;
  for (let number = 1; number <= limit; number += 1) {
    total += number;
  }
  return total;
}

function main() {
  const limit = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`A soma de 1 até ${limit} é ${sumUpTo(limit)}.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { sumUpTo };
