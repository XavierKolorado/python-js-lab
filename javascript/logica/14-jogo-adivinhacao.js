// 14. Jogo de adivinhação: uso `node 14-jogo-adivinhacao.js [maior-numero]`.
"use strict";

const readline = require("node:readline");

const DEFAULT_HIGHEST = 100;

function drawSecret(highest, random = Math.random) {
  return Math.floor(random() * highest) + 1;
}

function evaluateGuess(guess, secret) {
  if (guess < secret) {
    return "O número secreto é maior.";
  }
  if (guess > secret) {
    return "O número secreto é menor.";
  }
  return null;
}

async function play(highest) {
  const secret = drawSecret(highest);
  const lines = readline.createInterface({ input: process.stdin });
  let attempts = 0;
  console.log(`Adivinhe o número de 1 a ${highest}:`);
  for await (const line of lines) {
    const guess = Number(line.trim());
    if (line.trim() === "" || !Number.isInteger(guess) || guess < 1 || guess > highest) {
      console.log(`Digite um inteiro de 1 a ${highest}.`);
      continue;
    }
    attempts += 1;
    const hint = evaluateGuess(guess, secret);
    if (hint === null) {
      console.log(`Parabéns! Você acertou em ${attempts} tentativa(s).`);
      lines.close();
      return;
    }
    console.log(hint);
  }
  console.log(`Jogo encerrado. O número era ${secret}.`);
}

function main() {
  const highest = Number(process.argv[2] ?? DEFAULT_HIGHEST);
  if (!Number.isInteger(highest) || highest < 2) {
    console.error("Erro: o maior número precisa ser um inteiro maior que 1.");
    process.exitCode = 1;
    return;
  }
  play(highest);
}

if (require.main === module) {
  main();
}

module.exports = { drawSecret, evaluateGuess };
