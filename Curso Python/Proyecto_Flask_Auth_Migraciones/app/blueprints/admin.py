"""Blueprint de administracion sencillo protegido por rol."""
from __future__ import annotations

from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..extensions import db
from ..models import User
from ..services.auth_utils import admin_required

# =========================================================================================
#  BLUEPRINT ADMIN
#  ---------------------------------------------------------------------------------------
#  Este modulo demuestra:
#    * control de acceso por rol
#    * panel de gestion sencillo
#    * cambios de estado y rol sobre usuarios
#
#  ! No es un admin "completo" tipo Django Admin. Es un panel didactico y pequeño.
# =========================================================================================

bp = Blueprint("admin", __name__)


@bp.get("/admin")
@admin_required
def panel():
    # * Vista principal del panel de administracion
    usuarios = User.query.order_by(User.id.asc()).all()
    return render_template("admin.html", usuarios=usuarios)


@bp.post("/admin/toggle/<int:user_id>")
@admin_required
def toggle_user(user_id: int):
    # ? Activar/desactivar es una forma simple de introducir estados de usuario
    user = User.query.get_or_404(user_id)
    user.activo = not user.activo
    db.session.commit()
    flash(f"Estado de {user.email} actualizado.", "success")
    return redirect(url_for("admin.panel"))


@bp.post("/admin/role/<int:user_id>")
@admin_required
def change_role(user_id: int):
    # * Cambio de rol manual para practicar permisos
    user = User.query.get_or_404(user_id)
    new_role = (request.form.get("role") or "student").strip()
    if new_role not in {"student", "admin"}:
        flash("Rol no valido.", "error")
        return redirect(url_for("admin.panel"))
    user.role = new_role
    db.session.commit()
    flash(f"Rol de {user.email} actualizado a {new_role}.", "success")
    return redirect(url_for("admin.panel"))
