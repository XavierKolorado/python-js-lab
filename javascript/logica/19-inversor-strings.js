// 19. Inversor de strings: uso `node 19-inversor-strings.js "Olá, mundo"`.
"use strict";

function reverseString(text) {
  // O espalhamento percorre caracteres completos, preservando emojis.
  return [...text].reverse().join("");
}

function main() {
  console.log(reverseString(process.argv[2] ?? ""));
}

if (require.main === module) {
  main();
}

module.exports = { reverseString };
