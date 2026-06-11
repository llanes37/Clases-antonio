"""CONTROLADOR: rutas principales.
- GET /      -> lista cursos y muestra formulario
- POST /crear -> añade un curso y redirige a /
- GET /borrar/<id> -> borra un curso

# * CONTROLADOR (Blueprint): recibe peticiones y decide qué hacer
# ? Para mantenerlo simple, todo está en un archivo
"""
from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Curso

bp = Blueprint('main', __name__)

@bp.get('/')
def index():
    # * Leemos los cursos (MODELO) y los pasamos a la plantilla (VISTA)
    cursos = Curso.query.order_by(Curso.id.desc()).all()
    return render_template('index.html', cursos=cursos)

@bp.post('/crear')
def crear():
    # ? Obtenemos datos del formulario HTML
    titulo = request.form.get('titulo', '').strip()
    descripcion = request.form.get('descripcion', '').strip()
    if not titulo:
        # ! En un proyecto real mostraríamos un mensaje de error (flash)
        return redirect(url_for('main.index'))
    c = Curso(titulo=titulo, descripcion=descripcion)
    db.session.add(c)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.get('/borrar/<int:curso_id>')
def borrar(curso_id):
    c = Curso.query.get_or_404(curso_id)
    db.session.delete(c)
    db.session.commit()
    return redirect(url_for('main.index'))
