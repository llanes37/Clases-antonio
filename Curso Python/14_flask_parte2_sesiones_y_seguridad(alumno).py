# =========================================================================================
#  FLASK PARTE 2 · SESIONES Y SEGURIDAD (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  En esta plantilla trabajaras:
#    * sesiones
#    * login basico
#    * proteccion CSRF
#    * validacion de formularios
#    * API JSON sencilla
#
#  Objetivo:
#    * entender que una app web no es solo mostrar HTML
#    * practicar proteccion basica antes de tocar datos sensibles
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica ·  # NOTE: apunte util   ·  # // evitar
#
#  Como ejecutar:
#    pip install flask
#    python "cursos/Curso Python/14_flask_parte2_sesiones_y_seguridad(alumno).py"
# =========================================================================================

from __future__ import annotations

import os
import secrets
from typing import Any, List, Optional

from flask import (
    Blueprint,
    Flask,
    abort,
    flash,
    g,
    jsonify,
    redirect,
    render_template_string,
    request,
    session,
    url_for,
)

DEBUG_MODE = True
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")

app = Flask(__name__)
app.config.update(SECRET_KEY=SECRET_KEY, JSON_AS_ASCII=False)


# =========================================================================================
#  SECCION 1 · HELPERS
# =========================================================================================
# * Estas funciones concentran tareas repetidas para que las rutas queden
#   mas limpias y mas faciles de entender.
def get_todos() -> List[str]:
    todos = session.get("todos")
    if not isinstance(todos, list):
        session["todos"] = []
    return session["todos"]


def get_csrf_token() -> str:
    # * Genera o recupera un token CSRF desde sesion.
    token = session.get("csrf_token")
    if not isinstance(token, str) or len(token) < 16:
        token = secrets.token_urlsafe(32)
        session["csrf_token"] = token
    return token


def require_csrf() -> None:
    # TODO:
    # - leer request.form["csrf_token"] o request.form.get("csrf_token")
    # - compararlo con session["csrf_token"]
    # - si no coincide, abort(400, description="CSRF token invalido o ausente")
    # ! Valida el token antes de modificar datos.
    pass


def normalize_username(raw: str) -> Optional[str]:
    # TODO:
    # - aplicar strip()
    # - comprobar que no este vacio
    # - comprobar minimo 3 caracteres
    # - comprobar maximo 30
    # - devolver el username normalizado o None
    pass


def require_login() -> str:
    # * Si no hay usuario en sesion, redirige al login.
    user = session.get("user")
    if isinstance(user, str) and user:
        return user
    flash("Necesitas iniciar sesion.", "warning")
    return redirect(url_for("auth.login", next=request.path))  # type: ignore[return-value]


# =========================================================================================
#  SECCION 2 · HOOKS
# =========================================================================================
@app.before_request
def load_user() -> None:
    # * Dejamos datos comunes preparados en `g` para todas las vistas.
    user = session.get("user")
    g.user = user if isinstance(user, str) and user else None  # type: ignore[attr-defined]
    g.csrf_token = get_csrf_token()  # type: ignore[attr-defined]


# =========================================================================================
#  SECCION 3 · BLUEPRINTS Y PLANTILLA BASE
# =========================================================================================
pages = Blueprint("pages", __name__)
auth = Blueprint("auth", __name__, url_prefix="/auth")
api = Blueprint("api", __name__, url_prefix="/api")

BASE = """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>{{ title }}</title>
  </head>
  <body>
    {% with msgs = get_flashed_messages(with_categories=true) %}
      {% for c, m in msgs %}<p><strong>{{ c }}:</strong> {{ m }}</p>{% endfor %}
    {% endwith %}
    <p>
      <a href="{{ url_for('pages.home') }}">Home</a> |
      <a href="{{ url_for('pages.todos') }}">Tareas</a> |
      <a href="{{ url_for('auth.login') }}">Login</a>
    </p>
    <hr>
    {{ body|safe }}
  </body>
</html>
"""


def render_page(title: str, body: str):
    return render_template_string(BASE, title=title, body=body)


# =========================================================================================
#  SECCION 4 · RUTAS WEB
# =========================================================================================
@pages.get("/")
def home():
    return render_page("Home", "<h1>Flask Parte 2 (Alumno)</h1>")


@pages.get("/tareas")
def todos():
    maybe = require_login()
    if not isinstance(maybe, str):
        return maybe

    body = """
      <h2>Tareas</h2>
      <form method="post" action="{{ url_for('pages.todos_add') }}">
        <input type="hidden" name="csrf_token" value="{{ g.csrf_token }}">
        <input name="texto" placeholder="tarea...">
        <button type="submit">Anadir</button>
      </form>
      <ul>
        {% for t in todos %}<li>{{ t }}</li>{% endfor %}
      </ul>
    """
    return render_template_string(BASE, title="Tareas", body=body, todos=get_todos())


@pages.post("/tareas/add")
def todos_add():
    maybe = require_login()
    if not isinstance(maybe, str):
        return maybe

    # TODO:
    # - activar CSRF llamando a require_csrf()
    # - leer request.form["texto"]
    # - validar que no este vacio
    # - guardar la tarea en sesion
    # - redirigir a la lista
    pass


# =========================================================================================
#  SECCION 5 · LOGIN
# =========================================================================================
@auth.get("/login")
def login():
    next_url = request.args.get("next") or url_for("pages.home")
    body = """
      <h2>Login</h2>
      <form method="post" action="{{ url_for('auth.login_post', next=next_url) }}">
        <input type="hidden" name="csrf_token" value="{{ g.csrf_token }}">
        <input name="username" placeholder="usuario">
        <button type="submit">Entrar</button>
      </form>
    """
    return render_template_string(BASE, title="Login", body=body, next_url=next_url)


@auth.post("/login")
def login_post():
    # TODO:
    # - activar CSRF
    # - leer username del formulario
    # - validar con normalize_username()
    # - si es valido, guardarlo en session["user"]
    # - redirigir al destino `next` o a home
    pass


# =========================================================================================
#  SECCION 6 · API JSON
# =========================================================================================
@api.post("/tareas")
def api_tareas_post():
    # TODO:
    # - comprobar que exista usuario en sesion; si no, devolver 401 JSON
    # - leer payload JSON con request.get_json(silent=True)
    # - extraer `texto`
    # - validar que no este vacio; si falla, devolver 400 JSON
    # - anadir la tarea
    # - devolver 201 con la lista completa
    # ! Aqui no devolvemos HTML; devolvemos JSON con codigos HTTP coherentes.
    return jsonify(ok=False, error="TODO"), 501


app.register_blueprint(pages)
app.register_blueprint(auth)
app.register_blueprint(api)


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)
