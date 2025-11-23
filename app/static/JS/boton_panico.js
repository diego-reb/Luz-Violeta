
document.getElementById('phone-button').addEventListener('click', function(e) {
    e.preventDefault(); 

    fetch('/boton_panico', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({}) 
    })
    .then(response => response.json())
    .then(data => {
        if(data.success){
            console.log("Botón de pánico registrado");
        } else {
            console.error("Error al registrar el botón:", data.mensaje);
        }
    })
    .catch(err => console.error("Error en fetch:", err));

    window.location.href = 'tel:911';
});
