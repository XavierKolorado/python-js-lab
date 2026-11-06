// 03. Calculadora: uso `node 03-calculadora.js 10 + 5`. No shell, escreva "*" entre aspas.
"use strict";

const OPERATIONS = {
  "+": (first, second) => first + second,
  "-": (first, second) => first - second,
  "*": (first, second) => first * second,
  "/": (first, second) => {
    if (second === 0) {
      throw new Error("Não é possível dividir por zero.");
    }
    return first / second;
  },
};

function parseNumber(rawValue) {
  const number = Number(String(rawValue).replace(",", "."));
  if (rawValue === undefined || String(rawValue).trim() === "" || !Number.isFinite(number)) {
    throw new Error(`Número inválido: ${rawValue}`);
  }
  return number;
}

function calculate(first, symbol, second) {
  const operation = OPERATIONS[symbol];
  if (!operation) {
    throw new Error(`Operação inválida: ${symbol}`);
  }
  return operation(first, second);
}

function main() {
  const [rawFirst, symbol, rawSecond] = process.argv.slice(2);
  try {
    const first = parseNumber(rawFirst);
    const second = parseNumber(rawSecond);
    console.log(`${first} ${symbol} ${second} = ${calculate(first, symbol, second)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { calculate, parseNumber };
