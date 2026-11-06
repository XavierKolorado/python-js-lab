"use strict";

// Credencial pública e didática: qualquer pessoa pode lê-la neste arquivo.
const DEMO_USER = { username: "aluno", password: "lab-demo" };
const SESSION_KEY = "lab-demo-session";

const loginView = document.querySelector("#login-view");
const welcomeView = document.querySelector("#welcome-view");
const loginForm = document.querySelector("#login-form");
const loginError = document.querySelector("#login-error");
const welcomeMessage = document.querySelector("#welcome-message");

function validateCredentials(username, password) {
  if (!username.trim() || !password) {
    return "Preencha usuário e senha.";
  }
  const isValid = username.trim() === DEMO_USER.username && password === DEMO_USER.password;
  return isValid ? "" : "Usuário ou senha incorretos.";
}

function render() {
  const username = sessionStorage.getItem(SESSION_KEY);
  loginView.hidden = username !== null;
  welcomeView.hidden = username === null;
  welcomeMessage.textContent = username ? `Sessão de demonstração ativa para ${username}.` : "";
}

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const { username, password } = loginForm.elements;
  const error = validateCredentials(username.value, password.value);
  loginError.textContent = error;
  if (!error) {
    sessionStorage.setItem(SESSION_KEY, username.value.trim());
    loginForm.reset();
    render();
  }
});

document.querySelector("#logout").addEventListener("click", () => {
  sessionStorage.removeItem(SESSION_KEY);
  render();
});

render();
