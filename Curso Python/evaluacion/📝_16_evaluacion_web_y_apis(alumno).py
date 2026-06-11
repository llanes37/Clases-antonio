# =========================================================================================
#  EVALUACION 16 · WEB Y APIS (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  Objetivo:
#    * construir una mini API con Flask
#    * validar JSON de entrada
#    * responder con codigos HTTP correctos
#    * probar la API con `test_client()`
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: tarea    ·  # NOTE: apunte util   ·  # // evitar
#
#  Orden recomendado:
#    1) estado base
#    2) auxiliares
#    3) rutas GET
#    4) ruta POST
#    5) pruebas con cliente
# =========================================================================================

from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, request

API_KEY = "evaluacion-web-demo"


# =========================================================================================
#  SECCION 1 · ESTADO Y AUXILIARES
# =========================================================================================
def crear_estado_inicial() -> dict[str, Any]:
    # TODO:
    # - crear lista de cursos con id, titulo y plazas
    # - crear lista vacia de inscripciones
    # - guardar ultimo_id
    # NOTE:
    # No compliques la estructura; esta evaluacion mide API y validacion.
    pass


STATE = crear_estado_inicial()


def buscar_curso(curso_id: int) -> dict[str, Any] | None:
    # TODO:
    # - recorrer STATE["cursos"]
    # - devolver el curso si coincide el id
    # - devolver None si no existe
    pass


def validar_api_key(headers: dict[str, Any]) -> bool:
    # TODO:
    # - leer X-API-Key
    # - compararla con API_KEY
    pass


# =========================================================================================
#  SECCION 2 · API
# =========================================================================================
def crear_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> Any:
        # TODO:
        # - devolver {"status": "ok"}
        # - responder con 200
        pass

    @app.get("/api/cursos")
    def listar_cursos() -> Any:
        # TODO:
        # - devolver lista de cursos
        # - incluir total
        pass

    @app.post("/api/inscripciones")
    def crear_inscripcion() -> Any:
        # TODO:
        # 1. validar API key
        # 2. leer payload JSON
        # 3. extraer curso_id y alumno
        # 4. validar datos
        # 5. comprobar que el curso exista
        # 6. comprobar que queden plazas
        # 7. crear la inscripcion
        # 8. descontar plazas
        # 9. devolver 201
        #
        # ! Usa estos codigos cuando corresponda:
        # - 400 para datos invalidos
        # - 401 para API key invalida
        # - 404 para curso no encontrado
        # - 409 para falta de plazas
        pass

    return app


APP = crear_app()


# =========================================================================================
#  SECCION 3 · FLUJO FINAL
# =========================================================================================
# TODO:
# 1. crear `client = APP.test_client()`
# 2. probar `/health`
# 3. probar `/api/cursos`
# 4. probar una inscripcion valida
# 5. probar una inscripcion sin API key
#
# NOTE:
# Una buena resolucion aqui no solo devuelve algo; tambien sabe explicar por que
# cada error usa un codigo HTTP distinto.
