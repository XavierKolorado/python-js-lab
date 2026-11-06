// 13. Fatorial: uso `node 13-fatorial.js 25`. BigInt mantém a precisão em valores grandes.
"use strict";

function factorial(number) {
  if (!Number.isInteger(number) || number < 0) {
    throw new Error("Informe um inteiro maior ou igual a zero.");
  }
  let result = 1n;
  for (let factor = 2n; factor <= BigInt(number); factor += 1n) {
    result *= factor;
  }
  return result;
}

function main() {
  const number = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${number}! = ${factorial(number)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { factorial };
