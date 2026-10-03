document.documentElement.classList.add("js");
const menu = document.querySelector(".menu-toggle");
const nav = document.querySelector(".site-nav");
if (menu && nav) {
  const mobileLayout = window.matchMedia("(max-width: 1000px)");
  const closeMenu = () => { menu.setAttribute("aria-expanded", "false"); nav.classList.remove("is-open"); };
  const syncMenuLayout = () => {
    menu.hidden = !mobileLayout.matches;
    closeMenu();
  };
  syncMenuLayout();
  menu.addEventListener("click", () => {
    const open = menu.getAttribute("aria-expanded") !== "true";
    menu.setAttribute("aria-expanded", String(open)); nav.classList.toggle("is-open", open);
  });
  nav.addEventListener("click", event => { if (event.target.closest("a")) closeMenu(); });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && menu.getAttribute("aria-expanded") === "true") { closeMenu(); menu.focus(); }
  });
  mobileLayout.addEventListener("change", syncMenuLayout);
}
document.querySelectorAll("[data-current-year]").forEach(el => { el.textContent = new Date().getFullYear(); });
