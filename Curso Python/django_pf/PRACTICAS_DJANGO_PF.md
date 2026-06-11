# 🧪 PRÁCTICAS GUIADAS – Django Proyecto Fácil (`django_pf`)

Autor: Joaquín | Web: https://clasesonlinejoaquin.es/

---

## 📚 Índice de prácticas

1. [Configuración inicial](#configuración-inicial)
2. [Práctica 1: Rutas básicas](#práctica-1-rutas-básicas)
3. [Práctica 2: Rutas con parámetros](#práctica-2-rutas-con-parámetros)
4. [Práctica 3: Formularios POST](#práctica-3-formularios-post)
5. [Práctica 4: Query strings (GET)](#práctica-4-query-strings-get)
6. [Práctica 5: API JSON](#práctica-5-api-json)
7. [Práctica 6: Middleware y errores](#práctica-6-middleware-y-errores)
8. [Retos avanzados](#retos-avanzados)

---

## Configuración inicial

### Paso 1: Crear entorno virtual

```bash
python -m venv env
```

### Paso 2: Activar (Windows)

```bash
.\env\Scripts\activate
```

En macOS/Linux:

```bash
source env/bin/activate
```

### Paso 3: Instalar Django

```bash
pip install django
```

### Paso 4: Entrar en la carpeta del proyecto

```bash
cd "cursos/Curso Python/django_pf"
```

### Paso 5: Ejecutar el servidor

```bash
python manage.py runserver
```

Abre en el navegador:

```text
http://127.0.0.1:8000/
```

---

## Práctica 1: Rutas básicas

### 🎯 Objetivo

Entender cómo Django mapea URLs a funciones Python (vistas).

### 🔍 Tarea

1. Visita `http://127.0.0.1:8000/`
   - ¿Qué vista se ejecuta? (Mira `core/urls.py` y `core/views.py`).
   - ¿Qué plantilla se renderiza?

2. Visita `http://127.0.0.1:8000/about/`
   - ¿En qué se diferencia esta vista de la anterior?
   - ¿Qué título aparece en la página?

3. **Añade una nueva ruta** en `core/views.py`:

   ```python
   def contacto(request):
       """Página de contacto muy sencilla."""
       return HttpResponse(
           "<h1>Contacto</h1>"
           "<p>Email: hola@clasesonlinejoaquin.es</p>"
           '<a href="/">Volver</a>'
       )
   ```

4. Registra la ruta en `core/urls.py`:

   ```python
   path("contacto/", views.contacto, name="contacto"),
   ```

5. Recarga el servidor y visita `http://127.0.0.1:8000/contacto/`.

✅ **Éxito si**: ves tu página de contacto personalizada.

---

## Práctica 2: Rutas con parámetros

### 🎯 Objetivo

Recibir valores dinámicos en la URL y usarlos en la respuesta.

### 🔍 Tarea

1. Visita `http://127.0.0.1:8000/saluda/Juan/`
   - Cambia `Juan` por tu nombre.
   - ¿Ves el cambio en la respuesta?

2. Visita `http://127.0.0.1:8000/suma/10/20/`
   - ¿Cuál es el resultado?
   - Prueba con otros números.

3. **Crea una nueva ruta tipada** en `core/views.py`:

   ```python
   def precio_con_descuento(request, monto: float) -> HttpResponse:
       """Calcula un 10% de descuento sobre el monto."""
       descuento = monto * 0.10
       final = monto - descuento
       return HttpResponse(
           f"<h2>Precio original: {monto:.2f}</h2>"
           f"<p>Descuento 10%: {descuento:.2f}</p>"
           f"<strong>Precio final: {final:.2f}</strong>"
       )
   ```

4. Registra la ruta:

   ```python
   path("precio/<float:monto>/", views.precio_con_descuento, name="precio"),
   ```

5. Prueba con `http://127.0.0.1:8000/precio/99.99/`.

✅ **Éxito si**: ves los cálculos de descuento en HTML.

---

## Práctica 3: Formularios POST

### 🎯 Objetivo

Procesar formularios HTML enviados por POST y devolver una vista de resultado.

### 🔍 Tarea

1. En `index.html`, localiza el formulario que envía a `{% url 'core:procesar' %}`.
   - ¿Tiene `{% csrf_token %}`?
   - ¿Qué campo de formulario envía?

2. En `core/views.py`, abre la vista `procesar`:
   - ¿Qué comprueba antes de procesar?
   - ¿Qué pasa si el método no es POST?

3. **Amplía el formulario**:
   - Añade campos `email` y `edad` en `index.html`.
   - En la vista `procesar`:
     - Lee esos campos con `request.POST`.
     - Valida que `email` no esté vacío.
     - Valida que `edad` sea un entero > 0 (usa `int()` y controla errores).

4. Muestra los nuevos datos en `resultado.html`.

✅ **Éxito si**: al enviar el formulario, ves nombre, email y edad validados en la página de resultado.

---

## Práctica 4: Query strings (GET)

### 🎯 Objetivo

Usar `request.GET` para leer parámetros que llegan tras el `?` en la URL.

### 🔍 Tarea

1. Visita `http://127.0.0.1:8000/buscar/?q=django&page=1`.
   - Abre DevTools → pestaña Network → mira la respuesta JSON.

2. Cambia `q` y `page` en la URL y observa cómo cambia la respuesta.

3. **Amplía la vista `buscar`**:
   - Añade parámetro opcional `lang` (`es`, `en`, etc.).
   - Devuélvelo también en el JSON (`"lang": "es"` por defecto).

4. Añade una validación:
   - Si `page <= 0`, fuerza `page = 1` y añade un campo `"warning": "Página corregida a 1"`.

✅ **Éxito si**: el JSON refleja `q`, `page` corregida y `lang`.

---

## Práctica 5: API JSON

### 🎯 Objetivo

Trabajar con `JsonResponse` y body JSON en peticiones POST.

### 🔍 Tarea

1. Prueba `GET /api/echo/?q=hola` y `GET /api/health/`.
   - Observa los JSON devueltos.

2. Para `api_calculadora`, prueba:
   - `/api/calculadora/suma/3/5/`
   - `/api/calculadora/divide/10/0/`
   - `/api/calculadora/xyz/3/5/`
   - ¿Qué códigos HTTP y mensajes ves?

3. **Prueba `api_saludo` con POST JSON**:
   - Usa una herramienta tipo Thunder Client, Insomnia, Postman o el propio DevTools (Fetch/XHR).
   - Envía `{"nombre": "Ada"}` en el body y `Content-Type: application/json`.
   - Comprueba el mensaje de éxito.

4. **Modifica `api_saludo`**:
   - Añade campo opcional `edad` (int).
   - Si `edad` < 0 o no es un número, devuelve error 400 con mensaje adecuado.
   - En el saludo, incluye también la edad si es válida.

✅ **Éxito si**: manejas bien errores 400 y 405, y `api_saludo` devuelve un JSON claro y validado.

---

## Práctica 6: Middleware y errores

### 🎯 Objetivo

Entender cómo funciona el middleware personalizado y los manejadores de error.

### 🔍 Tarea

1. Abre `core/middleware.py` y lee los comentarios de `RequestLogMiddleware`.
   - ¿Qué hace en `process_request`?
   - ¿Qué añade en `process_response`?

2. Con el servidor en marcha y `DEBUG=True`, visita varias rutas:
   - Observa en la consola los logs `[middleware] MÉTODO RUTA`.

3. Abre DevTools → pestaña Network → selecciona una petición.
   - En **Headers**, busca `X-Response-Time-ms`, `X-Ejemplo` y `X-Author`.

4. Visita:
   - `/ruta-que-no-existe/` → debe lanzar 404.
   - `/error-intencional/` → debe provocar un 500.

5. **Activa `DEBUG=False` (solo para probar)**:
   - Cambia en `djpf/settings.py`: `DEBUG = False`.
   - Añade temporalmente `ALLOWED_HOSTS = ["127.0.0.1", "localhost"]`.
   - Reinicia el servidor.
   - Vuelve a probar 404 y 500 y observa los JSON de `error_404` y `error_500`.

✅ **Éxito si**: entiendes qué parte del flujo pasa por el middleware y qué pasa cuando ocurre un 404/500.

---

## Retos avanzados

1. **Modelo `Curso` + listado HTML**
   - Crea un modelo `Curso` con `titulo`, `duracion_horas`, `nivel`, `activo`.
   - Ejecuta migraciones.
   - Crea una vista y template que liste cursos reales desde la BD.

2. **API `/api/cursos/`**
   - Crea un endpoint que devuelva los cursos activos en JSON.
   - Añade validaciones y un filtro por `nivel` usando query string.

3. **Protege una ruta con sesión**
   - Crea una vista `/panel/` que solo se muestre si hay una variable de sesión `is_admin = True`.
   - Si no, redirige a `/`.

4. **Tests**
   - Usa `pytest` o `unittest` para probar:
     - `/buscar/`
     - `/api/echo/`
     - `/api/calculadora/...`

5. **Comparativa Flask vs Django**
   - Elige una ruta o API (por ejemplo `/api/echo/`) y escribe en 5–6 líneas:
     - Cómo está hecha en Flask.
     - Cómo está hecha en Django.
     - Ventajas o inconvenientes que ves en cada caso.

---

Usa estas prácticas como “guion de laboratorio” para clase.  
Puedes marcar cada sección como completada y añadir más retos según el nivel del grupo. 💻📘

