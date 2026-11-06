"use strict";

const menuToggle = document.querySelector("#menu-toggle");
const siteMenu = document.querySelector("#site-menu");

function setMenuOpen(isOpen) {
  siteMenu.classList.toggle("site-menu--open", isOpen);
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.textContent = isOpen ? "Fechar" : "Menu";
}

menuToggle.addEventListener("click", () => {
  setMenuOpen(menuToggle.getAttribute("aria-expanded") !== "true");
});

siteMenu.addEventListener("click", (event) => {
  if (event.target.matches("a")) {
    setMenuOpen(false);
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    setMenuOpen(false);
  }
});
