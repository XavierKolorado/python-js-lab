// 02. Variáveis: demonstra a diferença entre let e const.
"use strict";

function demonstrateLet() {
  let score = 10;
  score += 5;
  return score;
}

function demonstrateConstReassignment() {
  const language = "JavaScript";
  try {
    const fixedValue = 1;
    fixedValue = 2;
  } catch (error) {
    return `${language}: ${error.name} ao reatribuir uma const`;
  }
  return language;
}

function demonstrateConstObject() {
  const profile = { name: "Lab" };
  profile.level = 1;
  return profile;
}

function demonstrateBlockScope() {
  const insideValue = "fora";
  {
    const insideValue = "dentro";
    if (insideValue !== "dentro") {
      throw new Error("Escopo de bloco inesperado.");
    }
  }
  return insideValue;
}

function main() {
  console.log("let pode ser reatribuída:", demonstrateLet());
  console.log("const não pode:", demonstrateConstReassignment());
  console.log("const com objeto aceita mutação:", demonstrateConstObject());
  console.log("escopo de bloco preserva o valor externo:", demonstrateBlockScope());
}

if (require.main === module) {
  main();
}

module.exports = {
  demonstrateLet,
  demonstrateConstReassignment,
  demonstrateConstObject,
  demonstrateBlockScope,
};
