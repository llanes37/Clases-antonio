# UT6 - DevTools + Git + Flujo de trabajo real
**Autor:** Joaquín Rodríguez  
**Nivel:** Iniciación (con práctica supervisada)  
**Modo de uso:** Explica + demuestra + deja practicar sobre el portfolio final de UT5.

> Esta unidad cierra el bloque de iniciación. El alumnado ya sabe crear un portfolio con HTML, CSS, Bootstrap, JavaScript y apoyo de IA. Ahora aprenderá a trabajar como desarrollador: inspeccionar su web con DevTools, depurar JavaScript y versionar el proyecto con Git.

---

## Índice
- [Cómo leer este documento](#como-leer-este-documento)
- [Objetivo general de la UT6](#objetivo-general-de-la-ut6)
- [DevTools para HTML y CSS](#devtools-para-html-y-css)
- [DevTools para JavaScript](#devtools-para-javascript)
- [Git básico aplicado al portfolio](#git-basico-aplicado-al-portfolio)
- [Reto integrador UT6](#reto-integrador-ut6)
- [Checklist final y próximos pasos](#checklist-final-y-proximos-pasos)

---

## Cómo leer este documento
Mantiene exactamente la convención de comentarios Better Comments usada en las UT anteriores:
- **! Importante:** idea clave o alerta conceptual.
- **? Nota:** contexto adicional útil.
- **\* Ejemplo:** snippet demostrativo listo para copiar.
- **TODO Alumno:** ejercicios guiados durante la clase.
- **Solución sugerida:** quedará comentada en el HTML para mostrarla en directo cuando convenga.

En cada bloque encontrarás:
1. **Objetivo didáctico.**
2. **Buenas prácticas.**
3. **Ejemplo(s) de código o comandos.**
4. **TODO Alumno** para que pruebe en su propio portfolio.

---

## Objetivo general de la UT6
**Objetivo didáctico:**  
Dominar un flujo de trabajo profesional mínimo: inspeccionar, modificar, probar y versionar la web final creada en UT5.

**Resultados esperados:**
- El alumno usa DevTools para entender y depurar HTML/CSS (box model, reglas activas, etc.).
- Analiza y corrige JavaScript desde la consola (errores, `console.log`, breakpoints sencillos).
- Crea un repositorio Git, registra cambios con `git add` y `git commit`, y redacta mensajes claros.
- Ejecuta un reto integrador que mejore la estética, la interacción y la trazabilidad del proyecto.

---

## DevTools para HTML y CSS
**Objetivo didáctico:**  
Practicar el inspector de elementos para localizar, modificar y copiar estilos antes de tocar los archivos reales.

**Buenas prácticas:**
- Abrir DevTools con `F12` o `Ctrl+Shift+I` y fijarse en las pestañas **Elements** y **Styles**.
- Usar el icono de selección (`Select an element in the page`) para navegar por el DOM.
- Cambiar propiedades en vivo, verificar el resultado y luego trasladar el cambio al archivo CSS/HTML correcto.
- Revisar pestaña **Computed** para entender el box model y detectar márgenes/paddings heredados.

**Ejemplo:** Ajustar la tarjeta de proyectos del portfolio de UT5.

```html
<!-- Tarjeta actual dentro de UT5 -->
<div class="card shadow-sm project-card">
  <img src="img/proyecto1.jpg" alt="Proyecto destacado">
  <div class="card-body">
    <h5>Proyecto 1</h5>
    <p class="text-muted">Descripción breve.</p>
  </div>
</div>
```

```css
/* Ajustes añadidos tras probar en DevTools */
.project-card {
  border-radius: 1.25rem;
  border: 1px solid rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.project-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.25);
}
```

**TODO Alumno**
1. Abre tu `UT5_Clase_Final_IA.html` con Live Server.
2. Usa DevTools para seleccionar el botón de WhatsApp del hero.
3. Cambia el color y padding desde la pestaña Styles.
4. Copia el CSS generado (click derecho > Copy > Copy rule) y pégalo en el archivo correspondiente.

**Solución sugerida**
```css
.btn-whatsapp {
  background-color: #16a34a;
  padding: 0.85rem 1.5rem;
  border-radius: 999px;
  font-weight: 600;
}
```
(Aplica la clase `btn-whatsapp` al botón cuando termines de probarlo en DevTools.)

---

## DevTools para JavaScript
**Objetivo didáctico:**  
Identificar errores de JavaScript, usar la consola y pausar la ejecución para comprender qué ocurre en cada paso.

**Buenas prácticas:**
- Limpiar la consola (`Ctrl+L`) antes de empezar una prueba.
- Usar `console.log` para mostrar valores críticos (inputs de formularios, banderas de modo oscuro, etc.).
- Romper deliberadamente el código (por ejemplo, quitar una llave) y leer el mensaje de error para interiorizar la sintaxis.
- Colocar breakpoints en funciones clave (toggle de tema, envío de formularios) para inspeccionar variables.

**Ejemplo:** Depurar el modo oscuro del portfolio.

```js
const toggle = document.querySelector("#toggleTheme");
const root = document.body;

const setTheme = (mode) => {
  console.log("Cambiando tema a:", mode);
  root.dataset.theme = mode;
  localStorage.setItem("theme-mode", mode);
};

toggle.addEventListener("click", () => {
  const next = root.dataset.theme === "light" ? "dark" : "light";
  setTheme(next);
});

const stored = localStorage.getItem("theme-mode");
if (stored) {
  setTheme(stored);
}
```

**TODO Alumno**
1. Abre DevTools > pestaña **Console**.
2. Copia tu código del modo oscuro y añade `console.log` dentro de la función que cambia el tema.
3. Introduce un error controlado (por ejemplo, elimina un paréntesis) y observa el mensaje exacto.
4. Vuelve a dejarlo bien y practica un breakpoint en `setTheme`.

**Solución sugerida**
- `console.log("Modo previo:", root.dataset.theme);`
- `console.log("Modo nuevo:", next);`

---

## Git básico aplicado al portfolio
**Objetivo didáctico:**  
Crear un repositorio local y registrar cambios significativos del portfolio con mensajes explicativos.

**Buenas prácticas:**
- Inicializa el repositorio en la carpeta raíz del proyecto (por ejemplo, `cursos/Curso Iniciacion/ut5-portfolio` si separas la práctica).
- Agrupa cambios coherentes antes de hacer `git add`.
- Escribe mensajes de commit en imperativo breve (`feat:`, `fix:`, `style:` ayudan a identificar la intención).
- Revisa `git status` antes y después de cada commit para confirmar qué se guardará.

**Ejemplo de flujo**
```bash
git init
git status
git add index.html css/portfolio.css js/main.js
git commit -m "feat: mejora tarjetas de proyectos con hover"

# Tras depurar JavaScript:
git status
git add js/main.js
git commit -m "fix: recuerda modo oscuro con localStorage"
```

**TODO Alumno**
1. Crea un repositorio en la carpeta donde tengas tu versión de UT5.
2. Haz un primer commit llamado `chore: versión inicial de UT5`.
3. Implementa el ajuste de CSS probado en DevTools y confirma con `style: pulido de botón WhatsApp`.
4. Añade los `console.log` y persiste el modo oscuro con un commit `fix: depura toggle de tema`.

**Solución sugerida**
```bash
git add index.html css/styles.css
git commit -m "style: pulido de botón WhatsApp en hero"
git add js/app.js
git commit -m "fix: depura toggle de tema con logs y localStorage"
```

---

## Reto integrador UT6
**Objetivo didáctico:**  
Combinar DevTools y Git para mejorar el portfolio real y dejar huella en el historial de commits.

**Brief del reto:**
1. **Mejora visual rápida:** Usa DevTools para refinar una sección (hero, proyectos o contacto). Tras validar el cambio, transpórtalo al código.
2. **Mejora funcional:** Añade un comportamiento JavaScript:
   - Confirmación de envío en el formulario.
   - Recordatorio del modo oscuro tras recargar.
   - Animación con `classList` y `setTimeout`.
3. **Commit por cada bloque:** al menos tres commits con mensajes descriptivos (visual, funcional, limpieza final).

**Checklist sugerido para los alumnos**
- [ ] He documentado en un comentario qué cambio visual hice.
- [ ] He validado mi JavaScript en consola antes de guardar.
- [ ] He usado `git status` para revisar qué archivos van en cada commit.
- [ ] He actualizado mi README/nota del proyecto explicando la mejora.

**TODO Alumno**
1. Crea una rama mental del reto y apóyate en los pasos anteriores.
2. Muestra al profesor tus commits y explica qué problema solucionó cada uno.
3. Exporta un ZIP o sube a GitHub (opcional) solo cuando asegures que `git status` está limpio.

**Solución sugerida (guion breve)**
```bash
# 1. Ajuste visual
git add index.html css/styles.css
git commit -m "style: refuerza contraste y botones del hero"

# 2. Mejora JavaScript
git add js/main.js
git commit -m "feat: añade mensaje de éxito en formulario"

# 3. Limpieza final
git add .
git commit -m "chore: documenta reto UT6 y limpia consola"
```

---

## Checklist final y próximos pasos
**Antes de cerrar la clase:**
- [ ] Portfolio actualizado con los nuevos estilos y scripts.
- [ ] DevTools dominado para localizar problemas básicos.
- [ ] Repositorio con al menos 3 commits bien descritos.
- [ ] Alumno capaz de explicar qué cambio hizo en cada commit.

**Próximos pasos recomendados:**
1. Repasar UT5 y UT6 para asegurar el flujo completo (diseño → prueba → depuración → versionado).
2. Crear nuevas ramas o proyectos para seguir practicando Git (cuando el nivel lo permita).
3. Publicar el portfolio mejorado en GitHub Pages o Netlify y compartir el enlace con el profesor/tutor.

> ¡Enhorabuena! Con esta UT el alumnado ya trabaja como desarrollador principiante: diagnostica, corrige y deja un historial claro de sus progresos.
