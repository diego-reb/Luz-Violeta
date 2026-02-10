/* === ACCESIBILIDAD - SCRIPT FINAL SIN ERRORES === */

document.addEventListener("DOMContentLoaded", function () {

    /* ====== REESTAURAR ESTADO GUARDADO ====== */
    const savedState = JSON.parse(localStorage.getItem("accesibilityState")) || {
        mode: "",
        grayscale: false,
        contrast: false,
        font: false,
        guide: false,
        scale: 0  // 0 = tamaño normal
    };

    function saveState() {
        localStorage.setItem("accesibilityState", JSON.stringify(savedState));
    }

    /* ========= CREAR BOTÓN ========= */
const toggleBtn = document.createElement("button");
toggleBtn.id = "accesibility-toggle";
toggleBtn.innerHTML = `
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <!-- Brazo izquierdo extendido -->
        <path d="M4 11h4v2H4z"/>
        <!-- Cabeza -->
        <circle cx="12" cy="5" r="2.5"/>
        <!-- Torso -->
        <path d="M10 8h4v7h-4z"/>
        <!-- Brazo derecho extendido -->
        <path d="M16 11h4v2h-4z"/>
        <!-- Pierna izquierda -->
        <path d="M10 15v4l2 1v-5z"/>
        <!-- Pierna derecha -->
        <path d="M14 15v4l-2 1v-5z"/>
    </svg>
`;
document.body.appendChild(toggleBtn);

    /* ========= CREAR PANEL ========= */
    const panel = document.createElement("div");
    panel.id = "accesibility-panel";
    panel.innerHTML = `
        <button id="toggle-dark">Modo oscuro</button>
        <button id="toggle-light">Modo claro</button>
        <button id="toggle-contrast">Alto contraste</button>
        <button id="toggle-grayscale">Escala de grises</button>
        <button id="toggle-font">Cambio tipografía</button>

        <button id="text-minus">A+ Aumentar</button>
        <button id="text-plus">A- Disminuir</button>

        <button id="toggle-guide">Guía de lectura</button>

        <button id="toggle-read">Lectura en voz alta</button>
    `;
    document.body.appendChild(panel);

    /* ========= GUÍA DE LECTURA ========= */
    let readingMask = document.querySelector(".reading-guide-mask");
    if (!readingMask) {
        readingMask = document.createElement("div");
        readingMask.className = "reading-guide-mask";
        document.body.appendChild(readingMask);
    }

    /* ========= MOSTRAR PANEL ========= */
    toggleBtn.addEventListener("click", () => {
        panel.classList.toggle("active");
    });

    /* ========= APLICAR ESTADO GUARDADO ========= */
    function applySavedState() {
        document.body.classList.remove(
            "dark-mode", "light-mode", "high-contrast", "grayscale",
            "scale-text-small", "scale-text-medium", "scale-text-large",
            "scale-text-extra-large", "scale-text-max", "alt-font",
            "reading-guide-active"
        );

        if (savedState.mode) document.body.classList.add(savedState.mode);
        if (savedState.grayscale) document.body.classList.add("grayscale");
        if (savedState.contrast) document.body.classList.add("high-contrast");
        if (savedState.font) document.body.classList.add("alt-font");
        if (savedState.guide) document.body.classList.add("reading-guide-active");

        /* Tamaño */
        if (savedState.scale === 1) document.body.classList.add("scale-text-small");
        if (savedState.scale === 2) document.body.classList.add("scale-text-medium");
        if (savedState.scale === 3) document.body.classList.add("scale-text-large");
        if (savedState.scale === 4) document.body.classList.add("scale-text-extra-large");
        if (savedState.scale === 5) document.body.classList.add("scale-text-max");
    }

    applySavedState();

    /* ========= MARCAR ACTIVO ========= */
    function marcarActivo(boton) {
        panel.querySelectorAll("button").forEach(b => b.classList.remove("active-acc"));
        boton.classList.add("active-acc");
    }

    /* ========= MODOS ========= */
    document.getElementById("toggle-dark").addEventListener("click", function () {
        savedState.mode = "dark-mode";
        savedState.contrast = false;
        savedState.grayscale = false;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    document.getElementById("toggle-light").addEventListener("click", function () {
        savedState.mode = "light-mode";
        savedState.contrast = false;
        savedState.grayscale = false;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    document.getElementById("toggle-contrast").addEventListener("click", function () {
        savedState.mode = "";
        savedState.contrast = !savedState.contrast;
        savedState.grayscale = false;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    document.getElementById("toggle-grayscale").addEventListener("click", function () {
        savedState.mode = "";
        savedState.grayscale = !savedState.grayscale;
        savedState.contrast = false;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    /* ========= TIPOGRAFÍA ========= */
    document.getElementById("toggle-font").addEventListener("click", function () {
        savedState.font = !savedState.font;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    /* ========= ESCALA DE TEXTO ========= */
    document.getElementById("text-minus").addEventListener("click", function () {
        if (savedState.scale > 0) savedState.scale--;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    document.getElementById("text-plus").addEventListener("click", function () {
        if (savedState.scale < 5) savedState.scale++;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    /* ========= GUÍA ========= */
    let guideActive = savedState.guide;

    document.getElementById("toggle-guide").addEventListener("click", function () {
        guideActive = !guideActive;
        savedState.guide = guideActive;
        saveState();
        applySavedState();
        marcarActivo(this);
    });

    document.addEventListener("mousemove", function (e) {
        if (guideActive) {
            readingMask.style.top = e.clientY - 20 + "px";
        }
    });

    /* ========= LECTURA EN VOZ ALTA ========= */
    const readBtn = document.getElementById("toggle-read");
    let lecturaActiva = false;

    readBtn.addEventListener("click", function () {
        if (!("speechSynthesis" in window)) return alert("Tu navegador no soporta lectura de texto.");

        if (!lecturaActiva) {
            const texto = new SpeechSynthesisUtterance(document.body.innerText);
            texto.lang = "es-ES";
            texto.rate = 1;

            speechSynthesis.speak(texto);
            lecturaActiva = true;
            readBtn.innerText = "Detener lectura";

            texto.onend = () => {
                lecturaActiva = false;
                readBtn.innerText = "Lectura en voz alta";
            };

        } else {
            speechSynthesis.cancel();
            lecturaActiva = false;
            readBtn.innerText = "Lectura en voz alta";
        }
    });

});
