// 28. Busca de usuários: uso `node 28-busca-usuarios.js ana`.
"use strict";

const USERS = [
  { id: 1, name: "Ana Souza", city: "Recife" },
  { id: 2, name: "Bruno Lima", city: "Curitiba" },
  { id: 3, name: "Luana Melo", city: "Manaus" },
  { id: 4, name: "João Araújo", city: "Salvador" },
];

function normalize(text) {
  return text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase().trim();
}

function searchUsers(users, term) {
  const needle = normalize(term);
  return users.filter((user) => normalize(user.name).includes(needle));
}

function main() {
  const term = process.argv[2] ?? "";
  if (term.trim() === "") {
    console.error("Erro: informe parte de um nome.");
    process.exitCode = 1;
    return;
  }
  const results = searchUsers(USERS, term);
  if (results.length === 0) {
    console.log("Nenhum usuário encontrado.");
  }
  results.forEach(({ name, city }) => console.log(`${name} (${city})`));
}

if (require.main === module) {
  main();
}

module.exports = { USERS, searchUsers };
