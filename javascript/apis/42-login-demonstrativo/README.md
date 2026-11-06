<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 42. Login demonstrativo / Demo login

**Problema:** Criar uma interface de login com validação local, sem apresentá-la como segurança real.  
**Problem:** Build a login interface with local validation, without presenting it as real security.

**Objetivo:** Entender por que autenticação não pode depender do navegador.  
**Goal:** Understand why authentication cannot rely on the browser.

**Conceitos / Concepts:** `sessionStorage`, formulários, segurança

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/apis/42-login-demonstrativo/`

**Resultado esperado:** Sessão de demonstração com aviso visível. A senha não é salva.  
**Expected result:** A demo session with a visible warning. The password is not stored.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>42. Login demonstrativo</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card stack">
      <h1>Login demonstrativo</h1>
      <p class="warning" role="note">
        <strong>Isto não é segurança real.</strong> Todo código no navegador pode ser lido
        e alterado. Autenticação de verdade acontece no servidor.
      </p>
      <section id="login-view">
        <p class="muted">Use <code>aluno</code> e a senha <code>lab-demo</code>.</p>
        <form id="login-form" class="stack" novalidate>
          <label>Usuário <input name="username" autocomplete="off" /></label>
          <label>Senha <input name="password" type="password" autocomplete="off" /></label>
          <button class="btn" type="submit">Entrar</button>
        </form>
        <p id="login-error" class="status status--error" role="alert"></p>
      </section>
      <section id="welcome-view" hidden>
        <p id="welcome-message"></p>
        <button id="logout" class="btn btn--ghost" type="button">Sair</button>
      </section>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
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
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
