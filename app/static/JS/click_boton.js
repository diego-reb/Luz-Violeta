
document.getElementById('phone-button').addEventListener('click', function() {
    fetch('/registrar_click_telefono', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
        if(data.status === 'ok'){
            console.log('Click registrado');
        } else {
            console.error('Error registrando click:', data.message);
        }
    });
});
