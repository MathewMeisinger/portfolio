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