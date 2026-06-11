"""Blueprint de páginas HTML públicas.
- Muestra páginas con Jinja2 y datos desde la BD.

# * Recuerda: usar plantillas evita mezclar HTML con la lógica Python.
"""
from flask import Blueprint, render_template
from ..models import Curso

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    # * Página de inicio
    cursos_publicados = Curso.query.filter_by(publicado=True).all()
    return render_template("index.html", cursos=cursos_publicados)


@bp.route("/cursos")
def cursos():
    # * Página con listado de cursos y enlace al API
    cursos = Curso.query.order_by(Curso.titulo).all()
    return render_template("cursos.html", cursos=cursos)
