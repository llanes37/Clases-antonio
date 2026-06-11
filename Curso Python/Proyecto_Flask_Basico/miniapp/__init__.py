"""App mínima Flask con MVC básico.
- create_app: crea la app
- registra el blueprint principal
- crea la BD SQLite en instance/

Better Comments que verás aquí:
- # * Idea clave (lo más importante que debes recordar)
- # ! Advertencia o buena práctica de seguridad
- # ? Explicación o contexto didáctico
- # TODO: Sugerencia de mejora para practicar
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# * SQLAlchemy global muy simple (sin módulo extensions separado)
# ? Mantenerlo en este archivo hace el ejemplo más corto para principiantes.
db = SQLAlchemy()


def create_app():
    # * 1) Crear la app
    # ? instance_relative_config=True -> crea/usa carpeta "instance/" para ficheros locales
    app = Flask(__name__, instance_relative_config=True)

    # * 2) Config mínima: SQLite en archivo dentro de instance/
    # ! En producción cambia SECRET_KEY por una clave robusta y secreta
    app.config['SECRET_KEY'] = 'dev-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_basico.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    os.makedirs(app.instance_path, exist_ok=True)

    # * 3) Inicializar DB
    db.init_app(app)
    with app.app_context():
        from .models import Curso  # * Import aquí para registrar el modelo
        db.create_all()

    # * 4) Registrar rutas (CONTROLADOR)
    from .views import bp as main_bp
    app.register_blueprint(main_bp)

    # TODO: (Nivel siguiente) añadir mensajes flash y validaciones de formularios
    # TODO: (Nivel siguiente) separar config en un archivo config.py

    return app
