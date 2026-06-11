"""Configuración de pytest para la app.
- Crea una instancia en modo testing con SQLite en memoria.
- Expone fixtures `app` y `client` para los tests.
"""
import os
import pytest
from app import create_app
from app.extensions import db

@pytest.fixture()
def app():
    os.environ["APP_ENV"] = "testing"
    application = create_app()
    with application.app_context():
        db.create_all()
    yield application

@pytest.fixture()
def client(app):
    return app.test_client()
