// 10. Calculadora de desconto: uso `node 10-calculadora-desconto.js 200 15`.
"use strict";

function calculateDiscount(price, percentage) {
  if (!Number.isFinite(price) || price < 0) {
    throw new Error("O preço precisa ser um número positivo.");
  }
  if (!Number.isFinite(percentage) || percentage < 0 || percentage > 100) {
    throw new Error("O desconto deve estar entre 0 e 100.");
  }
  const discount = (price * percentage) / 100;
  return { discount, finalPrice: price - discount };
}

function formatCurrency(value) {
  return new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value);
}

function main() {
  const [price, percentage] = process.argv.slice(2).map(Number);
  try {
    const { discount, finalPrice } = calculateDiscount(price, percentage);
    console.log(`Desconto: ${formatCurrency(discount)}`);
    console.log(`Preço final: ${formatCurrency(finalPrice)}`);
  } catch (error) {
    console.error(`Erro: ${error.message}`);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { calculateDiscount, formatCurrency };
