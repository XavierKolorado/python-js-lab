"use strict";

const STORAGE_KEY = "lab-preferences";
const DEFAULT_PREFERENCES = { name: "", fontSize: "16", highlight: false };

const form = document.querySelector("#preferences-form");
const greeting = document.querySelector("#greeting");
const statusMessage = document.querySelector("#status");

function loadPreferences() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return { ...DEFAULT_PREFERENCES, ...saved };
  } catch {
    // Dado corrompido não deve impedir a página de abrir.
    return { ...DEFAULT_PREFERENCES };
  }
}

function applyPreferences({ name, fontSize, highlight }) {
  document.documentElement.style.fontSize = `${fontSize}px`;
  document.querySelector(".card").classList.toggle("card--highlight", highlight);
  greeting.textContent = name ? `Olá, ${name}!` : "Nenhum nome salvo.";
}

function fillForm({ name, fontSize, highlight }) {
  form.elements.name.value = name;
  form.elements.fontSize.value = fontSize;
  form.elements.highlight.checked = highlight;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const preferences = {
    name: form.elements.name.value.trim(),
    fontSize: form.elements.fontSize.value,
    highlight: form.elements.highlight.checked,
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(preferences));
  applyPreferences(preferences);
  statusMessage.textContent = "Preferências salvas.";
});

document.querySelector("#clear-preferences").addEventListener("click", () => {
  localStorage.removeItem(STORAGE_KEY);
  fillForm(DEFAULT_PREFERENCES);
  applyPreferences(DEFAULT_PREFERENCES);
  statusMessage.textContent = "Preferências removidas.";
});

const initialPreferences = loadPreferences();
fillForm(initialPreferences);
applyPreferences(initialPreferences);
