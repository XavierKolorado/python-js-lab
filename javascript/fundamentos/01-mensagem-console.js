// 01. Mensagem no console: exibe uma mensagem usando console.log().
"use strict";

function buildMessage(name = "visitante") {
  const cleanName = name.trim() || "visitante";
  return `Olá, ${cleanName}! Boas-vindas ao Python & JavaScript Lab.`;
}

function main() {
  console.log(buildMessage(process.argv[2]));
}

if (require.main === module) {
  main();
}

module.exports = { buildMessage };
