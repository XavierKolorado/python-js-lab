<!-- Gerado por tools/build_docs.py. Edite tools/catalog.py. -->

# 33. Formulário validado / Validated form

**Problema:** Criar um formulário com validação de campos.  
**Problem:** Build a form with field validation.

**Objetivo:** Validar por campo e informar erros com acessibilidade.  
**Goal:** Validate per field and report errors accessibly.

**Conceitos / Concepts:** `FormData`, regex, `aria-invalid`

**Como executar / How to run**

```bash
python -m http.server 8000
```

Abra / Open: `http://localhost:8000/javascript/dom/33-formulario-validado/`

**Resultado esperado:** Mensagens por campo e sucesso quando tudo está válido.  
**Expected result:** Per-field messages and success when all is valid.

<details><summary>Código completo / Full code: <code>index.html</code></summary>

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>33. Formulário validado</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <main class="card">
      <h1>Formulário validado</h1>
      <p class="muted">Nenhum dado sai do navegador.</p>
      <form id="signup-form" class="stack" novalidate>
        <label>Nome
          <input name="name" autocomplete="name" />
          <small class="field-error" data-error-for="name"></small>
        </label>
        <label>E-mail
          <input name="email" type="email" autocomplete="email" />
          <small class="field-error" data-error-for="email"></small>
        </label>
        <label>Idade
          <input name="age" inputmode="numeric" />
          <small class="field-error" data-error-for="age"></small>
        </label>
        <label>Senha
          <input name="password" type="password" autocomplete="new-password" />
          <small class="field-error" data-error-for="password"></small>
        </label>
        <label>Confirmar senha
          <input name="confirmation" type="password" autocomplete="new-password" />
          <small class="field-error" data-error-for="confirmation"></small>
        </label>
        <button class="btn" type="submit">Enviar</button>
      </form>
      <p id="form-status" class="status" role="status"></p>
    </main>
  </body>
</html>
```

</details>

<details><summary>Código completo / Full code: <code>script.js</code></summary>

```javascript
"use strict";

const MIN_PASSWORD_LENGTH = 8;
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const signupForm = document.querySelector("#signup-form");
const formStatus = document.querySelector("#form-status");

const validators = {
  name: ({ name }) => (name.trim().length >= 2 ? "" : "Informe ao menos 2 caracteres."),
  email: ({ email }) => (EMAIL_PATTERN.test(email.trim()) ? "" : "Informe um e-mail válido."),
  age: ({ age }) => {
    const parsedAge = Number(age);
    const isValid = age.trim() !== "" && Number.isInteger(parsedAge) && parsedAge >= 18 && parsedAge <= 130;
    return isValid ? "" : "Informe uma idade de 18 a 130 anos.";
  },
  password: ({ password }) => {
    const isStrong = password.length >= MIN_PASSWORD_LENGTH && /\d/.test(password) && /[a-zA-Z]/.test(password);
    return isStrong ? "" : `Use ${MIN_PASSWORD_LENGTH}+ caracteres, com letras e números.`;
  },
  confirmation: ({ password, confirmation }) =>
    confirmation && password === confirmation ? "" : "As senhas não coincidem.",
};

function showFieldError(fieldName, message) {
  signupForm.elements[fieldName].setAttribute("aria-invalid", String(Boolean(message)));
  signupForm.querySelector(`[data-error-for="${fieldName}"]`).textContent = message;
}

function validateField(fieldName) {
  const values = Object.fromEntries(new FormData(signupForm));
  const message = validators[fieldName](values);
  showFieldError(fieldName, message);
  return message === "";
}

function validateForm() {
  return Object.keys(validators).map(validateField).every(Boolean);
}

Object.keys(validators).forEach((fieldName) => {
  signupForm.elements[fieldName].addEventListener("blur", () => validateField(fieldName));
});

signupForm.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!validateForm()) {
    formStatus.textContent = "Corrija os campos destacados.";
    return;
  }
  formStatus.textContent = "Cadastro validado com sucesso!";
  signupForm.reset();
});
```

</details>

O arquivo `style.css` completo está nesta pasta. / The full `style.css` is in this folder.
