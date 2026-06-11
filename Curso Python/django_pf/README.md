# Django Proyecto Fácil Completo (paralelo a `flask_proyecto_didactico`)

Guía didáctica para entender y extender una mini app Django con rutas, plantillas, formularios y API JSON. Es la “hermana” en Django de `flask_proyecto_didactico`: misma idea, pero usando el framework Django y el patrón **MVT (Model‑View‑Template)**.

---

## 1️⃣ Objetivo del proyecto

- Ver en un solo sitio:
  - Rutas y vistas (`urls.py` + `views.py`)
  - Templates con herencia (`base.html` + `index.html` + `about.html` + `resultado.html`)
  - Formularios POST y lectura de datos (`request.POST`)
  - Query strings GET (`request.GET`)
  - Endpoints de API JSON (`JsonResponse`)
  - Manejo básico de errores (404, 500)
  - Middleware tipo “before/after request”
- Usar comentarios estilo **Better Comments** (`# !`, `# *`, `# ?`, `# TODO`) en el código para seguir el flujo rápidamente.
- Servir como base para prácticas: desde nivel básico hasta intermedio (rutas, ORM, tests, despliegue).

---

## 2️⃣ ¿Qué deberías conocer antes?

- Python básico (funciones, módulos, diccionarios, listas).
- Haber visto el proyecto `flask_proyecto_didactico` ayuda a comparar mentalmente Flask vs Django.
- Conceptos mínimos de web:
  - HTTP (GET, POST)  
  - URL, ruta, query string  
  - Qué es JSON (`{"campo": "valor"}`)

---

## 3️⃣ Requisitos y stack

- Python 3.10+ y `pip`.
- Dependencias:
  - `django` (framework principal)
  - Opcional: `gunicorn` para despliegue.
- Base de datos:
  - SQLite (lista por defecto en `djpf/settings.py`; en este proyecto se usa solo como ejemplo).

---

## 4️⃣ Estructura de carpetas y archivos

Raíz del proyecto Django:

- `manage.py`  
  - Script de línea de comandos de Django.  
  - Úsalo para `runserver`, `migrate`, `createsuperuser`, etc.

- Carpeta `djpf/` (configuración del proyecto)
  - `djpf/settings.py`  
    - Configuración principal: `SECRET_KEY`, `DEBUG`, `INSTALLED_APPS`, `MIDDLEWARE`, `TEMPLATES`, `DATABASES`, etc.  
    - MUY comentado para usar en clase (ver secciones con `# !` y `# *`).
  - `djpf/urls.py`  
    - Enrutador raíz: incluye `core.urls` y registra los manejadores de error `handler404` y `handler500`.
  - `djpf/wsgi.py`  
    - Punto de entrada WSGI (servidores como `gunicorn`).
  - `djpf/asgi.py`  
    - Punto de entrada ASGI (servidores async como `uvicorn`).

- Carpeta `core/` (app principal del proyecto)
  - `core/apps.py`  
    - Configuración de la app (nombre, `verbose_name`).
  - `core/views.py`  
    - Vistas HTML (`inicio`, `about`, `procesar`) y vistas API JSON (`api_echo`, `api_saludo`, `api_health`, `api_calculadora`).  
    - Manejadores de errores `error_404`, `error_500` y vista `error_intencional`.  
    - Todo muy comentado con Better Comments.
  - `core/urls.py`  
    - Rutas de la app (`/`, `/about/`, `/procesar/`, `/saluda/<nombre>/`, `/suma/<int:a>/<int:b>/`, `/buscar/`, `/api/...`).
  - `core/middleware.py`  
    - Middleware didáctico `RequestLogMiddleware` que:
      - Imprime logs de cada petición (método + ruta) cuando `DEBUG=True`.
      - Mide el tiempo de respuesta (`X-Response-Time-ms`).
      - Añade cabeceras `X-Ejemplo` y `X-Author`.

- Carpeta `core/templates/` (templates HTML)
  - `base.html`  
    - Layout general con navbar, Bootstrap y bloque `{% block content %}`.
  - `index.html`  
    - Página principal con formulario, rutas con parámetros, query strings, enlaces a API y sección de errores.
  - `resultado.html`  
    - Muestra el nombre enviado en el formulario POST.
  - `about.html`  
    - Explica la estructura del proyecto y próximos pasos.

---

## 5️⃣ Puesta en marcha rápida (entorno local)

```bash
cd "cursos/Curso Python/django_pf"

# 1) Crear y activar entorno virtual
python -m venv env
.\env\Scripts\activate        # Windows
# source env/bin/activate     # macOS/Linux

# 2) Instalar dependencias
pip install django

# 3) Lanzar servidor de desarrollo
python manage.py runserver
```

Abre en el navegador: <http://127.0.0.1:8000/>

Si todo va bien, verás la página de inicio con el formulario y las tarjetas de ejemplo.

---

## 6️⃣ Flujo simplificado de la app

