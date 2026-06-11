"""Extensiones Flask registradas de forma diferida.

# * Mantener estas instancias fuera de create_app evita dependencias circulares.
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# =========================================================================================
#  EXTENSIONES GLOBALES
#  ---------------------------------------------------------------------------------------
#  Aqui viven las extensiones que luego se inicializan dentro de create_app():
#    * db       -> SQLAlchemy
#    * migrate  -> Flask-Migrate (Alembic)
#
#  ? Idea importante:
#    No creamos la app aqui. Solo creamos las instancias "vacías".
# =========================================================================================

db = SQLAlchemy()
migrate = Migrate()
