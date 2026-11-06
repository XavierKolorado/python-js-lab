// 21. Maior e menor: uso `node 21-maior-menor.js 8 3 15`.
"use strict";

function findMinMax(numbers) {
  if (numbers.length === 0) {
    throw new Error("O array está vazio.");
  }
  if (!numbers.every(Number.isFinite)) {
    throw new Error("O array contém valores que não são números.");
  }
  return numbers.reduce(
    ({ smallest, largest }, number) => ({
      smallest: Math.min(smallest, number),
      largest: Math.max(largest, number),
    }),
    { smallest: numbers[0], largest: numbers[0] },
  );
}

function main() {
  try {
    const { smallest, largest } = findMinMax(process.argv.slice(2).map(Number));
    console.log(`Menor: ${smallest}`);
    console.log(`Maior: ${largest}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { findMinMax };
