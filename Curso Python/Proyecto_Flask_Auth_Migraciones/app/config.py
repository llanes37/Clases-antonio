"""Configuracion por entorno para el proyecto de autenticacion.

# * SECRET_KEY protege cookies de sesion y mensajes flash.
# * DATABASE_URL define la base de datos usada por SQLAlchemy.
# * En testing usamos SQLite en memoria para tests rapidos.
"""
from __future__ import annotations

import os

# =========================================================================================
#  CONFIGURACION DEL PROYECTO - AUTH + MIGRACIONES
#  ---------------------------------------------------------------------------------------
#  En este archivo se define:
#    * que configuracion usa la app segun el entorno
#    * donde vive la base de datos
#    * que SECRET_KEY se usa para sesiones y flash messages
#    * que cambia entre desarrollo, testing y produccion
#
#  Better Comments:
#    # ! importante   |  # * definicion/foco   |  # ? idea/nota
#    # TODO: practica |  # NOTE: apunte util   |  # // deprecado
# =========================================================================================

# * Variables leidas desde entorno ------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-auth-secret-cambia-esto")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///auth_migraciones.db")
APP_ENV = os.getenv("APP_ENV", "development").lower()


class BaseConfig:
    # * Configuracion comun a todos los entornos
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    # ? Modo recomendado para clase: debug activo
    DEBUG = True


class TestingConfig(BaseConfig):
    # * En tests usamos SQLite en memoria para no tocar ficheros reales
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    # ! En produccion nunca deberiamos exponer debug
    DEBUG = False


def get_config():
    """# * Devuelve la clase de configuracion apropiada segun APP_ENV."""
    mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    return mapping.get(APP_ENV, DevelopmentConfig)
