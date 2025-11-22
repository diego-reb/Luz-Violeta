async function abrirModalEditar(id) {
    const loader = document.getElementById("loader");
    loader.classList.remove("hidden");

    try {
        const response = await fetch(`/admin/Gestion_Usuarios/usuario/${id}`);
        const data = await response.json();

        document.getElementById("tituloModal").textContent = "Editar Usuario";
        document.getElementById("id_usuario").value = data.id_usuario;
        document.getElementById("nombre").value = data.nombre;
        document.getElementById("correo").value = data.correo;
        document.getElementById("username").value = data.username;

        // La contraseña NO se llena por seguridad
        document.getElementById("password").value = "";

        document.getElementById("rol_id").value = data.rol_id;
        document.getElementById("activo").value = data.activo ? "1" : "0";

        document.getElementById("modalUsuario").classList.remove("hidden");
    } catch (e) {
        alert("Error al obtener datos del usuario");
    }

    loader.classList.add("hidden");
}


function abrirModalNuevo() {
    document.getElementById("tituloModal").textContent = "Registrar Nuevo Usuario";

    document.getElementById("id_usuario").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("correo").value = "";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("rol_id").selectedIndex = 0;
    document.getElementById("activo").value = "1";

    document.getElementById("modalUsuario").classList.remove("hidden");
}

function cerrarModal() {
    document.getElementById("modalUsuario").classList.add("hidden");
}

async function guardarUsuario() {
    const loader = document.getElementById("loader");
    loader.classList.remove("hidden");

    const id = document.getElementById("id_usuario").value;
    const nombre = document.getElementById("nombre").value;
    const correo = document.getElementById("correo").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const rol_id = document.getElementById("rol_id").value;
    const activo = document.getElementById("activo").value;

    const payload = {
        nombre,
        correo,
        username,
        password,
        rol_id,
        activo
    };

    try {
        let response;

        // EDITAR
        if (id) {
            response = await fetch(`/admin/Gestion_Usuarios/editar/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
        } 
        // REGISTRAR
        else {
            response = await fetch(`/admin/Gestion_Usuarios/registrar`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
        }

        const res = await response.json();

        if (res.status === "ok") {
            cerrarModal();
            location.reload();
        } else {
            alert("Error al guardar el usuario");
        }

    } catch (e) {
        console.error(e);
        alert("Error de conexión con el servidor");
    }

    loader.classList.add("hidden");
}

function cerrarModal() {
    document.getElementById("modalUsuario").classList.add("hidden");

    // Limpia los campos del formulario
    document.getElementById("id_usuario").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("correo").value = "";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("rol_id").selectedIndex = 0;
    document.getElementById("activo").value = "1";
}
