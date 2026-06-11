# 🚀 Clase 15 de Python – Introducción a Django (MVT, URLs, Templates, Modelos y Admin)

**Autor:** Joaquín Rodríguez – [https://clasesonlinejoaquin.es/](https://clasesonlinejoaquin.es/)  
**Objetivo global:** que puedas levantar un proyecto Django funcional en una sesión, entendiendo el patrón **MVT (Model‑View‑Template)**, la configuración básica (`settings.py`), las **URLs y vistas**, los **templates**, los **modelos + migraciones** y el **panel de administración**, siguiendo el mismo estilo didáctico que el resto del curso (Better Comments, ZONA DEL ALUMNO, laboratorio IA y autoevaluación).

---

## 🤔 Cómo usar este material

1. Avanza sección por sección: objetivos → teoría clara → demo → TODO.  
2. Ejecuta exactamente los comandos indicados en PowerShell/terminal.  
3. Copia/pega los fragmentos de código en tu proyecto Django (o combina con `15_django_tutorial.py`).  
4. Completa las **ZONAS DEL ALUMNO** antes de pasar a la siguiente sección.  
5. Cierra con la **Autoevaluación** para integrar todo.

> **Tip docente:** mantén una ventana con `python manage.py runserver` y otra con el editor. Django recarga automáticamente cuando guardas.

---

## ⚙️ Instalación rápida (Windows / macOS / Linux)

```powershell
python -m venv env
.\env\Scripts\activate      # macOS/Linux: source env/bin/activate
pip install django
python -c "import django; print(django.get_version())"
```

> **Flask vs Django (resumen):** Flask es un “micro” framework muy flexible; tú decides qué añadir. Django viene con “baterías incluidas”: ORM, panel de admin, sistema de templates, autenticación, etc. Esta unidad se centra en **Django** como framework completo para proyectos medianos/grandes.

---

## 🗺️ Mapa del temario

1. Crear proyecto y app (`startproject`, `startapp`)  
2. Configuración mínima (`settings.py`, idioma, zona horaria, apps)  
3. URLs y vistas con `HttpResponse`  
4. Templates y `render()`  
5. Modelos y migraciones (ORM de Django)  
6. Panel de administración  
7. Laboratorio IA (Prompt Kit)  
8. Autoevaluación final + rúbrica  
9. Apéndices: estructura de proyecto, comandos clave, errores comunes

---

## SECCIÓN 1 · Crear proyecto y app

### 🎯 Objetivos
- Entender qué generan `django-admin startproject` y `python manage.py startapp`.  
- Arrancar el servidor de desarrollo y ver la pantalla inicial de Django.

### 📚 Teoría en claro
- `startproject` crea el esqueleto principal: configuración, URLs de nivel proyecto, etc.  
- `startapp` crea una “mini‑aplicación” reutilizable: vistas, modelos, tests, admin.  
- En proyectos reales tendrás varias apps (ej. `alumnos`, `cursos`, `blog`).

### 🧪 Demo guiada

```powershell
django-admin startproject campus_django
cd campus_django
python manage.py startapp alumnos
python manage.py runserver   # http://127.0.0.1:8000/
```

### ✅ ZONA DEL ALUMNO · TODO
- Repite los comandos con **tus** nombres (por ejemplo, proyecto `gestor_clases` y app `cursos`).  
- Anota qué archivos y carpetas aparecieron.  
- Haz una captura o descripción de la página inicial de Django (el cohete).

---

## SECCIÓN 2 · Configuración mínima (`settings.py`)

### 🎯 Objetivos
- Registrar tu app en `INSTALLED_APPS`.  
- Ajustar idioma (`LANGUAGE_CODE`) y zona horaria (`TIME_ZONE`).  
- Recordar el papel de `DEBUG`, `ALLOWED_HOSTS` y `STATIC_URL`.

### 📚 Teoría en claro
- `INSTALLED_APPS` indica qué apps están activas (sin estar ahí, Django ignora sus modelos).  
- `LANGUAGE_CODE` y `TIME_ZONE` afectan a formatos de fecha/hora y mensajes.  
- `DEBUG=True` solo en desarrollo; en producción debe ser `False`.  
- `ALLOWED_HOSTS` lista los dominios válidos cuando `DEBUG=False`.

### 🧪 Demo guiada

```python
# campus_django/settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "alumnos",  # ← tu app
]

LANGUAGE_CODE = "es-es"
TIME_ZONE = "Europe/Madrid"
```

### ✅ ZONA DEL ALUMNO · TODO
- Añade tu app a `INSTALLED_APPS`.  
- Configura idioma y zona horaria de tu zona.  
- Ejecuta `python manage.py check` y deja anotado si hay advertencias/errores.  
- Añade un comentario en el código tipo `# TODO: configurar STATICFILES_DIRS si usamos assets propios`.

---

## SECCIÓN 3 · URLs y vistas (HttpResponse)

### 🎯 Objetivos
- Crear tus primeras vistas como funciones (FBV: Function‑Based Views).  
- Mapear URLs con `path()` y parámetros dinámicos.

### 📚 Teoría en claro
- Cada vista recibe un `request` y devuelve una respuesta (`HttpResponse`, `render`, `JsonResponse`, etc.).  
- `urls.py` de proyecto es la “tabla de rutas” principal.  
- Puedes importar vistas desde tus apps para asignarlas a rutas específicas.

### 🧪 Demo guiada

```python
# alumnos/views.py
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido al portal de alumnos</h1>")

def saluda(request, nombre):
    return HttpResponse(f"<p>Hola, {nombre}. Listo para aprender Django.</p>")
```

```python
# campus_django/urls.py
from django.contrib import admin
from django.urls import path
from alumnos import views as alumnos_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", alumnos_views.inicio, name="inicio"),
    path("saluda/<str:nombre>/", alumnos_views.saluda, name="saluda"),
]
```

### ✅ ZONA DEL ALUMNO · TODO
- Crea una vista `acerca` que muestre un pequeño texto sobre el curso.  
- Añade la ruta `/acerca/` apuntando a esa vista.  
- Crea una ruta `curso/<int:id>/` con una vista que devuelva el ID recibido.  
- Documenta con comentarios qué parámetros usas (`<str:nombre>`, `<int:id>`, etc.).

---

## SECCIÓN 4 · Templates y `render()`

### 🎯 Objetivos
- Configurar una carpeta de templates compartidos.  
- Renderizar HTML con variables y bucles.

### 📚 Teoría en claro
- Un template es HTML con “huecos” (`{{ variable }}`) y estructuras (`{% for %}`, `{% if %}`).  
- `render(request, "archivo.html", contexto)` combina el template con datos y lo devuelve.  
- Puedes tener templates globales (`templates/`) y específicos de app (`alumnos/templates/alumnos/`).

### 🧪 Demo guiada

```python
# settings.py
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]
```

Estructura:

```
templates/
└── inicio.html
```

```html
<!-- templates/inicio.html -->
<!doctype html>
<html lang="es">
  <head><meta charset="utf-8"><title>Campus Django</title></head>
  <body>
    <h1>{{ titulo }}</h1>
    <p>Alumnos activos: {{ total_alumnos }}</p>
    <ul>
      {% for nombre in alumnos %}
        <li>{{ nombre }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

```python
# alumnos/views.py
from django.shortcuts import render

def inicio(request):
    contexto = {
        "titulo": "Panel de alumnos",
        "alumnos": ["Ana", "Luis", "Marcos"],
        "total_alumnos": 3,
    }
    return render(request, "inicio.html", contexto)
```

### ✅ ZONA DEL ALUMNO · TODO
- Crea `inicio.html` y `about.html`.  
- En `about.html`, muestra tu nombre, el nombre del curso y el año.  
- Añade un comentario de template `{% comment %} TODO: añadir enlaces a redes {% endcomment %}`.  
- Cambia la vista `acerca` para usar `render()` en lugar de `HttpResponse`.

---

## SECCIÓN 5 · Modelos y migraciones (ORM)

### 🎯 Objetivos
- Definir un modelo con `models.Model`.  
- Generar y aplicar migraciones (`makemigrations` y `migrate`).  
- Crear registros desde la shell.

### 📚 Teoría en claro
- Un modelo es una representación en Python de una tabla de base de datos.  
- El ORM genera SQL por ti, evitando que tengas que escribir consultas a mano.  
- Cada cambio en modelos → nueva migración → `migrate`.

### 🧪 Demo guiada

```python
# alumnos/models.py
from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({'Activo' if self.esta_activo else 'Inactivo'})"
```

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

```python
from alumnos.models import Alumno
Alumno.objects.create(nombre="Ana", email="ana@test.com")
Alumno.objects.filter(esta_activo=True)
```

### ✅ ZONA DEL ALUMNO · TODO
- Crea un modelo `Curso` con: `titulo`, `descripcion`, `duracion_horas`, `nivel`, `esta_activo`.  
- Genera migraciones y aplícalas.  
- Desde la shell, crea al menos 2 cursos y recupera solo los activos.  
- Añade un método `__str__` legible para `Curso`.

---

## SECCIÓN 6 · Panel de administración

### 🎯 Objetivos
- Crear un superusuario.  
- Registrar tus modelos en el admin.  
- Personalizar columnas y filtros básicos.

### 📚 Teoría en claro
- El admin de Django es una herramienta de backoffice gratuita que viene “de serie”.  
- Registrar un modelo permite gestionarlo (crear, editar, borrar) desde la web.  
- `list_display`, `search_fields` y `list_filter` mejoran mucho la usabilidad.

### 🧪 Demo guiada

```powershell
python manage.py createsuperuser
```

```python
# alumnos/admin.py
from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "esta_activo", "fecha_registro")
    search_fields = ("nombre", "email")
    list_filter = ("esta_activo",)
