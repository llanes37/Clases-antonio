from __future__ import annotations
# ==============================================================================
# ARCHIVO: core/apps.py (CONFIGURACIÓN DE LA APP)
# ==============================================================================
# ¿QUÉ ES?
#   Cada app Django tiene un archivo apps.py que define su configuración.
#   Django lo usa para:
#   - Registrar la app en INSTALLED_APPS
#   - Mostrar nombres legibles en el panel de administración
#   - Configurar señales (signals) y otras opciones avanzadas
#
# ¿CUÁNDO SE USA?
#   - Django lo carga automáticamente al arrancar
#   - Lo referenciamos en settings.py: INSTALLED_APPS = ["core", ...]
#     (Django busca core/apps.py → CoreConfig)
#
# ¿LO MODIFICO?
#   - Normalmente solo para cambiar `verbose_name` (nombre bonito)
#   - Para apps avanzadas: método `ready()` para registrar signals
# ==============================================================================

from django.apps import AppConfig  # * Clase base para configuración de apps


class CoreConfig(AppConfig):
    """
    Configuración de la app 'core'.
    
    # * ATRIBUTOS:
    #   - default_auto_field: Tipo de campo para IDs automáticos en modelos
    #   - name: Nombre técnico de la app (debe coincidir con la carpeta)
    #   - verbose_name: Nombre legible que aparece en el admin
    """
    
    # -------------------------------------------------------------------------
    # TIPO DE CAMPO AUTO-INCREMENTAL
    # -------------------------------------------------------------------------
    # ! Esto define qué tipo de ID usan los modelos por defecto.
    # ! Opciones comunes:
    #   - AutoField: enteros (1, 2, 3...) - el clásico
    #   - BigAutoField: enteros grandes (para millones de registros)
    #   - UUIDField: identificadores únicos universales
    default_auto_field = "django.db.models.AutoField"
    
    # -------------------------------------------------------------------------
    # NOMBRE TÉCNICO (debe coincidir con la carpeta)
    # -------------------------------------------------------------------------
    name = "core"
    
    # -------------------------------------------------------------------------
    # NOMBRE LEGIBLE (aparece en el admin)
    # -------------------------------------------------------------------------
    verbose_name = "Proyecto Django Fácil"
    
    # -------------------------------------------------------------------------
    # MÉTODO READY (opcional - para inicialización avanzada)
    # -------------------------------------------------------------------------
    # def ready(self):
    #     """Se ejecuta cuando Django termina de cargar la app."""
    #     # Aquí podrías importar signals:
    #     # from . import signals
    #     pass

