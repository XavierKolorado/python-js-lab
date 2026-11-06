"use strict";

const CHARACTERS_URL = "https://rickandmortyapi.com/api/character/";
const STORAGE_KEY = "lab-favorite-characters";
const TIMEOUT_MS = 10000;

const filterForm = document.querySelector("#filter-form");
const nameFilter = document.querySelector("#name-filter");
const statusFilter = document.querySelector("#status-filter");
const onlyFavorites = document.querySelector("#only-favorites");
const statusMessage = document.querySelector("#status");
const characterGrid = document.querySelector("#character-grid");

let characters = [];
let favorites = loadFavorites();

function loadFavorites() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return Array.isArray(saved) ? saved : [];
  } catch {
    return [];
  }
}

function persistFavorites() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites));
}

function isFavorite(id) {
  return favorites.some((favorite) => favorite.id === id);
}

function toggleFavorite(character) {
  favorites = isFavorite(character.id)
    ? favorites.filter(({ id }) => id !== character.id)
    : [...favorites, character];
  persistFavorites();
  render();
}

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

async function fetchCharacters(name, status) {
  const parameters = new URLSearchParams();
  if (name) {
    parameters.set("name", name);
  }
  if (status) {
    parameters.set("status", status);
  }
  const response = await fetch(`${CHARACTERS_URL}?${parameters}`, {
    signal: AbortSignal.timeout(TIMEOUT_MS),
  });
  // Esta API usa 404 para buscas sem resultado.
  if (response.status === 404) {
    return [];
  }
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  return (await response.json()).results;
}

function createCharacterCard(character) {
  const card = document.createElement("article");
  card.className = "character";
  const picture = document.createElement("img");
  picture.src = character.image;
  picture.alt = character.name;
  picture.loading = "lazy";
  const body = document.createElement("div");
  body.className = "character-body";
  const heading = document.createElement("h2");
  heading.textContent = character.name;
  const details = document.createElement("span");
  details.className = "muted";
  details.textContent = `${character.species} · ${character.status}`;
  const favoriteButton = document.createElement("button");
  const favorite = isFavorite(character.id);
  favoriteButton.type = "button";
  favoriteButton.className = "btn btn--ghost";
  favoriteButton.textContent = favorite ? "★ Favorito" : "☆ Favoritar";
  favoriteButton.setAttribute("aria-pressed", String(favorite));
  favoriteButton.addEventListener("click", () => toggleFavorite(character));
  body.append(heading, details, favoriteButton);
  card.append(picture, body);
  return card;
}

function render() {
  const visible = onlyFavorites.checked ? favorites : characters;
  characterGrid.replaceChildren(...visible.map(createCharacterCard));
  const emptyMessage = onlyFavorites.checked
    ? "Nenhum favorito salvo."
    : "Nenhum personagem encontrado.";
  setStatus(visible.length ? `${visible.length} personagem(ns)` : emptyMessage);
}

async function search() {
  setStatus("Buscando...");
  try {
    characters = await fetchCharacters(nameFilter.value.trim(), statusFilter.value);
    render();
  } catch (error) {
    setStatus(`Falha ao buscar: ${error.message}`, true);
  }
}

filterForm.addEventListener("submit", (event) => {
  event.preventDefault();
  onlyFavorites.checked = false;
  search();
});

onlyFavorites.addEventListener("change", render);

search();
