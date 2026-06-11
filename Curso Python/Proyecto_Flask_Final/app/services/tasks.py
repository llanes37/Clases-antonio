"""Comandos CLI para Flask (usando Click).
- Registramos comandos como `flask seed` para poblar la base de datos.
"""
import click
from flask import current_app
from flask.cli import with_appcontext
from ..extensions import db
from ..models import Usuario, Curso, Inscripcion


@click.command("seed")
@with_appcontext
def seed_command():
    """Crea datos de ejemplo en la BD."""
    click.echo("Creando datos de ejemplo...")

    # * Limpiar tablas
    Inscripcion.query.delete()
    Usuario.query.delete()
    Curso.query.delete()
    db.session.commit()

    # * Crear cursos y usuarios
    curso1 = Curso(titulo="Python Básico", descripcion="Variables, bucles y funciones", publicado=True)
    curso2 = Curso(titulo="Flask Intro", descripcion="Rutas, plantillas y API", publicado=True)
    curso3 = Curso(titulo="SQLAlchemy", descripcion="Modelos y consultas", publicado=False)

    u1 = Usuario(nombre="Ana", email="ana@example.com")
    u2 = Usuario(nombre="Luis", email="luis@example.com")

    db.session.add_all([curso1, curso2, curso3, u1, u2])
    db.session.commit()

    # * Inscribir usuarios
    db.session.add_all([
        Inscripcion(usuario_id=u1.id, curso_id=curso1.id),
        Inscripcion(usuario_id=u2.id, curso_id=curso2.id),
    ])
    db.session.commit()

    click.echo("Datos de ejemplo creados.")


def register_cli(app):
    """Registrar los comandos en la app."""
    app.cli.add_command(seed_command)
