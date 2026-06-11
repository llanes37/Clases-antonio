from __future__ import annotations
# ==============================================================================
# ARCHIVO: djpf/asgi.py (PUNTO DE ENTRADA ASGI)
# ==============================================================================
# ¿QUÉ ES ASGI?
#   - Asynchronous Server Gateway Interface (WSGI asíncrono)
#   - Evolución de WSGI que soporta:
#       • Peticiones asíncronas (async/await)
#       • WebSockets (comunicación bidireccional en tiempo real)
#       • HTTP/2 y conexiones de larga duración
#
# ¿CUÁNDO USAR ASGI EN LUGAR DE WSGI?
#   - Si tu app tiene WebSockets (chats, notificaciones en vivo)
#   - Si usas Django Channels
#   - Si necesitas alto rendimiento con muchas conexiones simultáneas
#   - Para apps modernas con funcionalidades en tiempo real
#
# SERVIDORES ASGI POPULARES:
#   - Uvicorn (rápido, basado en uvloop)
#   - Daphne (del equipo de Django Channels)
#   - Hypercorn
#
# COMANDO PARA PRODUCCIÓN CON UVICORN:
#   uvicorn djpf.asgi:application --host 0.0.0.0 --port 8000
#
# WSGI vs ASGI:
#   │ Característica    │ WSGI          │ ASGI              │
#   ├───────────────────┼───────────────┼───────────────────┤
#   │ Síncrono          │ ✓             │ ✓                 │
#   │ Asíncrono         │ ✗             │ ✓                 │
#   │ WebSockets        │ ✗             │ ✓                 │
#   │ HTTP/2            │ ✗             │ ✓                 │
# ==============================================================================

"""Punto de entrada ASGI (para uvicorn, daphne, hypercorn, etc.)."""

import os  # * Módulo para variables de entorno

from django.core.asgi import get_asgi_application  # * Crea la app ASGI

# ! Establecemos la configuración ANTES de crear la aplicación
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djpf.settings")

# * `application` es el objeto ASGI que buscan los servidores
application = get_asgi_application()

