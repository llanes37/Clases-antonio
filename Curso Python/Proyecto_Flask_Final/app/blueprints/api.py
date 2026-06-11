"""Blueprint API JSON para Curso (CRUD).
Rutas:
- GET    /api/cursos           -> listar
- GET    /api/cursos/<id>      -> detalle
- POST   /api/cursos           -> crear {titulo, descripcion, publicado}
- PUT    /api/cursos/<id>      -> actualizar
- DELETE /api/cursos/<id>      -> borrar

Notas didácticas:
- # * Validación ligera de payload en _validate_curso_payload
- # ! Evitamos explotar por JSON inválido usando get_json(silent=True)
"""
from flask import Blueprint, jsonify, request
from ..extensions import db
from ..models import Curso

bp = Blueprint("api", __name__)


def _validate_curso_payload(data: dict | None, parcial: bool = False) -> str | None:
    """Valida payload de curso.
    - parcial=True permite PUT parcial; False obliga campos mínimos.
    """
    if not isinstance(data, dict):
        return "JSON inválido"
    if not parcial:
        if "titulo" not in data:
            return "Falta 'titulo'"
    return None


@bp.get("/cursos")
def listar_cursos():
    # ? Filtros y paginación opcionales para practicar queries
    q = request.args.get("q", type=str)
    page = request.args.get("page", type=int)
    per_page = request.args.get("per_page", type=int)

    query = Curso.query
    if q:
        query = query.filter(Curso.titulo.ilike(f"%{q}%"))
    query = query.order_by(Curso.id.desc())

    # * Si el usuario pide paginación, devolvemos {items, meta}
    if page and per_page:
        p = query.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({
            "items": [c.to_dict() for c in p.items],
            "meta": {
                "page": p.page,
                "per_page": p.per_page,
                "total": p.total,
                "pages": p.pages
            }
        })

    # * Compatibilidad: sin paginación devolvemos una lista simple
    cursos = query.all()
    return jsonify([c.to_dict() for c in cursos])


@bp.get("/health")
def health():
    """Healthcheck sencillo para practicar endpoints informativos."""
    from ..models import Usuario
    cursos_count = Curso.query.count()
    usuarios_count = Usuario.query.count()
    return jsonify({
        "status": "ok",
        "cursos": cursos_count,
        "usuarios": usuarios_count
    })


@bp.get("/cursos/<int:curso_id>")
def detalle_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    return jsonify(curso.to_dict())


@bp.post("/cursos")
def crear_curso():
    data = request.get_json(silent=True) or {}
    error = _validate_curso_payload(data)
    if error:
        return jsonify({"error": error}), 400

    curso = Curso(
        titulo=data.get("titulo", ""),
        descripcion=data.get("descripcion", ""),
        publicado=bool(data.get("publicado", True)),
    )
    try:
        db.session.add(curso)
        db.session.commit()
    except Exception as e:  # ! Mantener simple para el curso (no exponer detalles)
        db.session.rollback()
        return jsonify({"error": "No se pudo crear el curso"}), 500
    return jsonify(curso.to_dict()), 201


@bp.put("/cursos/<int:curso_id>")
def actualizar_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    data = request.get_json(silent=True) or {}
    error = _validate_curso_payload(data, parcial=True)
    if error:
        return jsonify({"error": error}), 400

    # * Actualización parcial
    if "titulo" in data:
        curso.titulo = data["titulo"]
    if "descripcion" in data:
        curso.descripcion = data["descripcion"]
    if "publicado" in data:
        curso.publicado = bool(data["publicado"])
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"error": "No se pudo actualizar"}), 500
    return jsonify(curso.to_dict())


@bp.delete("/cursos/<int:curso_id>")
def borrar_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    try:
        db.session.delete(curso)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"error": "No se pudo borrar"}), 500
    return jsonify({"deleted": True, "id": curso_id})
