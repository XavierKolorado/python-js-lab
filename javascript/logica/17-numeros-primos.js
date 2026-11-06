// 17. Números primos: uso `node 17-numeros-primos.js 97`.
"use strict";

function isPrime(number) {
  if (!Number.isInteger(number)) {
    throw new Error("Informe um número inteiro.");
  }
  if (number < 2) {
    return false;
  }
  if (number % 2 === 0) {
    return number === 2;
  }
  for (let divisor = 3; divisor * divisor <= number; divisor += 2) {
    if (number % divisor === 0) {
      return false;
    }
  }
  return true;
}

function main() {
  const number = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${number} ${isPrime(number) ? "é" : "não é"} primo.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { isPrime };
