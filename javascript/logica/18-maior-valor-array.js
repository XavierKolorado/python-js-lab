// 18. Maior valor de array: uso `node 18-maior-valor-array.js 3 9 2`.
"use strict";

function findLargest(numbers) {
  if (numbers.length === 0) {
    throw new Error("O array está vazio.");
  }
  if (!numbers.every(Number.isFinite)) {
    throw new Error("O array contém valores que não são números.");
  }
  let largest = numbers[0];
  for (const number of numbers) {
    if (number > largest) {
      largest = number;
    }
  }
  return largest;
}

function main() {
  try {
    console.log(`Maior valor: ${findLargest(process.argv.slice(2).map(Number))}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { findLargest };
