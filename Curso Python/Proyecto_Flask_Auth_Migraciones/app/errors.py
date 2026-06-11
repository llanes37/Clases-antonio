"""Manejadores de errores centralizados."""
from __future__ import annotations

from flask import render_template

# =========================================================================================
#  ERRORES CENTRALIZADOS
#  ---------------------------------------------------------------------------------------
#  Este modulo centraliza respuestas HTML para errores comunes:
#    * 403 -> permiso denegado
#    * 404 -> ruta no encontrada
#    * 500 -> error interno del servidor
#
#  ? Ventaja didactica:
#    el alumno ve que los errores tambien forman parte de la arquitectura.
# =========================================================================================


def register_error_handlers(app) -> None:
    @app.errorhandler(403)
    def forbidden(_e):
        # ! Se lanza cuando un alumno intenta entrar en una zona de admin sin permisos
        return render_template("403.html"), 403

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(_e):
        return render_template("500.html"), 500
