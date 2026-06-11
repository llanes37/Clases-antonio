from __future__ import annotations
# ==============================================================================
# ARCHIVO: core/urls.py (RUTAS DE LA APP CORE)
# ==============================================================================
# ¿QUÉ ES?
#   Define las URLs específicas de esta app. Se "conectan" al proyecto
#   principal mediante include() en djpf/urls.py.
#
# ¿POR QUÉ SEPARAR URLS POR APP?
#   - Organización: cada app maneja sus propias rutas
#   - Reutilización: puedes copiar la app a otro proyecto
#   - Claridad: es más fácil encontrar dónde está cada cosa
#
# SINTAXIS DE PATH:
#   path("ruta/", vista, name="nombre")
#   
#   - "ruta/": la URL (sin el dominio)
#   - vista: función o clase que procesa la petición
#   - name: identificador para usar en templates y redirects
#
# PARÁMETROS EN RUTAS:
#   <tipo:nombre> captura un valor de la URL
#   
#   Tipos disponibles:
#   - str:   cualquier texto (sin /)     → <str:nombre>
#   - int:   números enteros             → <int:id>
#   - slug:  texto-con-guiones           → <slug:titulo>
#   - uuid:  identificador único         → <uuid:token>
#   - path:  cualquier texto (con /)     → <path:ruta>
# ==============================================================================

"""Rutas de la app `core`."""

from django.urls import path  # * Función para definir rutas

from . import views  # * Importamos las vistas de esta app

# ==============================================================================
# APP_NAME - Namespace de la app
# ==============================================================================
# ! Esto permite usar {% url 'core:inicio' %} en templates
# ! Sin namespace sería {% url 'inicio' %} y podría colisionar con otras apps
app_name = "core"

# ==============================================================================
# URLPATTERNS - Lista de rutas de la app
# ==============================================================================
urlpatterns = [
    # =========================================================================
    # SECCIÓN 1: VISTAS HTML (páginas web normales)
    # =========================================================================
    
    # * Página de inicio (raíz del sitio)
    # URL: http://localhost:8000/
    # Template: index.html
    path("", views.inicio, name="inicio"),
    
    # * Página "Acerca de"
    # URL: http://localhost:8000/about/
    # Template: about.html
    path("about/", views.about, name="about"),
    
    # * Procesar formulario (recibe POST)
    # URL: http://localhost:8000/procesar/
    # Template: resultado.html
    path("procesar/", views.procesar, name="procesar"),
    
    # =========================================================================
    # SECCIÓN 2: RUTAS CON PARÁMETROS (capturan valores de la URL)
    # =========================================================================
    
    # * Saludo con nombre en la URL
    # URL: http://localhost:8000/saluda/Joaquin/
    # <str:nombre> captura "Joaquin" y lo pasa a la vista
    path("saluda/<str:nombre>/", views.saluda, name="saluda"),
    
    # * Suma de dos números enteros
    # URL: http://localhost:8000/suma/3/5/
    # <int:a> y <int:b> capturan 3 y 5 como enteros (no strings)
    path("suma/<int:a>/<int:b>/", views.suma, name="suma"),
    
    # * Búsqueda con query strings
    # URL: http://localhost:8000/buscar/?q=django&page=1
    # Los parámetros van en request.GET, no en la ruta
    path("buscar/", views.buscar, name="buscar"),
    
    # =========================================================================
    # SECCIÓN 3: API JSON (devuelven datos, no HTML)
    # =========================================================================
    
    # * Echo: devuelve lo que envías
    # URL: http://localhost:8000/api/echo/?q=hola
    # Respuesta: {"ok": true, "echo": "hola"}
    path("api/echo/", views.api_echo, name="api_echo"),
    
    # * Saludo por POST con JSON
    # URL: POST http://localhost:8000/api/saludo/
    # Body: {"nombre": "Ada"}
    # Respuesta: {"ok": true, "mensaje": "Hola, Ada!"}
    path("api/saludo/", views.api_saludo, name="api_saludo"),
    
    # * Health check (comprueba que la app está viva)
    # URL: http://localhost:8000/api/health/
    # Respuesta: {"status": "ok"}
    path("api/health/", views.api_health, name="api_health"),
    
    # * Calculadora con parámetros en la URL
    # URL: http://localhost:8000/api/calculadora/suma/3/5/
    # Respuesta: {"ok": true, "operacion": "suma", "resultado": 8}
    path(
        "api/calculadora/<str:operacion>/<int:a>/<int:b>/",
        views.api_calculadora,
        name="api_calculadora",
    ),
    
    # =========================================================================
    # SECCIÓN 4: PRUEBAS DE ERRORES
    # =========================================================================
    
    # * Genera un error 500 intencionalmente (para probar el handler)
    # URL: http://localhost:8000/error-intencional/
    # ! Solo funciona con DEBUG=False
    path("error-intencional/", views.error_intencional, name="error_intencional"),
]

