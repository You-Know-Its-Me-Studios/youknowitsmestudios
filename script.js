document.documentElement.classList.add("js");
const menu = document.querySelector(".menu-toggle");
const nav = document.querySelector(".site-nav");
if (menu && nav) {
  menu.hidden = false;
  const closeMenu = () => { menu.setAttribute("aria-expanded", "false"); nav.classList.remove("is-open"); };
  menu.addEventListener("click", () => {
    const open = menu.getAttribute("aria-expanded") !== "true";
    menu.setAttribute("aria-expanded", String(open)); nav.classList.toggle("is-open", open);
  });
  nav.addEventListener("click", event => { if (event.target.closest("a")) closeMenu(); });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && menu.getAttribute("aria-expanded") === "true") { closeMenu(); menu.focus(); }
  });
  window.matchMedia("(min-width: 1001px)").addEventListener("change", event => { if (event.matches) closeMenu(); });
}
document.querySelectorAll("[data-current-year]").forEach(el => { el.textContent = new Date().getFullYear(); });
