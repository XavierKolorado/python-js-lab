"use strict";

const modal = document.querySelector("#modal");
const modalResult = document.querySelector("#modal-result");

document.querySelector("#open-modal").addEventListener("click", () => {
  modal.returnValue = "";
  modal.showModal();
});

modal.addEventListener("click", (event) => {
  // Um clique no fundo tem o próprio dialog como alvo; no conteúdo, não.
  const box = modal.getBoundingClientRect();
  const isInside =
    event.clientX >= box.left && event.clientX <= box.right &&
    event.clientY >= box.top && event.clientY <= box.bottom;
  if (event.target === modal && !isInside) {
    modal.close("fechado");
  }
});

modal.addEventListener("close", () => {
  modalResult.textContent = `Resultado: ${modal.returnValue || "fechado"}`;
});
