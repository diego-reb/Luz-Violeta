function abrirRegistro() {
    document.getElementById("form-registrar").classList.remove("hidden");
    document.getElementById("form-editar").classList.add("hidden");
}

function cerrarRegistro() {
    document.getElementById("form-registrar").classList.add("hidden");
}

document.getElementById("formRegistrarAlbergue").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        nombre: document.getElementById("reg-nombre").value,
        ciudad: document.getElementById("reg-ciudad").value,
        capacidad: document.getElementById("reg-capacidad").value,
        ocupacion: document.getElementById("reg-ocupacion").value,
        estado: document.getElementById("reg-estado").value,
    };

    const res = await fetch("/admin/Gestion_Albergues/registrar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    if (res.ok) {
        alert("Albergue registrado con éxito");
        location.reload();
    } else {
        alert("Error al registrar");
    }
});
