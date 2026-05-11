# 📘 Curso de Iniciación al Desarrollo Web
**Autor:** Joaquín Rodríguez

---

## 🎯 Objetivo del Curso
Este curso está diseñado para que cualquier persona, incluso sin conocimientos previos, pueda aprender a crear su **primera página web completa**.  
Avanzaremos de forma **progresiva**: primero la **estructura** con **HTML**, luego el **diseño** con **CSS**, después **Bootstrap** para maquetar rápido y, por último, **JavaScript** para dotar de **interactividad**.  
Al final, integrarás todo en un **Proyecto Real (Portfolio personal)** y aprenderás a apoyarte en la **Inteligencia Artificial (IA)** para explicar, mejorar y publicar tu web (Netlify).

---

## 📂 Estructura del Curso (unidades y contenidos)

> Cada UT incluye **dos tipos de archivos**:
> - **Teoría (`.md`)**: explicación detallada, ejemplos comentados y buenas prácticas.  
> - **Práctica (`.html` rellenable)**: plantilla con `TODO Alumno` y cajas de resultado para trabajar en clase.  
> Además, hay una versión **docente (.html)** hipercomentada para proyectar.

### UT1 · HTML — Estructura y Etiquetas
**Qué aprenderás**
- Estructura base de un documento **HTML5** (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`).
- **Semántica**: uso correcto de `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.
- Contenidos: **títulos y párrafos**, **enlaces** (internos `#id`/externos con `target="_blank"`), **imágenes** con `alt`, **listas** (`ul`, `ol`, `dl`), **tablas accesibles** (`caption`, `thead`, `tbody`, `tfoot`, `th scope`).
- **Formularios**: `label/for`, `input` semánticos (`email`, `tel`, `number`), `textarea`, `required`, `pattern`.
- **Multimedia**: `<img>`, `<video>`, `<audio>`, uso de `<source>` y `track` (subtítulos).

**Ejercicios guiados**
- Estructurar una página con navegación por anclas.
- Tabla con `caption` y totales en `tfoot`.
- Formulario con validación nativa (sin backend).

**Mini-Proyecto**
- **Esqueleto de Portfolio** con `header + nav`, secciones “Sobre mí”, “Proyectos”, “Galería”, “Contacto”, y `footer`.

**Archivos recomendados**
- `UT1_Clase_HTML_Completa.md` · `UT1_Plantilla_HTML_Rellenable.html` · `UT1_Clase_HTML_Completa.html`

---

### UT2 · CSS — Estilos y Diseño
**Qué aprenderás**
- **Selectores** (tipo, clase, id, descendientes), **especificidad** y cascada.
- **Colores**, **tipografía** (familias, tamaños, pesos, alto de línea), **espaciado** (**Box Model**: `margin`, `padding`, `border`).
- **Layout moderno**: **Flexbox** (alineación, distribución, wrap) y **CSS Grid** (plantillas de columnas/filas).
- **Responsive** con medias queries y utilidades simples.
- **Transiciones y efectos**: `transition`, `transform`, `:hover`, `:focus`.

**Ejercicios guiados**
- Cajas de color con esquinas redondeadas, sombras y `padding`.
- Tipografías diferenciadas por secciones.
- Layout básico con **Flex** y rejilla con **Grid**.

**Mini-Proyecto**
- **Mejora visual del Portfolio**: esquema de color, tipografía consistente, espaciados, tarjetas con sombra, galería responsive.

**Archivos recomendados**
- `UT2_Clase_CSS_Completa.md` · `UT2_Plantilla_CSS_Rellenable.html` · `UT2_Clase_CSS_Completa.html`

---

### UT3 · Bootstrap — Componentes y Maquetación
**Qué aprenderás**
- **Grid de 12 columnas**: `container`, `row`, `col-*`, breakpoints.
- **Utilidades**: espaciado (`mt-?`, `p-?`), tipografía (`lead`, `text-muted`, `text-center`), colores (`bg-*`, `text-*`).
- **Componentes**: **botones** (`btn`, variantes e `outline`), **formularios** (`form-control`, `form-select`), **tablas** (`table`, `table-striped`, `table-hover`), **alertas**, **cards**, **navbar**, **carousel**.
- **JS de Bootstrap** (bundle): navbar colapsable y carrusel.

**Ejercicios guiados**
- Encabezado con `navbar` responsive.
- Formulario accesible y coherente estéticamente (clases Bootstrap).
- Carrusel de imágenes con controles prev/next.

**Mini-Proyecto**
- **Rehacer el Portfolio con Bootstrap**: grid responsive, cards de proyectos, formulario estilizado y carrusel/galería.

**Archivos recomendados**
- `UT3_Clase_BOOSTRAP_Completa.md` · `UT3_Plantilla_Bootstrap_Rellenable.html` · `UT3_Clase_BOOSTRAP_Completa.html`

---

### UT4 · JavaScript — Interactividad
**Qué aprenderás (en profundidad)**
- **Variables y tipos** (`const`/`let`), coerción y conversión (`Number()`, `String()`), manejo de `NaN`.
- **Funciones** (declaración y flecha), **parámetros** y `return`.
- **Estructuras de control**: condicionales (`if/else if/else`) y **bucles** (`for`, `while`); patrones prácticos (contador asc/desc, pares/impares, FizzBuzz).
- **Eventos** con `addEventListener` (`click`, `input`, `mouseover`, `mouseout`), `preventDefault`.
- **DOM**: seleccionar (`getElementById`, `querySelector`), leer/escribir (`innerText`, `innerHTML`, `value`), **estilos** (`style`) y **clases** (`classList.toggle`).
- **Imágenes**: cambiar `src`, `alt`, tamaños.
- **Persistencia**: `localStorage` (`setItem`, `getItem`, `removeItem`), guardar/leer **objetos** con `JSON.stringify`/`JSON.parse`.
- **Validación** en cliente: atributos (`required`, `minlength`, `type="email"`), `checkValidity()`, feedback visual con clases de **Bootstrap**.

**Ejercicios guiados**
- `alert`/`prompt` + escritura del resultado en una caja `.resultado`.
- Contadores con bucles y representación en el DOM.
- Cambios de estilo/HTML por botón (negrita/itálica, color, tamaño).
- **Perfil con skills** guardado en `localStorage`.

**Mini-Proyecto**
- **Tarjeta de Perfil** interactiva + mejoras del Portfolio (filtro básico, modal simple, validación amigable).

**Archivos recomendados**
- `UT4_Clase_JAVASCRIPT_Completa.md` · `UT4_Plantilla_JavaScript_Rellenable.html` · `UT4_Clase_JAVASCRIPT_Completa.html`

---

### UT5 · Proyecto Final — Portfolio Completo
**Qué integrarás**
- **HTML + CSS + Bootstrap + JS** en una sola experiencia:  
  - **Tema claro/oscuro** con persistencia en `localStorage`.  
  - **Filtro de proyectos** por texto (`data-tags`, título y descripción).  
  - **Galería** con **modal** al hacer clic en la imagen.  
  - **Formulario de contacto** con validación y accesos rápidos (**mailto**, **WhatsApp**).  
  - **Navbar** responsive con scroll suave y cierre automático al navegar en móvil.

**Qué entregas**
- **Portfolio publicado** (Netlify o GitHub Pages).
- Código claro con comentarios, imágenes correctas y README corto de decisiones.

**Archivos recomendados**
- `UT5_Clase_Final_IA.md` (teoría + prompts) · `UT5_Clase_Final_IA.html` (docente funcional hipercomentado) · `UT5_Plantilla_Final_Rellenable.html` (alumno)

---

## 🤖 Clase Extra: IA como Asistente de Programación
La IA es tu **aliada** para aprender más rápido y con menos frustración. Úsala así:

**Cuándo usarla**
- Para **explicar** un fragmento confuso línea a línea, con alternativas más limpias.
- Para **refactorizar** (quitar duplicación, mejorar nombres, separar responsabilidades).
- Para **accesibilidad** (revisar `alt`, `label/for`, roles, contraste, foco visible).
- Para **generar variaciones** (por ejemplo, tres cards responsive diferentes).
- Para **diagnóstico** (por qué no colapsa la navbar, por qué no valida el formulario).

**Cómo preguntar (prompts efectivos)**
- *Explicar + A11y:*  
  _“Explica línea a línea este bloque. Señala mejoras de semántica y accesibilidad (alt, label/for, roles, contraste). Devuélveme solo el bloque corregido con comentarios.”_
- *Refactor (solo bloque):*  
  _“Refactoriza este fragmento para hacerlo más claro (DRY). Entrega solo el nuevo bloque y añade comentarios de por qué cada cambio.”_
- *Dark mode persistente:*  
  _“Dame CSS con variables para light/dark, un botón toggle y el JS mínimo para alternar y guardar en localStorage.”_
- *Filtro multi-palabra (UT5):*  
  _“Mejora mi filtro para aceptar varias palabras separadas por espacios y exigir que todas coincidan en data-tags, título o descripción. Devuélveme solo el handler JS.”_

**Buenas prácticas**
- Pega **solo el bloque** relevante y resume el problema en **1–2 frases**.
- Pide **código mínimo** y **comentado**.
- **Prueba** la solución en tu navegador (Live Server) y guarda un antes/después.

---

## 🚀 Publicar el Portfolio en Netlify (rápido y sin complicaciones)
**Objetivo:** tener tu web **online** en 2 minutos.

**Pasos**
1. **Prepara el proyecto**: debe existir un `index.html` en la **raíz** de la carpeta.  
2. Asegúrate de que **todas las rutas** son **relativas** (`./img/...`, `./css/...`, `./js/...`).  
3. Entra en **https://app.netlify.com** y accede con GitHub/Google/email.  
4. Click en **Add new site → Deploy manually**.  
5. **Arrastra la carpeta** de tu proyecto a la caja de Netlify y suéltala.  
6. Netlify genera una **URL pública** automática.  
7. (Opcional) Cambia el subdominio en **Site settings → Domain management**.  
8. **Actualizar** tu web = volver a arrastrar la **carpeta actualizada**.

**Consejos**
- Si navbar/modal no funcionan, añade el **bundle JS** de Bootstrap justo antes de `</body>`.  
- Si imágenes no cargan, revisa nombres (sensible a mayúsculas) y rutas relativas.  
- Para formularios reales sin backend, usa servicios como **Formspree** o **EmailJS**.

**Alternativa: GitHub Pages**
1. Sube la carpeta (con `index.html`) a un repositorio en GitHub.  
2. Repo → **Settings → Pages** → *Deploy from branch* → `main` / `root`.  
3. Espera a que se genere tu **URL pública**.

---

## 🛠 Requisitos mínimos del alumno
- **VS Code** instalado.  
- Extensiones: **Live Server** (ejecutar y recargar) y **Better Comments** (leer comentarios tipo `! ? * TODO`).  
- Navegador actualizado y ganas de **probar** todo en local (Live Server) antes de publicar.

---

## ✅ Resultado Final
Al terminar el curso tendrás:  
- Un **Portfolio personal completo** (secciones: Sobre mí, Proyectos, Galería, Contacto, Footer).  
- Conocimientos sólidos de **HTML, CSS, Bootstrap y JavaScript**.  
- Experiencia usando la **IA** como apoyo para explicar, mejorar y refactorizar tu código.  
- Tu web **publicada** y lista para compartir en tu CV y redes.
