#!/usr/bin/env python
# ==============================================================================
# ARCHIVO: manage.py
# ==============================================================================
# ¿QUÉ ES?
#   Es el "control remoto" del proyecto Django. Desde la terminal ejecutamos
#   comandos como:
#       python manage.py runserver   → Arranca el servidor de desarrollo
#       python manage.py migrate      → Aplica migraciones a la base de datos
#       python manage.py createsuperuser → Crea un admin
#       python manage.py shell        → Abre una consola Python con Django cargado
#
# ¿DÓNDE VIVE?
#   Siempre en la raíz del proyecto, junto a la carpeta del proyecto (djpf/).
#
# ¿LO MODIFICO?
#   Normalmente NO. Django lo genera automáticamente con `django-admin startproject`.
# ==============================================================================

"""Utilidad de línea de comandos para tareas administrativas de Django."""

import os   # * Módulo para interactuar con el sistema operativo
import sys  # * Módulo para acceder a argumentos de la terminal (sys.argv)


def main() -> None:
    """
    Punto de entrada principal cuando ejecutamos `python manage.py <comando>`.
    
    # ! PASO 1: Establecer la variable de entorno DJANGO_SETTINGS_MODULE
    #   - Esto le dice a Django DÓNDE está el archivo de configuración.
    #   - "djpf.settings" significa: carpeta `djpf`, archivo `settings.py`.
    #   - setdefault() solo la establece si NO existe ya (por si la definimos antes).
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djpf.settings")
    
    # ! PASO 2: Importar y ejecutar el sistema de comandos de Django
    #   - `execute_from_command_line` lee sys.argv (los argumentos de terminal)
    #   - Ejemplo: `python manage.py runserver 8080`
    #     sys.argv = ['manage.py', 'runserver', '8080']
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


# ==============================================================================
# ¿QUÉ HACE ESTO?
# ==============================================================================
# if __name__ == "__main__":
#   - Comprueba si este archivo se ejecuta DIRECTAMENTE (python manage.py ...)
#   - Si lo importamos desde otro sitio, esta condición es False y no hace nada.
#   - Es un patrón estándar en Python para scripts ejecutables.
# ==============================================================================
if __name__ == "__main__":
    main()
