const form = document.querySelector("form");
    const loader = document.getElementById("loader");

    form.addEventListener("submit", function() {
        // Mostrar loader al enviar formulario
        loader.classList.remove("hidden");

        // Deshabilitar botón para evitar múltiples envíos
        const button = form.querySelector("button[type='submit']");
        button.disabled = true;
        button.classList.add("opacity-70", "cursor-not-allowed");
    });