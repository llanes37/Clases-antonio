# =========================================================================================
#  EVALUACION 16 · WEB Y APIS
#  ---------------------------------------------------------------------------------------
#  En esta evaluacion se comprueba si el alumno puede:
#    * definir rutas pequenas y claras
#    * validar un payload antes de tocar estado
#    * devolver codigos HTTP coherentes
#    * diferenciar autenticacion, validacion y negocio
#    * probar la API con un cliente sencillo
#
#  Objetivo docente:
#    * medir pensamiento web basico, no solo copiar rutas
#    * comprobar si el alumno entiende el contrato cliente-servidor
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: tarea    ·  # NOTE: apunte util   ·  # // evitar
# =========================================================================================

from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, request

API_KEY = "evaluacion-web-demo"


# =========================================================================================
#  SECCION 1 · ESTADO Y AUXILIARES
# =========================================================================================
# * El estado se mantiene en memoria para que el foco de la evaluacion sea:
#   - rutas
#   - validacion
#   - codigos HTTP
#   - lectura de JSON
def crear_estado_inicial() -> dict[str, Any]:
    return {
        "cursos": [
            {"id": 1, "titulo": "Python Base", "plazas": 5},
            {"id": 2, "titulo": "Flask Practico", "plazas": 3},
        ],
        "inscripciones": [],
        "ultimo_id": 0,
    }


STATE = crear_estado_inicial()


def buscar_curso(curso_id: int) -> dict[str, Any] | None:
    # * Localiza un curso por id.
    for curso in STATE["cursos"]:
        if curso["id"] == curso_id:
            return curso
    return None


def validar_api_key(headers: dict[str, Any]) -> bool:
    # * Mini validacion para introducir autenticacion por cabecera.
    # ! No es seguridad real; es una regla docente sencilla.
    return headers.get("X-API-Key") == API_KEY


# =========================================================================================
#  SECCION 2 · API
# =========================================================================================
def crear_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> Any:
        # * Ruta minima para comprobar que el servicio responde.
        return jsonify({"status": "ok"}), 200

    @app.get("/api/cursos")
    def listar_cursos() -> Any:
        return jsonify({"items": STATE["cursos"], "total": len(STATE["cursos"])}), 200

    @app.post("/api/inscripciones")
    def crear_inscripcion() -> Any:
        # ! Orden correcto del endpoint:
        # 1) autenticar
        # 2) leer payload
        # 3) validar tipos y reglas
        # 4) comprobar negocio
        # 5) modificar estado
        # 6) responder
        if not validar_api_key(request.headers):
            return jsonify({"error": "API key invalida"}), 401

        payload = request.get_json(silent=True) or {}
        curso_id = payload.get("curso_id")
        alumno = str(payload.get("alumno", "")).strip()

        if not isinstance(curso_id, int):
            return jsonify({"error": "curso_id debe ser entero"}), 400
        if alumno == "":
            return jsonify({"error": "alumno es obligatorio"}), 400

        curso = buscar_curso(curso_id)
        if curso is None:
            return jsonify({"error": "Curso no encontrado"}), 404
        if curso["plazas"] <= 0:
            return jsonify({"error": "No quedan plazas"}), 409

        curso["plazas"] -= 1
        STATE["ultimo_id"] += 1
        inscripcion = {
            "id": STATE["ultimo_id"],
            "curso_id": curso_id,
            "alumno": alumno,
        }
        STATE["inscripciones"].append(inscripcion)
        return jsonify(inscripcion), 201

    return app


APP = crear_app()


# =========================================================================================
#  SECCION 3 · DEMOSTRACION FINAL DEL PROFESOR
# =========================================================================================
def demo_profesor() -> None:
    client = APP.test_client()

    # * Paso 1 · healthcheck
    print("Health:", client.get("/health").status_code)

    # * Paso 2 · catalogo inicial
    print("Cursos:", client.get("/api/cursos").get_json())

    # * Paso 3 · inscripcion valida
    respuesta = client.post(
        "/api/inscripciones",
        json={"curso_id": 1, "alumno": "Ana"},
        headers={"X-API-Key": API_KEY},
    )
    print("Inscripcion valida:", respuesta.status_code, respuesta.get_json())

    # * Paso 4 · error sin API key
    error_auth = client.post(
        "/api/inscripciones",
        json={"curso_id": 1, "alumno": "Sin Token"},
    )
    print("Error auth:", error_auth.status_code, error_auth.get_json())


if __name__ == "__main__":
    demo_profesor()
