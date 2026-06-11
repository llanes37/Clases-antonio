from __future__ import annotations
# ==============================================================================
# ARCHIVO: djpf/wsgi.py (PUNTO DE ENTRADA WSGI)
# ==============================================================================
# ¿QUÉ ES WSGI?
#   - Web Server Gateway Interface (Interfaz de Puerta de Enlace del Servidor Web)
#   - Es el ESTÁNDAR para conectar aplicaciones Python con servidores web.
#   - Permite que servidores como Gunicorn, uWSGI o Apache ejecuten tu app Django.
#
# ¿CUÁNDO SE USA?
#   - En PRODUCCIÓN, cuando despliegas en Render, Heroku, AWS, etc.
#   - El servidor de desarrollo (`runserver`) NO usa este archivo.
#
# ¿CÓMO FUNCIONA?
#   1. El servidor web (Gunicorn) importa este archivo
#   2. Busca la variable `application` (un objeto callable WSGI)
#   3. Por cada petición HTTP, llama a `application(environ, start_response)`
#   4. Django procesa la petición y devuelve la respuesta
#
# COMANDO PARA PRODUCCIÓN:
#   gunicorn djpf.wsgi:application --bind 0.0.0.0:8000
#   └─ djpf.wsgi = este archivo
#   └─ :application = la variable que contiene la app WSGI
# ==============================================================================

"""Punto de entrada WSGI (para gunicorn, uwsgi, Apache mod_wsgi, etc.)."""

import os  # * Módulo para variables de entorno

from django.core.wsgi import get_wsgi_application  # * Función que crea la app WSGI

# ! Establecemos la configuración de Django ANTES de crear la aplicación
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djpf.settings")

# * `application` es el objeto que el servidor web busca y ejecuta
# * get_wsgi_application() configura Django y devuelve un callable WSGI
application = get_wsgi_application()

