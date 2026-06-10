document.addEventListener("DOMContentLoaded", () => {

    const toggleBtn = document.getElementById("theme-toggle");

    // Exit early on pages where the theme toggle button is not rendered.
    if (!toggleBtn) return;

    // Restore the previously selected theme, defaulting to light mode.
    const savedTheme = localStorage.getItem("theme") || "light";

    document.documentElement.setAttribute(
        "data-bs-theme",
        savedTheme
    );

    // Keep the button label in sync with the active theme.
    toggleBtn.textContent =
        savedTheme === "dark"
            ? "Light Mode"
            : "Dark Mode";

    // Switch themes when the user clicks the toggle button.
    toggleBtn.addEventListener("click", () => {

        const currentTheme =
            document.documentElement.getAttribute("data-bs-theme");

        // Flip between the two supported Bootstrap theme values.
        const newTheme =
            currentTheme === "dark"
                ? "light"
                : "dark";

        document.documentElement.setAttribute(
            "data-bs-theme",
            newTheme
        );

        // Save the new preference so it persists across page reloads.
        localStorage.setItem("theme", newTheme);

        toggleBtn.textContent =
            newTheme === "dark"
                ? "Light Mode"
                : "Dark Mode";
    });

});


document.addEventListener("DOMContentLoaded", () => {

    const contactForm = document.getElementById("contact-formspree-form");
    const contactAlert = document.getElementById("contact-form-alert");

    // Exit early on pages where the contact form is not rendered.
    if (!contactForm || !contactAlert) return;

    contactForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const submitButton = contactForm.querySelector("button[type='submit']");
        const originalButtonText = submitButton.textContent;
        const formData = new FormData(contactForm);

        contactAlert.className = "alert d-none";
        contactAlert.textContent = "";
        submitButton.disabled = true;
        submitButton.textContent = "Sending...";

        try {
            const response = await fetch(contactForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "Accept": "application/json"
                }
            });

            if (response.ok) {
                contactAlert.className = "alert alert-success";
                contactAlert.textContent =
                    "Thank you! Your message has been sent. " +
                    "I’ll get back to you as soon as possible.";
                contactForm.reset();
            } else {
                contactAlert.className = "alert alert-danger";
                contactAlert.textContent =
                    "Sorry, your message could not be sent right now. " +
                    "Please try again later.";
            }
        } catch (error) {
            contactAlert.className = "alert alert-danger";
            contactAlert.textContent =
                "Sorry, your message could not be sent right now. " +
                "Please try again later.";
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = originalButtonText;
        }
    });

});