// -------------------------------
// ABRIR / CERRAR MODALES
// -------------------------------
function abrirRegistro() {
    const modal = document.getElementById("overlay-registrar");
    modal.classList.remove("hidden");
}

function cerrarRegistro() {
    const modal = document.getElementById("overlay-registrar");
    modal.classList.add("hidden");
}

function abrirFormularioEditar() {
    const modal = document.getElementById("overlay-editar");
    modal.classList.remove("hidden");
}

function cerrarFormulario() {
    const modal = document.getElementById("overlay-editar");
    modal.classList.add("hidden");
}

// ----------------------------------
// CARGAR SELECT DE ALCALDÍAS (EDICIÓN)
// ----------------------------------
async function cargarAlcaldiasSelect(selectId, selectedId = null) {
    const select = document.getElementById(selectId);

    try {
        const res = await fetch("/admin/Gestion_Albergues/alcaldias");
        const alcaldias = await res.json();

        select.innerHTML = '<option value="">-- Seleccionar alcaldía --</option>';

        alcaldias.forEach(a => {
            const opt = document.createElement("option");
            opt.value = a.id;
            opt.textContent = a.nombre;

            if (selectedId && selectedId == a.id) {
                opt.selected = true;
            }
            select.appendChild(opt);
        });

        // Forzar scroll al seleccionado
        setTimeout(() => {
            const index = [...select.options].findIndex(o => o.selected);
            if (index >= 0) select.selectedIndex = index;
        }, 50);

    } catch (e) {
        console.error("Error cargando alcaldías:", e);
    }
}

// ----------------------------------
// BOTONES EDITAR
// ----------------------------------
document.querySelectorAll(".btn-editar").forEach(btn => {

    btn.addEventListener("click", async () => {

        abrirFormularioEditar();

        document.getElementById("edit-id").value = btn.dataset.id;
        document.getElementById("edit-nombre").value = btn.dataset.nombre;
        document.getElementById("edit-capacidad").value = btn.dataset.capacidad;
        document.getElementById("edit-ocupacion").value = btn.dataset.ocupacion;
        document.getElementById("edit-estado").value = btn.dataset.estado;

        const idAlcaldia = btn.dataset.alcaldia || null;
        await cargarAlcaldiasSelect("edit-id_alcaldia", idAlcaldia);

    });
});

// ----------------------------------
// SUBMIT REGISTRO
// ----------------------------------
document.getElementById("formRegistrarAlbergue").addEventListener("submit", async function (e) {
    e.preventDefault();

    const capacidadTotal = parseInt(document.getElementById("reg-capacidad").value);
    const capacidadOcupada = parseInt(document.getElementById("reg-ocupacion").value);

    if (capacidadOcupada > capacidadTotal) {
        alert("La capacidad ocupada no puede ser mayor que la capacidad total.");
        return;
    }

    const data = {
        nombre: document.getElementById("reg-nombre").value,
        alcaldia_id: document.getElementById("reg-id_alcaldia").value,
        direccion: document.getElementById("reg-direccion").value,
        telefono: document.getElementById("reg-telefono").value,
        codigo_postal: document.getElementById("reg-codigo_postal").value,
        latitud: parseFloat(document.getElementById("reg-latitud").value),
        longitud: parseFloat(document.getElementById("reg-longitud").value),
        capacidad_total: document.getElementById("reg-capacidad").value,
        capacidad_ocupada: document.getElementById("reg-ocupacion").value,
        estado: document.getElementById("reg-estado").value,
    };

    const res = await fetch("/admin/Gestion_Albergues/registrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    const result = await res.json();
    if (result.success) {
        alert("Albergue registrado correctamente");
        location.reload();
    } else {
        alert("Error: " + result.message);
    }
});

// ----------------------------------
// SUBMIT EDICIÓN
// ----------------------------------
document.getElementById("formEditarAlbergue").addEventListener("submit", async function (e) {
    e.preventDefault();

    const id = document.getElementById("edit-id").value;
    const capacidadTotal = parseInt(document.getElementById("edit-capacidad").value);
    const capacidadOcupada = parseInt(document.getElementById("edit-ocupacion").value);

    if (capacidadOcupada > capacidadTotal){
        alert ("La capacidad ocupada no puede ser mayor que la capacidad total.");
        return;
    }

    const data = {
        nombre: document.getElementById("edit-nombre").value,
        alcaldia_id: document.getElementById("edit-id_alcaldia").value,
        direccion : document.getElementById("edit-direccion").value,
        telefono : document.getElementById("edit-telefono").value,
        codigo_postal : document.getElementById("edit-codigo_postal").value,
        latitud : document.getElementById("edit-latitud").value,
        longitud : document.getElementById("edit-longitud").value,
        capacidad_total: document.getElementById("edit-capacidad").value,
        capacidad_ocupada: document.getElementById("edit-ocupacion").value,
        estado: document.getElementById("edit-estado").value,
    };

    const res = await fetch(`/admin/Gestion_Albergues/editar/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    const result = await res.json();
    if (result.success) {
        alert("Cambios guardados correctamente");
        location.reload();
    } else {
        alert("Error: " + result.message);
    }
});

// ----------------------------------
// BOTONES ELIMINAR
// ----------------------------------
document.querySelectorAll(".btn-eliminar").forEach(btn => {
    btn.addEventListener("click", async () => {
        const id = btn.dataset.id;

        if (!confirm("¿Seguro que deseas cerrar este albergue?")) return;

        const res = await fetch(`/admin/Gestion_Albergues/eliminar/${id}`, {
            method: "DELETE"
        });

        const result = await res.json();
        if (result.success) {
            alert("Albergue eliminado");
            location.reload();
        } else {
            alert("Error: " + result.message);
        }
    });
});
