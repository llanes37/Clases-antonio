# =========================================================================================
#  FLASK (PARTE 2): SESIONES + FLASH + BLUEPRINTS + CSRF (SEGURIDAD BÁSICA)
#  -----------------------------------------------------------------------------------------
#  En esta clase practicarás:
#    * session: "recordar" al usuario (login sencillo)
#    * flash: mensajes de éxito/error (feedback)
#    * blueprints: organizar la app (auth / pages / api)
#    * CSRF token: proteger formularios POST (sin librerías externas)
#    * abort + códigos HTTP correctos (400/401/403/404)
#
#  Requisitos:
#    - Python 3.8+
#    - Flask: pip install flask
#
#  Cómo usar (Windows):
#    1) python -m venv .venv
#    2) .\.venv\Scripts\Activate.ps1
#    3) pip install flask
#    4) python "cursos/Curso Python/14_flask_parte2_sesiones_y_seguridad.py"
#    5) http://127.0.0.1:5000/
#
#  Better Comments:
#    # ! importante   # * foco/definición   # ? idea/nota
#    # TODO: práctica # NOTE: apunte útil    # // deprecated
# 
#  ✅ Objetivo didáctico:
#    Este archivo está diseñado para leerse de ARRIBA a ABAJO, como el tutorial anterior.
#    Mantiene todo en un solo .py (plantillas incluidas) para que el alumno no se pierda.
# 
#  ⚠️ Nota de seguridad:
#    - Esto es una demo. No es un sistema de login real (no hay contraseña).
#    - El CSRF está implementado "a mano" para aprender el concepto.
#    - En proyectos reales se usan extensiones (Flask-WTF) y usuarios en BD.
# =========================================================================================

from __future__ import annotations

import os
import secrets
from typing import Any, Dict, List, Optional

