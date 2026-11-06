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
