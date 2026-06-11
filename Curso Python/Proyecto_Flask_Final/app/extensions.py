"""Extensiones de Flask inicializadas de forma diferida.
Mantener en un módulo separado evita dependencias circulares.
"""
from flask_sqlalchemy import SQLAlchemy

# * Instancia global (se inicializa en create_app)
db = SQLAlchemy()
