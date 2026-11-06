// 09. Classificação de notas: uso `node 09-classificacao-notas.js 8.5`.
"use strict";

const CATEGORIES = [
  { minimum: 9, label: "Excelente" },
  { minimum: 7, label: "Bom" },
  { minimum: 5, label: "Regular" },
  { minimum: 0, label: "Insuficiente" },
];

function classifyGrade(grade) {
  if (!Number.isFinite(grade) || grade < 0 || grade > 10) {
    throw new Error("A nota deve estar entre 0 e 10.");
  }
  return CATEGORIES.find(({ minimum }) => grade >= minimum).label;
}

function main() {
  const grade = Number(process.argv[2] ?? "NaN");
  try {
    console.log(`Nota ${grade}: ${classifyGrade(grade)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { classifyGrade };
