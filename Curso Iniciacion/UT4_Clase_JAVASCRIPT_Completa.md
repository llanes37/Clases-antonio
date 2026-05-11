
# ⚡ UT4 — Clase Completa de **JavaScript** (Markdown Docente)
**Autor:** Joaquín Rodríguez  
**Nivel:** Iniciación  
**Modo de uso:** Explica + construye + ejercita (ideal con Live Server).

> Este `.md` reúne **todas las explicaciones y ejemplos** de la UT4 que estaban en tu `.html`, ampliados pedagógicamente y listos para copiar/pegar. Mantiene el enfoque docente: teoría breve, ejemplos copiables, **TODO Alumno** y **Soluciones sugeridas**. Los resultados se muestran **en pantalla** (no solo `alert`/consola) para reforzar el aprendizaje visual.

---

## 🧭 Índice
- [Cómo leer este documento](#-cómo-leer-este-documento)
- [0) Introducción · ¿Qué es JavaScript y cómo se conecta con HTML?](#0-introducción--qué-es-javascript-y-cómo-se-conecta-con-html)
- [1) alert() — Mensajes emergentes](#1-alert--mensajes-emergentes)
- [2) prompt() + Variables](#2-prompt--variables)
- [3) Condicionales](#3-condicionales)
- [4) Funciones (parámetros y return)](#4-funciones-parámetros-y-return)
- [5) Bucles](#5-bucles)
- [6) Arrays](#6-arrays)
- [7) Objetos](#7-objetos)
- [8) DOM: cambiar texto/HTML/estilos](#8-dom-cambiar-textohtmlestilos)
- [9) Eventos (click, input)](#9-eventos-click-input)
- [10) Imágenes: cambiar atributos](#10-imágenes-cambiar-atributos)
- [11) localStorage](#11-localstorage)
- [12) Mini-proyecto · Tarjeta de Perfil interactiva](#12-mini-proyecto--tarjeta-de-perfil-interactiva)
- [Proyecto Final · Portfolio con Bootstrap + JavaScript](#proyecto-final--portfolio-con-bootstrap--javascript)
- [Resumen rápido de la UT4](#-resumen-rápido-de-la-ut4)

---

## 📝 Cómo leer este documento
Convención **Better Comments** (igual que en UT1–UT3):

- **! Importante** → idea clave.  
- **? Nota** → aclaración útil.  
- **\* Ejemplo** → fragmento demostrativo.  
- **TODO Alumno** → tareas concretas.  
- **✅ Solución** → posible implementación (cuando aporta valor).

En cada bloque incluimos **Objetivo didáctico**, **Buenas prácticas** y **Ejemplos**.  
Recuerda abrir la **Consola** (F12 → “Console”) como apoyo de depuración.

---

## 0) Introducción · ¿Qué es JavaScript y cómo se conecta con HTML?
**Objetivo didáctico:**  
Comprender el papel de **JavaScript (JS)** como **interactividad**: reacciona a eventos, modifica el DOM, valida formularios y puede **guardar datos**.

**Flujo típico**
1. El HTML define elementos (botones, textos, inputs) → **DOM**.  
2. Un **evento** (por ejemplo, `click`) dispara una **función JS**.  
3. La función **lee o cambia** el DOM → el usuario **ve el cambio** en pantalla.

**Consejo**
> 💡 Trabaja con **Live Server** para ver cambios al guardar y muestra el resultado en una caja `div.resultado` además de en consola/alert.

---

## 1) `alert()` — Mensajes emergentes
**Objetivo didáctico:**  
Verificar rápidamente que una función ha sido llamada.

**Ejemplo**
```html
<button onclick="saludar()">Mostrar saludo</button>
<div id="res1" class="resultado"></div>

<script>
  function saludar(){
    alert("¡Hola! Bienvenido/a a JavaScript 🎉");
    document.getElementById('res1').innerText = "Se mostró un alert() de saludo.";
  }
</script>
```

**TODO Alumno**
- Implementa `despedir()` que muestre `alert("¡Hasta luego!")` y escriba en `#res1` “Se mostró un alert() de despedida.”

**✅ Solución sugerida**
```html
<button onclick="despedir()">Despedirme</button>
<script>
  function despedir(){
    alert("¡Hasta luego!");
    document.getElementById('res1').innerText = "Se mostró un alert() de despedida.";
  }
</script>
```

---

## 2) `prompt()` + Variables
**Objetivo didáctico:**  
Capturar **entrada de usuario** y guardarla en **variables** (`let` / `const`).

**Ejemplo**
```html
<button onclick="preguntarNombre()">Pedir nombre</button>
<div id="res2" class="resultado"></div>

<script>
  function preguntarNombre(){
    const nombre = prompt("¿Cómo te llamas?");
    if(nombre){
      const mensaje = `Encantado/a, ${nombre}.`;
      alert(mensaje);
      document.getElementById('res2').innerText = mensaje;
    }else{
      document.getElementById('res2').innerText = "No escribiste nombre.";
    }
  }
</script>
```

**TODO Alumno**
1. Crea `preguntarCiudad()` que pida una ciudad y la muestre en `#res2`.  
2. **Bonus:** concatena nombre + ciudad con **template strings**.

**✅ Pista**
```js
const ciudad = prompt("¿De qué ciudad eres?");
document.getElementById('res2').innerText = `Hola, ${nombre} de ${ciudad}`;
```

---

## 3) Condicionales
**Objetivo didáctico:**  
Tomar decisiones con `if/else if/else` y validar entradas numéricas.

**Ejemplo**
```html
<button onclick="esMayor()">¿Eres mayor de edad?</button>
<div id="res3" class="resultado"></div>

<script>
  function esMayor(){
    const edad = Number(prompt("¿Cuántos años tienes?"));
    let msg = "";
    if(Number.isNaN(edad)){ msg = "No escribiste un número."; }
    else if(edad >= 18){ msg = "Eres mayor de edad ✅"; }
    else if(edad < 5){ msg = "Eres un bebé 👶"; }
    else{ msg = "Eres menor de edad 🚫"; }
    alert(msg);
    document.getElementById('res3').innerText = msg;
  }
</script>
```

**TODO Alumno**
- `comprobarTreinta()` que indique si tienes **30 o más**.  
- **Bonus:** tercer caso “entre 13 y 17”.

---

## 4) Funciones (parámetros y `return`)
**Objetivo didáctico:**  
Crear funciones **reutilizables** con parámetros y retorno de valores.

**Ejemplo**
```html
<button onclick="demoMultiplicar()">Calcular 3 × 4</button>
<div id="res4" class="resultado"></div>

<script>
  function multiplicar(a,b){ return a*b; }
  function demoMultiplicar(){
    const r = multiplicar(3,4);
    document.getElementById('res4').innerText = "3 × 4 = " + r;
  }
</script>
```

**TODO Alumno**
1. `restar(a,b)` y `demoRestar()` pidiendo 2 números con `prompt` y mostrando el resultado.  
2. **Bonus:** validar no numéricos → “Entrada no válida”.

**✅ Pista**
```js
const a = Number(prompt("A:"));
const b = Number(prompt("B:"));
if(Number.isNaN(a) || Number.isNaN(b)){ /* ... */ }
```

---

## 5) Bucles
**Objetivo didáctico:**  
Repetición con `for`, `while` o `do...while`.

**Ejemplo**
```html
<button onclick="contarAsc()">Contar 1 → 5</button>
<button onclick="contarDesc()">Contar 5 → 1</button>
<div id="res5" class="resultado"></div>

<script>
  function contarAsc(){
    let s = "";
    for(let i=1;i<=5;i++){ s += i + (i<5?" • ":""); }
    document.getElementById('res5').innerText = s;
  }
  function contarDesc(){
    let s = "";
    for(let i=5;i>=1;i--){ s += i + (i>1?" • ":""); }
    document.getElementById('res5').innerText = s;
  }
</script>
```

**TODO Alumno**
- Mostrar **pares** de 2 a 10.  
- **Bonus:** **FizzBuzz** 1→20.

---

## 6) Arrays
**Objetivo didáctico:**  
Crear listas con `[]`, añadir/eliminar elementos y renderizar en pantalla.

**Ejemplo**
```html
<button onclick="listarFrutas()">Mostrar frutas</button>
<button onclick="quitarPrimera()">Quitar primera</button>
<div id="res6" class="resultado"></div>

<script>
  const frutas = ["manzana","banana","pera"];
  function renderFrutas(){
    document.getElementById('res6').innerText = "Frutas: " + frutas.join(", ");
  }
  function listarFrutas(){ renderFrutas(); }
  function quitarPrimera(){ frutas.shift(); renderFrutas(); }
</script>
```

**TODO Alumno**
1. Crea `const animales = ["perro","gato","loro"]` y muéstralos.  
2. **Bonus:** input + botón “Agregar animal” (usar `push()` y volver a pintar).

---

## 7) Objetos
**Objetivo didáctico:**  
Agrupar datos relacionados en **pares clave:valor** y acceder a sus propiedades.

**Ejemplo**
```html
<button onclick="mostrarPersona()">Mostrar persona</button>
<div id="res7" class="resultado"></div>

<script>
  function mostrarPersona(){
    const persona = { nombre:"Alex", edad:28, ciudad:"Madrid" };
    const msg = `Me llamo ${persona.nombre}, tengo ${persona.edad} años y vivo en ${persona.ciudad}.`;
    document.getElementById('res7').innerText = msg;
  }
</script>
```

**TODO Alumno**
- Crea `coche = { marca, modelo, año }` y muéstralo.  
- **Bonus:** método `coche.resumen()` que devuelva una frase y muéstrala.

---

## 8) DOM: cambiar texto/HTML/estilos
**Objetivo didáctico:**  
Seleccionar elementos (`getElementById`) y modificar **texto**, **HTML** o **estilos**.

**Ejemplo**
```html
<p id="parrafoDemo">Este texto se puede cambiar desde JS.</p>
<button onclick="cambiarTexto()">Cambiar texto</button>
<button onclick="cambiarEstilo()">Cambiar estilo</button>
<div id="res8" class="resultado"></div>

<script>
  function cambiarTexto(){
    const p = document.getElementById('parrafoDemo');
    p.innerText = "¡Texto cambiado con JS!";
    document.getElementById('res8').innerText = "innerText actualizado 👌";
  }
  function cambiarEstilo(){
    const p = document.getElementById('parrafoDemo');
    p.style.color = "#2563eb";
    p.style.fontWeight = "700";
    document.getElementById('res8').innerText = "Estilos aplicados (color y negrita).";
  }
</script>
```

**TODO Alumno**
- Botón que ponga **cursiva** (`fontStyle="italic"`).  
- **Bonus:** alternar normal/negra con **toggle** de estado.

---

## 9) Eventos (click, input)
**Objetivo didáctico:**  
Entender que un **evento** dispara una función; practicar `addEventListener`.

**Ejemplo**
```html
<p id="textoEvento">Pasa el ratón por aquí…</p>
<input id="nombreInput" type="text" placeholder="Escribe tu nombre" />
<div id="res9" class="resultado"></div>

<script>
  // mouseover: cambia el texto y el color
  document.getElementById('textoEvento').addEventListener('mouseover', function(){
    this.style.color = "crimson";
    this.innerText = "¡Pasaste el ratón! 👋";
    document.getElementById('res9').innerText = "Evento mouseover detectado.";
  });

  // input: refleja en vivo lo que escribes
  document.getElementById('nombreInput').addEventListener('input', function(){
    document.getElementById('res9').innerText = "Escribiendo: " + this.value;
  });
</script>
```

**TODO Alumno**
- `mouseout` para restaurar el texto original.  
- **Bonus:** si el input está vacío, muestra “Vacío”.

---

## 10) Imágenes: cambiar atributos
**Objetivo didáctico:**  
Cambiar `src`, `alt`, `width/height` desde JS y aplicar estilos.

**Ejemplo**
```html
<img id="imgDemo" src="https://via.placeholder.com/200" alt="Imagen demo" />
<button onclick="cambiarImagen()">Cambiar imagen</button>
<button onclick="añadirBorde()">Añadir borde</button>
<div id="res10" class="resultado"></div>

<script>
  function cambiarImagen(){
    const img = document.getElementById('imgDemo');
    img.src = "https://picsum.photos/300";
    img.alt = "Imagen aleatoria";
    document.getElementById('res10').innerText = "Imagen y alt actualizados.";
  }
  function añadirBorde(){
    document.getElementById('imgDemo').style.border = "4px solid #ef4444";
    document.getElementById('res10').innerText = "Borde rojo aplicado.";
  }
</script>
```

**TODO Alumno**
- Botón que cambie el **alt** a “Mi imagen personalizada”.  
- **Bonus:** botón que quite el borde (`border = "none"`).

---

## 11) `localStorage`
**Objetivo didáctico:**  
Persistir datos simples en el navegador.

**API**
- `setItem("clave", "valor")`  
- `getItem("clave")`  
- `removeItem("clave")`

**Ejemplo**
```html
<input id="datoGuardar" type="text" placeholder="Escribe algo para guardar" />
<button onclick="guardarDato()">Guardar</button>
<button onclick="mostrarDato()">Mostrar</button>
<button onclick="borrarDato()">Borrar</button>
<div id="res11" class="resultado"></div>

<script>
  function guardarDato(){
    const v = document.getElementById('datoGuardar').value;
    localStorage.setItem("miDato", v);
    document.getElementById('res11').innerText = "Dato guardado ✅";
  }
  function mostrarDato(){
    const v = localStorage.getItem("miDato");
    document.getElementById('res11').innerText = "Dato guardado: " + (v ?? "(ninguno)");
  }
  function borrarDato(){
    localStorage.removeItem("miDato");
    document.getElementById('res11').innerText = "Dato borrado 🗑️";
  }
</script>
```

**TODO Alumno**
- Guarda un **objeto** `{nombre, edad}` usando `JSON.stringify` y recupéralo con `JSON.parse()`; pinta sus propiedades.

**✅ Pista**
```js
const persona = { nombre:"Ana", edad:30 };
localStorage.setItem("persona", JSON.stringify(persona));
const p = JSON.parse(localStorage.getItem("persona") || "{}");
```

---

## 12) Mini-proyecto · **Tarjeta de Perfil** interactiva
**Objetivo:** Integrar **inputs**, **eventos**, **arrays**, **DOM** y **localStorage**.

**Interfaz sugerida**
```html
<label>Nombre</label><input id="pfNombre" type="text">
<label>Ciudad</label><input id="pfCiudad" type="text">
<label>Habilidad</label><input id="pfSkill" type="text">

<button onclick="agregarSkill()">+ Añadir habilidad</button>
<button onclick="pintarPerfil()">🖼️ Pintar perfil</button>
<button onclick="guardarPerfil()">💾 Guardar</button>
<button onclick="cargarPerfil()">⤓ Cargar</button>
<button onclick="resetPerfil()">🗑️ Reset</button>

<div id="perfilCard" class="resultado"></div>
```

**Lógica base**
```js
const perfil = { nombre:"", ciudad:"", skills:[] };

function agregarSkill(){
  const s = document.getElementById('pfSkill').value.trim();
  if(!s) return;
  perfil.skills.push(s);
  document.getElementById('pfSkill').value = "";
  pintarPerfil();
}
function pintarPerfil(){
  perfil.nombre = document.getElementById('pfNombre').value.trim();
  perfil.ciudad = document.getElementById('pfCiudad').value.trim();
  const lista = perfil.skills.map(sk=>`<li>${sk}</li>`).join("");
  const html = `
    <h3>${perfil.nombre || "Sin nombre"}</h3>
    <p class="muted">📍 ${perfil.ciudad || "Sin ciudad"}</p>
    <h4>Habilidades</h4>
    <ul>${lista || "<li>(Añade habilidades)</li>"}</ul>
  `;
  document.getElementById('perfilCard').innerHTML = html;
}
function guardarPerfil(){
  localStorage.setItem("perfilJS", JSON.stringify(perfil));
  document.getElementById('perfilCard').insertAdjacentHTML('beforeend', `<p class="muted">Guardado ✅</p>`);
}
function cargarPerfil(){
  const raw = localStorage.getItem("perfilJS");
  if(!raw) return;
  const data = JSON.parse(raw);
  perfil.nombre = data.nombre || "";
  perfil.ciudad = data.ciudad || "";
  perfil.skills = Array.isArray(data.skills)? data.skills : [];
  document.getElementById('pfNombre').value = perfil.nombre;
  document.getElementById('pfCiudad').value = perfil.ciudad;
  document.getElementById('pfSkill').value = "";
  pintarPerfil();
}
function resetPerfil(){
  perfil.nombre=""; perfil.ciudad=""; perfil.skills=[];
  document.getElementById('pfNombre').value="";
  document.getElementById('pfCiudad').value="";
  document.getElementById('pfSkill').value="";
  pintarPerfil();
}
```

**TODO Alumno**
- Botón **“Eliminar última habilidad”** (`pop()` y repintar).  
- **Bonus:** botón **“Exportar”** que muestre el JSON en `alert` o consola.

---

## Proyecto Final · **Portfolio con Bootstrap + JavaScript**
**Objetivo:** Llevar tu Portfolio a otro nivel con **interacciones reales**.

**Checklist de mejoras**
1. **Navbar** fija con Bootstrap y **scroll suave** con JS hacia secciones.  
2. **Sobre mí**: botón “WhatsApp” que abra tu número:  
   ```js
   window.open("https://wa.me/34XXXXXXXXX");
   ```
3. **Proyectos**: tarjetas (**cards**) con **filtro por palabra clave** en JS.  
4. **Galería**: grid con `row/col` y **modal** en JS al hacer clic en imagen.  
5. **Formulario**: validación en JS (email válido y mensaje no vacío).  
   ```js
   window.location.href = "mailto:tuemail@correo.com";
   ```
6. **Footer**: `bg-dark text-white text-center p-3` + **modo oscuro** con JS que cambie la paleta de toda la página.

**Ideas para pedir a la IA**
- “Genérame un navbar fijo con Bootstrap que use scroll suave en JS.”  
- “Ejemplo de filtro de tarjetas por palabra clave en JavaScript.”  
- “Valida un formulario con Bootstrap y JS (email no vacío + formato).”  
- “Botón de modo oscuro que alterne variables CSS o clases en `<body>`.”

---

## ✅ Resumen rápido de la UT4
- JS añade **interactividad**: eventos → funciones → cambios en el DOM.  
- Has practicado **alert/prompt**, **condicionales**, **funciones**, **bucles**, **arrays**, **objetos**, **DOM**, **eventos**, **imágenes** y **localStorage**.  
- Integra todo con el **mini‑proyecto** y remata en tu **Portfolio final** con Bootstrap + JS.
