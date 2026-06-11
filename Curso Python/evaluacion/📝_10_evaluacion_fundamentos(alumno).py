# =========================================================================================
#  EVALUACION 10 · FUNDAMENTOS (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  Objetivo:
#    * calcular importes correctamente
#    * clasificar pedidos por importe
#    * filtrar listas de diccionarios
#    * resumir informacion sin desorden
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: tarea    ·  # NOTE: apunte util   ·  # // evitar
#
#  Orden recomendado:
#    1) funciones pequenas
#    2) trabajo con listas
#    3) resumen final
# =========================================================================================

from __future__ import annotations

from typing import Any


# =========================================================================================
#  SECCION 1 · DATOS DE PARTIDA
# =========================================================================================
PEDIDOS = [
    {"cliente": "Ana", "producto": "Curso Python", "cantidad": 2, "precio": 29.99},
    {"cliente": "Luis", "producto": "Pack Web", "cantidad": 1, "precio": 49.50},
    {"cliente": "Marta", "producto": "Curso Python", "cantidad": 3, "precio": 29.99},
]


# =========================================================================================
#  SECCION 2 · OPERACIONES PEQUENAS
# =========================================================================================
def calcular_total_pedido(cantidad: int, precio: float) -> float:
    # TODO:
    # - multiplicar cantidad por precio
    # - redondear a 2 decimales
    # ? Pista: round(cantidad * precio, 2)
    pass


def clasificar_total(total: float) -> str:
    # TODO:
    # - si total >= 100 -> "pedido_alto"
    # - si total >= 50 -> "pedido_medio"
    # - en otro caso -> "pedido_bajo"
    # ! Esta funcion clasifica un numero; no metas aqui logica de listas.
    pass


# =========================================================================================
#  SECCION 3 · TRABAJO CON COLECCIONES
# =========================================================================================
def filtrar_pedidos_por_cliente(pedidos: list[dict[str, Any]], cliente: str) -> list[dict[str, Any]]:
    # TODO:
    # - normalizar el nombre del cliente
    # - recorrer la lista de pedidos
    # - devolver solo los que coincidan
    pass


def resumen_pedidos(pedidos: list[dict[str, Any]]) -> dict[str, Any]:
    # TODO:
    # - calcular total_pedidos
    # - calcular total_unidades
    # - calcular facturacion_total
    # - localizar pedido_mayor
    # NOTE:
    # Reutiliza `calcular_total_pedido` para no repetir la misma operacion.
    pass


def mostrar_resumen(pedidos: list[dict[str, Any]]) -> None:
    # TODO:
    # - llamar a `resumen_pedidos`
    # - imprimir el resultado de forma legible
    # ! Esta funcion presenta; no deberia recalcular todo desde cero.
    pass


# =========================================================================================
#  SECCION 4 · FLUJO FINAL
# =========================================================================================
# TODO:
# 1. recorre PEDIDOS
# 2. calcula el total de cada pedido
# 3. clasifica ese total
# 4. muestra los pedidos de Ana
# 5. muestra el resumen global
#
# NOTE:
# Una buena resolucion aqui no es la mas larga, sino la que se entiende con
# facilidad al leerla.
