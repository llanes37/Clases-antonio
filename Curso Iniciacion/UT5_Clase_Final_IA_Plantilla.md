
# 🧠 UT5 — Clase Final con IA · **Plantilla de Portfolio Comentada (HTML + CSS + Bootstrap + JS)**
**Autor:** Joaquín Rodríguez  
**Nivel:** Iniciación → Proyecto final  
**Modo de uso:** Explica + construye + ejercita con ayuda de IA (ideal con Live Server).

> Esta **plantilla docente** es el “manual de referencia” para tu proyecto final.  
> Incluye un **portfolio completo** (HTML + CSS + Bootstrap + JS) con **comentarios línea a línea**, tareas **TODO Alumno** y pistas.  
> Úsala como **base** y como **documento explicativo**: cada parte está comentada para que el alumno entienda el _qué_ y el _por qué_.

---

## 🧭 Índice
- [Cómo usar esta plantilla con IA](#-cómo-usar-esta-plantilla-con-ia)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [1) index.html — Portfolio completo y comentado](#1-indexhtml--portfolio-completo-y-comentado)
- [2) styles.css — Estilos y variables (light/dark)](#2-stylescss--estilos-y-variables-lightdark)
- [3) app.js — Interactividad: scroll, filtro, modal, validación, dark mode](#3-appjs--interactividad-scroll-filtro-modal-validación-dark-mode)
- [Checklist de mejora guiada](#-checklist-de-mejora-guiada)
- [Resumen final](#-resumen-final)

---

## 🤖 Cómo usar esta plantilla con IA
**Objetivo didáctico:** Aprender a _dialogar con la IA_ para generar, revisar y mejorar tu código.

**Prompts útiles:**
- “**Explica** línea a línea el siguiente bloque de HTML/CSS/JS y sugiere mejoras de accesibilidad.”  
- “**Reescribe** mi sección de **Proyectos** usando **cards** de Bootstrap y añade **filtro por palabra clave**.”  
- “**Añade** un **modo oscuro** con **localStorage** y explícame el código.”  
- “**Valida** mi formulario en **JavaScript** con mensajes claros para el usuario.”

**TODO Alumno**
- Copia partes del código en la IA y pídele **explicaciones/ajustes** concretos.
- Documenta en este `.md` qué has cambiado y **por qué** (tus conclusiones).

---

## 📁 Estructura del proyecto
```
/tu-portfolio/
├─ index.html      # Documento principal (Bootstrap + secciones completas)
├─ styles.css      # Estilos propios (variables + light/dark + detalles)
└─ app.js          # Interacciones JS (scroll, filtro, modal, validación, tema)
```

> 💡 Puedes trabajar con CSS y JS **externos** (recomendado) o copiar los bloques dentro de `<style>` y `<script>` del HTML si prefieres 1 solo archivo para la demo.

---

## 1) `index.html` — **Portfolio completo y comentado**

```html
<!-- ===============================================================
  🌐 PORTFOLIO FINAL · HTML + BOOTSTRAP + JS
  ---------------------------------------------------------------
  Convención de comentarios (estilo Better Comments):
    ! Importante/idea clave   ? Nota/aclaración   * Ejemplo/patrón
    TODO Alumno: tarea concreta
  Objetivo: portfolio listo para personalizar y entender cada parte.
=============================================================== -->
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- ! Metadatos básicos -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Mi Portfolio — Alumno</title>

  <!-- ! Bootstrap 5 (CSS) desde CDN -->
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    rel="stylesheet">

  <!-- ? Iconos de Bootstrap (opcional, para WhatsApp, etc.) -->
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css"
    rel="stylesheet">

  <!-- ! Hoja de estilos propia -->
  <link rel="stylesheet" href="styles.css">
</head>

<!-- ? data-theme se usa para alternar light/dark desde JS y CSS -->
<body data-theme="light">
  <!-- ===========================================================
    HEADER + NAVBAR (fija y responsive)
  ============================================================ -->
  <header class="sticky-top shadow-sm">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <!-- * Marca (logo/texto) -->
        <a class="navbar-brand fw-bold" href="#home">Mi Portfolio</a>

        <!-- * Botón hamburguesa (móvil) -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- * Menú colapsable -->
        <div id="nav" class="collapse navbar-collapse">
          <ul class="navbar-nav ms-auto gap-2">
            <li class="nav-item"><a class="nav-link" href="#home">Inicio</a></li>
            <li class="nav-item"><a class="nav-link" href="#about">Sobre mí</a></li>
            <li class="nav-item"><a class="nav-link" href="#projects">Proyectos</a></li>
            <li class="nav-item"><a class="nav-link" href="#gallery">Galería</a></li>
            <li class="nav-item"><a class="nav-link" href="#contact">Contacto</a></li>
          </ul>

          <!-- * Botón tema claro/oscuro -->
          <button id="toggleTheme" class="btn btn-outline-light ms-3">
            <i class="bi bi-moon-stars"></i> Tema
          </button>
        </div>
      </div>
    </nav>
  </header>

  <!-- ===========================================================
    HERO / HOME (presentación)
  ============================================================ -->
  <section id="home" class="py-5 bg-gradient-primary text-white text-center">
    <div class="container">
      <h1 class="display-5 fw-bold">Hola, soy <span class="text-accent">Tu Nombre</span></h1>
      <p class="lead mb-4">Desarrollador/a web — HTML · CSS · Bootstrap · JavaScript</p>
      <div class="d-flex justify-content-center gap-2 flex-wrap">
        <a href="#projects" class="btn btn-light btn-lg">Ver proyectos</a>
        <a href="#contact" class="btn btn-outline-light btn-lg">Contactar</a>
        <!-- * Enlace directo a WhatsApp -->
        <a href="https://wa.me/34XXXXXXXXX" target="_blank" class="btn btn-success btn-lg">
          <i class="bi bi-whatsapp"></i> WhatsApp
        </a>
      </div>
    </div>
  </section>

  <!-- ===========================================================
    SOBRE MÍ
  ============================================================ -->
  <section id="about" class="py-5">
    <div class="container">
      <div class="row align-items-center g-4">
        <div class="col-12 col-md-5">
          <!-- * Foto/placeholder -->
          <img class="img-fluid rounded-4 shadow" src="https://via.placeholder.com/720x480" alt="Foto del autor">
        </div>
        <div class="col-12 col-md-7">
          <h2 class="mb-3">Sobre mí</h2>
          <p class="text-muted">
            Me apasiona crear interfaces limpias y funcionales. Domino las bases
            de HTML, CSS, Bootstrap y JavaScript, y sigo aprendiendo cada día.
          </p>
          <!-- * “Badges” de habilidades -->
          <div class="d-flex flex-wrap gap-2">
            <span class="badge text-bg-primary">HTML</span>
            <span class="badge text-bg-success">CSS</span>
            <span class="badge text-bg-dark">Bootstrap</span>
            <span class="badge text-bg-warning text-dark">JavaScript</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===========================================================
    PROYECTOS (cards + filtro por palabra clave)
  ============================================================ -->
  <section id="projects" class="py-5 bg-body-tertiary">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-3 mb-4">
        <h2 class="m-0">Proyectos</h2>

        <!-- * Buscador/filtro: filtra por data-tags -->
        <div class="input-group input-group-lg w-auto">
          <span class="input-group-text"><i class="bi bi-search"></i></span>
          <input id="filterInput" type="text" class="form-control" placeholder="Filtra por palabra (ej. 'api', 'ui', 'js')">
        </div>
      </div>

      <!-- * Grid responsivo de tarjetas -->
      <div id="projectsGrid" class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        <!-- ? data-tags: palabras clave para filtrar desde JS -->
        <div class="col project" data-tags="html css ui">
          <div class="card h-100 shadow-sm">
            <img class="card-img-top" src="https://picsum.photos/seed/p1/600/400" alt="Proyecto 1">
            <div class="card-body">
              <h5 class="card-title">Proyecto 1</h5>
              <p class="card-text text-muted">Maquetación con HTML/CSS y componentes Bootstrap.</p>
            </div>
          </div>
        </div>

        <div class="col project" data-tags="js api fetch">
          <div class="card h-100 shadow-sm">
            <img class="card-img-top" src="https://picsum.photos/seed/p2/600/400" alt="Proyecto 2">
            <div class="card-body">
              <h5 class="card-title">Proyecto 2</h5>
              <p class="card-text text-muted">Interacción con JavaScript y consumo de API.</p>
            </div>
          </div>
        </div>

        <div class="col project" data-tags="bootstrap responsive ui">
          <div class="card h-100 shadow-sm">
            <img class="card-img-top" src="https://picsum.photos/seed/p3/600/400" alt="Proyecto 3">
            <div class="card-body">
              <h5 class="card-title">Proyecto 3</h5>
              <p class="card-text text-muted">Diseño responsive usando grid de Bootstrap.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===========================================================
    GALERÍA (grid + modal)
  ============================================================ -->
  <section id="gallery" class="py-5">
    <div class="container">
      <h2 class="mb-4">Galería</h2>
      <!-- * Mini-grid de imágenes clicables -->
      <div class="row g-3">
        <div class="col-6 col-md-4">
          <img class="img-fluid rounded gallery-item" src="https://picsum.photos/seed/g1/800/600" alt="Imagen 1">
        </div>
        <div class="col-6 col-md-4">
          <img class="img-fluid rounded gallery-item" src="https://picsum.photos/seed/g2/800/600" alt="Imagen 2">
        </div>
        <div class="col-6 col-md-4">
          <img class="img-fluid rounded gallery-item" src="https://picsum.photos/seed/g3/800/600" alt="Imagen 3">
        </div>
      </div>
    </div>
  </section>

  <!-- * Modal reutilizable para mostrar imágenes en grande -->
  <div class="modal fade" id="imgModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <img id="imgModalSrc" alt="Vista ampliada">
      </div>
    </div>
  </div>

  <!-- ===========================================================
    CONTACTO (form + validación JS + mailto + WhatsApp)
  ============================================================ -->
  <section id="contact" class="py-5 bg-body-tertiary">
    <div class="container">
      <h2 class="mb-3">Contacto</h2>
      <p class="text-muted">Completa el formulario o usa los accesos directos.</p>

      <form id="contactForm" class="col-12 col-md-8 col-lg-6 needs-validation" novalidate>
        <div class="mb-3">
          <label for="c-name" class="form-label">Nombre</label>
          <input id="c-name" name="name" type="text" class="form-control" required>
          <div class="invalid-feedback">Introduce tu nombre.</div>
        </div>
        <div class="mb-3">
          <label for="c-email" class="form-label">Email</label>
          <input id="c-email" name="email" type="email" class="form-control" required>
          <div class="invalid-feedback">Introduce un email válido.</div>
        </div>
        <div class="mb-3">
          <label for="c-msg" class="form-label">Mensaje</label>
          <textarea id="c-msg" name="msg" class="form-control" rows="4" minlength="10" required></textarea>
          <div class="invalid-feedback">Escribe al menos 10 caracteres.</div>
        </div>

        <div class="d-flex gap-2">
          <button class="btn btn-primary" type="submit"><i class="bi bi-send"></i> Enviar</button>
          <!-- * Acceso directo por email -->
          <a class="btn btn-outline-secondary" href="mailto:tuemail@correo.com">
            <i class="bi bi-envelope"></i> Email
          </a>
          <!-- * Acceso directo por WhatsApp -->
          <a class="btn btn-success" target="_blank" href="https://wa.me/34XXXXXXXXX">
            <i class="bi bi-whatsapp"></i> WhatsApp
          </a>
        </div>
      </form>
    </div>
  </section>

  <!-- ===========================================================
    FOOTER
  ============================================================ -->
  <footer class="bg-dark text-white text-center p-4">
    <div class="container">
      <p class="m-0">&copy; <span id="year"></span> · Tu Nombre — Todos los derechos reservados.</p>
    </div>
  </footer>

  <!-- ! Bootstrap 5 (JS) bundle -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

  <!-- ! Tu script -->
  <script src="app.js"></script>
</body>
</html>
```

**Notas clave sobre `index.html`:**
- **Navbar fija** y **colapsable** en móvil con `navbar-expand-lg + navbar-toggler`.  
- **Botón de tema**: `#toggleTheme` alterna `data-theme="light|dark"` en `<body>`.  
- **Filtro de proyectos**: los elementos `.project` llevan `data-tags="..."` y se filtran por texto.  
- **Galería**: las imágenes `.gallery-item` abren un **modal** común `#imgModal` actualizando su `src`.  
- **Formulario**: usa validación nativa + mejora en JS; atajos por `mailto:` y `wa.me`.  
- **Footer**: el año se inyecta desde JS.

**TODO Alumno**
1. Cambia textos, imágenes y enlaces por tu contenido real.  
2. Ajusta las **palabras clave** (`data-tags`) para que el filtro tenga sentido.  
3. Revisa accesibilidad: `alt` descriptivos, orden de etiquetas, contraste de colores.

---

## 2) `styles.css` — Estilos y variables (light/dark)
```css
/* ===============================================================
   🎨 ESTILOS PROPIOS · variables + detalles + dark mode
   ---------------------------------------------------------------
   ! Solo lo esencial; apóyate en Bootstrap para el resto.
=============================================================== */

/* ? Variables de color (cambiamos según data-theme en <body>) */
:root{
  --bg: #f6f7fb;
  --ink: #111827;
  --accent: #2563eb;
  --accent-contrast: #ffffff;
  --muted: #6b7280;
  --surface: #ffffff;
  --surface-2: #f3f4f6;
}

/* ! Modo oscuro: redefine las variables cuando data-theme="dark" */
body[data-theme="dark"]{
  --bg: #0b1220;
  --ink: #e5e7eb;
  --accent: #60a5fa;
  --accent-contrast: #0b1220;
  --muted: #9ca3af;
  --surface: #0f172a;
  --surface-2: #111827;
}

/* Base */
html, body{ height: 100%; }
body{
  background: var(--bg);
  color: var(--ink);
}

/* Hero */
.bg-gradient-primary{
  /* * Degradado simple: base -> acento */
  background: linear-gradient(135deg, #0ea5e9, var(--accent));
}
.text-accent{ color: var(--accent-contrast); background: rgba(255,255,255,.15); padding:.1em .4em; border-radius:.4rem; }

/* Galería (modal) */
#imgModal .modal-content{
  background: transparent;
  border: none;
  box-shadow: none;
}
#imgModal img{
  display:block;
  width: 100%;
  height: auto;
  border-radius: .8rem;
}

/* Utilidades pequeñas */
.text-muted{ color: var(--muted) !important; }
.bg-body-tertiary{ background: var(--surface-2) !important; }
```

**Notas clave sobre `styles.css`:**
- Las **variables CSS** permiten cambiar paleta con **una sola clase** (`data-theme` en `<body>`).  
- El hero usa un **degradado** y un resaltado suave en el nombre.  
- El **modal** de la galería se deja transparente para centrar la imagen.

**TODO Alumno**
- Ajusta la paleta del **modo claro** y **oscuro** a tu estilo.  
- Añade transiciones (p. ej., `transition: color .2s, background .2s`).

---

## 3) `app.js` — Interactividad: scroll, filtro, modal, validación, dark mode
```js
/* ===============================================================
   ⚙️ INTERACCIONES DEL PORTFOLIO
   ---------------------------------------------------------------
   Incluye:
   - Año dinámico en footer
   - Scroll suave entre secciones
   - Filtro por palabra en Proyectos
   - Modal de galería (click para ampliar)
   - Validación del formulario de contacto
   - Tema claro/oscuro con localStorage
=============================================================== */

// 1) Año dinámico en el footer
document.getElementById('year').textContent = new Date().getFullYear();

// 2) Scroll suave (captura enlaces internos del navbar)
document.querySelectorAll('a.nav-link[href^="#"]').forEach(a => {
  a.addEventListener('click', (e) => {
    e.preventDefault();
    const id = a.getAttribute('href');
    const el = document.querySelector(id);
    if(!el) return;
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    // si el menú está abierto en móvil, ciérralo
    const nav = document.getElementById('nav');
    if(nav.classList.contains('show')){
      new bootstrap.Collapse(nav).hide();
    }
  });
});

// 3) Filtro de proyectos por palabra clave (busca en data-tags y título)
const filterInput = document.getElementById('filterInput');
if(filterInput){
  filterInput.addEventListener('input', () => {
    const q = filterInput.value.trim().toLowerCase();
    document.querySelectorAll('#projectsGrid .project').forEach(card => {
      const tags = (card.dataset.tags || '').toLowerCase();
      const title = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const text = (card.querySelector('.card-text')?.textContent || '').toLowerCase();
      const hayCoincidencia = tags.includes(q) || title.includes(q) || text.includes(q);
      card.parentElement.classList.toggle('d-none', q && !hayCoincidencia);
    });
  });
}

// 4) Galería: abrir imagen en modal al hacer clic
const imgModal = document.getElementById('imgModal');
const imgModalSrc = document.getElementById('imgModalSrc');
document.querySelectorAll('.gallery-item').forEach(img => {
  img.addEventListener('click', () => {
    imgModalSrc.src = img.src;                 // * Reutiliza el mismo modal para todas las imágenes
    const modal = new bootstrap.Modal(imgModal);
    modal.show();
  });
});

// 5) Validación del formulario (Bootstrap + JS)
//    - Usa 'novalidate' en el form y controlamos manualmente
const form = document.getElementById('contactForm');
if(form){
  form.addEventListener('submit', (e) => {
    // ? API nativa de validación HTML
    if(!form.checkValidity()){
      e.preventDefault();
      e.stopPropagation();
    }else{
      e.preventDefault(); // demo: no enviamos a servidor
      alert('Formulario enviado correctamente ✅');
      form.reset();
    }
    form.classList.add('was-validated');  // * Estilos de Bootstrap para feedback
  });
}

// 6) Tema claro/oscuro con persistencia
const THEME_KEY = 'portfolio-theme';
const body = document.body;
const toggleTheme = document.getElementById('toggleTheme');

// * Cargar preferencia previa
const saved = localStorage.getItem(THEME_KEY);
if(saved === 'dark'){ body.setAttribute('data-theme', 'dark'); }

// * Alternar con botón
if(toggleTheme){
  toggleTheme.addEventListener('click', () => {
    const now = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', now);
    localStorage.setItem(THEME_KEY, now);
  });
}
```

**Notas clave sobre `app.js`:**
- El **scroll suave** mejora la UX en navegación.  
- El **filtro** busca en `data-tags`, título y texto de cada tarjeta.  
- La **galería** usa **un único modal** para todas las imágenes.  
- La **validación** combina reglas nativas (required, type, minlength) con **Bootstrap** (`was-validated`).  
- El **modo oscuro** persiste con `localStorage` (clave `portfolio-theme`).

**TODO Alumno**
- Añade un **“volver arriba”** (scrollTop) que aparezca tras hacer scroll.  
- Mejora el filtro para **múltiples palabras** (separadas por espacios).

---

## ✅ Checklist de mejora guiada
- [ ] Sustituí **imágenes** y **textos** por mi contenido.  
- [ ] Ajusté **paleta** (variables CSS) para mi identidad visual.  
- [ ] Cambié **data-tags** en proyectos y probé el **filtro**.  
- [ ] Añadí al menos **3 proyectos** y **6 imágenes** nuevas.  
- [ ] Personalicé el **formulario** y verifiqué su **validación**.  
- [ ] Probé el **modo oscuro** y confirmé que persiste al recargar.  
- [ ] Pasé **Lighthouse** (o similar) y apliqué **mejoras** básicas.

---

## 🧾 Resumen final
- Tienes un **portfolio completo** con **Bootstrap** y **JS** listo para personalizar.  
- El documento explica **qué hace cada parte** y cómo **mejorarla con IA**.  
- Avanza iterando: pide a la IA _ajustes puntuales_, entiende los cambios y valídalos en el navegador.

> Si lo deseas, puedo **integrar esta plantilla dentro de tu `UT5_Clase_Final_IA.md`** original o dejarla como **archivo compañero** de referencia.