1. El usuario visita `/` → `core.views.inicio` renderiza `index.html`.  
2. Envía el formulario a `/procesar/` (POST) → `core.views.procesar`:
   - Valida el nombre.
   - Redirige si está vacío.
   - Si es válido, muestra `resultado.html`.  
3. Rutas con parámetros (`/saluda/<nombre>/`, `/suma/<int:a>/<int:b>/`) muestran resultados en HTML.  
4. Endpoints de API JSON:
   - `/buscar/?q=valor&page=n` → devuelve `{"ok": true, "q": ..., "page": ..., "total_results": 42}`.  
   - `/api/echo/?q=hola` → devuelve `{"ok": true, "echo": "hola"}`.  
   - `/api/saludo/` (POST JSON) → procesa `{ "nombre": "Ada" }` y responde con saludo o error 400.  
   - `/api/health/` → `{ "status": "ok" }`.  
   - `/api/calculadora/<operacion>/<int:a>/<int:b>/` → suma, resta, multiply, divide (400 si operación inválida o división por cero).  
5. El middleware `RequestLogMiddleware` envuelve todas las peticiones:
   - Mide tiempo y añade cabeceras.
   - Imprime un log en consola para cada petición cuando `DEBUG=True`.  
6. Los errores 404/500 (cuando `DEBUG=False`) pasan por `error_404` y `error_500` en `core.views`, que devuelven JSON.

---

## 7️⃣ Rutas HTML principales (resumen)

- `/` → Home con formulario y enlaces de práctica.  
- `/about/` → Explica la estructura de la app.  
- `/procesar/` (POST) → Recibe nombre, valida y responde.  
- `/saluda/<nombre>/` → Parámetro en la URL, devuelve saludo.  
- `/suma/<int:a>/<int:b>/` → Parámetros tipados (int), devuelve HTML con el resultado.

---

## 8️⃣ Endpoints de API JSON

- `GET /buscar/?q=valor&page=n`  
  → JSON con `q`, `page` y `total_results`.  
- `GET /api/echo/?q=hola`  
  → JSON con `{"ok": true, "echo": "hola"}`.  
- `POST /api/saludo/` con body JSON `{"nombre": "Ada"}`  
  → Si es correcto: `{"ok": true, "mensaje": "...", "status": "success"}`  
  → Si falta `nombre` o el JSON es inválido: 400 con `{"ok": false, "error": "..."}`.  
- `GET /api/health/`  
  → `{"status": "ok"}`.  
- `GET /api/calculadora/<operacion>/<int:a>/<int:b>/`  
  → `{"ok": true, "resultado": ...}` o 400 si la operación no existe / división por cero.

---

## 9️⃣ Middleware y errores

- `core.middleware.RequestLogMiddleware`:
  - Usa `process_request` para:
    - Imprimir `[middleware] MÉTODO RUTA` en consola (si `DEBUG=True`).
    - Guardar la hora de inicio de la petición.
  - Usa `process_response` para:
    - Calcular el tiempo de respuesta y añadir la cabecera `X-Response-Time-ms`.
    - Añadir cabeceras `X-Ejemplo` y `X-Author`.

- Manejadores de error:
  - `error_404` → JSON con mensaje de ruta no encontrada.  
  - `error_500` → JSON con mensaje de error interno.  
  - `error_intencional` → vista que lanza una excepción para probar el 500.

---

## 🔟 Ideas de ejercicios (para clase o deberes)

### Básico
- Modifica el formulario para pedir también email y edad; valida que:
  - email no esté vacío.
  - edad sea un número entero > 0.  
- En `/buscar/`, añade un parámetro opcional `lang` y devuélvelo en el JSON.  
- En `/api/echo/`, añade la hora del servidor (`datetime.now().isoformat()`).

### Intermedio
- Añade un modelo `Curso` con campos `titulo`, `duracion_horas`, `nivel`, `activo` y crea:
  - Vista que liste cursos desde la base de datos.
  - Endpoint `/api/cursos/` que devuelva JSON con los cursos activos.  
- Introduce autenticación:
  - Protege una ruta (`/panel/`) para que solo usuarios logueados la vean.  
- Añade un sistema de “contador de visitas” usando sesiones.

### Avanzado
- Escribe tests para la API con `pytest` o `unittest`.  
- Prepara despliegue:
  - Crea `requirements.txt`.  
  - Configura `gunicorn djpf.wsgi:application`.  
- Compara el código de este proyecto con `flask_proyecto_didactico`:
  - ¿Qué piezas están en los dos?
  - ¿Qué tareas simplifica Django respecto a Flask?

---

## 1️⃣1️⃣ Siguiente paso recomendado

Cuando domines este proyecto:

- Salta a la unidad `15_django_tutorial.py` para ver un tutorial de Django “en un solo archivo” dentro del Curso Python.  
- O bien, amplía este proyecto añadiendo modelos, panel de administración y alguna pequeña app extra (blog, tareas, etc.).

Usa este README como mapa general y el código comentado como guion de explicación en clase.  
Dale tu propio estilo y anima a tus alumnos a modificarlo sin miedo. 💻📚

