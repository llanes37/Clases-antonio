"""
Aplicación Flask (Factory Pattern)
- Carga configuración por entorno
- Inicializa extensiones (SQLAlchemy)
- Registra blueprints
- Registra manejadores de errores y comandos CLI

Mezcla teoría + práctica con comentarios estilo Better Comments.

Etiquetas Better Comments usadas en el código:
- # TODO: tareas pendientes
- # ! Importante/Advertencia
- # ? Duda/explicación
- # * Idea clave o nota positiva
"""
# * Importaciones estándar
import os

# * Librerías de terceros
from flask import Flask
from dotenv import load_dotenv

# * Módulos internos
from .config import get_config
from .extensions import db
from .errors import register_error_handlers
from .blueprints.main import bp as main_bp
from .blueprints.api import bp as api_bp
from .blueprints.files import bp as files_bp
from .services.tasks import register_cli

# ! Punto de entrada principal de Flask: create_app

def create_app() -> Flask:
    """Factory que crea y configura la app Flask.

    Retorna:
        Flask: instancia configurada y lista.

    # * ¿Por qué factory? Permite crear instancias separadas para desarrollo, tests y producción
    #   cambiando configuración y extensiones sin duplicar código.
    """
    # * 1) Cargar variables del .env si existe
    load_dotenv()

    # * 2) Crear instancia de Flask
    # ? ¿Qué es instance_relative_config?
    #   Permite usar la carpeta instance/ (fuera del control de git) para datos locales como DB o uploads.
    app = Flask(__name__, instance_relative_config=True)

    # * 3) Configuración por entorno (development/testing/production)
    app.config.from_object(get_config())

    # * 4) Asegurar carpetas necesarias
    os.makedirs(app.instance_path, exist_ok=True)
    os.makedirs(os.path.join(app.instance_path, "uploads"), exist_ok=True)

    # * 5) Inicializar extensiones
    db.init_app(app)

    # * 6) Crear tablas si no existen (para nivel básico sin migraciones)
    # ! En proyectos grandes usar Alembic (migraciones). Aquí simplificamos para el curso.
    with app.app_context():
        db.create_all()

    # * 7) Registrar blueprints (módulos de rutas)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(files_bp, url_prefix="/files")

    # * 8) Manejadores de errores
    register_error_handlers(app)

    # * 9) Comandos CLI (seed de datos, utilidades)
    register_cli(app)

    # ? DevTip: puedes añadir aquí filtros Jinja personalizados si los necesitas
    #   Ej: app.jinja_env.filters['resumen'] = mi_filtro

    return app
