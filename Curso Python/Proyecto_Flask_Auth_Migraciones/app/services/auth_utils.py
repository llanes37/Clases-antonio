"""Utilidades didacticas para autenticacion y permisos."""
from __future__ import annotations

from functools import wraps

from flask import abort, g, redirect, session, url_for

# =========================================================================================
#  UTILIDADES DE AUTH
#  ---------------------------------------------------------------------------------------
#  Este modulo concentra las piezas reutilizables de autenticacion:
#    * guardar usuario en sesion
#    * cerrar sesion
#    * proteger rutas privadas
#    * proteger rutas de admin
#
#  ? Mantener esto fuera de los blueprints simplifica mucho la lectura.
# =========================================================================================


def login_user(user) -> None:
    # * Guardamos solo el user_id en sesion, no el objeto completo
    session["user_id"] = user.id


def logout_user() -> None:
    # * Cerramos sesion eliminando la clave
    session.pop("user_id", None)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        # ! Si no hay usuario cargado en g, redirigimos al login
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        # * Primer filtro: debe existir sesion
        if g.user is None:
            return redirect(url_for("auth.login"))
        # * Segundo filtro: debe tener rol admin
        if not g.user.is_admin():
            abort(403)
        return view(*args, **kwargs)

    return wrapped
