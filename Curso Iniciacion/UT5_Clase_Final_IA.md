# 🎓 Clase Final con IA: Crea tu Página Web Completa con Inteligencia Artificial

**Autor:** Joaquín Rodríguez
**Destinatario:** Alumno/a de Programación Web

------------------------------------------------------------------------

## 🎯 Objetivo de la Clase Final

En esta clase aprenderás a **usar la Inteligencia Artificial como tu
copiloto de desarrollo web**.\
Ya tienes experiencia con **HTML, CSS, Bootstrap y JavaScript** creando
un portafolio básico.\
Ahora darás un paso más:\
- Aprender a **escribir prompts claros y útiles**.\
- Pedirle a la IA **plantillas completas comentadas**.\
- Copiar tu código en la IA para que lo **explique paso a paso**.\
- **Mejorar secciones concretas** de tu web (WhatsApp, animaciones,
formularios, etc.).\
- Terminar con una **aplicación web final, moderna, comentada y
funcional**.

------------------------------------------------------------------------

## 🚀 Paso 1. Crear tu plantilla base con IA

### Prompt sugerido

    Quiero crear una plantilla de portafolio con HTML, CSS y Bootstrap. 
    Elige un tema bonito y moderno (viajes, música, películas, deportes…). 
    Hazlo todo comentado y explícame paso a paso cada parte del código.

### Ejemplo de resultado esperado

``` html
<!-- 🌐 Plantilla base de portfolio -->
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Portfolio</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <!-- Encabezado con navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Mi Portfolio</a>
    </div>
  </nav>

  <!-- Sección principal -->
  <header class="text-center p-5 bg-primary text-white">
    <h1>Bienvenido a mi sitio</h1>
    <p>Desarrollador web en progreso 🚀</p>
  </header>
</body>
</html>
```

👉 **TODO Alumno**:\
1. Elige un tema que te guste.\
2. Copia el código generado por la IA en tu editor.\
3. Prueba cómo se ve en el navegador.\
4. Lee las explicaciones de la IA y asegúrate de entender cada parte.

------------------------------------------------------------------------

## 📘 Paso 2. Pide explicación de tu propio código

### Prompt sugerido

    Aquí tienes mi código actual. Explícamelo paso a paso como si fuera 
    principiante para que lo entienda todo.

👉 **TODO Alumno**:\
- Copia tu propio código en la IA.\
- Pide que te lo explique con detalle (estructura, etiquetas, clases,
estilos).\
- Anota lo que no entiendas y vuelve a preguntarle a la IA.

------------------------------------------------------------------------

## 🛠️ Paso 3. Mejorar secciones con IA (una por una)

### Ejemplo 1: Botón de WhatsApp

Prompt sugerido:

    Aquí está mi sección de contacto. ¿Puedes añadir un botón de WhatsApp 
    que abra un chat directo conmigo? Explica qué código has añadido y dónde.

Ejemplo de resultado:

``` html
<!-- Botón de WhatsApp -->
<a href="https://wa.me/34600000000" target="_blank" 
   class="btn btn-success mt-3">
   <i class="bi bi-whatsapp"></i> Escríbeme en WhatsApp
</a>
```

### Ejemplo 2: Formulario con validación

Prompt sugerido:

    Tengo este formulario en mi portfolio. ¿Puedes hacerlo más moderno con Bootstrap
    y añadir validación con JavaScript?

Ejemplo de resultado:

``` html
<form id="contactForm" class="mt-4">
  <input type="email" class="form-control" id="email" placeholder="Tu correo" required>
  <button type="submit" class="btn btn-primary mt-3">Enviar</button>
</form>

<script>
  document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();
    alert("Formulario enviado correctamente ✅");
  });
</script>
```

### Ejemplo 3: Animaciones con CSS y JS

Prompt sugerido:

    Tengo esta sección con mis proyectos. ¿Puedes añadir animaciones con CSS y 
    JavaScript para que cada tarjeta aparezca con efecto fade-in?

