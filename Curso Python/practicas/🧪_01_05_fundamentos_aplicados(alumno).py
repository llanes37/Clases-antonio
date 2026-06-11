# =========================================================================================
#  🧪 PRACTICA INTEGRADA 01_05 · FUNDAMENTOS APLICADOS (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  📘 Objetivo:
#    * completar un gestor de inventario sencillo en memoria
#    * practicar funciones, listas, diccionarios y validaciones
#    * entender un flujo pequeño de principio a fin
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica ·  # NOTE: apunte útil   ·  # // evitar
#
#  ? Regla de trabajo:
#    1) resuelve función a función
#    2) prueba cada parte
#    3) no mires la solución completa demasiado pronto
# =========================================================================================

from __future__ import annotations

from typing import Any


# =========================================================================================
#  SECCION 1 · DATOS BASE
# =========================================================================================
INVENTARIO_INICIAL = [
    {"id": 1, "nombre": "Teclado", "categoria": "perifericos", "precio": 29.99, "stock": 8},
    {"id": 2, "nombre": "Raton", "categoria": "perifericos", "precio": 15.50, "stock": 12},
    {"id": 3, "nombre": "Monitor", "categoria": "pantallas", "precio": 189.00, "stock": 4},
]


# =========================================================================================
#  SECCION 2 · OPERACIONES BASICAS
# =========================================================================================
# * Paso 1
# Crea una copia del inventario para no tocar los datos iniciales.
# ? Pista: recorre INVENTARIO_INICIAL y usa `.copy()` en cada diccionario.
def clonar_inventario() -> list[dict[str, Any]]:
    # TODO: devuelve una copia del inventario inicial
    pass


# * Paso 2
# Busca un producto por su id y devuelve el diccionario correspondiente.
# Si no lo encuentras, devuelve None.
def buscar_producto(items: list[dict[str, Any]], producto_id: int) -> dict[str, Any] | None:
    # TODO: busca por id y devuelve el producto
    pass


# * Paso 3
# Muestra el inventario de forma legible.
def listar_productos(items: list[dict[str, Any]]) -> None:
    # TODO: muestra nombre, precio y stock
    pass


# * Paso 4
# Agrega un producto nuevo.
def agregar_producto(
    items: list[dict[str, Any]],
    nombre: str,
    categoria: str,
    precio: float,
    stock: int,
) -> None:
    # TODO:
    # - calcular nuevo id
    # - validar datos
    # - crear diccionario
    # - anadirlo a items
    pass


# * Paso 5
# Registra una venta.
# Si el producto no existe o no hay stock suficiente, devuelve None.
def vender_producto(items: list[dict[str, Any]], producto_id: int, cantidad: int) -> float | None:
    # TODO:
    # - localizar producto
    # - validar stock
    # - restar stock
    # - devolver total
    pass


# =========================================================================================
#  SECCION 3 · ANALISIS DEL INVENTARIO
# =========================================================================================
# * Paso 6
# Devuelve una lista con los productos cuyo stock sea menor o igual al limite.
def mostrar_bajo_stock(items: list[dict[str, Any]], limite: int = 5) -> list[dict[str, Any]]:
    # TODO: devuelve productos con stock <= limite
    pass


# * Paso 7
# Calcula informacion agregada del inventario.
def mostrar_estadisticas(items: list[dict[str, Any]]) -> None:
    # TODO: calcula total de productos, unidades y valor de inventario
    pass


# =========================================================================================
#  PRUEBA GUIADA
# =========================================================================================
# ! Si algo falla, prueba cada paso por separado. En este bloque casi todos los
# errores importantes se detectan antes de llegar al final.
# TODO:
# 1. crea items = clonar_inventario()
# 2. agrega un producto
# 3. vende unidades
# 4. muestra productos con bajo stock
# 5. muestra estadisticas


# =========================================================================================
#  RETO FINAL
# =========================================================================================
# TODO FINAL:
# - filtrar por categoria
# - actualizar precio
# - mostrar top 3 productos por valor total en stock