from flask import (
    Blueprint,
    Flask,
    abort,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from jinja2 import DictLoader

# =========================================================================================
#  SECCIÓN 1 — Configuración base (debug, secret_key)
# =========================================================================================
DEBUG_MODE = True
ECHO_LOGS = True

# ! En producción: usa una SECRET_KEY fuerte (variable de entorno)
#   PowerShell (sesión actual):   $env:FLASK_SECRET_KEY="..."
#   PowerShell (persistente):     setx FLASK_SECRET_KEY "..."
# 
# ? ¿Para qué sirve SECRET_KEY?
#   Flask firma (y opcionalmente cifra en otros sistemas) cookies como la de sesión.
#   Sin SECRET_KEY no hay sesiones seguras, ni flash, ni CSRF por sesión.
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")


def pause_if(msg: str) -> None:
    """Pausa opcional para demos (si quieres parar entre secciones).
    
    # ? Útil si estás dando clase y quieres:
      - explicar un concepto antes de seguir probando
      - que los alumnos prueben una URL concreta
    
    # * Activación:
      PowerShell: $env:PAUSE_ON_DEMO="true"
    """
    if os.environ.get("PAUSE_ON_DEMO", "").lower() in {"1", "true", "yes"}:
        input(f"\nPAUSA: {msg} (Enter para continuar) ")


# =========================================================================================
#  SECCIÓN 2 — Crear la app Flask
# =========================================================================================
# ? Flask(__name__):
#   - Crea la instancia de aplicación.
#   - __name__ ayuda a Flask a localizar recursos (templates/static) si los tuviéramos en disco.
app = Flask(__name__)
app.config.update(
    DEBUG=DEBUG_MODE,
    SECRET_KEY=SECRET_KEY,
    JSON_AS_ASCII=False,
)


# =========================================================================================
#  SECCIÓN 3 — Plantillas en memoria (DictLoader)
# =========================================================================================
# ? En un proyecto real:
#   - templates/base.html, templates/login.html, etc.
#   - static/css, static/js...
# 
# * En este curso (modo didáctico):
#   - Guardamos HTML en strings
#   - Jinja2 las carga desde un dict (DictLoader)
#   - Resultado: 1 archivo ejecutable, fácil de seguir
TEMPLATES: Dict[str, str] = {
    "base.html": """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title or "Flask Parte 2" }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body { font-family: "Segoe UI", sans-serif; }
      .container { max-width: 1000px; }
      code { background: #f6f6f6; padding: 2px 6px; border-radius: 6px; }
    </style>
  </head>
  <body class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="{{ url_for('pages.home') }}">Flask Parte 2</a>
        <div class="d-flex gap-2">
          <a class="btn btn-sm btn-outline-light" href="{{ url_for('pages.todos') }}">Tareas</a>
          <a class="btn btn-sm btn-outline-light" href="{{ url_for('pages.profile') }}">Perfil</a>

          {% if g.user %}
            <form method="post" action="{{ url_for('auth.logout') }}" class="d-inline">
              <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
              <button class="btn btn-sm btn-warning" type="submit">Logout</button>
            </form>
          {% else %}
            <a class="btn btn-sm btn-success" href="{{ url_for('auth.login') }}">Login</a>
          {% endif %}
        </div>
      </div>
    </nav>

    <main class="container py-4">
      {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
          <div class="mb-3">
            {% for category, message in messages %}
              <div class="alert alert-{{ category }} mb-2" role="alert">{{ message }}</div>
            {% endfor %}
          </div>
        {% endif %}
      {% endwith %}

      {% block content %}{% endblock %}
    </main>
  </body>
</html>
""",
    "home.html": """{% extends "base.html" %}
{% block content %}
  <div class="p-4 bg-white rounded shadow-sm">
    <h1 class="h3 mb-2">Continuación de Flask</h1>
    <p class="text-muted mb-3">
      Aquí practicamos <code>session</code>, <code>flash</code>, <code>blueprints</code> y un CSRF token básico.
    </p>

    <ul class="mb-3">
      <li><a href="{{ url_for('auth.login') }}">Login</a> (crea sesión)</li>
      <li><a href="{{ url_for('pages.todos') }}">Tareas</a> (CRUD en memoria en la sesión)</li>
      <li><a href="{{ url_for('pages.profile') }}">Perfil</a> (ruta protegida)</li>
      <li><a href="{{ url_for('api.health') }}">API health</a> (JSON)</li>
    </ul>

    <div class="alert alert-info mb-0">
      <strong>Tip:</strong> abre DevTools (F12) → Network para ver GET/POST.
    </div>
  </div>
{% endblock %}
""",
    "login.html": """{% extends "base.html" %}
{% block content %}
  <div class="row">
    <div class="col-md-6">
      <div class="p-4 bg-white rounded shadow-sm">
        <h1 class="h4 mb-3">Login (simple)</h1>
        <form method="post" action="{{ url_for('auth.login', next=next_url) }}">
          <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
          <div class="mb-3">
            <label class="form-label">Nombre de usuario</label>
            <input class="form-control" type="text" name="username" placeholder="ej: ada" autofocus>
            <div class="form-text">Demo didáctica: no hay contraseña.</div>
          </div>
          <button class="btn btn-success" type="submit">Entrar</button>
          <a class="btn btn-outline-secondary" href="{{ url_for('pages.home') }}">Cancelar</a>
        </form>
      </div>
    </div>
  </div>
{% endblock %}
""",
    "profile.html": """{% extends "base.html" %}
{% block content %}
  <div class="p-4 bg-white rounded shadow-sm">
    <h1 class="h4 mb-2">Perfil</h1>
    <p class="mb-0">Usuario actual: <strong>{{ g.user }}</strong></p>
  </div>
{% endblock %}
""",
    "todos.html": """{% extends "base.html" %}
{% block content %}
  <div class="p-4 bg-white rounded shadow-sm">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h1 class="h4 mb-0">Tareas (en sesión)</h1>
      <a class="btn btn-sm btn-outline-primary" href="{{ url_for('api.todos') }}">Ver JSON</a>
    </div>

    <form method="post" action="{{ url_for('pages.todos_add') }}" class="row g-2 mb-3">
      <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
      <div class="col-md-9">
        <input class="form-control" name="texto" placeholder="Escribe una tarea..." />
      </div>
      <div class="col-md-3 d-grid">
        <button class="btn btn-primary" type="submit">Añadir</button>
      </div>
    </form>

    {% if todos %}
      <ul class="list-group">
        {% for item in todos %}
          <li class="list-group-item d-flex justify-content-between align-items-center">
            <span>{{ loop.index }}. {{ item }}</span>
            <form method="post" action="{{ url_for('pages.todos_delete', idx=loop.index0) }}" class="d-inline">
              <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
              <button class="btn btn-sm btn-outline-danger" type="submit">Borrar</button>
            </form>
          </li>
        {% endfor %}
      </ul>
    {% else %}
      <div class="alert alert-secondary mb-0">No hay tareas todavía.</div>
    {% endif %}
  </div>
{% endblock %}
""",
}

app.jinja_loader = DictLoader(TEMPLATES)


# =========================================================================================
#  SECCIÓN 4 — Helpers (sesión, CSRF, validaciones)
# =========================================================================================
# ? Aquí concentramos funciones "utilidad":
#   - get_todos(): lista de tareas en la sesión
#   - get_csrf_token(): token CSRF por sesión
#   - require_csrf(): valida POST
#   - require_login(): protege páginas privadas
#   - normalize_username(): validación simple
# 
# ! Importante:
#   La sesión de Flask (por defecto) se guarda en cookie firmada.
#   No metas objetos enormes o datos secretos.
def get_todos() -> List[str]:
    """Devuelve la lista de tareas guardada en sesión (si no existe, la crea)."""
    todos = session.get("todos")
    if not isinstance(todos, list):
        session["todos"] = []
    return session["todos"]


def get_csrf_token() -> str:
    """Genera/recupera un CSRF token por sesión."""
    token = session.get("csrf_token")
    if not isinstance(token, str) or len(token) < 16:
        # * token_urlsafe: aleatorio, seguro y cómodo para usar en HTML
        token = secrets.token_urlsafe(32)
        session["csrf_token"] = token
    return token


def require_csrf() -> None:
    """Valida CSRF en formularios POST."""
    # ? ¿Qué es CSRF?
    #   Cross-Site Request Forgery: una web maliciosa intenta hacer un POST a tu app
    #   aprovechando que el usuario ya está logueado (y su navegador envía cookies).
    #
    # * Solución:
    #   - Token aleatorio guardado en sesión
    #   - Se envía en el formulario (input hidden)
    #   - Se valida en el POST
    form_token = request.form.get("csrf_token", "")
    session_token = session.get("csrf_token", "")
    if not (isinstance(session_token, str) and session_token and form_token == session_token):
        abort(400, description="CSRF token inválido o ausente")


def require_login() -> str:
    """Asegura que hay usuario logueado; si no, redirige a login."""
    # NOTE: Esta función devuelve:
    #   - str (username) si está logueado
    #   - Response redirect si NO está logueado
    #
    # ! Esto es útil en rutas HTML (pages), pero en API devolveremos 401 JSON.
    user = session.get("user")
    if isinstance(user, str) and user:
        return user
    flash("Necesitas iniciar sesión para entrar aquí.", "warning")
    return redirect(url_for("auth.login", next=request.path))  # type: ignore[return-value]


def normalize_username(raw: str) -> Optional[str]:
    """Valida el nombre de usuario (demo). Devuelve el username limpio o None."""
    # TODO: Reto: añade más reglas (solo letras/números, sin espacios, etc.)
    username = raw.strip()
    if not username:
        return None
    if len(username) < 3:
        return None
    if len(username) > 30:
        return None
    return username


def safe_next_url(value: Optional[str]) -> str:
    """Evita open-redirects: solo permitimos rutas relativas (/algo)."""
    # ? Open redirect:
    #   Si aceptas "next=https://evil.com", un atacante puede usar TU dominio
    #   para redirigir a una web maliciosa.
    #
    # * Regla didáctica:
    #   - Permitimos solo rutas internas que empiecen por "/" y no por "//"
    if not value:
        return url_for("pages.home")
    if value.startswith("/") and not value.startswith("//"):
        return value
    return url_for("pages.home")


# =========================================================================================
#  SECCIÓN 5 — Hooks (before_request, after_request, context_processor)
# =========================================================================================
@app.before_request
def load_user_and_csrf() -> None:
    # * Guardamos el usuario en g para usarlo en plantillas sin pasar variables siempre
    # ? g = "global" por request (vive solo durante una petición)
    user = session.get("user")
    g.user = user if isinstance(user, str) and user else None  # type: ignore[attr-defined]

    # * Aseguramos CSRF token disponible para plantillas y POSTs
    g.csrf_token = get_csrf_token()  # type: ignore[attr-defined]

    if ECHO_LOGS:
        # NOTE: En apps reales usarías logging, no print()
        print(f"[REQ] {request.method} {request.path}")


@app.after_request
def add_headers(response):  # type: ignore[no-untyped-def]
    response.headers.setdefault("X-Curso", "Flask-Parte-2")
    return response


@app.context_processor
def inject_globals() -> Dict[str, Any]:
    # * Inyecta variables globales a TODAS las plantillas
    # ? Ejemplo: csrf_token disponible sin pasarlo manualmente en cada render_template(...)
    return {"csrf_token": get_csrf_token()}


# =========================================================================================
#  SECCIÓN 6 — Blueprints (organización de la app)
# =========================================================================================
# ? ¿Por qué blueprints?
#   Cuando una app crece, tener 200 rutas en un solo archivo es un caos.
#   Un blueprint te permite separar por "área":
#     - auth: login/logout
#     - pages: HTML
#     - api: JSON
pages = Blueprint("pages", __name__)
auth = Blueprint("auth", __name__, url_prefix="/auth")
api = Blueprint("api", __name__, url_prefix="/api")


# =========================================================================================
#  SECCIÓN 7 — Pages (HTML)
# =========================================================================================
@pages.get("/")
def home():
    return render_template("home.html", title="Home")


@pages.get("/perfil")
def profile():
    # * Ruta protegida: requiere login
    maybe_redirect = require_login()
    if not isinstance(maybe_redirect, str):
        return maybe_redirect
    return render_template("profile.html", title="Perfil")


@pages.get("/tareas")
def todos():
    # * Ruta protegida: requiere login
    maybe_redirect = require_login()
    if not isinstance(maybe_redirect, str):
        return maybe_redirect
    return render_template("todos.html", title="Tareas", todos=get_todos())


@pages.post("/tareas/add")
def todos_add():
    # * Acciones que modifican estado deben ser POST y deben validar CSRF
    maybe_redirect = require_login()
    if not isinstance(maybe_redirect, str):
        return maybe_redirect
    require_csrf()

    text = request.form.get("texto", "").strip()
    if not text:
        flash("La tarea no puede estar vacía.", "danger")
        return redirect(url_for("pages.todos"))

    get_todos().append(text)
    flash("Tarea añadida.", "success")
    return redirect(url_for("pages.todos"))


@pages.post("/tareas/delete/<int:idx>")
def todos_delete(idx: int):
    # * Borrado: POST + CSRF + validación de índice
    maybe_redirect = require_login()
    if not isinstance(maybe_redirect, str):
        return maybe_redirect
    require_csrf()

    todos_list = get_todos()
    if idx < 0 or idx >= len(todos_list):
        abort(404, description="No existe esa tarea")
    deleted = todos_list.pop(idx)
    flash(f"Tarea borrada: {deleted}", "info")
    return redirect(url_for("pages.todos"))


# =========================================================================================
#  SECCIÓN 8 — Auth (login/logout)
# =========================================================================================
@auth.get("/login")
def login():
    # ? next = "a dónde volver" después del login
    next_url = safe_next_url(request.args.get("next"))
    return render_template("login.html", title="Login", next_url=next_url)


@auth.post("/login")
def login_post():
    # ! Login con POST:
    #   - valida CSRF
    #   - valida username
    #   - crea session["user"]
    require_csrf()

    username = normalize_username(request.form.get("username", ""))
    if not username:
        flash("Usuario inválido (mínimo 3 caracteres).", "danger")
        return redirect(url_for("auth.login", next=safe_next_url(request.args.get("next"))))

    session["user"] = username
    flash(f"Bienvenido, {username}.", "success")
    pause_if("Haz clic en Perfil o Tareas")
    return redirect(safe_next_url(request.args.get("next")))


@auth.post("/logout")
def logout():
    # ! Logout también debe ser POST y debe validar CSRF
    require_csrf()
    session.pop("user", None)
    flash("Has cerrado sesión.", "info")
    return redirect(url_for("pages.home"))


# =========================================================================================
#  SECCIÓN 9 — API (JSON)
# =========================================================================================
@api.get("/health")
def health():
    # * Endpoint de salud (útil para comprobar que el server está vivo)
    # ? Devuelve:
    #   - ok: bool
    #   - user: username o None
    #   - todos_count: cuántas tareas tiene el usuario (si está logueado)
    return jsonify(
        ok=True,
        user=g.user,
        todos_count=len(get_todos()) if g.user else 0,
    )


@api.get("/tareas")
def todos_api_get():
    maybe_redirect = require_login()
    if not isinstance(maybe_redirect, str):
        # ! En API: preferimos 401 JSON en lugar de redirect HTML
        return jsonify(ok=False, error="unauthorized"), 401
    return jsonify(ok=True, todos=get_todos())


@api.post("/tareas")
def todos_api_post():
    # * POST JSON: {"texto": "..." }
    # ! Nota:
    #   Para APIs reales, también usarías:
    #     - autenticación (token / jwt)
    #     - rate limiting
    #     - validación de esquemas (pydantic)
    maybe_redirect = require_login()
    if not isinstance(maybe_redirect, str):
        return jsonify(ok=False, error="unauthorized"), 401

    data = request.get_json(silent=True) or {}
    if not isinstance(data, dict):
        return jsonify(ok=False, error="invalid_json"), 400

    text = str(data.get("texto", "")).strip()
    if not text:
        return jsonify(ok=False, error="texto_required"), 400

    get_todos().append(text)
    return jsonify(ok=True, todos=get_todos()), 201


# =========================================================================================
#  SECCIÓN 10 — Errores (HTML vs JSON)
# =========================================================================================
# ? Idea:
#   - Si la ruta empieza por /api o el cliente pide JSON -> devolvemos JSON
#   - En rutas normales -> devolvemos HTML sencillo
# 
# NOTE: En una app real tendrías templates 404.html, 500.html, etc.
@app.errorhandler(400)
def err_400(error):  # type: ignore[no-untyped-def]
    if request.path.startswith("/api/") or request.accept_mimetypes.best == "application/json":
        return (
            jsonify(ok=False, error="bad_request", detail=str(getattr(error, "description", error))),
            400,
        )
    return (
        f"<h1>400 Bad Request</h1><p>{getattr(error, 'description', error)}</p>",
        400,
        {"Content-Type": "text/html; charset=utf-8"},
    )


@app.errorhandler(403)
def err_403(error):  # type: ignore[no-untyped-def]
    if request.path.startswith("/api/") or request.accept_mimetypes.best == "application/json":
        return (
            jsonify(ok=False, error="forbidden", detail=str(getattr(error, "description", error))),
            403,
        )
    return (
        f"<h1>403 Forbidden</h1><p>{getattr(error, 'description', error)}</p>",
        403,
        {"Content-Type": "text/html; charset=utf-8"},
    )


@app.errorhandler(404)
def err_404(error):  # type: ignore[no-untyped-def]
    if request.path.startswith("/api/") or request.accept_mimetypes.best == "application/json":
        return (
            jsonify(ok=False, error="not_found", detail=str(getattr(error, "description", error))),
            404,
        )
    return (
        f"<h1>404 Not Found</h1><p>{getattr(error, 'description', error)}</p>",
        404,
        {"Content-Type": "text/html; charset=utf-8"},
    )


# =========================================================================================
#  SECCIÓN 11 — Registro de blueprints + ejecución
# =========================================================================================
app.register_blueprint(pages)
app.register_blueprint(auth)
app.register_blueprint(api)

# TODO: Prácticas sugeridas (para alumnos)
#   1) Añade una ruta /admin que solo funcione si g.user == "admin" (si no, 403)
#   2) Añade endpoint POST /api/logout (devuelva 200) y decide si debe requerir CSRF
#   3) Añade "completado" a las tareas (en vez de solo strings) y actualiza HTML/JSON
#   4) Implementa "limpiar todas las tareas" con POST + CSRF


if __name__ == "__main__":
    print("=" * 80)
    print("Flask Parte 2 iniciándose…")
    print("URL: http://127.0.0.1:5000/")
    print("=" * 80)
    app.run(debug=DEBUG_MODE)
