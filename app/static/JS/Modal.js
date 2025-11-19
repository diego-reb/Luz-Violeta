function abrirModalNuevo() {
    document.getElementById("tituloModal").innerText = "Registrar Usuario";
    document.getElementById("formUsuario").reset();
    document.getElementById("id_usuario").value = "";
    document.getElementById("modalUsuario").classList.remove("hidden");
}

function abrirModalEditar(id) {
    fetch(`/admin/Gestion_Usuarios/usuario/${id}`)
        .then(resp => resp.json())
        .then(u => {
            document.getElementById("tituloModal").innerText = "Editar Usuario";

            document.getElementById("id_usuario").value = u.id_usuario;
            document.getElementById("nombre").value = u.nombre;
            document.getElementById("correo").value = u.correo;
            document.getElementById("username").value = u.username;
            document.getElementById("rol_id").value = u.rol_id;
            document.getElementById("activo").value = u.activo ? 1 : 0;

            document.getElementById("modalUsuario").classList.remove("hidden");
        });
}
function cambiarEstado(id, nuevoEstado) {
    if (!confirm("¿Seguro que quieres cambiar el estado de este usuario?")) return;

    fetch(`/admin/Gestion_Usuarios/cambiar_estado/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ activo: nuevoEstado })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "ok") {
            location.reload();
        }
    });
}


function cerrarModal() {
    document.getElementById("modalUsuario").classList.add("hidden");
}

function mostrarLoader() {
    document.getElementById("loader").classList.remove("hidden");
}

function ocultarLoader() {
    document.getElementById("loader").classList.add("hidden");
}

function guardarUsuario() {
    mostrarLoader();

    const id = document.getElementById("id_usuario").value;
    const data = {
        nombre: document.getElementById("nombre").value,
        correo: document.getElementById("correo").value,
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
        rol_id: document.getElementById("rol_id").value,
        activo: document.getElementById("activo").value
    };

    let url = id
        ? `/admin/Gestion_Usuarios/editar/${id}`
        : "/admin/Gestion_Usuarios/registrar";

    let method = id ? "PUT" : "POST";

    fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(resp => resp.json())
    .then(() => {
        setTimeout(() => {
            ocultarLoader();
            location.reload();
        }, 1500);
    });
}
