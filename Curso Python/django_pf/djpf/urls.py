from __future__ import annotations
# ==============================================================================
# ARCHIVO: djpf/urls.py (ENRUTADOR RAÍZ DEL PROYECTO)
# ==============================================================================
# ¿QUÉ ES?
#   El "mapa de carreteras" principal del proyecto. Aquí se define:
#   - Qué URL lleva a qué vista o app.
#   - Manejadores de errores personalizados (404, 500).
#
# FLUJO DE UNA PETICIÓN:
#   1. Usuario visita http://localhost:8000/about/
#   2. Django busca en este archivo (ROOT_URLCONF en settings.py)
#   3. Encuentra path("", include("core.urls")) → delega a core/urls.py
#   4. En core/urls.py encuentra path("about/", views.about)
#   5. Ejecuta la vista `about()` y devuelve el HTML
#
# ¿CÓMO FUNCIONA EL INCLUDE?
#   - include("core.urls") carga las rutas de la app `core`
#   - namespace="core" permite usar {% url 'core:inicio' %} en templates
#   - Si tuvieras más apps: include("blog.urls", namespace="blog")
# ==============================================================================

"""Enrutador raíz del proyecto Django."""

from django.contrib import admin  # * Panel de administración de Django
from django.urls import include, path  # * Funciones para definir rutas

# ==============================================================================
# URLPATTERNS - Lista de rutas del proyecto
# ==============================================================================
# Cada elemento es un path() que asocia una URL con una vista o app.
#
# SINTAXIS:
#   path("ruta/", vista_o_include, name="nombre_opcional")
#
# EJEMPLOS:
#   path("admin/", admin.site.urls)       → /admin/ lleva al panel admin
#   path("", include("core.urls"))         → /cualquier-cosa delega a core.urls
#   path("api/", include("api.urls"))      → /api/... delega a api.urls
# ==============================================================================
urlpatterns = [
    # -------------------------------------------------------------------------
    # RUTA DEL PANEL DE ADMINISTRACIÓN
    # -------------------------------------------------------------------------
    # ! El admin de Django es un CRUD automático para tus modelos.
    # ! Accede en: http://localhost:8000/admin/
    # ! Necesitas crear un superusuario: python manage.py createsuperuser
    path("admin/", admin.site.urls),
    
    # -------------------------------------------------------------------------
    # RUTAS DE LA APP CORE (nuestra app principal)
    # -------------------------------------------------------------------------
    # * path("") significa "sin prefijo" → las rutas de core empiezan desde /
    # * Si pusiéramos path("app/", include(...)) → las rutas serían /app/...
    # * namespace="core" permite referencias como {% url 'core:inicio' %}
    path("", include("core.urls", namespace="core")),
]

# ==============================================================================
# MANEJADORES DE ERRORES PERSONALIZADOS
# ==============================================================================
# Django tiene páginas de error por defecto, pero podemos personalizarlas.
#
# ! IMPORTANTE: Solo funcionan cuando DEBUG=False en settings.py
# ! En desarrollo (DEBUG=True), Django muestra el traceback completo.
#
# ERRORES COMUNES:
#   - 400 Bad Request      → Petición mal formada
#   - 403 Forbidden        → Sin permiso para acceder
#   - 404 Not Found        → Página no existe
#   - 500 Internal Error   → Error en el servidor (bug en el código)
# ==============================================================================
handler404 = "core.views.error_404"  # ? Ruta no encontrada
handler500 = "core.views.error_500"  # ? Error interno del servidor

