"""MODELO: definición de la entidad Curso.
Muy simple: id, titulo, descripcion.

# * El MODELO representa los datos y sus reglas básicas.
# ? SQLAlchemy mapea esta clase a una tabla de SQLite.
"""
from . import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.String(255), default="")

    def __repr__(self):
        return f"<Curso {self.titulo}>"
