"use strict";

const USERS_URL = "https://jsonplaceholder.typicode.com/users";
const TIMEOUT_MS = 10000;

const loadButton = document.querySelector("#load-users");
const statusMessage = document.querySelector("#status");
const userList = document.querySelector("#user-list");

async function fetchJson(url) {
  const response = await fetch(url, { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!response.ok) {
    throw new Error(`A API respondeu com status ${response.status}.`);
  }
  return response.json();
}

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("status--error", isError);
}

function createUserItem({ name, email, address }) {
  const item = document.createElement("li");
  const title = document.createElement("strong");
  title.textContent = name;
  const details = document.createElement("div");
  details.className = "muted";
  details.textContent = `${email} · ${address.city}`;
  item.append(title, details);
  return item;
}

async function loadUsers() {
  loadButton.disabled = true;
  userList.replaceChildren();
  setStatus("Carregando...");
  try {
    const users = await fetchJson(USERS_URL);
    userList.replaceChildren(...users.map(createUserItem));
    setStatus(`${users.length} usuário(s) carregado(s).`);
  } catch (error) {
    setStatus(`Falha ao carregar: ${error.message}`, true);
  } finally {
    loadButton.disabled = false;
  }
}

loadButton.addEventListener("click", loadUsers);
