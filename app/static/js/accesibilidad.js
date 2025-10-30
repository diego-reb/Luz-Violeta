document.addEventListener('DOMContentLoaded', () => {
  // --- Configuración de Clases Mutuamente Excluyentes ---
  const EXCLUSIVE_CLASSES_MAP = {
    'high-contrast': 'highContrast',
    'grayscale': 'grayscale',
    'reading-guide-active': 'readingGuide'
  };
  const EXCLUSIVE_CLASSES = Object.keys(EXCLUSIVE_CLASSES_MAP);

  // --- Creación de Elementos HTML y Eventos Básicos ---
  
  // Crear botón flotante
  const toggleBtn = document.createElement('button');
  toggleBtn.id = 'accesibility-toggle';
  toggleBtn.title = 'Opciones de accesibilidad';
  toggleBtn.innerHTML = '♿';
  document.body.appendChild(toggleBtn);

  // Crear panel
  const panel = document.createElement('div');
  panel.id = 'accesibility-panel';
  panel.innerHTML = `
    <button id="toggle-dark">Modo Claro</button>
    <button id="toggle-contrast">Alto contraste</button>
    <button id="toggle-font">Tipografía accesible</button>
    <div id="font-size-controls">
      <button id="toggle-size">Tamaño de texto</button>
      <div id="font-size-options" style="display:none; flex-direction:row; gap:6px; margin-top:5px;">
        <button id="decrease-font" title="Reducir tamaño">−</button>
        <button id="increase-font" title="Aumentar tamaño">+</button>
      </div>
    </div>
    <button id="toggle-grayscale">Escala de grises</button>
    <button id="toggle-guide">Guía de lectura</button>
    <button id="toggle-read">Lectura en voz alta</button>
  `;
  document.body.appendChild(panel);

  // Mostrar/ocultar panel
  toggleBtn.addEventListener('click', () => panel.classList.toggle('active'));
  document.addEventListener('click', e => {
    // Si el clic no es en el panel ni en el botón de toggle, lo oculta
    if (!panel.contains(e.target) && e.target !== toggleBtn) panel.classList.remove('active');
  });

  // Crear guía de lectura
  let guia = document.querySelector('.reading-guide-mask');
  if (!guia) {
    guia = document.createElement('div');
    guia.className = 'reading-guide-mask';
    document.body.appendChild(guia);
  }
  
  // --- Funciones de Estado ---
  const saveState = (key, value) => localStorage.setItem(key, value);
  const loadState = key => localStorage.getItem(key) === 'true';

  // --- Lógicas de Clases ---
  
  // Función utilitaria para desactivar TODOS los modos exclusivos
  const disableExclusiveClasses = () => {
    EXCLUSIVE_CLASSES.forEach(c => {
      if (document.body.classList.contains(c)) {
        document.body.classList.remove(c);
        
        // Desactivar el estado guardado
        const oldStorageKey = EXCLUSIVE_CLASSES_MAP[c];
        saveState(oldStorageKey, false); 
        
        // Desactivar visualmente el botón
        const otherBtn = document.querySelector(`#accesibility-panel button[id*="${c.includes('guide') ? 'guide' : c.split('-')[1]}"]`);
        if(otherBtn) otherBtn.classList.remove('active-acc');

        // Lógica específica para la guía de lectura
        if (c === 'reading-guide-active') guia.style.display = 'none';
      }
    });
  };

  // Función para inicializar/alternar una clase NO exclusiva (Tipografía)
  const toggleClass = (className, storageKey, btn) => {
    const isActive = document.body.classList.contains(className);
    if (isActive) {
      document.body.classList.remove(className);
      saveState(storageKey, false);
      if (btn) btn.classList.remove('active-acc'); 
    } else {
      document.body.classList.add(className);
      saveState(storageKey, true);
      if (btn) btn.classList.add('active-acc');
    }
  };

  // Función CLAVE para establecer clases EXCLUSIVAS
  const setExclusiveClass = (newClassName, storageKey, btn) => {
    const isActive = document.body.classList.contains(newClassName);
    
    // Si una clase exclusiva se activa, eliminamos las clases dark/light del body para que el modo exclusivo domine.
    document.body.classList.remove('dark-mode', 'light-mode');
    
    // 1. Si ya está activa, la desactivamos.
    if (isActive) {
      document.body.classList.remove(newClassName);
      saveState(storageKey, false);
      btn.classList.remove('active-acc');
      if (newClassName === 'reading-guide-active') guia.style.display = 'none';
      
      // Al desactivar el modo exclusivo, restauramos el modo de color guardado
      if (loadState('lightMode')) {
        document.body.classList.add('light-mode');
      } else {
        document.body.classList.add('dark-mode');
      }
      return;
    }

    // 2. Desactivamos todas las demás opciones exclusivas antes de activar la nueva
    disableExclusiveClasses();

    // 3. Activamos la nueva clase exclusiva
    document.body.classList.add(newClassName);
    saveState(storageKey, true);
    btn.classList.add('active-acc');

    // Lógica específica para la guía de lectura
    if (newClassName === 'reading-guide-active') guia.style.display = 'block';
  };
  
  // --- Inicializar estados guardados y botones ---
  const initButtonState = (btnId, className, storageKey) => {
    const btn = document.getElementById(btnId);
    if (loadState(storageKey)) {
      document.body.classList.add(className);
      btn.classList.add('active-acc');
    }
    return btn;
  }

  // Inicialización de Opciones Exclusivas PRIMERO
  const contrastBtn = initButtonState('toggle-contrast', 'high-contrast', EXCLUSIVE_CLASSES_MAP['high-contrast']);
  const grayscaleBtn = initButtonState('toggle-grayscale', 'grayscale', EXCLUSIVE_CLASSES_MAP['grayscale']);
  const guideBtn = initButtonState('toggle-guide', 'reading-guide-active', EXCLUSIVE_CLASSES_MAP['reading-guide-active']);

  // Variable de control para saber si un modo exclusivo está activo
  const isExclusiveModeActive = document.body.classList.contains('high-contrast') || 
                                document.body.classList.contains('grayscale') || 
                                document.body.classList.contains('reading-guide-active');

  // Inicialización de Modo Claro/Oscuro (Solo si NO hay un modo exclusivo activo)
  const darkBtn = document.getElementById('toggle-dark');
  let isLightMode = loadState('lightMode'); 

  if (!isExclusiveModeActive) {
      if (isLightMode) {
          document.body.classList.add('light-mode');
          darkBtn.innerText = 'Modo Oscuro';
      } else {
          document.body.classList.add('dark-mode');
          darkBtn.innerText = 'Modo Claro';
      }
  } else {
      // Si SÍ hay un modo exclusivo activo, aseguramos que las clases de color NO estén.
      document.body.classList.remove('dark-mode', 'light-mode');
      // Aseguramos que el botón de Modo Claro/Oscuro refleje el último estado *guardado*
      darkBtn.innerText = isLightMode ? 'Modo Oscuro' : 'Modo Claro';
      
      if (document.body.classList.contains('reading-guide-active')) guia.style.display = 'block';
  }

  // Inicialización de Tipografía accesible
  const fontBtn = initButtonState('toggle-font', 'alt-font', 'altFont');
  
  // Guardar tamaño base (sin cambios)
  let currentFontSize = parseFloat(localStorage.getItem('fontSize')) || 1;
  document.body.style.fontSize = `${currentFontSize}em`;


  // --- Event Listeners para Toggles ---

  // Toggle modo oscuro/diurno
  darkBtn.addEventListener('click', () => {
    // Primero, desactivamos cualquier modo exclusivo que esté activo
    disableExclusiveClasses(); 

    if (document.body.classList.contains('dark-mode')) {
      // Pasando de Modo Oscuro a Modo Claro
      document.body.classList.remove('dark-mode');
      document.body.classList.add('light-mode');
      darkBtn.innerText = 'Modo Oscuro';
      saveState('lightMode', true);
      
    } else {
      // Pasando de Modo Claro a Modo Oscuro
      document.body.classList.remove('light-mode');
      document.body.classList.add('dark-mode');
      darkBtn.innerText = 'Modo Claro';
      saveState('lightMode', false);
    }
  });

  // Toggle Tipografía accesible
  fontBtn.addEventListener('click', () => toggleClass('alt-font', 'altFont', fontBtn));

  // Toggles de Clases Exclusivas
  contrastBtn.addEventListener('click', () => setExclusiveClass('high-contrast', EXCLUSIVE_CLASSES_MAP['high-contrast'], contrastBtn));
  grayscaleBtn.addEventListener('click', () => setExclusiveClass('grayscale', EXCLUSIVE_CLASSES_MAP['grayscale'], grayscaleBtn));
  guideBtn.addEventListener('click', () => setExclusiveClass('reading-guide-active', EXCLUSIVE_CLASSES_MAP['reading-guide-active'], guideBtn));


  // Controles de tamaño, Movimiento de la guía de lectura, Lectura en voz alta (sin cambios)
  const sizeBtn = document.getElementById('toggle-size');
  const sizeOptions = document.getElementById('font-size-options');

  sizeBtn.addEventListener('click', () => {
    sizeOptions.style.display = sizeOptions.style.display === 'none' ? 'flex' : 'none';
  });

  const increaseBtn = document.getElementById('increase-font');
  const decreaseBtn = document.getElementById('decrease-font');

  increaseBtn.addEventListener('click', () => {
    currentFontSize = Math.min(currentFontSize + 0.1, 2);
    document.body.style.fontSize = `${currentFontSize}em`;
    localStorage.setItem('fontSize', currentFontSize);
  });

  decreaseBtn.addEventListener('click', () => {
    currentFontSize = Math.max(currentFontSize - 0.1, 0.8);
    document.body.style.fontSize = `${currentFontSize}em`;
    localStorage.setItem('fontSize', currentFontSize);
  });

  document.addEventListener('mousemove', e => {
    if (document.body.classList.contains('reading-guide-active')) {
      guia.style.top = `${e.clientY - 20}px`;
    }
  });

  const readBtn = document.getElementById('toggle-read');
  let lecturaActiva = false;
  readBtn.addEventListener('click', () => {
    if (!('speechSynthesis' in window)) return alert("Tu navegador no soporta lectura de texto.");
    if (!lecturaActiva) {
      const utterance = new SpeechSynthesisUtterance(document.body.innerText);
      utterance.lang = 'es-ES';
      utterance.rate = 1;
      speechSynthesis.speak(utterance);
      lecturaActiva = true;
      readBtn.innerText = 'Detener lectura';
      utterance.onend = () => { lecturaActiva = false; readBtn.innerText = 'Lectura en voz alta'; };
    } else {
      speechSynthesis.cancel();
      lecturaActiva = false;
      readBtn.innerText = 'Lectura en voz alta';
    }
  });
});