// 16. Contador de vogais: uso `node 16-contador-vogais.js "Programação é prática"`.
"use strict";

const VOWELS = "aeiou";

function countVowels(text) {
  const decomposed = text.normalize("NFD").toLowerCase();
  const counts = Object.fromEntries([...VOWELS].map((vowel) => [vowel, 0]));
  for (const character of decomposed) {
    if (character in counts) {
      counts[character] += 1;
    }
  }
  return counts;
}

function main() {
  const counts = countVowels(process.argv[2] ?? "");
  const total = Object.values(counts).reduce((sum, amount) => sum + amount, 0);
  console.log(`Total de vogais: ${total}`);
  console.log(counts);
}

if (require.main === module) {
  main();
}

module.exports = { countVowels };
