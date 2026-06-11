# =========================================================================================
#  🚀 PYTHON CLASE 15 – DJANGO EN UN SOLO ARCHIVO (MVT básico + URLs + Templates + API)
# =========================================================================================
#  🎯 En esta sesión practicarás:
#     * Qué es Django y en qué se diferencia de Flask
#     * Cómo funciona el patrón MVT (Model–View–Template) en la práctica
#     * Cómo configurar Django “a mano” en un archivo único (settings + URLs)
#     * Cómo definir rutas y vistas (incluyendo parámetros dinámicos en la URL)
#     * Cómo renderizar templates con datos reales y devolver HTML
#     * Cómo exponer una pequeña API JSON de cursos
#     * Cómo usar ZONAS DEL ALUMNO y un Laboratorio IA para extender el código
#
#  🧠 Mini‑teoría: ¿qué es Django?
#     - Es un framework web de alto nivel para Python, pensado para ir “de cero
#       a producción” con muchas piezas integradas: ORM, templates, admin, auth…
#     - Sigue el patrón MVT:
#         * Model    → capa de datos (tablas representadas como clases Python)
#         * View     → lógica de negocio (funciones/clases que preparan datos)
#         * Template → capa de presentación (HTML con variables y estructuras)
#     - Comparado con Flask:
#         * Flask es micro; tú eliges qué piezas añadir.
#         * Django viene con “baterías incluidas” para proyectos medianos/grandes.
#
#  ✅ Better Comments (mismo convenio que el resto del curso):
#     # ! importante   ·   # * definición/foco   ·   # ? idea/nota
#     # TODO: práctica  ·   # NOTE: apunte útil   ·   # // deprecado
# =========================================================================================

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Dict, List

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import path

# =========================================================================================
#  CONFIGURACIÓN GLOBAL
# =========================================================================================
# * Aquí definimos constantes y datos de ejemplo.
# * No estamos usando `django-admin startproject`, así que este archivo hace
#   el papel de:
#     - settings.py
#     - urls.py
#     - views.py
#   todo en uno, sólo para fines didácticos.

BASE_DIR = Path(__file__).resolve().parent
DEBUG_MODE = True
SECRET_KEY = "django-tutorial-ultra-secreto"  # ! Solo para demos en clase

# * Datos simulados (en un proyecto real vendrían del modelo/BD) -------------------------
ALUMNOS = ["Ana", "Luis", "Marcos"]

CURSOS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "titulo": "Fundamentos de Python",
        "duracion_horas": 20,
        "nivel": "Inicial",
        "activo": True,
    },
    {
        "id": 2,
        "titulo": "Automatización con Scripts",
        "duracion_horas": 15,
        "nivel": "Intermedio",
        "activo": True,
    },
    {
        "id": 3,
        "titulo": "APIs con Django",
        "duracion_horas": 18,
        "nivel": "Intermedio",
        "activo": False,
    },
]

# * Templates embebidos (loader en memoria) ----------------------------------------------
#   Normalmente los templates viven como archivos `.html` en una carpeta `templates/`.
#   Aquí usamos el loader de memoria (`locmem.Loader`) para guardar las plantillas en
#   un diccionario Python, de forma que este archivo sea autocontenido para clase.

INLINE_TEMPLATES: Dict[str, str] = {
    "inicio.html": """
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>Campus Django</title>
        <style>
          body { font-family: 'Segoe UI', sans-serif; margin: 2rem; }
          h1 { color: #0d6efd; }
        </style>
      </head>
      <body>
        <h1>{{ titulo }}</h1>
        <p>Alumnos activos: {{ total_alumnos }}</p>
        <ul>
          {% for alumno in alumnos %}
            <li>{{ alumno }}</li>
          {% endfor %}
        </ul>
        <p><a href="{% url 'acerca' %}">Acerca del curso</a></p>
        <p><a href="{% url 'cursos' %}">Ver lista de cursos</a></p>
      </body>
    </html>
    """,
    "acerca.html": """
    <!doctype html>
    <html lang="es">
      <head><meta charset="utf-8"><title>Acerca</title></head>
      <body>
        <h1>¿Por qué Django?</h1>
        <p>{{ mensaje }}</p>
        <p>Este tutorial vive en un solo archivo para enseñar la anatomía mínima.</p>
        <p>→ <a href="{% url 'inicio' %}">Volver al inicio</a></p>
      </body>
    </html>
    """,
    "cursos.html": """
    <!doctype html>
    <html lang="es">
      <head><meta charset="utf-8"><title>Cursos disponibles</title></head>
      <body>
        <h1>Cursos activos</h1>
        <ul>
          {% for curso in cursos %}
            <li>
              <strong>{{ curso.titulo }}</strong> · {{ curso.duracion_horas }} h ·
              {{ curso.nivel }}
              (<a href="{% url 'detalle_curso' curso.id %}">detalle</a>)
            </li>
          {% empty %}
            <li>No hay cursos activos aún.</li>
          {% endfor %}
        </ul>
        <p><a href="{% url 'inicio' %}">Inicio</a></p>
      </body>
    </html>
    """,
    "detalle.html": """
    <!doctype html>
    <html lang="es">
      <head><meta charset="utf-8"><title>Detalle curso</title></head>
      <body>
        <h1>{{ curso.titulo }}</h1>
        <p>Duración: {{ curso.duracion_horas }} horas</p>
        <p>Nivel: {{ curso.nivel }}</p>
        <p>Estado: {{ "Activo" if curso.activo else "Inactivo" }}</p>
        <p><a href="{% url 'cursos' %}">⟵ Volver a cursos</a></p>
      </body>
    </html>
    """,
}


