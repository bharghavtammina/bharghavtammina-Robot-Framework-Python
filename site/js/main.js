(function () {
  const DEMO_USER = "demo";
  const DEMO_PASS = "secret123";

  const loginForm = document.getElementById("login-form");
  if (loginForm) {
    loginForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value;
      const error = document.getElementById("login-error");

      if (username === DEMO_USER && password === DEMO_PASS) {
        window.location.href = "dashboard.html";
        return;
      }

      error.classList.remove("hidden");
    });
  }

  const contactForm = document.getElementById("contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      event.preventDefault();
      document.getElementById("contact-success").classList.remove("hidden");
      contactForm.reset();
    });
  }
})();
