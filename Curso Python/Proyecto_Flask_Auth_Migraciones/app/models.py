"""Modelos SQLAlchemy del proyecto.

Este proyecto se centra en tres ideas:
- autenticacion basica con usuarios y passwords hasheados
- roles simples (student / admin)
- una entidad de negocio pequeña (NotaPrivada) para dar sentido al panel
"""
from __future__ import annotations

from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from .extensions import db

# =========================================================================================
#  MODELOS SQLALCHEMY
#  ---------------------------------------------------------------------------------------
#  Este proyecto se centra en:
#    * User        -> autenticacion y roles
#    * NotaPrivada -> recurso sencillo protegido por usuario
#
#  ? Elegimos una entidad muy simple ("nota privada") para que el foco del proyecto no
#    sea el dominio de negocio, sino auth, permisos y migraciones.
# =========================================================================================


class User(db.Model):
    # * Tabla principal de usuarios
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="student")
    activo = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    notas = db.relationship("NotaPrivada", back_populates="owner", cascade="all, delete-orphan")

    def set_password(self, password: str) -> None:
        # ! Nunca guardamos la password en texto plano
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        # * Compara la password introducida con el hash almacenado
        return check_password_hash(self.password_hash, password)

    def is_admin(self) -> bool:
        # * Atajo legible para templates, decoradores y panel admin
        return self.role == "admin"

    def to_dict(self) -> dict:
        # ? Util si mañana queremos exponer estos datos en una API
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "role": self.role,
            "activo": self.activo,
            "created_at": self.created_at.isoformat(),
        }


class NotaPrivada(db.Model):
    # * Entidad de negocio pequeña asociada a un usuario
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    contenido = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    owner = db.relationship("User", back_populates="notas")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
        }
