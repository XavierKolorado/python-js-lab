"use strict";

const MOVIES_URL = "https://ghibliapi.vercel.app/films";
const TIMEOUT_MS = 10000;

const searchInput = document.querySelector("#movie-search");
const statusMessage = document.querySelector("#status");
const movieGrid = document.querySelector("#movie-grid");

let movies = [];

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function matchesSearch(movie, term) {
  return [movie.title, movie.director, movie.release_date]
    .join(" ")
    .toLowerCase()
    .includes(term);
}

function createMovieCard({ title, director, release_date: year, image, rt_score: score }) {
  const card = document.createElement("article");
  card.className = "movie";
  const poster = document.createElement("img");
  poster.src = image;
  poster.alt = `Pôster de ${title}`;
  poster.loading = "lazy";
  const body = document.createElement("div");
  body.className = "movie-body";
  const heading = document.createElement("h2");
  heading.textContent = title;
  const details = document.createElement("p");
  details.className = "muted";
  details.textContent = `${year} · ${director} · nota ${score}`;
  body.append(heading, details);
  card.append(poster, body);
  return card;
}

function render() {
  const term = searchInput.value.trim().toLowerCase();
  const results = movies.filter((movie) => matchesSearch(movie, term));
  movieGrid.replaceChildren(...results.map(createMovieCard));
  setStatus(results.length ? `${results.length} filme(s)` : "Nenhum filme encontrado.");
}

async function loadMovies() {
  setStatus("Carregando filmes...");
  searchInput.disabled = true;
  try {
    const response = await fetch(MOVIES_URL, { signal: AbortSignal.timeout(TIMEOUT_MS) });
    if (!response.ok) {
      throw new Error(`A API respondeu com status ${response.status}.`);
    }
    movies = await response.json();
    searchInput.disabled = false;
    render();
  } catch (error) {
    setStatus(`Falha ao carregar: ${error.message}`, true);
  }
}

searchInput.addEventListener("input", render);
loadMovies();
