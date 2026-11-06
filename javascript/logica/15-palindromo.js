// 15. Palíndromo: uso `node 15-palindromo.js "Ame a ema"`.
"use strict";

function normalizeText(text) {
  return text
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]/gu, "");
}

function isPalindrome(text) {
  const normalized = normalizeText(text);
  if (normalized === "") {
    throw new Error("Informe ao menos uma letra ou número.");
  }
  return normalized === [...normalized].reverse().join("");
}

function main() {
  const text = process.argv[2] ?? "";
  try {
    console.log(`"${text}" ${isPalindrome(text) ? "é" : "não é"} um palíndromo.`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { isPalindrome };