def configure_django() -> None:
    """Configura `settings` para ejecutar Django en un solo archivo.

    En un proyecto creado con `django-admin startproject` tendríamos un
    `settings.py`. Aquí llamamos manualmente a `settings.configure(...)` para
    indicar:

      - DEBUG, SECRET_KEY, TIME_ZONE, LANGUAGE_CODE
      - INSTALLED_APPS con los componentes básicos de Django
      - MIDDLEWARE mínimo para sesiones, autenticación y protección CSRF
      - Sistema de plantillas con loader en memoria (INLINE_TEMPLATES)
      - Base de datos SQLite de ejemplo (DATABASES)
    """

    if settings.configured:
        return

    settings.configure(
        DEBUG=DEBUG_MODE,
        SECRET_KEY=SECRET_KEY,
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        LANGUAGE_CODE="es-es",
        TIME_ZONE="Europe/Madrid",
        USE_I18N=True,
        USE_TZ=True,
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
        ],
        MIDDLEWARE=[
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": False,
                "OPTIONS": {
                    "loaders": [
                        (
                            "django.template.loaders.locmem.Loader",
                            INLINE_TEMPLATES,
                        )
                    ]
                },
            }
        ],
        STATIC_URL="/static/",
        DEFAULT_AUTO_FIELD="django.db.models.AutoField",
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": str(BASE_DIR / "tutorial_django.sqlite3"),
            }
        },
    )


# =========================================================================================
#  SECCIÓN 1 – Vistas base (HTML simple)
# =========================================================================================
# * Teoría rápida:
#   - Una “vista” en Django es una función (o clase) que recibe un `HttpRequest`
#     y devuelve una `HttpResponse`.
#   - Aquí empezamos con dos vistas muy sencillas:
#       · `inicio`: prepara un contexto con datos y usa `render()` para devolver HTML.
#       · `acerca`: devuelve una página casi estática explicando el tutorial.
#   - Este patrón se repetirá en todo el proyecto:
#       datos → lógica en la vista → template → respuesta al navegador.


def inicio(request: HttpRequest) -> HttpResponse:
    """Página principal con datos simulados."""

    contexto = {
        "titulo": "Campus Django (demo en vivo)",
        "alumnos": ALUMNOS,
        "total_alumnos": len(ALUMNOS),
    }
    return render(request, "inicio.html", contexto)


def acerca(request: HttpRequest) -> HttpResponse:
    """Vista estática para explicar el propósito del tutorial."""

    return render(
        request,
        "acerca.html",
        {"mensaje": "Django integra MVT, admin y ORM en un solo framework."},
    )


# =========================================================================================
#  SECCIÓN 2 – Parámetros en URL + validaciones
# =========================================================================================
# * Teoría rápida:
#   - Las rutas pueden contener segmentos dinámicos:
#       /saluda/<str:nombre>/  → la parte entre <> se pasa como argumento a la vista.
#   - Tipos más usados:
#       <str:valor>, <int:id>, <slug:slug>, <path:ruta>
#   - Esto nos permite crear URLs legibles para detalles, filtros, etc.
#   - Introducimos también una validación manual: si no encontramos un curso,
#     devolvemos un 404 con un mensaje sencillo.


def saluda(request: HttpRequest, nombre: str) -> HttpResponse:
    """Devuelve un saludo personalizado usando parámetros en la URL."""

    return HttpResponse(f"<h2>Hola, {nombre}. ¡Bienvenido a Django!</h2>")


def detalle_curso(request: HttpRequest, curso_id: int) -> HttpResponse:
    """Muestra un curso buscando en la lista simulada."""

    curso = next((c for c in CURSOS if c["id"] == curso_id), None)
    if curso is None:
        return HttpResponse("<h2>Curso no encontrado</h2>", status=404)
    return render(request, "detalle.html", {"curso": curso})


# TODO: (ZONA DEL ALUMNO – RUTA EXTRA)
# 1. Crea una vista `estadisticas` que calcule:
#       - número total de cursos
#       - número de cursos activos
#       - media de horas de los cursos activos
# 2. Muestra los datos en HTML (HttpResponse o template nuevo).
# 3. Registra la ruta en urlpatterns (por ejemplo, "/estadisticas/").
# -----------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 – Listados HTML y API JSON
# =========================================================================================
# * Teoría rápida:
#   - Una misma fuente de datos puede presentarse como:
#       · HTML para humanos (`listar_cursos` + template `cursos.html`)
#       · JSON para otras aplicaciones (`api_cursos`)
#   - `JsonResponse` funciona como `HttpResponse`, pero:
#       · serializa automáticamente listas/dicts a JSON
#       · fija el Content-Type a `application/json`


