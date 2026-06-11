"""Configuracion de pytest para auth + migraciones."""
import os

import pytest

from app import create_app
from app.extensions import db
from app.models import User

# =========================================================================================
#  FIXTURES DE TEST
#  ---------------------------------------------------------------------------------------
#  Se crea una app en modo testing y una base SQLite en memoria.
#  Esto permite probar auth y permisos sin tocar archivos reales.
# =========================================================================================


@pytest.fixture()
def app():
    os.environ["APP_ENV"] = "testing"
    application = create_app()
    with application.app_context():
        db.create_all()
        # * Usuario admin de prueba
        admin = User(nombre="Admin Test", email="admin@test.local", role="admin")
        admin.set_password("admin123")
        # * Usuario alumno de prueba
        alumno = User(nombre="Alumno Test", email="alumno@test.local", role="student")
        alumno.set_password("alumno123")
        db.session.add_all([admin, alumno])
        db.session.commit()
    yield application


@pytest.fixture()
def client(app):
    return app.test_client()
