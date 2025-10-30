document.addEventListener('DOMContentLoaded', () => {
  // --- Configuración de Clases Mutuamente Excluyentes ---
  const EXCLUSIVE_CLASSES_MAP = {
    'high-contrast': 'highContrast',
    'grayscale': 'grayscale',
    'reading-guide-active': 'readingGuide'
  };
  const EXCLUSIVE_CLASSES = Object.keys(EXCLUSIVE_CLASSES_MAP);

  // --- Crear botón flotante ---
  const toggleBtn = document.createElement('button');
  toggleBtn.id = 'accesibility-toggle';
  toggleBtn.title = 'Opciones de accesibilidad';
  toggleBtn.innerHTML = '♿';
  document.body.appendChild(toggleBtn);

  // --- Crear panel ---
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

  toggleBtn.addEventListener('click', () => panel.classList.toggle('active'));
  document.addEventListener('click', e => {
    if (!panel.contains(e.target) && e.target !== toggleBtn) panel.classList.remove('active');
  });

  // --- Crear guía de lectura ---
  let guia = document.querySelector('.reading-guide-mask');
  if (!guia) {
    guia = document.createElement('div');
    guia.className = 'reading-guide-mask';
    document.body.appendChild(guia);
  }

  // --- Funciones de Estado ---
  const saveState = (key, value) => localStorage.setItem(key, value);
  const loadState = key => localStorage.getItem(key) === 'true';

  // --- Funciones exclusivas ---
  const disableExclusiveClasses = () => {
    EXCLUSIVE_CLASSES.forEach(c => {
      if (document.body.classList.contains(c)) {
        document.body.classList.remove(c);
        localStorage.setItem(EXCLUSIVE_CLASSES_MAP[c], 'false');

        const otherBtn = document.querySelector(`#accesibility-panel button[id*="${c.includes('guide') ? 'guide' : c.split('-')[1]}"]`);
        if(otherBtn) otherBtn.classList.remove('active-acc');

        if (c === 'reading-guide-active') guia.style.display = 'none';
      }
    });
  };

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

  const setExclusiveClass = (newClassName, storageKey, btn) => {
    const isActive = document.body.classList.contains(newClassName);
    document.body.classList.remove('dark-mode', 'light-mode');

    if (isActive) {
      document.body.classList.remove(newClassName);
      saveState(storageKey, false);
      btn.classList.remove('active-acc');
      if (newClassName === 'reading-guide-active') guia.style.display = 'none';

      if (loadState('lightMode')) document.body.classList.add('light-mode');
      else document.body.classList.add('dark-mode');
      return;
    }

    disableExclusiveClasses();
    document.body.classList.add(newClassName);
    saveState(storageKey, true);
    btn.classList.add('active-acc');

    if (newClassName === 'reading-guide-active') guia.style.display = 'block';
  };

  // --- Inicialización limpia al cargar ---
  EXCLUSIVE_CLASSES.forEach(c => document.body.classList.remove(c));

  const initExclusiveState = (btnId, className, storageKey) => {
    const btn = document.getElementById(btnId);
    if (loadState(storageKey)) {
      document.body.classList.add(className);
      btn.classList.add('active-acc');
      if (className === 'reading-guide-active') guia.style.display = 'block';
    }
    return btn;
  };

  const contrastBtn = initExclusiveState('toggle-contrast', 'high-contrast', EXCLUSIVE_CLASSES_MAP['high-contrast']);
  const grayscaleBtn = initExclusiveState('toggle-grayscale', 'grayscale', EXCLUSIVE_CLASSES_MAP['grayscale']);
  const guideBtn = initExclusiveState('toggle-guide', 'reading-guide-active', EXCLUSIVE_CLASSES_MAP['reading-guide-active']);

  const isExclusiveModeActive = EXCLUSIVE_CLASSES.some(c => document.body.classList.contains(c));

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
    document.body.classList.remove('dark-mode', 'light-mode');
    darkBtn.innerText = isLightMode ? 'Modo Oscuro' : 'Modo Claro';
  }

  const fontBtn = initExclusiveState('toggle-font', 'alt-font', 'altFont');

  let currentFontSize = parseFloat(localStorage.getItem('fontSize')) || 1;
  document.body.style.fontSize = `${currentFontSize}em`;

  // --- Event Listeners ---
  darkBtn.addEventListener('click', () => {
    disableExclusiveClasses(); 
    if (document.body.classList.contains('dark-mode')) {
      document.body.classList.remove('dark-mode');
      document.body.classList.add('light-mode');
      darkBtn.innerText = 'Modo Oscuro';
      saveState('lightMode', true);
    } else {
      document.body.classList.remove('light-mode');
      document.body.classList.add('dark-mode');
      darkBtn.innerText = 'Modo Claro';
      saveState('lightMode', false);
    }
  });

  fontBtn.addEventListener('click', () => toggleClass('alt-font', 'altFont', fontBtn));

  contrastBtn.addEventListener('click', () => setExclusiveClass('high-contrast', EXCLUSIVE_CLASSES_MAP['high-contrast'], contrastBtn));
  grayscaleBtn.addEventListener('click', () => setExclusiveClass('grayscale', EXCLUSIVE_CLASSES_MAP['grayscale'], grayscaleBtn));
  guideBtn.addEventListener('click', () => setExclusiveClass('reading-guide-active', EXCLUSIVE_CLASSES_MAP['reading-guide-active'], guideBtn));

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
