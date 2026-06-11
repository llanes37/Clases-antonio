"""Manejadores de errores globales.
- Devuelven HTML para navegación web y JSON para la API.

Regla simple:
- # * Si la ruta empieza por /api -> JSON
- # ? Si el cliente pide application/json (cabeceras Accept) -> JSON
"""
from flask import jsonify, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge

# * Detección simple: si el cliente pide JSON o la ruta empieza con /api

def wants_json_response() -> bool:
    """Determina si la respuesta preferida es JSON.

    # * Usamos best_match para evitar KeyError y comparar preferencias.
    """
    if request.path.startswith("/api"):
        return True
    best = request.accept_mimetypes.best
    return best == "application/json"


def register_error_handlers(app):
    @app.errorhandler(404)
    def handle_404(err):
        if wants_json_response():
            return jsonify({"error": "Recurso no encontrado", "status": 404}), 404
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def handle_500(err):
        # ! No exponer detalles de error en producción
        if wants_json_response():
            return jsonify({"error": "Error interno del servidor", "status": 500}), 500
        return render_template("500.html"), 500

    @app.errorhandler(RequestEntityTooLarge)
    def handle_413(err):
        # * Ocurre cuando se supera MAX_CONTENT_LENGTH
        msg = {"error": "Archivo demasiado grande", "status": 413}
        if wants_json_response():
            return jsonify(msg), 413
        # ? Reutilizamos la plantilla 500 para simplicidad en el curso
        return render_template("500.html"), 413
