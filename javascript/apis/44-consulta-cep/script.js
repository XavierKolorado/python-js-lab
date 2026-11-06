"use strict";

const TIMEOUT_MS = 10000;
const ADDRESS_FIELDS = [
  ["CEP", "cep"],
  ["Logradouro", "logradouro"],
  ["Bairro", "bairro"],
  ["Cidade", "localidade"],
  ["Estado", "uf"],
  ["DDD", "ddd"],
];

const cepForm = document.querySelector("#cep-form");
const cepInput = document.querySelector("#cep-input");
const statusMessage = document.querySelector("#status");
const addressList = document.querySelector("#address");

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function normalizeCep(rawCep) {
  const digits = rawCep.replace(/\D/g, "");
  if (digits.length !== 8) {
    throw new Error("O CEP precisa ter 8 dígitos.");
  }
  return digits;
}

async function fetchAddress(cep) {
  const url = `https://viacep.com.br/ws/${cep}/json/`;
  const response = await fetch(url, { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  const data = await response.json();
  // A ViaCEP responde 200 com { erro: "true" } quando o CEP não existe.
  if (data.erro) {
    throw new Error("CEP não encontrado.");
  }
  return data;
}

function renderAddress(address) {
  const rows = ADDRESS_FIELDS.filter(([, key]) => address[key]).flatMap(([label, key]) => {
    const term = document.createElement("dt");
    const value = document.createElement("dd");
    term.textContent = label;
    value.textContent = address[key];
    return [term, value];
  });
  addressList.replaceChildren(...rows);
  addressList.hidden = false;
}

cepForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  addressList.hidden = true;
  setStatus("Buscando...");
  try {
    renderAddress(await fetchAddress(normalizeCep(cepInput.value)));
    setStatus("");
  } catch (error) {
    setStatus(error.message, true);
  }
});
