# 🛠️ UT0 — Configuración del Entorno de Desarrollo

**Autor:** Joaquín Rodríguez  
**Nivel:** Principiante absoluto  
**Duración estimada:** 45-60 minutos  
**Modo de uso:** Seguir paso a paso antes de empezar el curso

---

## 🎯 Objetivo de esta unidad

Antes de escribir tu primera línea de código, necesitas **preparar tu entorno de trabajo**. Al terminar esta unidad tendrás:

- ✅ **VS Code** instalado y configurado
- ✅ **Extensiones esenciales** para desarrollo web
- ✅ Tu **primera carpeta de proyecto** organizada
- ✅ Un archivo **"Hola Mundo"** funcionando en el navegador
- ✅ Conocimiento de los **atajos de teclado** básicos

---

## 📋 Índice

1. [¿Qué necesitamos?](#1-qué-necesitamos)
2. [Instalar Visual Studio Code](#2-instalar-visual-studio-code)
3. [Configurar VS Code en español](#3-configurar-vs-code-en-español)
4. [Instalar extensiones esenciales](#4-instalar-extensiones-esenciales)
5. [Crear tu primera carpeta de proyecto](#5-crear-tu-primera-carpeta-de-proyecto)
6. [Tu primer archivo HTML (Hola Mundo)](#6-tu-primer-archivo-html-hola-mundo)
7. [Ejecutar con Live Server](#7-ejecutar-con-live-server)
8. [Atajos de teclado imprescindibles](#8-atajos-de-teclado-imprescindibles)
9. [Navegador y DevTools](#9-navegador-y-devtools)
10. [Estructura de carpetas recomendada](#10-estructura-de-carpetas-recomendada)
11. [Checklist final](#11-checklist-final)
12. [Solución de problemas](#12-solución-de-problemas)

---

## 1. ¿Qué necesitamos?

Para desarrollar páginas web necesitas solo **3 cosas gratuitas**:

| Herramienta | ¿Para qué? | ¿Dónde conseguirla? |
|-------------|------------|---------------------|
| **Editor de código** | Escribir HTML, CSS, JavaScript | VS Code (gratis) |
| **Navegador moderno** | Ver el resultado de tu código | Chrome, Firefox, Edge |
| **Ganas de aprender** | ¡Lo más importante! | Ya las tienes 😄 |

### ¿Por qué VS Code?

- 🆓 **Gratuito** y de código abierto
- 🚀 **Ligero** pero muy potente
- 🧩 **Extensiones** para todo
- 🌍 **El más usado** en la industria
- 📚 **Mucha documentación** y tutoriales

---

## 2. Instalar Visual Studio Code

### 2.1 Descargar

1. Abre tu navegador
2. Ve a: **https://code.visualstudio.com**
3. Haz clic en el botón grande de descarga (detecta tu sistema automáticamente)

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│           Visual Studio Code                        │
│                                                     │
│     ┌─────────────────────────────────┐             │
│     │                                 │             │
│     │   ⬇️  Download for Windows     │             │
│     │      Stable Build               │             │
│     │                                 │             │
│     └─────────────────────────────────┘             │
│                                                     │
│     Other platforms: macOS | Linux                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 2.2 Instalar en Windows

1. Abre el archivo descargado (`VSCodeUserSetup-x64-X.XX.X.exe`)
2. Acepta los términos de licencia
3. **⚠️ IMPORTANTE:** Marca estas opciones:
   - ☑️ Agregar "Abrir con Code" al menú contextual de archivos
   - ☑️ Agregar "Abrir con Code" al menú contextual de directorios
   - ☑️ Agregar a PATH
4. Haz clic en "Instalar"
5. Al terminar, haz clic en "Finalizar"

### 2.3 Instalar en macOS

1. Abre el archivo `.zip` descargado
2. Arrastra **Visual Studio Code.app** a la carpeta **Aplicaciones**
3. Abre VS Code desde Aplicaciones
4. (Opcional) Arrastra al Dock para acceso rápido

### 2.4 Instalar en Linux (Ubuntu/Debian)

```bash
# Opción 1: Descargar .deb desde la web e instalar
sudo dpkg -i code_*.deb

# Opción 2: Usando snap
sudo snap install code --classic
```

---

## 3. Configurar VS Code en español

### 3.1 Abrir VS Code

Al abrirlo por primera vez verás la pantalla de bienvenida en inglés. Vamos a cambiarlo.

### 3.2 Instalar el paquete de idioma

1. Pulsa `Ctrl + Shift + X` (Windows/Linux) o `Cmd + Shift + X` (Mac)
2. Esto abre el panel de **Extensiones**
3. Escribe: `Spanish Language Pack`
4. Busca: **"Spanish Language Pack for Visual Studio Code"** (de Microsoft)
5. Haz clic en **"Install"**

```
┌─────────────────────────────────────────────────────┐
│ 🔍 Spanish Language Pack                            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  📦 Spanish Language Pack for Visual Studio Code    │
│     Microsoft                                       │
│     ⭐⭐⭐⭐⭐ (4.8)  |  10M+ downloads              │
│                                                     │
│     [Install]                                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 3.3 Reiniciar VS Code

1. Aparecerá un mensaje para cambiar el idioma
2. Haz clic en **"Change Language and Restart"**
3. VS Code se reiniciará en español

---

## 4. Instalar extensiones esenciales

Las extensiones añaden superpoderes a VS Code. Estas son **obligatorias** para el curso:

### 4.1 Cómo instalar extensiones

1. Pulsa `Ctrl + Shift + X` (abre Extensiones)
2. Escribe el nombre de la extensión
3. Haz clic en **"Instalar"**

### 4.2 Extensiones OBLIGATORIAS

#### 🔴 Live Server (Ritwick Dey)
**¿Para qué?** Ver tu página web en el navegador con recarga automática al guardar.

```
Nombre: Live Server
Autor: Ritwick Dey
Descargas: 40M+
```

#### 🟢 Better Comments (Aaron Bond)
**¿Para qué?** Comentarios de colores para entender mejor el código del curso.

```
Nombre: Better Comments
Autor: Aaron Bond
Descargas: 8M+
```

### 4.3 Extensiones RECOMENDADAS

#### 🟡 Prettier - Code formatter
**¿Para qué?** Formatea tu código automáticamente para que sea legible.

#### 🟡 Auto Rename Tag
**¿Para qué?** Al cambiar una etiqueta HTML, cambia automáticamente la de cierre.

#### 🟡 HTML CSS Support
**¿Para qué?** Autocompletado de clases CSS en HTML.

#### 🟡 Color Highlight
**¿Para qué?** Muestra los colores CSS visualmente en el código.

#### 🟡 indent-rainbow
**¿Para qué?** Colorea la indentación para ver mejor la estructura.

#### 🟡 Path Intellisense
**¿Para qué?** Autocompletado de rutas de archivos.

### 4.4 Resumen visual

```
OBLIGATORIAS (instalar SÍ o SÍ):
┌────────────────────────────────────────┐
│ ✅ Live Server                         │
│ ✅ Better Comments                     │
└────────────────────────────────────────┘

RECOMENDADAS (instalar cuando puedas):
┌────────────────────────────────────────┐
│ 📦 Prettier - Code formatter           │
│ 📦 Auto Rename Tag                     │
│ 📦 HTML CSS Support                    │
│ 📦 Color Highlight                     │
│ 📦 indent-rainbow                      │
│ 📦 Path Intellisense                   │
└────────────────────────────────────────┘
```

---

## 5. Crear tu primera carpeta de proyecto

### 5.1 Dónde guardar tus proyectos

Crea una carpeta principal para TODOS tus proyectos web:

**Windows:**
```
C:\Users\TuNombre\Documentos\desarrollo-web\
```

**macOS:**
```
/Users/TuNombre/Documents/desarrollo-web/
```

**Linux:**
```
/home/tunombre/desarrollo-web/
```

### 5.2 Crear la estructura

1. Abre el **Explorador de archivos**
2. Ve a **Documentos**
3. Crea una carpeta llamada `desarrollo-web`
4. Dentro, crea otra carpeta llamada `00-hola-mundo`

```
📁 Documentos/
   📁 desarrollo-web/           ← Carpeta principal del curso
      📁 00-hola-mundo/         ← Tu primer proyecto
      📁 01-portfolio-html/     ← (Lo crearás en UT1)
      📁 02-portfolio-css/      ← (Lo crearás en UT2)
      ...
```

### 5.3 Abrir la carpeta en VS Code

**Método 1: Desde VS Code**
1. Abre VS Code
2. `Archivo → Abrir carpeta...`
3. Navega hasta `00-hola-mundo`
4. Haz clic en "Seleccionar carpeta"

**Método 2: Desde el explorador (si marcaste la opción al instalar)**
1. Ve a la carpeta `00-hola-mundo`
2. Clic derecho en un espacio vacío
3. Selecciona "Abrir con Code"

---

## 6. Tu primer archivo HTML (Hola Mundo)

### 6.1 Crear el archivo

1. En VS Code, con la carpeta `00-hola-mundo` abierta
2. En el panel izquierdo (Explorador), haz clic en el icono de **"Nuevo archivo"** 📄
3. Escribe: `index.html`
4. Pulsa `Enter`

```
┌─────────────────────────────────────────────────────┐
│ EXPLORADOR                                          │
├─────────────────────────────────────────────────────┤
│ 📁 00-HOLA-MUNDO                                    │
│    📄 index.html  ← ¡Tu nuevo archivo!              │
└─────────────────────────────────────────────────────┘
```

### 6.2 Escribir el código

Haz clic en el archivo `index.html` para abrirlo y escribe:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Primera Página</title>
</head>
<body>
    <h1>¡Hola Mundo! 🌍</h1>
    <p>Esta es mi primera página web.</p>
    <p>Estoy aprendiendo desarrollo web.</p>
</body>
</html>
```

### 6.3 Atajo mágico: Emmet

En lugar de escribir todo eso, VS Code tiene un atajo:

1. En un archivo `.html` vacío
2. Escribe solo: `!`
3. Pulsa `Tab` o `Enter`
4. ¡Se genera la estructura automáticamente! 🎉

```
Escribes:  !
Pulsas:    Tab
Obtienes:  ¡Toda la estructura HTML básica!
```

### 6.4 Guardar el archivo

Pulsa `Ctrl + S` (Windows/Linux) o `Cmd + S` (Mac)

**💡 Consejo:** Activa el autoguardado:
1. `Archivo → Preferencias → Configuración`
2. Busca "Auto Save"
3. Cambia a "afterDelay"

---

## 7. Ejecutar con Live Server

### 7.1 Iniciar Live Server

Con el archivo `index.html` abierto:

**Método 1: Clic derecho**
1. Clic derecho en el código
2. Selecciona **"Open with Live Server"**

**Método 2: Barra inferior**
1. Mira la barra azul de abajo
2. Haz clic en **"Go Live"**

```
┌─────────────────────────────────────────────────────┐
│ [VS Code]                                           │
│                                                     │
│  ... tu código ...                                  │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Ln 1, Col 1    UTF-8    HTML    🔴 Go Live          │
└─────────────────────────────────────────────────────┘
                                     ↑
                              Haz clic aquí
```

### 7.2 Ver el resultado

1. Se abrirá tu navegador automáticamente
2. Verás tu página en: `http://127.0.0.1:5500`
3. ¡Ya tienes tu web funcionando!

```
┌─────────────────────────────────────────────────────┐
│ 🌐 http://127.0.0.1:5500/index.html                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ¡Hola Mundo! 🌍                                    │
│                                                     │
│  Esta es mi primera página web.                    │
│  Estoy aprendiendo desarrollo web.                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 7.3 La magia de Live Server

1. Vuelve a VS Code
2. Cambia el texto de `<h1>`:
```html
<h1>¡Hola Mundo! 🚀 ¡Esto es increíble!</h1>
```
3. Guarda (`Ctrl + S`)
4. ¡Mira el navegador! Se actualiza **automáticamente** 🎉

### 7.4 Detener Live Server

Haz clic en **"Port: 5500"** en la barra inferior (donde antes decía "Go Live")

---

## 8. Atajos de teclado imprescindibles

Memoriza estos atajos, ¡te ahorrarán MUCHO tiempo!

### 8.1 Atajos generales

| Acción | Windows/Linux | Mac |
|--------|---------------|-----|
| Guardar | `Ctrl + S` | `Cmd + S` |
| Guardar todo | `Ctrl + K, S` | `Cmd + K, S` |
| Deshacer | `Ctrl + Z` | `Cmd + Z` |
| Rehacer | `Ctrl + Y` | `Cmd + Shift + Z` |
| Buscar | `Ctrl + F` | `Cmd + F` |
| Buscar y reemplazar | `Ctrl + H` | `Cmd + H` |
| Paleta de comandos | `Ctrl + Shift + P` | `Cmd + Shift + P` |

### 8.2 Atajos de edición

| Acción | Windows/Linux | Mac |
|--------|---------------|-----|
| Duplicar línea | `Shift + Alt + ↓` | `Shift + Option + ↓` |
| Mover línea arriba/abajo | `Alt + ↑/↓` | `Option + ↑/↓` |
| Borrar línea | `Ctrl + Shift + K` | `Cmd + Shift + K` |
| Comentar línea | `Ctrl + /` | `Cmd + /` |
| Seleccionar palabra | `Ctrl + D` | `Cmd + D` |
| Seleccionar todas las ocurrencias | `Ctrl + Shift + L` | `Cmd + Shift + L` |

### 8.3 Atajos de navegación

| Acción | Windows/Linux | Mac |
|--------|---------------|-----|
| Ir a línea | `Ctrl + G` | `Cmd + G` |
| Abrir archivo | `Ctrl + P` | `Cmd + P` |
| Cerrar pestaña | `Ctrl + W` | `Cmd + W` |
| Cambiar pestaña | `Ctrl + Tab` | `Ctrl + Tab` |
| Panel de extensiones | `Ctrl + Shift + X` | `Cmd + Shift + X` |
| Terminal integrada | `` Ctrl + ` `` | `` Cmd + ` `` |

### 8.4 Atajos de Emmet (HTML)

| Escribes | Pulsas Tab | Obtienes |
|----------|------------|----------|
| `!` | → | Estructura HTML completa |
| `div` | → | `<div></div>` |
| `div.clase` | → | `<div class="clase"></div>` |
| `div#id` | → | `<div id="id"></div>` |
| `ul>li*3` | → | Lista con 3 items |
| `p{texto}` | → | `<p>texto</p>` |
| `a[href=#]` | → | `<a href="#"></a>` |

---

## 9. Navegador y DevTools

### 9.1 ¿Qué navegador usar?

Cualquiera de estos es válido:

| Navegador | Recomendación |
|-----------|---------------|
| **Google Chrome** | ⭐ El más usado, excelentes DevTools |
| **Mozilla Firefox** | ⭐ Muy bueno para desarrollo |
| **Microsoft Edge** | ✅ Basado en Chrome, funciona igual |
| **Safari** | ✅ Solo para Mac, necesario para probar |

### 9.2 Abrir DevTools (Herramientas de desarrollo)

Las DevTools son **esenciales** para ver errores y depurar:

| Método | Windows/Linux | Mac |
|--------|---------------|-----|
| Atajo de teclado | `F12` | `F12` o `Cmd + Option + I` |
| Menú | Menú → Más herramientas → Herramientas de desarrollo | |
| Clic derecho | Clic derecho → Inspeccionar | |

### 9.3 Pestañas importantes de DevTools

```
┌────────────────────────────────────────────────────────────────┐
│ Elements │ Console │ Sources │ Network │ Performance │ ...    │
└────────────────────────────────────────────────────────────────┘
     ↓          ↓
     │          └── Ver errores de JavaScript
     └── Inspeccionar y modificar HTML/CSS
```

- **Elements:** Ver y modificar HTML/CSS en tiempo real
- **Console:** Ver errores y mensajes de JavaScript
- **Network:** Ver qué archivos se cargan

### 9.4 Ejercicio: Inspecciona tu página

1. Abre tu página `index.html` con Live Server
2. Pulsa `F12` para abrir DevTools
3. En la pestaña **Elements**, busca tu `<h1>`
4. Haz doble clic en el texto y cámbialo
5. ¡Ves el cambio en la página! (temporal, no se guarda)

---

## 10. Estructura de carpetas recomendada

### 10.1 Para un proyecto simple

```
📁 mi-proyecto/
   📄 index.html          ← Página principal
   📄 about.html          ← Otras páginas
   📄 contact.html
   📁 css/
      📄 styles.css       ← Estilos
   📁 js/
      📄 app.js           ← JavaScript
   📁 img/
      🖼️ logo.png         ← Imágenes
      🖼️ foto.jpg
```

### 10.2 Para el portfolio del curso

```
📁 portfolio/
   📄 index.html
   📁 css/
      📄 styles.css
   📁 js/
      📄 app.js
   📁 img/
      🖼️ profile.jpg
      🖼️ project1.png
      🖼️ project2.png
   📁 docs/
      📄 cv.pdf           ← Opcional: tu CV
```

### 10.3 Reglas para nombres de archivos

```
✅ BIEN:
   index.html
   styles.css
   mi-proyecto.html
   foto-perfil.jpg
   app.js

❌ MAL:
   Index.HTML         ← No uses mayúsculas
   mi proyecto.html   ← No uses espacios
   página.html        ← No uses tildes
   foto (1).jpg       ← No uses paréntesis
```

---

## 11. Checklist final

Antes de pasar a la UT1, verifica que tienes todo:

### ✅ Software instalado

- [ ] VS Code instalado y funcionando
- [ ] VS Code en español
- [ ] Extensión **Live Server** instalada
- [ ] Extensión **Better Comments** instalada
- [ ] Navegador moderno (Chrome/Firefox/Edge)

### ✅ Proyecto de prueba

- [ ] Carpeta `desarrollo-web` creada
- [ ] Subcarpeta `00-hola-mundo` creada
- [ ] Archivo `index.html` con "Hola Mundo"
- [ ] Página funcionando con Live Server
- [ ] Sabes abrir DevTools (F12)

### ✅ Conocimientos básicos

- [ ] Sé crear archivos nuevos en VS Code
- [ ] Sé guardar archivos (Ctrl+S)
- [ ] Sé usar el atajo `!` + Tab para HTML
- [ ] Sé iniciar y detener Live Server
- [ ] Sé abrir la consola del navegador

---

## 12. Solución de problemas

### ❌ "Live Server no aparece"

**Causa:** La extensión no está instalada o no está activa.

**Solución:**
1. Pulsa `Ctrl + Shift + X`
2. Busca "Live Server"
3. Si dice "Disable", ya está instalada → reinicia VS Code
4. Si dice "Install", instálala

---

### ❌ "Go Live no aparece en la barra"

**Causa:** No tienes un archivo HTML abierto.

**Solución:**
1. Abre un archivo `.html`
2. Debería aparecer "Go Live" en la barra inferior

---

### ❌ "El navegador no se abre automáticamente"

**Solución manual:**
1. Abre tu navegador
2. Ve a: `http://127.0.0.1:5500`
3. O: `http://localhost:5500`

---

### ❌ "Los cambios no se actualizan"

**Causa:** No has guardado el archivo.

**Solución:**
1. Mira si hay un **punto blanco** en la pestaña del archivo
2. Eso indica cambios sin guardar
3. Pulsa `Ctrl + S` para guardar

```
┌──────────────────────────────┐
│ ● index.html    ← Sin guardar (punto blanco)
│   index.html    ← Guardado (sin punto)
└──────────────────────────────┘
```

---

### ❌ "VS Code está en inglés y no cambia"

**Solución:**
1. Pulsa `Ctrl + Shift + P`
2. Escribe: `Configure Display Language`
3. Selecciona `es` (Español)
4. Reinicia VS Code

---

### ❌ "No sé dónde está mi archivo"

**Solución:**
1. En VS Code, clic derecho en el archivo
2. Selecciona "Revelar en el Explorador de archivos"
3. Se abrirá la carpeta donde está

---

## 🎉 ¡Felicidades!

Has completado la configuración de tu entorno de desarrollo. Estás listo/a para empezar la **UT1: HTML**.

### Próximos pasos

1. **UT1:** Aprenderás la estructura de una página web con HTML
2. **UT2:** Darás estilo con CSS
3. **UT3:** Usarás Bootstrap para diseño rápido
4. **UT4:** Añadirás interactividad con JavaScript
5. **UT5:** Crearás tu portfolio completo
6. **UT6:** Aprenderás DevTools y Git

---

## 📚 Recursos adicionales

### Documentación oficial
- VS Code: https://code.visualstudio.com/docs
- MDN Web Docs: https://developer.mozilla.org/es/

### Atajos de VS Code (PDF descargable)
- Windows: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf
- Mac: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf
- Linux: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf

### Practica Emmet
- Cheat Sheet: https://docs.emmet.io/cheat-sheet/

---

**¡Nos vemos en la UT1!** 🚀

*Curso de Iniciación al Desarrollo Web — Joaquín Rodríguez*
