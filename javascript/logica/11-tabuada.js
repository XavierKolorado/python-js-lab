// 11. Tabuada: uso `node 11-tabuada.js 7`.
"use strict";

function buildMultiplicationTable(number, lastFactor = 10) {
  if (!Number.isInteger(number)) {
    throw new Error("Informe um número inteiro.");
  }
  const lines = [];
  for (let factor = 1; factor <= lastFactor; factor += 1) {
    lines.push(`${number} x ${String(factor).padStart(2)} = ${number * factor}`);
  }
  return lines;
}

function main() {
  try {
    console.log(buildMultiplicationTable(Number(process.argv[2] ?? "NaN")).join("\n"));
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { buildMultiplicationTable };
