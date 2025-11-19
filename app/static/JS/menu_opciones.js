document.addEventListener("DOMContentLoaded", () => {
    const userBtn = document.getElementById("userMenuBtn");
    const userMenu = document.getElementById("userMenu");

    const hamburgerBtn = document.getElementById("hamburgerBtn");
    const hamburgerMenu = document.getElementById("hamburgerMenu");

    // Toggle desktop dropdown
    if(userBtn && userMenu){
        userBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            userMenu.classList.toggle("hidden");
        });
    }

    // Toggle mobile hamburger menu
    if(hamburgerBtn && hamburgerMenu){
        hamburgerBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            hamburgerMenu.classList.toggle("hidden");
        });
    }

    // Cerrar menú al hacer clic fuera
    document.addEventListener("click", () => {
        if(userMenu && !userMenu.classList.contains("hidden")) userMenu.classList.add("hidden");
        if(hamburgerMenu && !hamburgerMenu.classList.contains("hidden")) hamburgerMenu.classList.add("hidden");
    });
});