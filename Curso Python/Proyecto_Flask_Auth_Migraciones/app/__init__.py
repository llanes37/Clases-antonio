"""Aplicacion Flask con auth, roles simples y soporte para migraciones.

El foco didactico es mostrar:
- app factory
- SQLAlchemy + Flask-Migrate
- sesiones de usuario
- permisos por rol
- mensajes flash y rutas protegidas
"""
from __future__ import annotations

import os

from dotenv import load_dotenv
from flask import Flask, g, session

from .blueprints.admin import bp as admin_bp
from .blueprints.auth import bp as auth_bp
from .blueprints.main import bp as main_bp
from .config import get_config
from .errors import register_error_handlers
from .extensions import db, migrate
from .models import User

# =========================================================================================
#  APP FACTORY - PROYECTO AUTH + MIGRACIONES
#  ---------------------------------------------------------------------------------------
#  Este archivo une todas las piezas:
#    * carga variables de entorno
#    * crea la app Flask
#    * inicializa extensiones
#    * registra blueprints
#    * carga usuario en cada request
#    * expone un comando CLI de seed
#
#  * Es uno de los archivos mas importantes del proyecto porque muestra la "columna
#    vertebral" de una app Flask moderadamente seria.
# =========================================================================================


def create_app() -> Flask:
    # * 1) Cargar .env si existe
    load_dotenv()

    # * 2) Crear app e importar configuracion segun APP_ENV
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(get_config())

    # * 3) Asegurar carpeta instance/
    os.makedirs(app.instance_path, exist_ok=True)

    # * 4) Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # * 5) Registrar blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    # * 6) Registrar errores comunes
    register_error_handlers(app)

    @app.before_request
    def load_logged_user():
        # ? En cada peticion intentamos recuperar el usuario desde la sesion
        user_id = session.get("user_id")
        if user_id is None:
            g.user = None
        else:
            g.user = User.query.get(user_id)

    @app.cli.command("seed-auth")
    def seed_auth():
        """Crea usuarios demo y una nota inicial."""
        from .models import NotaPrivada

        # * Usuario admin demo
        admin = User.query.filter_by(email="admin@demo.local").first()
        if admin is None:
            admin = User(nombre="Admin Demo", email="admin@demo.local", role="admin")
            admin.set_password("admin123")
            db.session.add(admin)

        # * Usuario alumno demo
        alumno = User.query.filter_by(email="alumno@demo.local").first()
        if alumno is None:
            alumno = User(nombre="Alumno Demo", email="alumno@demo.local", role="student")
            alumno.set_password("alumno123")
            db.session.add(alumno)

        db.session.commit()

        if not admin.notas:
            db.session.add(NotaPrivada(titulo="Primera nota admin", contenido="Panel listo para practicar.", owner=admin))
        if not alumno.notas:
            db.session.add(NotaPrivada(titulo="Nota del alumno", contenido="Esta nota prueba la zona privada.", owner=alumno))
        db.session.commit()

        # NOTE: Credenciales faciles porque es un entorno docente, no produccion
        print("Usuarios demo creados:")
        print("  admin@demo.local / admin123")
        print("  alumno@demo.local / alumno123")

    return app
