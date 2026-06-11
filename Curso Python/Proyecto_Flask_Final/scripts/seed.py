"""Script alternativo para sembrar datos sin usar CLI.
Puedes ejecutar: python scripts/seed.py
"""
import os
from app import create_app
from app.extensions import db
from app.models import Usuario, Curso, Inscripcion

os.environ["APP_ENV"] = "development"
app = create_app()

with app.app_context():
    Inscripcion.query.delete()
    Usuario.query.delete()
    Curso.query.delete()
    db.session.commit()

    curso1 = Curso(titulo="Python Básico", descripcion="Intro", publicado=True)
    curso2 = Curso(titulo="Flask Intro", descripcion="Web", publicado=True)
    u1 = Usuario(nombre="Ana", email="ana@example.com")

    db.session.add_all([curso1, curso2, u1])
    db.session.commit()

print("Semilla creada.")
