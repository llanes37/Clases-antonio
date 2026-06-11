"""Blueprint publico y area privada del usuario."""
from __future__ import annotations

from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from ..extensions import db
from ..models import NotaPrivada
from ..services.auth_utils import login_required

# =========================================================================================
#  BLUEPRINT PRINCIPAL
#  ---------------------------------------------------------------------------------------
#  Este modulo contiene:
#    * portada publica
#    * perfil del usuario
#    * creacion de notas privadas
#
#  ? Lo llamamos "main" porque concentra la navegacion general del proyecto.
# =========================================================================================

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    # * Si hay usuario cargado, le mostramos sus notas privadas
    notas = []
    if g.user:
        notas = NotaPrivada.query.filter_by(user_id=g.user.id).order_by(NotaPrivada.id.desc()).all()
    return render_template("index.html", notas=notas)


@bp.get("/perfil")
@login_required
def perfil():
    return render_template("perfil.html")


@bp.post("/notas/crear")
@login_required
def crear_nota():
    # ? Este formulario es sencillo a proposito: el foco no es CRUD complejo, sino auth
    titulo = (request.form.get("titulo") or "").strip()
    contenido = (request.form.get("contenido") or "").strip()

    if not titulo:
        # ! Validacion minima para que el alumno vea el patron flash + redirect
        flash("El titulo es obligatorio.", "error")
        return redirect(url_for("main.index"))

    nota = NotaPrivada(titulo=titulo, contenido=contenido, owner=g.user)
    db.session.add(nota)
    db.session.commit()
    flash("Nota creada correctamente.", "success")
    return redirect(url_for("main.index"))
