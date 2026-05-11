
# 🟣 UT3 — Clase Completa de **Bootstrap** (Markdown Docente)
**Autor:** Joaquín Rodríguez  
**Nivel:** Iniciación  
**Modo de uso:** Explica + construye + ejercita (ideal con Live Server).

> Este `.md` reúne **todas las explicaciones y ejemplos** de la UT3 que estaban en el `.html`, ampliados pedagógicamente y listos para copiar/pegar. Mantiene el enfoque docente: teoría breve, ejemplos copiables, **TODO Alumno** y **Soluciones sugeridas**.

---

## 🧭 Índice
- [Cómo leer este documento](#-cómo-leer-este-documento)
- [¿Qué es Bootstrap y por qué usarlo?](#-qué-es-bootstrap-y-por-qué-usarlo)
- [Instalación por CDN (CSS y JS)](#-instalación-por-cdn-css-y-js)
- [Contenedores y tipografía básica](#-contenedores-y-tipografía-básica)
- [Botones](#-botones)
- [Formularios](#-formularios)
- [Tablas](#-tablas)
- [Alertas](#-alertas)
- [Carrusel](#-carrusel)
- [Grid esencial (row/col) — extra recomendado](#-grid-esencial-rowcol--extra-recomendado)
- [Cards (tarjetas) — extra recomendado](#-cards-tarjetas--extra-recomendado)
- [Mini-proyecto · Portfolio con Bootstrap](#-mini-proyecto--portfolio-con-bootstrap)
- [Resumen rápido de la UT3](#-resumen-rápido-de-la-ut3)

---

## 📝 Cómo leer este documento
Convención **Better Comments** (como en tus unidades anteriores):

- **! Importante** → idea clave.  
- **? Nota** → aclaración útil.  
- **\* Ejemplo** → fragmento demostrativo.  
- **TODO Alumno** → tareas concretas.  
- **✅ Solución** → una posible solución explicada.

Cada bloque incluye **Objetivo didáctico**, **Buenas prácticas** y **Ejemplos**.

---

## 🚀 ¿Qué es Bootstrap y por qué usarlo?
**Objetivo didáctico:**  
Entender que **Bootstrap** es un framework CSS con **clases predefinidas** para componer UI rápidamente (botones, formularios, grid, tipografía…).

**Ventajas:**
- Ahorra mucho CSS manual.  
- Diseño **responsivo** por defecto.  
- Componentes y utilidades listas para usar.

---

## 🔗 Instalación por CDN (CSS y JS)
**Objetivo didáctico:**  
Incorporar Bootstrap con **CDN** (sin instalaciones locales).

**Buenas prácticas:**
- Cargar **CSS** en el `<head>`.  
- Cargar **JS bundle** (incluye Popper) **antes del `</body>`**.

```html
<!-- En el <head> -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Antes de </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

**TODO Alumno**
- Crea un archivo `ut3_bootstrap.html`, pega el esqueleto HTML5 y enlaza **CSS** y **JS** por CDN.

---

## 🧱 Contenedores y tipografía básica
**Objetivo didáctico:**  
Usar `.container` para centrar y limitar ancho; trabajar con utilidades de tipografía.

**Ejemplo (HTML)**
```html
<div class="container mt-5">
  <h1 class="text-center">Bienvenido a Bootstrap 🚀</h1>
  <p class="lead text-muted text-center">
    Bootstrap es un framework CSS con clases predefinidas que nos ahorra escribir mucho código.
    Solo tenemos que usar las clases correctas en nuestro HTML.
  </p>
</div>
```

**Notas de clase**
- `.container` centra y limita el ancho.  
- `mt-5` añade margen superior grande.  
- `lead` agranda ligeramente el texto; `text-muted` lo pone gris claro; `text-center` centra.

**TODO Alumno**
1. Cambia `text-center` por `text-start` o `text-end` para ver la diferencia.  
2. Añade `class="bg-light p-3"` al párrafo para darle fondo y padding.

**✅ Solución sugerida**
```html
<p class="lead text-muted text-start bg-light p-3">…</p>
```

---

## 🟦 Botones
**Objetivo didáctico:**  
Usar clases `btn` y sus variantes de color/tamaño.

**Ejemplo (HTML)**
```html
<section class="container mt-5">
  <h2>Botones en Bootstrap</h2>
  <button class="btn btn-primary">Primario</button>
  <button class="btn btn-secondary">Secundario</button>
  <button class="btn btn-success">Éxito</button>
  <button class="btn btn-danger">Peligro</button>
  <button class="btn btn-warning">Advertencia</button>
  <button class="btn btn-info">Info</button>
</section>
```

**TODO Alumno**
1. Prueba `btn-lg` y `btn-sm`.  
2. Crea un botón `btn btn-outline-dark`.

**✅ Solución sugerida**
```html
<button class="btn btn-primary btn-lg">Grande</button>
<button class="btn btn-secondary btn-sm">Pequeño</button>
<button class="btn btn-outline-dark">Contorno</button>
```

---

## 🧾 Formularios
**Objetivo didáctico:**  
Aplicar estilos consistentes con `form-label`, `form-control` y `form-select`.

**Ejemplo (HTML)**
```html
<section class="container mt-5">
  <h2>Formularios en Bootstrap</h2>
  <form>
    <div class="mb-3">
      <label for="nombre" class="form-label">Nombre:</label>
      <input type="text" class="form-control" id="nombre" placeholder="Introduce tu nombre">
    </div>

    <div class="mb-3">
      <label for="email" class="form-label">Correo:</label>
      <input type="email" class="form-control" id="email" placeholder="ejemplo@correo.com">
    </div>

    <div class="mb-3">
      <label for="pais" class="form-label">País:</label>
      <select class="form-select" id="pais">
        <option>España</option><option>México</option><option>Argentina</option>
      </select>
    </div>

    <button class="btn btn-primary">Enviar</button>
  </form>
</section>
```

**TODO Alumno**
1. Añade un campo **Contraseña** (`type="password"`).  
2. Cambia el botón a `btn-success`.

**✅ Solución sugerida**
```html
<div class="mb-3">
  <label for="pass" class="form-label">Contraseña:</label>
  <input type="password" class="form-control" id="pass" placeholder="••••••••">
</div>
<button class="btn btn-success">Enviar</button>
```

---

## 📊 Tablas
**Objetivo didáctico:**  
Usar `table`, `table-striped`, `table-hover` y tema oscuro.

**Ejemplo (HTML)**
```html
<section class="container mt-5">
  <h2>Tablas</h2>
  <table class="table table-striped table-hover">
    <thead>
      <tr><th>Producto</th><th>Precio</th><th>Cantidad</th></tr>
    </thead>
    <tbody>
      <tr><td>Manzanas</td><td>2.00 €</td><td>5</td></tr>
      <tr><td>Pan</td><td>1.50 €</td><td>10</td></tr>
    </tbody>
  </table>
</section>
```

**TODO Alumno**
1. Añade una fila con otro producto.  
2. Prueba `class="table-dark"` para tema oscuro.

**✅ Solución sugerida**
```html
<table class="table table-striped table-hover table-dark">…</table>
```

---

## ⚠️ Alertas
**Objetivo didáctico:**  
Destacar mensajes con `alert alert-...`.

**Ejemplo (HTML)**
```html
<section class="container mt-5">
  <h2>Alertas</h2>
  <div class="alert alert-success">✔ Operación exitosa</div>
  <div class="alert alert-danger">⚠ Error detectado</div>
  <div class="alert alert-warning">⚡ Cuidado</div>
  <div class="alert alert-info">ℹ Información</div>
</section>
```

**TODO Alumno**
- Crea una alerta `alert alert-primary`.

**✅ Solución sugerida**
```html
<div class="alert alert-primary">Mensaje primario</div>
```

---

## 🖼️ Carrusel
**Objetivo didáctico:**  
Insertar un **carousel** básico con controles y (opcional) captions.

**Ejemplo (HTML)**
```html
<section class="container mt-5">
  <h2>Carrusel</h2>
  <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="https://picsum.photos/id/101/800/400" class="d-block w-100" alt="Imagen 1">
      </div>
      <div class="carousel-item">
        <img src="https://picsum.photos/id/102/800/400" class="d-block w-100" alt="Imagen 2">
      </div>
      <div class="carousel-item">
        <img src="https://picsum.photos/id/103/800/400" class="d-block w-100" alt="Imagen 3">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
      <span class="carousel-control-prev-icon"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
      <span class="carousel-control-next-icon"></span>
    </button>
  </div>
</section>
```

**TODO Alumno**
1. Cambia las imágenes por 3 tuyas.  
2. Añade **captions** (texto sobre la imagen).

**✅ Solución sugerida (caption)**
```html
<div class="carousel-item active">
  <img src="img/foto1.jpg" class="d-block w-100" alt="Proyecto 1">
  <div class="carousel-caption d-none d-md-block">
    <h5>Proyecto 1</h5>
    <p>Descripción breve.</p>
  </div>
</div>
```

---

## 🧩 Grid esencial (row/col) — extra recomendado
**Objetivo didáctico:**  
Entender el **sistema de rejilla** de 12 columnas (`.row` + `.col-*`) para maquetación responsiva.

**Ejemplo básico**
```html
<div class="container my-4">
  <div class="row g-3">
    <div class="col-12 col-md-6 col-lg-4"><div class="p-3 bg-light border">Bloque A</div></div>
    <div class="col-12 col-md-6 col-lg-4"><div class="p-3 bg-light border">Bloque B</div></div>
    <div class="col-12 col-md-6 col-lg-4"><div class="p-3 bg-light border">Bloque C</div></div>
  </div>
</div>
```

**? Nota:** `col-12` móvil (fila completa), `col-md-6` (mitad en >=768px), `col-lg-4` (un tercio en >=992px).

---

## 🗂️ Cards (tarjetas) — extra recomendado
**Objetivo didáctico:**  
Presentar contenido en tarjetas limpias y consistentes.

**Ejemplo**
```html
<div class="container my-4">
  <div class="row row-cols-1 row-cols-md-3 g-3">
    <div class="col">
      <div class="card h-100">
        <img src="img/proyecto1.jpg" class="card-img-top" alt="Proyecto 1">
        <div class="card-body">
          <h5 class="card-title">Proyecto 1</h5>
          <p class="card-text">Descripción corta del proyecto.</p>
          <a href="#" class="btn btn-primary">Ver más</a>
        </div>
      </div>
    </div>
    <!-- Repite para más proyectos -->
  </div>
</div>
```

---

## 🧪 Mini-proyecto · **Portfolio con Bootstrap**
**Objetivo:** Mejorar tu **Portfolio** HTML/CSS con **componentes** y **grid** de Bootstrap.

**Checklist de pasos:**
1. **Header** con `navbar` de Bootstrap.  
2. Sección **Sobre mí** dentro de `container` y `row`.  
3. Sección **Proyectos** usando **cards**.  
4. **Galería** con `row` y `col` (3–6 imágenes).  
5. **Formulario** de contacto con `form-control` y validación nativa.  
6. **Footer** con `bg-dark text-white text-center p-3`.

**Plantilla mínima (HTML)**
```html
<header class="bg-dark text-white">
  <nav class="navbar navbar-expand-lg navbar-dark container">
    <a class="navbar-brand" href="#">Mi Portfolio</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div id="nav" class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto gap-2">
        <li class="nav-item"><a class="nav-link" href="#sobre-mi">Sobre mí</a></li>
        <li class="nav-item"><a class="nav-link" href="#proyectos">Proyectos</a></li>
        <li class="nav-item"><a class="nav-link" href="#galeria">Galería</a></li>
        <li class="nav-item"><a class="nav-link" href="#contacto">Contacto</a></li>
      </ul>
    </div>
  </nav>
</header>

<main class="container my-5">
  <section id="sobre-mi" class="mb-5">
    <h2>Sobre mí</h2>
    <p class="lead text-muted">Breve presentación…</p>
  </section>

  <section id="proyectos" class="mb-5">
    <h2>Proyectos</h2>
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3">
      <div class="col">
        <div class="card h-100">
          <img src="img/p1.jpg" class="card-img-top" alt="Proyecto 1">
          <div class="card-body">
            <h5 class="card-title">Proyecto 1</h5>
            <p class="card-text">Descripción corta.</p>
            <a href="#" class="btn btn-primary">Ver más</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="galeria" class="mb-5">
    <h2>Galería</h2>
    <div class="row g-3">
      <div class="col-6 col-md-4"><img class="img-fluid rounded" src="img/g1.jpg" alt=""></div>
      <div class="col-6 col-md-4"><img class="img-fluid rounded" src="img/g2.jpg" alt=""></div>
      <div class="col-6 col-md-4"><img class="img-fluid rounded" src="img/g3.jpg" alt=""></div>
    </div>
  </section>

  <section id="contacto" class="mb-5">
    <h2>Contacto</h2>
    <form class="col-12 col-md-8 col-lg-6">
      <label class="form-label" for="c-nombre">Nombre</label>
      <input id="c-nombre" class="form-control" type="text" required>
      <label class="form-label mt-3" for="c-email">Email</label>
      <input id="c-email" class="form-control" type="email" required>
      <label class="form-label mt-3" for="c-msg">Mensaje</label>
      <textarea id="c-msg" class="form-control" rows="4"></textarea>
      <button class="btn btn-primary mt-3">Enviar</button>
    </form>
  </section>
</main>

<footer class="bg-dark text-white text-center p-3">
  &copy; 2025 · Tu Nombre
</footer>
```

**TODO Alumno**
- Rehaz tu **portfolio** básico con **Bootstrap** (navbar, grid, cards, formulario, etc.).  
- Compara **antes vs. después** para medir la mejora visual y de tiempo.

---

## ✅ Resumen rápido de la UT3
- Bootstrap reduce **tiempos** con clases predefinidas.  
- Has practicado: **container**, **tipografía**, **botones**, **formularios**, **tablas**, **alertas** y **carrusel**.  
- Extra: **grid** y **cards** para maquetar tu portfolio de forma responsiva.
