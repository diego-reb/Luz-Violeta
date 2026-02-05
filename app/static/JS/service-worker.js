const CACHE_NAME = 'luz-violeta-v1';
const urlsToCache = [
    '/',
    '/static/css/accesibilidad.css',
    '/static/JS/boton_panico.js',
    '/static/JS/accesibilidad.js',
    '/static/JS/menu_opciones.js',
    '/static/JS/click_boton.js',
    '/static/JS/app.js',
    '/manifest.json'
];

// Instalar Service Worker
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Service Worker instalado, cacheando recursos');
                return cache.addAll(urlsToCache);
            })
            .catch(error => {
                console.error('Error al cachear recursos:', error);
            })
    );
    // Activar inmediatamente
    self.skipWaiting();
});

// Activar y limpiar caches antiguos
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('Eliminando cache antiguo:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            // Tomar control inmediato de todas las pestañas
            return self.clients.claim();
        })
    );
});

// Interceptar peticiones
self.addEventListener('fetch', event => {
    // No cachear peticiones a la API o endpoints dinámicos
    if (event.request.url.includes('/api/') || 
        event.request.url.includes('/login') || 
        event.request.url.includes('/perfil')) {
        return fetch(event.request);
    }

    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Si está en cache, devolver
                if (response) {
                    return response;
                }

                // Clonar la petición
                const fetchRequest = event.request.clone();

                // Intentar obtener de la red
                return fetch(fetchRequest)
                    .then(response => {
                        // Verificar si es una respuesta válida
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }

                        // Clonar la respuesta
                        const responseToCache = response.clone();

                        // Agregar al cache para futuras peticiones
                        caches.open(CACHE_NAME)
                            .then(cache => {
                                cache.put(event.request, responseToCache);
                            });

                        return response;
                    })
                    .catch(error => {
                        console.log('Error de red, recurso no disponible:', event.request.url);
                        
                        // Si la página principal falla, mostrar página offline
                        if (event.request.mode === 'navigate') {
                            return caches.match('/');
                        }
                        
                        // Para imágenes, puedes devolver una imagen por defecto
                        if (event.request.destination === 'image') {
                            return new Response(
                                '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200"><rect width="200" height="200" fill="#f7f1ff"/><text x="100" y="100" font-family="Arial" font-size="14" fill="#a78bfa" text-anchor="middle">Luz Violeta</text></svg>',
                                { headers: { 'Content-Type': 'image/svg+xml' } }
                            );
                        }
                        
                        return new Response('Contenido no disponible offline', {
                            status: 503,
                            statusText: 'Service Unavailable',
                            headers: new Headers({
                                'Content-Type': 'text/plain'
                            })
                        });
                    });
            })
    );
});

// Manejar mensajes desde la app
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});

// Manejar push notifications (opcional)
self.addEventListener('push', event => {
    const options = {
        body: event.data ? event.data.text() : 'Nueva información disponible',
        icon: '/static/images/icon-192.png',
        badge: '/static/images/badge-72.png',
        vibrate: [200, 100, 200],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: '1'
        },
        actions: [
            {
                action: 'explore',
                title: 'Ver más',
                icon: '/static/images/checkmark.png'
            },
            {
                action: 'close',
                title: 'Cerrar',
                icon: '/static/images/xmark.png'
            }
        ]
    };

    event.waitUntil(
        self.registration.showNotification('Luz Violeta', options)
    );
});

// Manejar clics en notificaciones
self.addEventListener('notificationclick', event => {
    console.log('Notificación clickeada:', event.notification.tag);
    event.notification.close();

    event.waitUntil(
        clients.matchAll({ type: 'window' })
            .then(clientList => {
                for (const client of clientList) {
                    if (client.url === '/' && 'focus' in client) {
                        return client.focus();
                    }
                }
                if (clients.openWindow) {
                    return clients.openWindow('/');
                }
            })
    );
});