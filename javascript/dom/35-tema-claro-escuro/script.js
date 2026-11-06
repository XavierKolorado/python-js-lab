"use strict";

const STORAGE_KEY = "lab-theme";
const themeToggle = document.querySelector("#theme-toggle");

function readSavedTheme() {
  const savedTheme = localStorage.getItem(STORAGE_KEY);
  return savedTheme === "dark" || savedTheme === "light" ? savedTheme : null;
}

function getSystemTheme() {
  return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyTheme(theme) {
  const isDark = theme === "dark";
  document.documentElement.dataset.theme = theme;
  themeToggle.setAttribute("aria-pressed", String(isDark));
  themeToggle.textContent = isDark ? "Ativar tema claro" : "Ativar tema escuro";
}

themeToggle.addEventListener("click", () => {
  const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  localStorage.setItem(STORAGE_KEY, nextTheme);
  applyTheme(nextTheme);
});

applyTheme(readSavedTheme() ?? getSystemTheme());