```

Visita `http://127.0.0.1:8000/admin/`, entra con tus credenciales y localiza el modelo.

### ✅ ZONA DEL ALUMNO · TODO
- Registra también el modelo `Curso` con `list_display` (`titulo`, `nivel`, `esta_activo`).  
- Añade `search_fields = ("titulo",)` y `list_filter = ("nivel", "esta_activo")`.  
- Escribe un pequeño texto para el alumno explicando por qué el admin es tan útil en proyectos reales.

---

## SECCIÓN 7 · Laboratorio IA (Prompt Kit)

### 🎯 Objetivos
- Aprender a pedir a la IA mini‑proyectos Django que puedas integrar.  
- Mejorar tus prompts para que sean cortos, claros y ejecutables.

### 🧰 Prompt Kit sugerido

1. **Generación – Blog básico**
   > “Eres profesor de Django. Crea una app `blog` con modelo `Entrada(titulo, cuerpo, publicado_el)` y vistas de lista/detalle. Usa templates sencillos y comentarios tipo Better Comments. Devuélveme solo código Python y HTML.”

2. **Mejora – Formularios**
   > “Amplía el ejemplo anterior creando un `ModelForm` para crear nuevas entradas desde una vista `/blog/nueva/`. Valida que el título tenga al menos 10 caracteres y muestra mensajes de error legibles.”

