// 06. Par ou ímpar: uso `node 06-par-ou-impar.js 7`.
"use strict";

function getParity(number) {
  if (!Number.isInteger(number)) {
    throw new Error("Informe um número inteiro.");
  }
  return number % 2 === 0 ? "par" : "ímpar";
}

function main() {
  const number = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${number} é ${getParity(number)}.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { getParity };
