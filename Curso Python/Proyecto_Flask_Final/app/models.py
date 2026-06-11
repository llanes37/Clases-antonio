"""Modelos SQLAlchemy: Usuario, Curso, Inscripcion
- Demuestran POO, relaciones y validaciones básicas.

Relaciones:
- # * Usuario N—M Curso (a través de Inscripcion)
- # ? Inscripcion guarda también la fecha de alta
"""
from datetime import datetime
from .extensions import db

# Tabla intermedia muchos-a-muchos entre Usuario y Curso
class Inscripcion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relación: cursos en los que está inscrito
    cursos = db.relationship('Curso', secondary='inscripcion', back_populates='alumnos')

    def __repr__(self) -> str:
        return f"<Usuario {self.nombre}>"


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, default="")
    publicado = db.Column(db.Boolean, default=True)

    # Relación inversa
    alumnos = db.relationship('Usuario', secondary='inscripcion', back_populates='cursos')

    def to_dict(self) -> dict:
        """Serializa el curso para respuestas JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "publicado": self.publicado,
        }

    def __repr__(self) -> str:
        return f"<Curso {self.titulo}>"

    # TODO: Ejercicio (opcional): añade un método publicar() que ponga publicado=True
    #       y registre una fecha de publicación si quieres extender el modelo.
