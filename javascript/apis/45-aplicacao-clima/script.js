"use strict";

const GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search";
const FORECAST_URL = "https://api.open-meteo.com/v1/forecast";
const TIMEOUT_MS = 10000;
const WEATHER_GROUPS = [
  { codes: [0], label: "Céu limpo" },
  { codes: [1, 2], label: "Parcialmente nublado" },
  { codes: [3], label: "Nublado" },
  { codes: [45, 48], label: "Neblina" },
  { codes: [51, 53, 55, 56, 57], label: "Garoa" },
  { codes: [61, 63, 65, 66, 67, 80, 81, 82], label: "Chuva" },
  { codes: [71, 73, 75, 77, 85, 86], label: "Neve" },
  { codes: [95, 96, 99], label: "Trovoada" },
];

const cityForm = document.querySelector("#city-form");
const cityInput = document.querySelector("#city-input");
const statusMessage = document.querySelector("#status");
const weatherCard = document.querySelector("#weather");

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function describeWeather(code) {
  return WEATHER_GROUPS.find(({ codes }) => codes.includes(code))?.label ?? "Condição desconhecida";
}

async function fetchJson(baseUrl, parameters) {
  const url = `${baseUrl}?${new URLSearchParams(parameters)}`;
  const response = await fetch(url, { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  return response.json();
}

async function findCity(name) {
  const { results } = await fetchJson(GEOCODING_URL, { name, count: 1, language: "pt" });
  if (!results?.length) {
    throw new Error("Cidade não encontrada.");
  }
  return results[0];
}

async function fetchWeather({ latitude, longitude }) {
  const { current } = await fetchJson(FORECAST_URL, {
    latitude,
    longitude,
    current: "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
    timezone: "auto",
  });
  return current;
}

function renderWeather(city, weather) {
  document.querySelector("#weather-city").textContent = `${city.name}, ${city.country ?? ""}`;
  document.querySelector("#weather-temperature").textContent = `${Math.round(weather.temperature_2m)} °C`;
  document.querySelector("#weather-description").textContent = describeWeather(weather.weather_code);
  document.querySelector("#weather-details").textContent =
    `Umidade ${weather.relative_humidity_2m}% · Vento ${weather.wind_speed_10m} km/h`;
  weatherCard.hidden = false;
}

cityForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const cityName = cityInput.value.trim();
  weatherCard.hidden = true;
  if (!cityName) {
    setStatus("Digite o nome de uma cidade.", true);
    return;
  }
  setStatus("Consultando...");
  try {
    const city = await findCity(cityName);
    renderWeather(city, await fetchWeather(city));
    setStatus("");
  } catch (error) {
    setStatus(error.message, true);
  }
});