Ejemplo de resultado:

``` css
/* Animación básica fade-in */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease-in-out;
}
.fade-in.show {
  opacity: 1;
  transform: translateY(0);
}
```

``` js
// JavaScript para aplicar animación
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".fade-in");
  cards.forEach((card, i) => {
    setTimeout(() => card.classList.add("show"), i * 300);
  });
});
```

👉 **TODO Alumno**:\
- Copia SOLO la sección que quieras mejorar.\
- Pide a la IA que la mejore y te explique los cambios.\
- Sustituye tu código por el nuevo y pruébalo en el navegador.

------------------------------------------------------------------------

## 🎨 Paso 4. Personalizar el diseño

Prompt sugerido:

    Quiero cambiar mi portfolio para que tenga un tema oscuro (dark mode). 
    Explícame cómo hacerlo con CSS y JavaScript para que el usuario 
    pueda alternar entre claro y oscuro.

Ejemplo de resultado:

``` js
// Botón para cambiar entre modos
const toggle = document.getElementById("toggleDark");
toggle.addEventListener("click", () => {
  document.body.classList.toggle("bg-dark");
  document.body.classList.toggle("text-white");
});
```

👉 **TODO Alumno**:\
- Implementa los cambios.\
- Comprueba que puedes alternar entre temas.

------------------------------------------------------------------------

## 📂 Paso 5. Añadir almacenamiento local (localStorage)

Prompt sugerido:

    Quiero que mi portfolio recuerde el modo oscuro o claro con localStorage. 
    Explícame el código paso a paso.

Ejemplo de resultado:

``` js
// Guardar preferencia en localStorage
const toggle = document.getElementById("toggleDark");
toggle.addEventListener("click", () => {
  const dark = document.body.classList.toggle("bg-dark");
  localStorage.setItem("dark-mode", dark);
});

// Mantener preferencia al recargar
if (localStorage.getItem("dark-mode") === "true") {
  document.body.classList.add("bg-dark", "text-white");
}
```

------------------------------------------------------------------------

## 🎯 Paso 6. Proyecto Final: Página Web Completa con IA

Prompt sugerido:

    Quiero crear una página web completa con HTML, CSS, Bootstrap y JavaScript
    para un tema que me guste (ejemplo: cine, música, deportes, viajes…).  
    Debe incluir:
    - Un header con navbar.
    - Una sección de presentación.
    - Una galería de proyectos con tarjetas.
    - Un formulario de contacto.
    - Botón de WhatsApp y enlaces a redes sociales.
    - Modo oscuro con localStorage.
    Hazlo todo comentado, paso a paso y bien explicado.

Ejemplo de estructura mínima:

``` html
<header class="bg-dark text-white p-4 text-center">
  <h1>Mi Página Final</h1>
</header>

<section class="container mt-5">
  <h2>Sobre mí</h2>
  <p>Aquí una breve descripción...</p>
</section>

<section class="container mt-5">
  <h2>Proyectos</h2>
  <div class="row">
    <div class="col-md-4">
      <div class="card fade-in">
        <img src="proyecto1.jpg" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Proyecto 1</h5>
        </div>
      </div>
    </div>
  </div>
</section>
```

👉 **TODO Alumno**:\
1. Copia el código generado.\
2. Pruébalo en tu navegador.\
3. Lee cada explicación.\
4. Modifícalo para personalizarlo (cambia textos, imágenes, colores).\
5. Pregunta a la IA cómo mejorar secciones específicas.

------------------------------------------------------------------------

## ✅ Conclusión

Al terminar esta clase tendrás:\
- Tu **primer proyecto web completo**, hecho por ti con ayuda de la IA.\
- Conocimiento para **pedir mejoras de forma precisa**.\
- Un método para seguir aprendiendo por tu cuenta, siempre con
**explicaciones comentadas y entendibles**.

------------------------------------------------------------------------
