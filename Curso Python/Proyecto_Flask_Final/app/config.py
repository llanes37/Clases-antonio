"""Configuración de Flask por entorno.
- Usa variables de entorno si existen, con valores por defecto seguros.
- Expone clases Config para development/testing/production.

Notas didácticas:
- # * SECRET_KEY: usada por Flask para sesiones/CSRF. En producción debe ser secreta y robusta.
- # ? DATABASE_URL: cadena SQLAlchemy (sqlite:///archivo.db o postgresql://user:pass@host/db)
"""
import os

# * Variables desde entorno
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-cambia-esto")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///proyecto.db")
APP_ENV = os.getenv("APP_ENV", "development").lower()


class BaseConfig:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Carpeta de subidas dentro de instance/
    UPLOAD_FOLDER_NAME = "uploads"
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    # * DB en memoria para tests rápidos
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # * Para tests no necesitamos subidas reales
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024


class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config():
    """Devuelve la clase de configuración según APP_ENV."""
    # * Importante: claves soportadas: development, testing, production
    mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    return mapping.get(APP_ENV, DevelopmentConfig)
