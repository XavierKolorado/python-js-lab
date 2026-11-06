// 08. Maioridade: uso `node 08-maioridade.js 20`.
"use strict";

const LEGAL_AGE = 18;
const MAX_AGE = 130;

function isAdult(age) {
  if (!Number.isInteger(age) || age < 0 || age > MAX_AGE) {
    throw new Error(`Idade inválida. Use um inteiro de 0 a ${MAX_AGE}.`);
  }
  return age >= LEGAL_AGE;
}

function main() {
  const age = Number(process.argv[2] ?? "NaN");
  try {
    console.log(isAdult(age) ? "Maior de idade." : "Menor de idade.");
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { isAdult };
