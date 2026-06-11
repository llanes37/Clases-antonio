# =========================================================================================
#  PRACTICA INTEGRADA 14_16 · WEB Y APIS APLICADAS (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  Objetivo:
#    * construir una mini API con Flask
#    * validar peticiones y cabeceras
#    * devolver respuestas JSON consistentes
#    * practicar codigos HTTP reales
#    * consumir la API con `test_client()`
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica ·  # NOTE: apunte util   ·  # // evitar
#
#  Orden recomendado:
#    1) estado inicial
#    2) auxiliares
#    3) rutas GET
#    4) ruta POST
#    5) cliente de prueba
# =========================================================================================

from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, request

API_KEY = "curso-python-demo"


# =========================================================================================
#  SECCION 1 · ESTADO Y AUXILIARES
# =========================================================================================
# * El objetivo de esta parte es dejar un estado sencillo pero suficiente para
#   poder probar varias rutas con sentido.
def crear_estado_inicial() -> dict[str, Any]:
    # TODO:
    # - crear una lista de productos con id, nombre, precio y stock
    # - crear una lista vacia de pedidos
    # - guardar un contador `ultimo_pedido_id`
    # NOTE:
    # Mantener el estado simple ayuda a que el foco siga siendo la API.
    pass


STATE = crear_estado_inicial()


def buscar_producto(producto_id: int) -> dict[str, Any] | None:
    # TODO:
    # - recorrer STATE["productos"]
    # - comparar el id recibido con cada producto
    # - devolver el producto si existe
    # - devolver None si no se encuentra
    pass


def validar_api_key(headers: dict[str, Any]) -> bool:
    # TODO:
    # - leer la cabecera X-API-Key
    # - compararla con API_KEY
    # - devolver True o False
    # ! Esta validacion es didactica, no seguridad real.
    pass


# =========================================================================================
#  SECCION 2 · API
# =========================================================================================
def crear_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> Any:
        # TODO:
        # - devolver un JSON simple
        # - incluir al menos status = "ok"
        # - responder con codigo 200
        pass

    @app.get("/api/productos")
    def listar_productos() -> Any:
        # TODO:
        # - devolver la lista de productos
        # - incluir un total
        pass

    @app.get("/api/productos/<int:producto_id>")
    def detalle_producto(producto_id: int) -> Any:
        # TODO:
        # - buscar el producto con la funcion auxiliar
        # - si no existe, devolver 404
        # - si existe, devolver su JSON
        pass

    @app.post("/api/pedidos")
    def crear_pedido() -> Any:
        # TODO:
        # 1. validar API key
        # 2. leer el payload JSON
        # 3. extraer producto_id, cantidad y cliente
        # 4. validar tipos y reglas de negocio
        # 5. comprobar si el producto existe
        # 6. comprobar si hay stock suficiente
        # 7. crear pedido y descontar stock
        # 8. devolver 201 con el pedido creado
        #
        # ! Usa estos codigos cuando toque:
        # - 400 para datos invalidos
        # - 401 para API key invalida
        # - 404 para producto no encontrado
        # - 409 para stock insuficiente
        pass

    @app.get("/api/pedidos")
    def listar_pedidos() -> Any:
        # TODO:
        # - devolver los pedidos acumulados
        # - incluir un total
        pass

    return app


APP = crear_app()


# =========================================================================================
#  SECCION 3 · PRUEBA GUIADA
# =========================================================================================
# NOTE:
# Aqui no necesitas arrancar un servidor real. Flask permite probar rutas desde
# Python usando `APP.test_client()`.
#
# TODO GUIADO:
# 1. crea `client = APP.test_client()`
# 2. llama a `/health` y muestra status + JSON
# 3. llama a `/api/productos` y revisa la estructura
# 4. intenta crear un pedido valido con API key correcta
# 5. intenta crear un pedido sin API key para ver el 401
# 6. consulta `/api/pedidos` para comprobar el resultado


# =========================================================================================
#  RETO FINAL
# =========================================================================================
# TODO FINAL:
# - anadir endpoint para actualizar stock
# - anadir filtro por nombre o precio minimo
# - separar cliente y servidor en modulos
# - escribir tests con pytest para las rutas principales
