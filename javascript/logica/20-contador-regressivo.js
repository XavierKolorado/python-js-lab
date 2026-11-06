// 20. Contador regressivo: uso `node 20-contador-regressivo.js 5`.
"use strict";

const TICK_MILLISECONDS = 1000;

function buildCountdown(start) {
  if (!Number.isInteger(start) || start < 0) {
    throw new Error("Informe um inteiro maior ou igual a zero.");
  }
  return Array.from({ length: start + 1 }, (_, index) => start - index);
}

function runCountdown(start, onTick, onFinish, delay = TICK_MILLISECONDS) {
  const remaining = buildCountdown(start);
  const timer = setInterval(() => {
    onTick(remaining.shift());
    if (remaining.length === 0) {
      clearInterval(timer);
      onFinish();
    }
  }, delay);
}

function main() {
  try {
    runCountdown(
      Number(process.argv[2] ?? "NaN"),
      (seconds) => console.log(seconds),
      () => console.log("Tempo esgotado!"),
    );
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { buildCountdown, runCountdown };
