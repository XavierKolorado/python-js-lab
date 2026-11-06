// 05. Conversor de temperatura: uso `node 05-conversor-temperatura.js 25`.
"use strict";

const ABSOLUTE_ZERO_CELSIUS = -273.15;

function celsiusToFahrenheit(celsius) {
  if (!Number.isFinite(celsius)) {
    throw new Error("Informe uma temperatura numérica.");
  }
  if (celsius < ABSOLUTE_ZERO_CELSIUS) {
    throw new Error("A temperatura está abaixo do zero absoluto.");
  }
  return (celsius * 9) / 5 + 32;
}

function main() {
  const celsius = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`${celsius} °C = ${celsiusToFahrenheit(celsius).toFixed(1)} °F`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { celsiusToFahrenheit };
