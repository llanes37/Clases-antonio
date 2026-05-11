# 🚀 Guía: Publica tu Primera Web en Netlify (GRATIS)

**Autor:** Joaquín Rodríguez  
**Nivel:** Principiante absoluto  
**Tiempo estimado:** 5-10 minutos

---

## 🎯 ¿Qué vamos a conseguir?

Al terminar esta guía tendrás:
- ✅ Tu página web **publicada en Internet**
- ✅ Una **URL pública** para compartir (ej: `mi-portfolio.netlify.app`)
- ✅ Acceso **gratuito** y **sin límite de tiempo**
- ✅ **HTTPS** incluido (candado verde = seguro)

---

## 📋 Requisitos previos

Antes de empezar, asegúrate de tener:

1. **Tu proyecto web listo** con al menos un archivo `index.html`
2. **Una cuenta de email** (Gmail, Outlook, etc.)
3. **5 minutos** de tu tiempo

### ⚠️ Estructura correcta de tu proyecto

Tu carpeta debe verse así:

```
📁 mi-portfolio/
   📄 index.html        ← ¡OBLIGATORIO! (página principal)
   📁 css/
      📄 styles.css
   📁 js/
      📄 app.js
   📁 img/
      🖼️ foto1.jpg
      🖼️ foto2.png
```

**❗ IMPORTANTE:** El archivo `index.html` DEBE estar en la **raíz** de la carpeta (no dentro de otra carpeta).

---

## 🔧 Paso 0: Preparar tu proyecto

Antes de subir, verifica estos puntos:

### ✅ Checklist de preparación

| Verificar | ¿Correcto? |
|-----------|------------|
| Existe `index.html` en la raíz | ☐ |
| Todas las rutas son **relativas** | ☐ |
| No hay errores en la consola (F12) | ☐ |
| La página se ve bien en Live Server | ☐ |

### 🔗 Rutas relativas vs absolutas

```html
<!-- ❌ MAL - Ruta absoluta (NO funcionará en Netlify) -->
<img src="C:\Users\Juan\Desktop\proyecto\img\foto.jpg">
<link href="D:\web\css\styles.css">

<!-- ✅ BIEN - Ruta relativa (SÍ funcionará) -->
<img src="img/foto.jpg">
<img src="./img/foto.jpg">
<link href="css/styles.css">
<link href="./css/styles.css">
```

### 📝 Nombres de archivos

```
❌ MAL:
   Mi Foto.jpg        (espacios)
   Página.html        (tildes)
   FOTO.JPG           (mayúsculas pueden dar problemas)

✅ BIEN:
   mi-foto.jpg
   pagina.html
   foto.jpg
```

---

## 📝 Paso 1: Crear cuenta en Netlify

### 1.1 Ir a Netlify

Abre tu navegador y ve a:

👉 **https://app.netlify.com**

### 1.2 Registrarte

Tienes varias opciones para crear tu cuenta:

| Opción | Recomendación |
|--------|---------------|
| **GitHub** | ⭐ Recomendado si ya tienes cuenta |
| **GitLab** | Alternativa a GitHub |
| **Bitbucket** | Alternativa a GitHub |
| **Email** | Si no tienes ninguna de las anteriores |

