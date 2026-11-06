// 07. Maior número: uso `node 07-maior-numero.js 4 19 7`.
"use strict";

function largestOfThree(first, second, third) {
  const numbers = [first, second, third];
  if (!numbers.every(Number.isFinite)) {
    throw new Error("Informe três números válidos.");
  }
  let largest = first;
  if (second > largest) {
    largest = second;
  }
  if (third > largest) {
    largest = third;
  }
  return largest;
}

function main() {
  const [first, second, third] = process.argv.slice(2).map(Number);
  try {
    console.log(`Maior número: ${largestOfThree(first, second, third)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { largestOfThree };
