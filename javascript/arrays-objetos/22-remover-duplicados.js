// 22. Remover duplicados: uso `node 22-remover-duplicados.js a b a c b`.
"use strict";

function removeDuplicates(items) {
  return [...new Set(items)];
}

function main() {
  const items = process.argv.slice(2);
  console.log(removeDuplicates(items));
}

if (require.main === module) {
  main();
}

module.exports = { removeDuplicates };
