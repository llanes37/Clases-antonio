
# 🎨 UT2 — Clase Completa de **CSS** (Markdown Docente)
**Autor:** Joaquín Rodríguez  
**Nivel:** Iniciación  
**Modo de uso:** Explica + construye + ejercita (ideal con Live Server).

> Este `.md` reúne **todas las explicaciones y ejemplos** de la UT2 que tenías en el `.html`, pero en formato **Markdown** listo para tu plataforma. Mantiene el enfoque docente: teoría breve, ejemplos copiables, **TODO Alumno** y **Soluciones sugeridas**.

---

## 🧭 Índice
- [Cómo leer este documento](#-cómo-leer-este-documento)
- [Introducción a CSS](#-introducción-a-css)
- [Estilos globales](#-estilos-globales)
- [Colores en CSS](#-colores-en-css)
- [Tipografía](#-tipografía)
- [Modelo de caja](#-modelo-de-caja)
- [Mini-proyecto · Portfolio con CSS](#-mini-proyecto--portfolio-con-css)

---

## 📝 Cómo leer este documento
Convención **Better Comments** (como en tu HTML original):

- **! Importante** → idea clave.  
- **? Nota** → aclaración útil.  
- **\* Ejemplo** → fragmento demostrativo.  
- **TODO Alumno** → tareas concretas.  
- **✅ Solución** → una posible solución explicada.

En cada bloque incluimos:
- **Objetivo didáctico** (qué se practica).  
- **Buenas prácticas**.  
- **Ejemplos** en bloques `css`/`html` listos para copiar.

---

## 🌱 Introducción a CSS
**Objetivo didáctico:**  
Entender que **CSS** define la **presentación** del HTML: colores, fuentes, tamaños, márgenes, etc. Empezamos por reglas sencillas y visibles.

**Cómo enlazar CSS**
```html
<!-- Opción A (recomendada): hoja externa -->
<link rel="stylesheet" href="styles.css">

<!-- Opción B (para demos/clase): CSS interno -->
<style>
  /* Reglas aquí */
</style>
```

**Estructura de una regla CSS**  
```
selector {
  propiedad: valor;
}
```

---

## 🧩 Estilos globales
**Objetivo didáctico:**  
Aplicar estilos **globales** a todo el documento (fuente, colores base, márgenes).

**Buenas prácticas:**
- Define una **fuente legible** y un **fondo** suave.  
- Normaliza márgenes/paddings del `body` para empezar de cero.

**Ejemplo**
```css
/* 1) ESTILOS GLOBALES */
body{
  font-family: Arial, sans-serif; /* * Fuente genérica y fácil de leer */
  background-color: #f0f0f0;      /* * Fondo suave */
  color:#333;                      /* * Texto gris oscuro */
  margin:0; padding:0;
}
header{
  background:#333; color:#fff; text-align:center; padding:20px;
}
nav ul{ list-style:none; padding:0; margin:10px 0 0 0; }
nav ul li{ display:inline; margin-right:15px; }
nav ul li a{ color:#fff; text-decoration:none; }
nav ul li a:hover{ text-decoration:underline; } /* ! Pequeño feedback */
section{
  margin:20px; padding:20px; background:#fff;
  border:1px solid #ccc; box-shadow:0 4px 8px rgba(0,0,0,.1);
}
```

**TODO Alumno**
1. Crea un `header` con título y un `nav` con 4 enlaces internos (`#introduccion`, `#colores`, `#tipografia`, `#modelo-caja`).  
2. Añade un `section` con un párrafo explicando para qué sirve CSS.

**✅ Solución sugerida (HTML mínimo)**
```html
<header>
  <h1>Clase CSS Completa (iniciación)</h1>
  <nav>
    <ul>
      <li><a href="#introduccion">Introducción</a></li>
      <li><a href="#colores">Colores</a></li>
      <li><a href="#tipografia">Tipografía</a></li>
      <li><a href="#modelo-caja">Modelo de Caja</a></li>
    </ul>
  </nav>
</header>

<section id="introduccion">
  <h2>Introducción a CSS</h2>
  <p>CSS sirve para dar estilo al HTML: colores, fuentes, tamaños, márgenes, etc.</p>
</section>
```

---

## 🎨 Colores en CSS
**Objetivo didáctico:**  
Practicar `background-color` (fondo) y `color` (texto), y entender `padding`, `margin` y `border-radius` en cajas sencillas.

**Buenas prácticas:**
- Usa **nombres**, **hex** (`#ff6b6b`), **rgb()** o **hsl()** para colores.  
- Mantén **contraste** suficiente entre texto y fondo.

**Ejemplo (HTML + CSS)**
```html
<section id="colores">
  <h2>Colores en CSS</h2>
  <p>Propiedades clave: <code>background-color</code> y <code>color</code>.</p>

  <div class="caja-roja">Caja con fondo rojo</div>
  <div class="caja-azul">Caja con fondo azul</div>
  <div class="caja-verde">Caja con fondo verde</div>
</section>
```

```css
.caja-roja{
  background:red; color:#fff; padding:10px; margin-bottom:10px; border-radius:5px;
}
.caja-azul{
  background:blue; color:#fff; padding:10px; margin-bottom:10px; border-radius:5px;
}
.caja-verde{
  background:green; color:#fff; padding:10px; margin-bottom:10px; border-radius:5px;
}
```

**TODO Alumno**
1. Crea una cuarta caja **`.caja-amarilla`** con **fondo amarillo** y **texto negro**.  
2. Crea **`.caja-personal`** usando un color **HEX** (p. ej., `#ff6b6b`) o `rgb(...)`.  
3. Aumenta el **padding** de `.caja-personal` a **20px** para notar el cambio.

**✅ Solución sugerida**
```css
.caja-amarilla{ background:yellow; color:#000; padding:10px; margin-bottom:10px; border-radius:5px; }
.caja-personal{ background:#ff6b6b; color:#111; padding:20px; margin-bottom:10px; border-radius:6px; }
```

---

## 🔤 Tipografía
**Objetivo didáctico:**  
Cambiar **fuentes** (`font-family`), **tamaños** (`font-size`) y **peso** (`font-weight`).

**Buenas prácticas:**
- Usa pilas de fuentes de respaldo: `"Georgia", "Times New Roman", serif`.  
- Usa `rem` para escalabilidad cuando empieces a maquetar a mayor nivel.

**Ejemplo**
```html
<section id="tipografia">
  <h2>Tipografía</h2>
  <p class="tipografia-courier">Texto en Courier (20px).</p>
  <p class="tipografia-verdana">Texto en Verdana (18px).</p>
  <p class="resaltado">Este texto está resaltado con fondo amarillo.</p>
</section>
```

```css
.tipografia-courier{ font-family:'Courier New', Courier, monospace; font-size:20px; }
.tipografia-verdana{ font-family:Verdana, sans-serif; font-size:18px; }
.resaltado{ background:yellow; font-weight:bold; }
```

**TODO Alumno**
1. Crea un párrafo con la fuente **Georgia** y **tamaño 22px**.  
2. Crea otro párrafo con **tamaño 14px** y **color gris** `#666` para simular texto secundario.  
3. *(Opcional)* Cambia el **`h2`** de esta sección a **24px** usando una regla específica `#tipografia h2`.

**✅ Solución sugerida**
```css
.georgia-22{ font-family: Georgia, 'Times New Roman', serif; font-size:22px; }
.secundario-14{ font-size:14px; color:#666; }
#tipografia h2{ font-size:24px; }
```

---

## 📦 Modelo de caja
**Objetivo didáctico:**  
Entender la caja del navegador: **contenido**, **padding**, **border** y **margin**.

**Buenas prácticas:**
- Añade `box-sizing: border-box;` si necesitas que `padding`/`border` formen parte del ancho total del elemento.  
- Usa **clases utilitarias** para experimentar rápido (p. ej., `.borde-azul`).

**Ejemplo**
```html
<section id="modelo-caja">
  <h2>Modelo de Caja</h2>
  <p>Todo elemento es una caja con: <strong>contenido</strong>, <strong>padding</strong>, <strong>border</strong> y <strong>margin</strong>.</p>

  <div class="modelo-caja">Caja 1: padding 20px, borde negro, fondo gris claro.</div>
</section>
```

```css
.modelo-caja{
  border:2px solid #000; padding:20px; margin:10px; background:#f9f9f9;
}
.borde-azul{ border-color:#2563eb; }
```

**TODO Alumno**
1. Duplica la caja anterior y añádele la clase **`.borde-azul`** para ver el borde azul.  
2. Crea `.modelo-caja-grande` con **padding: 40px** y aplícalo a una tercera caja.  
3. Añade **`margin-top: 20px`** a la tercera caja para separarla más.

**✅ Solución sugerida**
```css
.modelo-caja-grande{ padding:40px; margin-top:20px; }
```

```html
<div class="modelo-caja borde-azul">Caja 2 con borde azul</div>
<div class="modelo-caja modelo-caja-grande">Caja 3 grande</div>
```

---

## 🧪 Mini-proyecto · **Portfolio con CSS**
**Objetivo:** Aplicar **colores**, **tipografía** y **modelo de caja** para mejorar el **Portfolio HTML** hecho en UT1.

**Checklist de pasos:**
1. Abre tu `Proyecto_Portfolio.html`.  
2. Aplica **estilos globales** al `body` (fuente, color de fondo y color de texto).  
3. Pon un **fondo oscuro** al `header` y el menú en **horizontal**.  
4. Estiliza **Sobre mí** con **caja blanca** y **sombra suave**.  
5. Convierte **Proyectos** en **tarjetas** con borde y margen.  
6. Muestra la **galería** en fila con un borde fino en imágenes.  
7. Diseña el **formulario** con etiquetas en bloque y `padding` en los inputs.  
8. Cierra con un **footer** gris y enlaces centrados.

**Base CSS sugerida**
```css
body{ font-family: Arial, sans-serif; background:#f6f7fb; color:#1f2937; margin:0 }
header{ background:#111; color:#fff; padding:24px }
nav ul{ display:flex; gap:16px; list-style:none; padding:0; margin:0 }
nav a{ color:#fff; text-decoration:none }
section{ background:#fff; margin:20px; padding:20px; border:1px solid #e5e7eb; border-radius:10px; box-shadow:0 6px 14px rgba(0,0,0,.06) }
.proyecto{ border:1px solid #e5e7eb; border-radius:10px; padding:12px; margin-bottom:12px }
.galeria img{ max-width:100%; border:1px solid #ddd; border-radius:8px; padding:4px }
form label{ display:block; margin-top:10px }
input, textarea{ width:100%; padding:10px; border:1px solid #ccc; border-radius:8px }
footer{ background:#f1f5f9; color:#374151; text-align:center; padding:16px }
```

**TODO Alumno**
1. Crea un archivo **`styles.css`** y **enlázalo** a tu portfolio.  
2. Copia y **adapta** los estilos (colores, fuentes, cajas) a tu gusto.  
3. Cambia paleta/espaciados para darle **identidad propia**.

**💡 Usa la Inteligencia Artificial (prompt listo)**
```
Genérame un archivo CSS sencillo para un portfolio personal que incluya:
1. Estilos globales para body (fuente Arial, fondo claro).
2. Header oscuro con menú de navegación horizontal.
3. Sección "Sobre mí" con caja blanca y sombra suave.
4. Sección "Proyectos" con tarjetas con borde y margen.
5. Galería de imágenes en fila, con borde y padding.
6. Formulario de contacto con etiquetas en bloque y campos con padding.
7. Footer gris con enlaces centrados.
Devuélveme solo el CSS, sin HTML ni comentarios extra.
```

---

### ✅ Resumen rápido de la UT2
- CSS controla la **presentación** (colores, tipografías, espaciados).  
- Practicaste **globales, colores, tipografía y modelo de caja**.  
- Has mejorado tu **Portfolio** aplicando una estética coherente.
