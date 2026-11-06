"use strict";

const CAPITALS = [
  ["Belém", "Pará"], ["Belo Horizonte", "Minas Gerais"], ["Brasília", "Distrito Federal"],
  ["Curitiba", "Paraná"], ["Florianópolis", "Santa Catarina"], ["Fortaleza", "Ceará"],
  ["Goiânia", "Goiás"], ["João Pessoa", "Paraíba"], ["Maceió", "Alagoas"],
  ["Manaus", "Amazonas"], ["Natal", "Rio Grande do Norte"], ["Porto Alegre", "Rio Grande do Sul"],
  ["Recife", "Pernambuco"], ["Rio de Janeiro", "Rio de Janeiro"], ["Salvador", "Bahia"],
  ["São Luís", "Maranhão"], ["São Paulo", "São Paulo"], ["Teresina", "Piauí"], ["Vitória", "Espírito Santo"],
].map(([city, state]) => ({ city, state }));

const searchInput = document.querySelector("#search-input");
const resultCount = document.querySelector("#result-count");
const resultList = document.querySelector("#result-list");

function removeAccents(text) {
  return text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
}

function highlightMatch(text, term) {
  const fragment = document.createDocumentFragment();
  // Sem acentos, cada letra mantém a posição, então o índice vale para o original.
  const start = term ? removeAccents(text).indexOf(term) : -1;
  if (start < 0) {
    fragment.append(text);
    return fragment;
  }
  const mark = document.createElement("mark");
  mark.textContent = text.slice(start, start + term.length);
  fragment.append(text.slice(0, start), mark, text.slice(start + term.length));
  return fragment;
}

function render() {
  const term = removeAccents(searchInput.value.trim());
  const matches = CAPITALS.filter(({ city, state }) =>
    removeAccents(`${city} ${state}`).includes(term),
  );
  resultCount.textContent = matches.length
    ? `${matches.length} resultado(s)`
    : "Nenhum resultado encontrado.";
  resultList.replaceChildren(
    ...matches.map(({ city, state }) => {
      const item = document.createElement("li");
      const cityName = document.createElement("span");
      const stateName = document.createElement("span");
      cityName.append(highlightMatch(city, term));
      stateName.className = "muted";
      stateName.append(highlightMatch(state, term));
      item.append(cityName, stateName);
      return item;
    }),
  );
}

searchInput.addEventListener("input", render);
render();
