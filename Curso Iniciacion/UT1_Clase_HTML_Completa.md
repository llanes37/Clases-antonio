
# 📘 UT1 — Clase Completa de **HTML** (Plantilla de Clase en Markdown)
**Autor:** Joaquín Rodríguez  
**Nivel:** Iniciación  
**Modo de uso:** Explica + construye + ejercita (ideal con Live Server).

> Este `.md` reúne **todas las explicaciones y ejemplos** de la UT1 que tenías en el `.html`, pero en formato **Markdown** listo para compartir con tu alumnado o subir a tu plataforma. Mantiene el enfoque docente: teoría breve, ejemplos copiables, **TODO Alumno** y **Soluciones sugeridas**.

---

## 🧭 Índice
- [Cómo leer este documento](#-cómo-leer-este-documento)
- [Introducción a HTML](#-introducción-a-html)
- [Tablas en HTML](#-tablas-en-html)
- [Imágenes en HTML](#-imágenes-en-html)
- [Formularios en HTML](#-formularios-en-html)
- [Multimedia en HTML](#-multimedia-en-html)
- [Proyecto final · Mi Portfolio personal](#-proyecto-final--mi-portfolio-personal)
- [Pie de página (semántica y navegación secundaria)](#-pie-de-página-semántica-y-navegación-secundaria)

---

## 📝 Cómo leer este documento
Compatibilidad con la convención **Better Comments** (como en el `.html` original):

- **! Importante** → idea clave o alerta conceptual.  
- **? Nota** → aclaración útil o contexto.  
- **\* Ejemplo** → fragmento demostrativo.  
- **TODO Alumno** → tareas concretas a realizar.  
- **✅ Solución** → una posible solución explicada.

Además, se incluye en cada bloque:
- **Objetivo didáctico** (qué se aprende).
- **Buenas prácticas**.
- **Ejemplos** (bloques `html` listos para copiar).

---

## 🌱 Introducción a HTML
**Objetivo didáctico:**  
Entender el rol de **HTML** como **estructura** de una página y practicar **títulos, párrafos y listas**.

**Buenas prácticas:**
- Un único `h1` por documento y jerarquía correcta con `h2`, `h3`…  
- IDs **cortos, únicos y descriptivos** en tus secciones para poder enlazarlas con `#id`.  
- Usa texto semántico (listas para colecciones, tablas para datos tabulares, etc.).

### Estructura base (plantilla mínima)
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Página Web Completa para Alumnos · Plantilla de Clase</title>
</head>
<body>
  <header>
    <h1>Página Web Completa para Alumnos</h1>
    <p class="muted">Plantilla de clase: explica + construye + ejercita (Live Server)</p>

    <nav aria-label="Índice de secciones">
      <ul>
        <li><a href="#introduccion">Introducción</a></li>
        <li><a href="#seccion-tablas">Tablas</a></li>
        <li><a href="#seccion-imagenes">Imágenes</a></li>
        <li><a href="#seccion-formularios">Formularios</a></li>
        <li><a href="#seccion-multimedia">Multimedia</a></li>
      </ul>
    </nav>
  </header>

  <main>…</main>
  <footer id="contacto">…</footer>
</body>
</html>
```

### Listas básicas (`ul` y `ol`)
```html
<h3>Lista desordenada (ul)</h3>
<ul>
  <li>HTML: estructura</li>
  <li>CSS: presentación</li>
  <li>JavaScript: interactividad</li>
</ul>

<h3>Lista ordenada (ol)</h3>
<ol>
  <li>Planificar la página</li>
  <li>Escribir el HTML</li>
  <li>Publicar</li>
</ol>
```

**TODO Alumno**
- Crea un párrafo con un **enlace externo** que se abra en una nueva pestaña (`target="_blank"`) y use `rel="noopener"`:
  - Ejemplo de recurso: MDN HTML.
- Añade una lista de definiciones `dl` con **Frontend** y **Backend**.

**✅ Solución sugerida (comentada en el HTML original)**
```html
<p class="note">
  Recurso: <a href="https://developer.mozilla.org/es/docs/Web/HTML" target="_blank" rel="noopener">MDN HTML</a>
</p>
<dl>
  <dt>Frontend</dt><dd>Parte visible/interactiva del sitio.</dd>
  <dt>Backend</dt><dd>Lógica del servidor, datos, APIs.</dd>
</dl>
```

---

## 📊 Tablas en HTML
**Objetivo didáctico:**  
Aprender la estructura correcta con `caption`, `thead`, `tbody`, `tfoot` y el uso de `th scope="col/row"` para **accesibilidad**.

**Buenas prácticas:**
- Tablas **solo** para datos tabulares (no para maquetar).
- Añade `caption` para título y `scope` en encabezados.

**Ejemplo base (inventario simple)**
```html
<table>
  <caption>Inventario</caption>
  <thead>
    <tr>
      <th scope="col">Producto</th>
      <th scope="col">Precio</th>
      <th scope="col">Cantidad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Teclado</th>
      <td>19,99 €</td>
      <td>12</td>
    </tr>
    <tr>
      <th scope="row">Ratón</th>
      <td>9,50 €</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
```

**TODO Alumno**
1. Añade una fila para **Auriculares** (29,00 €, 8 uds) usando `th scope="row"`.  
2. Crea un `tfoot` con el total de ítems.

**✅ Solución sugerida**
```html
<tbody>
  <tr>
    <th scope="row">Auriculares</th>
    <td>29,00 €</td>
    <td>8</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <th scope="row">Total items</th>
    <td></td>
    <td>50</td>
  </tr>
</tfoot>
```

---

## 🖼️ Imágenes en HTML
**Objetivo didáctico:**  
Insertar imágenes correctamente, usar `alt` **descriptivo** (accesibilidad/SEO) y mantenerlas **responsivas**.

**Buenas prácticas:**
- Usa rutas relativas en proyectos locales (`./img/foto.jpg`).  
- Evita `width/height` fijos si no es imprescindible; emplea CSS o `max-width:100%`.

**Ejemplo con placeholder**
```html
<p class="note">Ejemplo con placeholder (recuerda usar <code>alt</code> descriptivo).</p>
<img src="https://via.placeholder.com/480x240" alt="Imagen de ejemplo rectangular">
```

**TODO Alumno**
1. Descarga una imagen y colócala en `/img/foto.jpg`.  
2. Insértala con `alt` descriptivo y limita su ancho al 50% usando `style="max-width:50%"`.  
3. Añade `figure` y `figcaption` con un pie de foto.

**✅ Solución sugerida**
```html
<figure>
  <img src="img/foto.jpg" alt="Retrato del autor trabajando en su portátil" style="max-width:50%;">
  <figcaption>Mi primera imagen local con pie de foto.</figcaption>
</figure>
```

---

## 🧾 Formularios en HTML
**Objetivo didáctico:**  
Construir un formulario **accesible** con `label/for`, `required` y tipos semánticos; comprender validación **nativa** del navegador.

**Buenas prácticas:**
- Empareja siempre `<label for="id">` con el control cuyo `id` coincide.  
- Usa tipos correctos (`email`, `tel`, `number`, etc.).  
- Agrupa campos relacionados con `fieldset` + `legend` cuando tenga sentido.

**Ejemplo mínimo (sin envío real de datos en esta unidad)**
```html
<form action="#" method="post" aria-describedby="ayuda-form" onsubmit="alert('En esta unidad no enviamos datos.'); return false;">
  <p id="ayuda-form" class="note">Campos con * son obligatorios.</p>

  <label for="nombre">Nombre *</label><br>
  <input id="nombre" name="nombre" type="text" required placeholder="Tu nombre"><br><br>

  <label for="email">Correo electrónico *</label><br>
  <input id="email" name="email" type="email" required placeholder="tucorreo@ejemplo.com"><br><br>

  <label for="comentarios">Comentarios</label><br>
  <textarea id="comentarios" name="comentarios" rows="4" cols="30" placeholder="Escribe aquí..."></textarea><br><br>

  <button type="submit">Enviar</button>
</form>
```

**TODO Alumno**
1. Añade un campo **teléfono** con patrón para España: `+34 600000000` o `600000000`.  
   - Pista: `pattern="\+?34?[\s-]?[0-9]{9}"`  
2. Inserta un `fieldset` **Preferencias** con `legend` y 2 checkboxes (Boletín, Acepto condiciones).  
3. Cambia `action="#"` por un **ancla interno** `#introduccion` y explica por qué **no** enviamos a servidor en esta unidad.

**✅ Solución sugerida**
```html
<label for="tel">Teléfono</label><br>
<input id="tel" name="tel" type="tel" pattern="\+?34?[\s-]?[0-9]{9}" placeholder="+34 600000000"><br><br>

<fieldset>
  <legend>Preferencias</legend>
  <label><input type="checkbox" name="boletin"> Suscribirme al boletín</label><br>
  <label><input type="checkbox" name="condiciones" required> Acepto condiciones *</label>
</fieldset>

<!-- action="#introduccion" para permanecer en la misma página en esta unidad -->
```

**? Nota:** La validación nativa (`required`, `type=email`, `pattern`, etc.) actúa **antes** de enviar el formulario. Es ideal en iniciación porque **no requiere JavaScript**.

---

## 🎬 Multimedia en HTML
**Objetivo didáctico:**  
Insertar **vídeo** y **audio** con etiquetas nativas, y conocer `track` para subtítulos.

**Buenas prácticas:**
- Añade `track` cuando tengas subtítulos disponibles.  
- Usa un `poster` representativo en vídeos locales.  
- Para reproducir automáticamente en navegadores modernos, suele requerirse `muted` junto con `autoplay` (por políticas de reproducción automática).

**Ejemplo con fuentes remotas**
```html
<h3>Video</h3>
<video controls width="100%">
  <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>

<h3>Audio</h3>
<audio controls>
  <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
  Tu navegador no soporta audio.
</audio>
```

**TODO Alumno**
1. Inserta un vídeo local en `/media/intro.mp4` con `poster="/img/portada.png"`.  
2. Añade subtítulos con `track` (`src="/media/subs.vtt"`, `srclang="es"`, `label="Español"`).  
3. Prueba `autoplay muted loop` y explica por qué **muted** suele ser necesario para que el autoplay funcione.

**✅ Solución sugerida**
```html
<video controls poster="img/portada.png" width="100%" autoplay muted loop>
  <source src="media/intro.mp4" type="video/mp4">
  <track kind="subtitles" src="media/subs.vtt" srclang="es" label="Español">
</video>
```

---

## 🚀 Proyecto final · **Mi Portfolio personal**
**Objetivo:** Construir un **Portfolio Web** básico con las piezas practicadas de HTML.

**Checklist de secciones:**
1. `header` con tu nombre y menú de navegación.  
2. Sección **Sobre mí** con un párrafo breve.  
3. Sección **Proyectos** con una lista o tabla de trabajos.  
4. Galería con 3 imágenes usando `figure` + `figcaption`.  
5. Formulario de contacto (nombre, email, mensaje).  
6. `footer` con enlaces a redes sociales.

**Plantilla mínima (estructura)**
```html
<header>
  <h1>Tu Nombre</h1>
  <nav>
    <a href="#sobre-mi">Sobre mí</a>
    <a href="#proyectos">Proyectos</a>
    <a href="#galeria">Galería</a>
    <a href="#contacto">Contacto</a>
  </nav>
</header>

<main>
  <section id="sobre-mi">
    <h2>Sobre mí</h2>
    <p>Breve presentación…</p>
  </section>

  <section id="proyectos">
    <h2>Proyectos</h2>
    <ul>
      <li>Proyecto A — breve descripción</li>
      <li>Proyecto B — breve descripción</li>
    </ul>
  </section>

  <section id="galeria">
    <h2>Galería</h2>
    <figure>
      <img src="img/proyecto1.jpg" alt="Captura del proyecto 1">
      <figcaption>Proyecto 1</figcaption>
    </figure>
    <figure>
      <img src="img/proyecto2.jpg" alt="Captura del proyecto 2">
      <figcaption>Proyecto 2</figcaption>
    </figure>
    <figure>
      <img src="img/proyecto3.jpg" alt="Captura del proyecto 3">
      <figcaption>Proyecto 3</figcaption>
    </figure>
  </section>

  <section id="contacto">
    <h2>Contacto</h2>
    <form action="#sobre-mi">
      <label for="c-nombre">Nombre</label><br>
      <input id="c-nombre" type="text" required><br><br>

      <label for="c-email">Email</label><br>
      <input id="c-email" type="email" required><br><br>

      <label for="c-msg">Mensaje</label><br>
      <textarea id="c-msg" rows="4"></textarea><br><br>

      <button type="submit">Enviar</button>
    </form>
  </section>
</main>

<footer>
  <p>&copy; 2025 · Tu Nombre</p>
  <nav>
    <a href="#sobre-mi">Inicio</a>
    <a href="https://twitter.com/tucuenta" target="_blank" rel="noopener">Twitter</a>
  </nav>
</footer>
```

**💡 Usa la Inteligencia Artificial (prompt listo)**
```
Genérame un archivo HTML básico para un portfolio personal que incluya:
1. Un header con mi nombre y un menú de navegación.
2. Una sección "Sobre mí" con un párrafo breve.
3. Una sección "Proyectos" con una lista de trabajos.
4. Una galería con 3 imágenes dentro de figure + figcaption.
5. Un formulario de contacto con nombre, email y mensaje.
6. Un footer con enlaces a mis redes sociales.
Devuélveme solo el HTML, sin CSS ni JavaScript.
```

---

## 🔚 Pie de página (semántica y navegación secundaria)
**Objetivo didáctico:**  
Cerrar la estructura con `footer`, añadir **navegación secundaria** y practicar enlaces especiales como `mailto:`.

**Ejemplo**
```html
<footer id="contacto" aria-labelledby="h-foot">
  <h2 id="h-foot">Pie de página</h2>
  <p>Creado por [Nombre del alumno].</p>
  <nav aria-label="Navegación secundaria">
    <ul>
      <li><a href="#introduccion">Inicio</a></li>
      <li><a href="#seccion-tablas">Tablas</a></li>
      <li><a href="#seccion-imagenes">Imágenes</a></li>
      <li><a href="#seccion-formularios">Formularios</a></li>
      <li><a href="#seccion-multimedia">Multimedia</a></li>
    </ul>
  </nav>
  <!-- Contacto: <a href="mailto:profesor@ejemplo.com">profesor@ejemplo.com</a> -->
</footer>
```

**TODO Alumno**
- Añade un enlace **“Contacto”** en el menú principal que apunte a `#contacto`.  
- Crea un `mailto:` práctico en el `footer` con tu correo real.

---

### ✅ Resumen rápido de la UT1
- HTML define la **estructura**.
- Practica **listas, tablas, imágenes, formularios y multimedia**.
- Usa semántica y accesibilidad básica (`alt`, `label/for`, `scope`, `legend`).
- Prepara tu **Portfolio** con secciones claras y navegación interna.
