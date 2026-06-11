from __future__ import annotations

"""
Configuración básica de Django para el proyecto didáctico `django_pf`.

Este archivo está MUY comentado para poder explicarlo en clase paso a paso.
"""

from pathlib import Path

# ======================================================================================
#  RUTAS BÁSICAS Y VARIABLES GLOBALES
# ======================================================================================

# * BASE_DIR:
#   - Carpeta raíz del proyecto (la que contiene `manage.py`).
#   - A partir de aquí construimos rutas relativas (templates, base de datos, etc.).
BASE_DIR = Path(__file__).resolve().parent.parent


# ======================================================================================
#  SEGURIDAD Y MODO DEBUG
# ======================================================================================

# ! SECRET_KEY:
#   - Clave criptográfica que Django usa para firmar cookies, tokens CSRF, etc.
#   - En producción DEBE ser larga, única y mantenerse en secreto (variables de entorno).
#   - Aquí usamos un valor fijo y público porque el proyecto es solo para aprendizaje.
SECRET_KEY = "django-proyecto-facil-super-secreto"

# * DEBUG:
#   - True  → errores detallados, recarga automática, mensajes de debug.
#   - False → páginas de error amigables, sin detalles internos (obligatorio en producción).
DEBUG = True

# * ALLOWED_HOSTS:
#   - Lista de dominios o IPs desde los que se permite acceder cuando DEBUG=False.
#   - En desarrollo se suele dejar vacío; en producción habría que poner dominios reales.
ALLOWED_HOSTS: list[str] = []


# ======================================================================================
#  APLICACIONES INSTALADAS (INSTALLED_APPS)
# ======================================================================================

# * Cada string es una “app” Django que aporta modelos, vistas, templates, etc.
# * Las apps `django.contrib.*` son parte del propio framework.
# * La app `core` es nuestra app didáctica con las vistas de este proyecto.
INSTALLED_APPS = [
    # * Apps del núcleo de Django ------------------------------------------------------
    "django.contrib.admin",         # Panel de administración (CRUD rápido sobre modelos)
    "django.contrib.auth",          # Sistema de usuarios y permisos
    "django.contrib.contenttypes",  # Tipos de contenido genéricos
    "django.contrib.sessions",      # Gestión de sesiones (usuario anónimo/logueado)
    "django.contrib.messages",      # Mensajes flash (success/error/info)
    "django.contrib.staticfiles",   # Gestión de archivos estáticos (CSS, JS, imágenes)

    # * App propia del proyecto --------------------------------------------------------
    "core",                         # Nuestra app: rutas, vistas, templates, middleware
]


# ======================================================================================
#  MIDDLEWARE (CAPAS QUE ENVUELVEN CADA PETICIÓN)
# ======================================================================================

# * El middleware se ejecuta ANTES y DESPUÉS de cada vista.
# * Aquí se hacen tareas transversales:
#     - Seguridad
#     - Autenticación
#     - Logs
#     - Cabeceras personalizadas
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",           # ! Cabeceras de seguridad
    "django.contrib.sessions.middleware.SessionMiddleware",    # * Habilita sesiones
    "django.middleware.common.CommonMiddleware",               # * Utilidades varias
    "django.middleware.csrf.CsrfViewMiddleware",               # ! Protección CSRF en POST
    "django.contrib.auth.middleware.AuthenticationMiddleware", # * Añade `user` a request
    "django.contrib.messages.middleware.MessageMiddleware",    # * Mensajes flash
    "django.middleware.clickjacking.XFrameOptionsMiddleware", # * Protege contra iframes maliciosos
    "core.middleware.RequestLogMiddleware",                    # ? Nuestro middleware didáctico
]


# ======================================================================================
#  URLS Y SISTEMA DE PLANTILLAS
# ======================================================================================

# * ROOT_URLCONF:
#   - Indica el módulo que contiene las rutas raíz del proyecto.
#   - Dentro de `djpf/urls.py` se incluyen las rutas de la app `core`.
ROOT_URLCONF = "djpf.urls"

# * TEMPLATES:
#   - BACKEND: motor de plantillas (el de Django por defecto).
#   - DIRS: carpetas extra donde buscar templates (además de las apps).
#   - APP_DIRS: si es True, también busca en `<app>/templates`.
#   - context_processors: funciones que añaden variables a todos los templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # ! Carpeta donde viven los templates principales de la app `core`
        "DIRS": [BASE_DIR / "core" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",    # ? Info extra si DEBUG=True
                "django.template.context_processors.request",  # * Añade `request` al contexto
                "django.contrib.auth.context_processors.auth", # * Añade `user` y `perms`
                "django.contrib.messages.context_processors.messages",  # * Mensajes flash
            ],
        },
    },
]


# * Aplicaciones ASGI/WSGI: puntos de entrada para servidores web -----------------------
WSGI_APPLICATION = "djpf.wsgi.application"
ASGI_APPLICATION = "djpf.asgi.application"


# ======================================================================================
#  BASE DE DATOS
# ======================================================================================

# * Usamos SQLite porque:
#     - No requiere instalar nada extra.
#     - El fichero se guarda en `db.sqlite3` en la raíz del proyecto.
#     - Es ideal para demos y desarrollo local.
# * En producción se recomienda cambiar a PostgreSQL, MySQL, etc.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Motor de BD
        "NAME": BASE_DIR / "db.sqlite3",         # Ruta del archivo de base de datos
    }
}


# ======================================================================================
#  INTERNACIONALIZACIÓN Y ZONA HORARIA
# ======================================================================================

# * Idioma por defecto y zona horaria del proyecto.
LANGUAGE_CODE = "es-es"        # Español (España)
TIME_ZONE = "Europe/Madrid"    # Ajusta si tu zona es distinta

USE_I18N = True                # * Activa el sistema de traducciones
USE_TZ = True                  # * Fechas almacenadas con zona horaria


# ======================================================================================
#  ARCHIVOS ESTÁTICOS (CSS / JS / IMÁGENES)
# ======================================================================================

# * `STATIC_URL` es el prefijo de la URL para servir archivos estáticos.
# * Más adelante se podría añadir `STATICFILES_DIRS` y `STATIC_ROOT` para producción.
STATIC_URL = "static/"


# ======================================================================================
#  OTRAS OPCIONES
# ======================================================================================

# * Tipo de campo auto-incremental por defecto para los modelos.
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

