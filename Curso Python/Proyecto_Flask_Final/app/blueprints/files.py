"""Blueprint para subida y descarga de ficheros.
Guarda archivos en instance/uploads.

Notas didácticas:
- # * Usamos `secure_filename` para evitar nombres peligrosos
- # ! Validamos extensión y nombre
"""
import os
from flask import Blueprint, current_app, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

bp = Blueprint("files", __name__)

ALLOWED = {"txt", "md", "png", "jpg", "jpeg", "pdf"}


def _allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED


@bp.post("/upload")
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No se envió el campo 'file'"}), 400
    f = request.files["file"]
    if f.filename == "":
        return jsonify({"error": "Nombre de fichero vacío"}), 400
    if not _allowed(f.filename):
        return jsonify({"error": "Extensión no permitida"}), 400

    filename = secure_filename(f.filename)
    upload_dir = os.path.join(current_app.instance_path, current_app.config.get("UPLOAD_FOLDER_NAME", "uploads"))
    os.makedirs(upload_dir, exist_ok=True)
    path = os.path.join(upload_dir, filename)
    # ? Aquí podrías limitar el tamaño o verificar el tipo MIME si quieres ampliar
    f.save(path)
    return jsonify({"uploaded": True, "filename": filename})


@bp.get("/download/<path:filename>")
def download(filename):
    upload_dir = os.path.join(current_app.instance_path, current_app.config.get("UPLOAD_FOLDER_NAME", "uploads"))
    return send_from_directory(upload_dir, filename, as_attachment=True)