def listar_cursos(request: HttpRequest) -> HttpResponse:
    """Lista solo los cursos activos."""

    activos = [c for c in CURSOS if c["activo"]]
    return render(request, "cursos.html", {"cursos": activos})


def api_cursos(request: HttpRequest) -> JsonResponse:
    """API mínima que devuelve cursos activos."""

    activos = [c for c in CURSOS if c["activo"]]
    data = {
        "ok": True,
        "total": len(activos),
        "cursos": activos,
    }
    return JsonResponse(data)


# TODO: (ZONA DEL ALUMNO – API POST)
# 1. Si el método es POST, lee JSON del cuerpo (titulo, duracion_horas, nivel).
# 2. Valida que `duracion_horas` sea > 0; si no, devuelve {"ok": False, "errores": [...] }.
# 3. Si todo es correcto, añade un nuevo curso a CURSOS y devuelve {"ok": True, "id": nuevo_id}.
# -----------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 – Laboratorio IA (Prompt Kit)
# =========================================================================================
# * Idea didáctica:
#   - Igual que en otras unidades del curso, usamos la IA como “ayudante”
#     para generar variantes de código Django (vistas, formularios, APIs…).
#   - Estos prompts están pensados para que el alumno:
#       · Pida código limpio y comentado
#       · Lo integre en este archivo o en un proyecto real
#       · Lo adapte y lo mejore (no sólo copiar/pegar)
#
# * PROMPT BÁSICO -------------------------------------------------------------
#   "Eres profesor de Django. Crea una vista basada en clases (ListView) para
#    listar cursos con paginación y filtro por nivel. Usa comentarios Better Comments
#    y muéstrame también cómo registrar la URL."
#
# * PROMPT DE MEJORA ----------------------------------------------------------
#   "Añade autenticación simple: vistas de login/logout, uso de sesiones y mensajes,
#    con templates mínimos. Mantén el código por debajo de 80 líneas."
#
# * PROMPT CREATIVO -----------------------------------------------------------
#   "Diseña una mini API REST para cursos (GET/POST/PUT/DELETE) usando solo Django
#    estándar (sin DRF). Incluye validaciones y respuestas JSON claras."
#
# TODO: (ZONA DEL ALUMNO – INTEGRA TU CÓDIGO IA)
# 1. Pide a la IA uno de los prompts anteriores.
# 2. Copia la respuesta en una función aparte (o módulo) dentro de este proyecto.
# 3. Registra una ruta nueva para probarlo y deja un comentario explicando qué has aprendido.
# -----------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 – URL patterns (enrutador)
# =========================================================================================
# * Teoría rápida:
#   - `urlpatterns` es la lista central de rutas de este archivo.
#   - Cada entrada `path("ruta/", vista, name="alias")` indica:
#       · qué URL se atiende
#       · qué función maneja la petición
#       · qué nombre tendrá para usarla desde templates (`{% url 'alias' %}`)
#   - En proyectos grandes, este archivo suele dividirse por apps usando `include()`.

urlpatterns = [
    path("", inicio, name="inicio"),
    path("acerca/", acerca, name="acerca"),
    path("saluda/<str:nombre>/", saluda, name="saluda"),
    path("cursos/", listar_cursos, name="cursos"),
    path("cursos/<int:curso_id>/", detalle_curso, name="detalle_curso"),
    path("api/cursos/", api_cursos, name="api_cursos"),
]


def print_menu() -> None:
    """Muestra instrucciones cuando no se pasan argumentos."""

    print("=" * 80)
    print("Django Tutorial (archivo único)")
    print("=" * 80)
    print("Comandos útiles:")
    print("  python 15_django_tutorial.py runserver 8000")
    print("  python 15_django_tutorial.py check")
    print("  python 15_django_tutorial.py shell")
    print()
    print("Rutas para probar en el navegador:")
    print("  http://127.0.0.1:8000/            -> Inicio")
    print("  http://127.0.0.1:8000/acerca/     -> Acerca")
    print("  http://127.0.0.1:8000/saluda/Ada/ -> Saludo")
    print("  http://127.0.0.1:8000/cursos/     -> Lista de cursos")
    print("  http://127.0.0.1:8000/api/cursos/ -> API JSON")
    print()
    print("Revisa las ZONAS DEL ALUMNO en el código para ampliarlo.")
    print("=" * 80)


def main(argv: List[str]) -> None:
    """Punto de entrada estándar."""

    configure_django()

    # NOTE: no usamos DJANGO_SETTINGS_MODULE porque configuramos settings a mano
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)

    if len(argv) == 1:
        print_menu()
        return

    execute_from_command_line(argv)


if __name__ == "__main__":
    main(sys.argv)