3. **Extensión – API JSON**
   > “Añade una vista que responda en `/api/entradas/` devolviendo JSON con las últimas 5 entradas publicadas. Usa `JsonResponse` y documenta el formato devuelto con comentarios.”

### ✅ ZONA DEL ALUMNO · TODO
- Elige uno de los prompts, pide el código a la IA y pégalo en tu proyecto (o en la zona IA del `.py`).  
- Ajusta nombres de variables y mensajes para que encajen con tu curso.  
- Escribe una mini reflexión (3–5 líneas) sobre qué has entendido del código generado.

---

## SECCIÓN 8 · Autoevaluación final

### 🎯 Objetivos
- Integrar MVT, admin y API en una mini app `cursos`.  
- Practicar lectura/interpretación de código Django.

### 📝 Tareas
1. Crea una app `cursos` y añádela a `INSTALLED_APPS`.  
2. Modelo `Curso`: `titulo`, `categoria`, `duracion_horas`, `esta_activo`, `fecha_creacion`.  
3. Vista `listar_cursos` que use un template con tarjetas para cada curso.  
4. Vista `detalle_curso` en `/cursos/<int:id>/`.  
5. Endpoint `/api/cursos/` (solo GET) que devuelva JSON con los cursos activos.  
6. Registra `Curso` en el admin con columnas, búsquedas y filtros.  
7. Muestra en alguna parte un resumen: `Cursos activos: X | Última alta: AAAA‑MM‑DD`.  
8. Usa un prompt IA para añadir una pequeña mejora (filtros por categoría, buscador, etc.).

### 📏 Rúbrica rápida
- **Correcto:** el proyecto arranca, las rutas funcionan, modelos migrados y admin operativo.  
- **Excelente:** API JSON clara, validaciones de datos, comentarios Better Comments, prompt IA aplicado y documentado.

---

## APÉNDICE A · Anatomía de un proyecto Django

```text
campus_django/
├── manage.py
├── campus_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py / wsgi.py
├── alumnos/
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── tests.py
└── templates/
    └── ...
```

---

## APÉNDICE B · Comandos clave

| Comando                          | Descripción                         |
|----------------------------------|-------------------------------------|
| `python manage.py runserver`     | Inicia el servidor local            |
| `python manage.py startapp app`  | Crea una nueva app                  |
| `python manage.py makemigrations`| Genera migraciones                  |
| `python manage.py migrate`       | Aplica migraciones                  |
| `python manage.py shell`         | Abre shell con Django cargado       |
| `python manage.py createsuperuser`| Crea usuario para el admin         |

---

## APÉNDICE C · Errores frecuentes (y solución rápida)

- **`ModuleNotFoundError: No module named 'alumnos'`**  
  → Revisa que la app esté en `INSTALLED_APPS` y el import sea correcto.

- **`TemplateDoesNotExist`**  
  → Asegúrate de que la ruta del template es correcta y que `TEMPLATES[0]["DIRS"]` incluye tu carpeta.

- **`no such table` / `OperationalError`**  
  → Falta ejecutar `makemigrations` y `migrate` después de crear o modificar modelos.

- **`CSRF verification failed`**  
  → Los formularios POST necesitan `{% csrf_token %}` dentro de `<form>`.

- **`DisallowedHost`**  
  → Añade tu dominio o `localhost` a `ALLOWED_HOSTS` (en desarrollo puedes usar `["*"]`).

---

## 🎉 Qué has aprendido

- Levantar un proyecto Django desde cero y registrar apps.  
- Crear vistas, URLs y templates para mostrar información dinámica.  
- Definir modelos con el ORM, migrarlos y operar con ellos desde la shell.  
- Configurar y aprovechar el panel de administración.  
- Diseñar prompts IA que generen código Django útil y didáctico.  
- Integrar todo en una mini app tipo “cursos” coherente con el resto de tu Curso Python.

> **Siguiente paso sugerido:** conectar Django con una base de datos externa (por ejemplo PostgreSQL) o preparar una segunda unidad centrada en Django REST Framework para APIs más avanzadas.

---

