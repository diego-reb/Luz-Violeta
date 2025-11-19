const form = document.querySelector("form");
    const loader = document.getElementById("loader");

    form.addEventListener("submit", function() {
        loader.classList.remove("hidden");
        const button = form.querySelector("button[type='submit']");
        button.disabled = true;
        button.classList.add("opacity-70", "cursor-not-allowed");
    });