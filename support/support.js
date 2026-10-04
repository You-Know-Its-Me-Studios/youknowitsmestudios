(() => {
  const form = document.querySelector("#support-form");
  if (!form) return;

  const product = form.elements.product;
  const requestedProduct = new URLSearchParams(window.location.search).get("product");
  if (["general", "bodyhub", "strata"].includes(requestedProduct)) {
    product.value = requestedProduct;
  }

  const email = form.elements.email;
  const message = form.elements.message;
  const validate = (field) => {
    let error = "";
    if (!field.value.trim()) {
      error = field === email ? "Enter a reply email address." : "Enter a message.";
    } else if (field === email && field.validity.typeMismatch) {
      error = "Enter a valid email address, such as name@example.com.";
    }
    field.setAttribute("aria-invalid", String(Boolean(error)));
    document.getElementById(field === email ? "email-error" : "message-error").textContent = error;
    return !error;
  };

  [email, message].forEach(field => {
    field.addEventListener("blur", () => validate(field));
    field.addEventListener("input", () => {
      if (field.getAttribute("aria-invalid") === "true") validate(field);
    });
  });

  // Keep the form inert until a real delivery service is explicitly configured.
  // Never fall back to a GET request that could put a private message in a URL.
  form.addEventListener("submit", event => {
    event.preventDefault();
    const validEmail = validate(email);
    const validMessage = validate(message);
    if (!validEmail || !validMessage) {
      (validEmail ? message : email).focus();
      return;
    }
    const status = document.querySelector("#form-status");
    status.textContent = "Your message has not been sent. Online sending is not available yet. Your text is still here; copy it to keep it or send it through your preferred email service.";
    status.focus();
  });
})();
