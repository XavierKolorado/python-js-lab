// 04. Média de notas: uso `node 04-media-notas.js 7 8.5 9`.
"use strict";

const GRADE_COUNT = 3;
const MAX_GRADE = 10;

function parseGrade(rawGrade) {
  const grade = Number(String(rawGrade).replace(",", "."));
  if (String(rawGrade).trim() === "" || !Number.isFinite(grade) || grade < 0 || grade > MAX_GRADE) {
    throw new Error(`Nota inválida: ${rawGrade}. Use valores de 0 a ${MAX_GRADE}.`);
  }
  return grade;
}

function calculateAverage(grades) {
  if (grades.length === 0) {
    throw new Error("Informe ao menos uma nota.");
  }
  return grades.reduce((total, grade) => total + grade, 0) / grades.length;
}

function main() {
  const rawGrades = process.argv.slice(2);
  try {
    if (rawGrades.length !== GRADE_COUNT) {
      throw new Error(`Informe exatamente ${GRADE_COUNT} notas.`);
    }
    console.log(`Média: ${calculateAverage(rawGrades.map(parseGrade)).toFixed(2)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { parseGrade, calculateAverage };
