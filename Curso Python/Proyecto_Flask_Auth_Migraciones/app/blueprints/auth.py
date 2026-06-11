"""Blueprint de autenticacion con sesiones."""
from __future__ import annotations

from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..extensions import db
from ..models import User
from ..services.auth_utils import login_user, logout_user

# =========================================================================================
#  BLUEPRINT DE AUTH
#  ---------------------------------------------------------------------------------------
#  Aqui viven las rutas de:
#    * registro
#    * login
#    * logout
#
#  * Este es el corazon didactico del proyecto:
#    enseña validacion, hash de passwords y sesiones.
# =========================================================================================

bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # * Leer y normalizar datos del formulario
        nombre = (request.form.get("nombre") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""

        if not nombre or not email or not password:
            flash("Nombre, email y password son obligatorios.", "error")
            return render_template("register.html")

        if User.query.filter_by(email=email).first():
            # ! Regla de negocio: email unico
            flash("Ese email ya existe.", "error")
            return render_template("register.html")

        user = User(nombre=nombre, email=email, role="student")
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Usuario registrado correctamente. Ya puedes iniciar sesion.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # * Buscar usuario activo y comprobar password
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""

        user = User.query.filter_by(email=email, activo=True).first()
        if user is None or not user.check_password(password):
            # ! No damos demasiados detalles para no filtrar informacion innecesaria
            flash("Credenciales incorrectas.", "error")
            return render_template("login.html")

        login_user(user)
        flash(f"Bienvenido, {user.nombre}.", "success")
        return redirect(url_for("main.index"))

    return render_template("login.html")


@bp.get("/logout")
def logout():
    logout_user()
    flash("Sesion cerrada correctamente.", "success")
    return redirect(url_for("main.index"))
