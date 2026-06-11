# =========================================================================================
#  EVALUACION 10 · FUNDAMENTOS
#  ---------------------------------------------------------------------------------------
#  En esta evaluacion se comprueba si el alumno puede:
#    * crear funciones pequenas y reutilizables
#    * aplicar condicionales con rangos claros
#    * recorrer listas de diccionarios sin perderse
#    * filtrar informacion con criterio
#    * construir un resumen final coherente
#
#  Objetivo docente:
#    * medir la base real del curso sin meter complejidad innecesaria
#    * comprobar si el alumno ya piensa en flujo y no solo en lineas sueltas
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: tarea    ·  # NOTE: apunte util   ·  # // evitar
# =========================================================================================

from __future__ import annotations

from typing import Any


# =========================================================================================
#  SECCION 1 · DATOS DE PARTIDA
# =========================================================================================
# * El escenario esta deliberadamente contenido.
# * Aqui no evaluamos POO ni base de datos; solo base de Python bien aplicada.
PEDIDOS = [
    {"cliente": "Ana", "producto": "Curso Python", "cantidad": 2, "precio": 29.99},
    {"cliente": "Luis", "producto": "Pack Web", "cantidad": 1, "precio": 49.50},
    {"cliente": "Marta", "producto": "Curso Python", "cantidad": 3, "precio": 29.99},
]


# =========================================================================================
#  SECCION 2 · OPERACIONES PEQUENAS
# =========================================================================================
def calcular_total_pedido(cantidad: int, precio: float) -> float:
    # * Convierte cantidad y precio en un total reutilizable.
    # NOTE:
    # Esta funcion es corta a proposito. Justo aqui se ve si el alumno entiende
    # el valor de encapsular una operacion repetible.
    return round(cantidad * precio, 2)


def clasificar_total(total: float) -> str:
    # * Traduce un numero a una etiqueta de negocio simple.
    # ! La clave no es memorizar if/elif, sino ordenar bien los rangos.
    if total >= 100:
        return "pedido_alto"
    if total >= 50:
        return "pedido_medio"
    return "pedido_bajo"


# =========================================================================================
#  SECCION 3 · TRABAJO CON COLECCIONES
# =========================================================================================
def filtrar_pedidos_por_cliente(pedidos: list[dict[str, Any]], cliente: str) -> list[dict[str, Any]]:
    # * Devuelve solo los pedidos del cliente indicado.
    # NOTE:
    # Antes de comparar texto conviene normalizarlo para evitar fallos tontos
    # por mayusculas, espacios o entradas inconsistentes.
    cliente_normalizado = cliente.strip().lower()
    return [pedido for pedido in pedidos if pedido["cliente"].lower() == cliente_normalizado]


def resumen_pedidos(pedidos: list[dict[str, Any]]) -> dict[str, Any]:
    # * Agrega varias metricas en una sola salida con sentido.
    # ? Este punto distingue a quien sabe operar con datos de quien solo imprime.
    total_pedidos = len(pedidos)
    total_unidades = sum(pedido["cantidad"] for pedido in pedidos)
    facturacion_total = round(
        sum(calcular_total_pedido(pedido["cantidad"], pedido["precio"]) for pedido in pedidos),
        2,
    )
    pedido_mayor = max(
        pedidos,
        key=lambda pedido: calcular_total_pedido(pedido["cantidad"], pedido["precio"]),
    )
    return {
        "total_pedidos": total_pedidos,
        "total_unidades": total_unidades,
        "facturacion_total": facturacion_total,
        "pedido_mayor": pedido_mayor,
    }


def mostrar_resumen(pedidos: list[dict[str, Any]]) -> None:
    # * Presenta el resumen de forma clara y legible.
    resumen = resumen_pedidos(pedidos)
    print("Resumen global:")
    print("- total de pedidos:", resumen["total_pedidos"])
    print("- total de unidades:", resumen["total_unidades"])
    print("- facturacion total:", f"{resumen['facturacion_total']:.2f} EUR")

    mayor = resumen["pedido_mayor"]
    mayor_total = calcular_total_pedido(mayor["cantidad"], mayor["precio"])
    print(
        "- pedido mayor:",
        f"{mayor['cliente']} -> {mayor['producto']} x{mayor['cantidad']} ({mayor_total:.2f} EUR)",
    )


# =========================================================================================
#  SECCION 4 · DEMOSTRACION FINAL DEL PROFESOR
# =========================================================================================
def demo_profesor() -> None:
    # * Recorre el flujo completo de la evaluacion resuelta.
    print("Detalle por pedido:")
    for pedido in PEDIDOS:
        total = calcular_total_pedido(pedido["cantidad"], pedido["precio"])
        etiqueta = clasificar_total(total)
        print(
            f"- {pedido['cliente']} | {pedido['producto']} x{pedido['cantidad']} "
            f"-> {total:.2f} EUR | {etiqueta}"
        )

    print("\nPedidos del cliente Ana:")
    for pedido in filtrar_pedidos_por_cliente(PEDIDOS, "Ana"):
        print(f"- {pedido['producto']} x{pedido['cantidad']}")

    print()
    mostrar_resumen(PEDIDOS)


if __name__ == "__main__":
    demo_profesor()