![Pantalla de registro](https://i.imgur.com/placeholder-signup.png)

**Si eliges Email:**
1. Escribe tu email
2. Crea una contraseña segura
3. Revisa tu bandeja de entrada
4. Haz clic en el enlace de verificación

---

## 📤 Paso 2: Subir tu proyecto (Método Drag & Drop)

Este es el método **más fácil** y no requiere conocimientos técnicos.

### 2.1 Ir al panel de Netlify

Una vez dentro, verás algo así:

```
┌─────────────────────────────────────────────────────┐
│  Netlify                                      Team ▼│
├─────────────────────────────────────────────────────┤
│                                                     │
│  Sites                                              │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │                                               │  │
│  │     Want to deploy a new site without         │  │
│  │     connecting to Git?                        │  │
│  │                                               │  │
│  │     Drag and drop your site output folder     │  │
│  │     here                                      │  │
│  │                                               │  │
│  │         ┌─────────────────────┐               │  │
│  │         │   📁 Arrastra tu    │               │  │
│  │         │   carpeta aquí      │               │  │
│  │         └─────────────────────┘               │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 2.2 Arrastrar tu carpeta

1. **Abre el explorador de archivos** de tu ordenador
2. **Localiza la carpeta** de tu proyecto (la que contiene `index.html`)
3. **Arrastra la carpeta completa** a la zona indicada en Netlify
4. **Suelta** y espera unos segundos

### 2.3 ¡Listo! 🎉

Netlify procesará tu sitio y en **menos de 1 minuto** verás:

```
┌─────────────────────────────────────────────────────┐
│  ✅ Deploy successful!                              │
│                                                     │
│  Your site is live at:                              │
│  🔗 https://random-name-12345.netlify.app           │
│                                                     │
│  [Open site]  [Site settings]                       │
└─────────────────────────────────────────────────────┘
```

**¡Ya tienes tu web en Internet!** 🌐

---

## ✏️ Paso 3: Cambiar el nombre del subdominio

El nombre automático (`random-name-12345`) no es muy bonito. Vamos a cambiarlo:

### 3.1 Ir a configuración del sitio

1. Haz clic en **"Site settings"** o **"Domain settings"**
2. Busca la sección **"Site information"** o **"Site details"**
3. Haz clic en **"Change site name"**

### 3.2 Elegir tu nombre

```
┌─────────────────────────────────────────────────────┐
│  Change site name                                   │
│                                                     │
│  Site name:                                         │
│  ┌─────────────────────────────────────────────┐    │
│  │ mi-portfolio-juan                           │    │
│  └─────────────────────────────────────────────┘    │
│  .netlify.app                                       │
│                                                     │
│  ⚠️ Only lowercase letters, numbers, and hyphens    │
│                                                     │
│  [Cancel]  [Save]                                   │
└─────────────────────────────────────────────────────┘
```

**Reglas para el nombre:**
- ✅ Solo letras minúsculas: `a-z`
- ✅ Números: `0-9`
- ✅ Guiones: `-`
- ❌ Sin espacios
- ❌ Sin tildes ni ñ
- ❌ Sin mayúsculas

**Ejemplos válidos:**
- `portfolio-maria-2024`
- `mi-primera-web`
- `juan-developer`
- `proyecto-final-daw`

### 3.3 Tu nueva URL

Ahora tu web estará en:

```
https://TU-NOMBRE-ELEGIDO.netlify.app
```

---

## 🔄 Paso 4: Actualizar tu web

¿Has hecho cambios y quieres actualizarla? ¡Es muy fácil!

### Método rápido (Drag & Drop de nuevo)

1. Ve a tu sitio en Netlify
2. Busca la sección **"Deploys"**
3. Verás otra zona de arrastrar:

```
┌─────────────────────────────────────────────────────┐
│  Deploys                                            │
│                                                     │
│  Need to update your site?                          │
│  Drag and drop your site output folder here         │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │        📁 Arrastra la carpeta aquí          │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

4. Arrastra tu carpeta **actualizada**
5. En segundos tendrás la nueva versión online

---

## ❌ Solución de problemas comunes

### Problema 1: "Page Not Found" (404)

**Causa:** No existe `index.html` en la raíz.

**Solución:**
```
❌ MAL:
📁 mi-proyecto/
   📁 html/
      📄 index.html    ← ¡Está dentro de otra carpeta!

✅ BIEN:
📁 mi-proyecto/
   📄 index.html       ← ¡En la raíz!
```

---

### Problema 2: Imágenes no cargan

**Causa:** Rutas incorrectas o nombres con mayúsculas/espacios.

**Solución:**
```html
<!-- Verifica que la ruta sea correcta -->
<img src="img/foto.jpg">

<!-- Y que el archivo se llame EXACTAMENTE igual -->
📁 img/
   📄 foto.jpg    ← ¡Coincide!
```

**⚠️ Linux (servidores) distingue mayúsculas:**
- `Foto.jpg` ≠ `foto.jpg` ≠ `FOTO.JPG`

---

### Problema 3: CSS no se aplica

**Causa:** Ruta incorrecta o caché del navegador.

**Solución:**
1. Verifica la ruta en el `<head>`:
```html
<link rel="stylesheet" href="css/styles.css">
```

2. Limpia la caché:
   - Windows/Linux: `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`

---

### Problema 4: JavaScript no funciona

**Causa:** Errores en el código o ruta incorrecta.

**Solución:**
1. Abre la consola del navegador (F12 → Console)
2. Busca errores en rojo
3. Verifica que el script esté enlazado:
```html
<!-- Justo antes de </body> -->
<script src="js/app.js"></script>
</body>
```

---

### Problema 5: Navbar/Modal de Bootstrap no funciona

**Causa:** Falta el JavaScript de Bootstrap.

**Solución:**
Asegúrate de tener esto **antes de `</body>`**:
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

### Problema 6: El formulario no envía

**Causa:** Los formularios necesitan un backend o servicio externo.

**Solución gratuita con Formspree:**

1. Ve a https://formspree.io y crea una cuenta
2. Crea un nuevo formulario
3. Copia el endpoint que te dan
4. Modifica tu formulario:

```html
<form action="https://formspree.io/f/TU-ID" method="POST">
  <input type="text" name="nombre" required>
  <input type="email" name="email" required>
  <textarea name="mensaje" required></textarea>
  <button type="submit">Enviar</button>
</form>
```

---

## 🌟 Consejos extra

### 💡 Añadir favicon (icono en la pestaña)

1. Crea o descarga un icono `.ico` o `.png` (32x32 px)
2. Ponlo en la raíz de tu proyecto
3. Añade en el `<head>`:

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
<!-- O si es PNG -->
<link rel="icon" href="favicon.png" type="image/png">
```

---

### 💡 Meta tags para compartir en redes

Añade esto en el `<head>` para que se vea bien al compartir:

```html
<!-- Descripción para Google -->
<meta name="description" content="Portfolio de Juan García - Desarrollador Web">

<!-- Open Graph (Facebook, LinkedIn, WhatsApp) -->
<meta property="og:title" content="Portfolio de Juan García">
<meta property="og:description" content="Desarrollador Web especializado en HTML, CSS y JavaScript">
<meta property="og:image" content="https://tu-web.netlify.app/img/preview.jpg">
<meta property="og:url" content="https://tu-web.netlify.app">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
```

---

### 💡 Dominio personalizado (opcional)

Si quieres un dominio propio como `www.tuportfolio.com`:

1. Compra un dominio en Namecheap, GoDaddy, etc. (~10-15€/año)
2. En Netlify: **Domain settings → Add custom domain**
3. Sigue las instrucciones para configurar DNS

---

## 📱 Verificar en móvil

Una vez publicada, **prueba tu web en el móvil**:

1. Abre la URL en tu smartphone
2. Verifica que:
   - ☐ El texto se lee bien
   - ☐ Las imágenes cargan
   - ☐ El menú funciona
   - ☐ Los botones se pueden pulsar
   - ☐ El formulario funciona

---

## 🎉 ¡Felicidades!

Ya tienes tu primera web publicada en Internet. Ahora puedes:

- 📧 **Compartir la URL** en tu CV
- 💼 **Añadirla a LinkedIn**
- 📱 **Enviarla por WhatsApp**
- 🐦 **Compartirla en redes sociales**

---

## 📚 Resumen rápido (Chuleta)

```
1. Prepara tu proyecto (index.html en la raíz)
2. Ve a https://app.netlify.com
3. Crea cuenta (GitHub o email)
4. Arrastra tu carpeta a la zona de deploy
5. ¡Listo! Tu web está online
6. (Opcional) Cambia el nombre del subdominio
7. Para actualizar: arrastra la carpeta de nuevo
```

---

## 🆘 ¿Necesitas ayuda?

Si algo no funciona:

1. **Revisa la consola** del navegador (F12)
2. **Verifica las rutas** de archivos
3. **Limpia la caché** (Ctrl+Shift+R)
4. **Pregunta a la IA** copiando el error exacto

---

**¡Mucha suerte con tu proyecto!** 🚀

*Guía creada para el Curso de Iniciación al Desarrollo Web*
