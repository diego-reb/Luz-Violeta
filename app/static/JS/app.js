// Registrar Service Worker para PWA
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/service-worker.js')
            .then(function(registration) {
                console.log('ServiceWorker registrado con éxito. Scope:', registration.scope);
                
                // Forzar actualización si hay nueva versión
                registration.addEventListener('updatefound', () => {
                    const newWorker = registration.installing;
                    console.log('Nueva versión del Service Worker encontrada');
                    
                    newWorker.addEventListener('statechange', () => {
                        if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                            console.log('Nueva versión lista. Recarga para actualizar.');
                            // Puedes mostrar un botón para recargar
                            showUpdateNotification();
                        }
                    });
                });
            })
            .catch(function(error) {
                console.log('Error al registrar ServiceWorker:', error);
            });
    });
}

// Detectar si la app está en modo standalone (instalada)
function isRunningStandalone() {
    return window.matchMedia('(display-mode: standalone)').matches || 
           window.navigator.standalone ||
           document.referrer.includes('android-app://');
}

// Manejar instalación de PWA
let deferredPrompt;
const installButton = document.createElement('button');
installButton.id = 'installPWA';
installButton.innerHTML = '📱 Instalar App';
installButton.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(135deg, #a78bfa, #e879f9);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 25px;
    font-weight: bold;
    box-shadow: 0 4px 12px rgba(167, 139, 250, 0.3);
    cursor: pointer;
    z-index: 1000;
    display: none;
    transition: all 0.3s;
`;

installButton.addEventListener('click', async () => {
    if (!deferredPrompt) return;
    
    deferredPrompt.prompt();
    
    const { outcome } = await deferredPrompt.userChoice;
    console.log(`Usuario ${outcome === 'accepted' ? 'aceptó' : 'rechazó'} la instalación`);
    
    deferredPrompt = null;
    installButton.style.display = 'none';
});

// Solo agregar el botón si no está ya instalado
if (!isRunningStandalone()) {
    document.body.appendChild(installButton);
    
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        installButton.style.display = 'block';
        
        // Ocultar automáticamente después de 10 segundos
        setTimeout(() => {
            if (installButton.style.display === 'block') {
                installButton.style.display = 'none';
            }
        }, 10000);
    });
}

// Mostrar notificación de actualización
function showUpdateNotification() {
    const updateDiv = document.createElement('div');
    updateDiv.id = 'updateNotification';
    updateDiv.innerHTML = `
        <div style="
            position: fixed;
            bottom: 80px;
            right: 20px;
            background: white;
            color: #333;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1001;
            max-width: 300px;
            border-left: 5px solid #4CAF50;
        ">
            <strong>Nueva versión disponible</strong>
            <p style="margin: 8px 0;">Recarga para actualizar la aplicación.</p>
            <button id="reloadBtn" style="
                background: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 5px;
                cursor: pointer;
                margin-right: 10px;
            ">Actualizar</button>
            <button id="closeUpdateBtn" style="
                background: #f44336;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 5px;
                cursor: pointer;
            ">Más tarde</button>
        </div>
    `;
    
    document.body.appendChild(updateDiv);
    
    document.getElementById('reloadBtn').addEventListener('click', () => {
        window.location.reload();
    });
    
    document.getElementById('closeUpdateBtn').addEventListener('click', () => {
        updateDiv.remove();
    });
}

// Detectar conexión
function updateOnlineStatus() {
    const status = navigator.onLine ? 'online' : 'offline';
    console.log('Estado de conexión:', status);
    
    // Puedes mostrar un indicador visual
    if (!navigator.onLine) {
        console.log('Modo offline activado');
    }
}

window.addEventListener('online', updateOnlineStatus);
window.addEventListener('offline', updateOnlineStatus);
updateOnlineStatus();