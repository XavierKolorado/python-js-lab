// 29. Agrupamento por idade: separa pessoas em faixas etárias.
"use strict";

const PEOPLE = [
  { name: "Lia", age: 9 },
  { name: "Davi", age: 15 },
  { name: "Marta", age: 34 },
  { name: "Caio", age: 41 },
  { name: "Rosa", age: 72 },
];

function getAgeGroup(age) {
  if (!Number.isInteger(age) || age < 0) {
    throw new Error(`Idade inválida: ${age}`);
  }
  if (age < 12) {
    return "crianças";
  }
  if (age < 18) {
    return "adolescentes";
  }
  return age < 60 ? "adultos" : "idosos";
}

function groupByAge(people) {
  return people.reduce((groups, person) => {
    const group = getAgeGroup(person.age);
    groups[group] = [...(groups[group] ?? []), person.name];
    return groups;
  }, {});
}

function main() {
  for (const [group, names] of Object.entries(groupByAge(PEOPLE))) {
    console.log(`${group}: ${names.join(", ")}`);
  }
}

if (require.main === module) {
  main();
}

module.exports = { getAgeGroup, groupByAge };
