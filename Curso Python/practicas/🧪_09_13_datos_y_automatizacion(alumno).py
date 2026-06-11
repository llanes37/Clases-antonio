# =========================================================================================
#  🧪 PRACTICA INTEGRADA 09_13 · DATOS Y AUTOMATIZACION (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  📘 Objetivo:
#    * montar una mini ETL de ventas paso a paso
#    * separar lectura, transformación y salida
#    * preparar una base buena para futuros tests
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica ·  # NOTE: apunte útil   ·  # // evitar
#
#  ? Recomendación de resolución:
#    1) prepara entorno
#    2) genera/lee datos
#    3) transforma
#    4) exporta
#    5) persiste
# =========================================================================================

from __future__ import annotations

import csv
import json
import sqlite3
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datos_09_13"
CSV_PATH = DATA_DIR / "ventas_demo.csv"
JSON_PATH = DATA_DIR / "resumen_ventas.json"
DB_PATH = DATA_DIR / "ventas.db"


# =========================================================================================
#  SECCION 1 · PREPARACION DEL ENTORNO
# =========================================================================================
# * Paso 1
# Antes de trabajar con datos reales conviene preparar un sitio claro donde
# guardar salidas y ficheros temporales del ejercicio.
def asegurar_directorio() -> None:
    # TODO: crea DATA_DIR si no existe
    pass


# * Paso 2
# Genera un CSV pequeño con ventas de ejemplo.
def generar_csv_demo() -> None:
    # TODO: genera un CSV pequeno con ventas de ejemplo
    pass


# =========================================================================================
#  SECCION 2 · EXTRACCION Y TRANSFORMACION
# =========================================================================================
# * Paso 3
# Lee el CSV y convierte tipos.
def leer_ventas_csv(path: Path) -> list[dict[str, Any]]:
    # TODO: lee CSV y convierte tipos
    pass


# * Paso 4
# Resume los datos en una función pura.
# NOTE: esta es la mejor parte para futuros tests porque no depende de consola
# ni de archivos: entra una lista simple y sale un resumen simple.
def transformar_ventas(datos: list[dict[str, Any]]) -> dict[str, Any]:
    # TODO:
    # - total_facturacion
    # - total_unidades
    # - top_producto
    # - conteo por categoria
    pass


# * Paso 5
# Exporta el resumen a JSON.
def guardar_resumen_json(resumen: dict[str, Any], path: Path) -> None:
    # TODO: guarda JSON con indentacion y UTF-8
    pass


# =========================================================================================
#  SECCION 3 · SQLITE
# =========================================================================================
# * Paso 6
# Crea una tabla SQLite sencilla para almacenar ventas.
def inicializar_db(path: Path) -> None:
    # TODO: crea tabla ventas
    pass


# * Paso 7
# Inserta los datos procesados en SQLite.
def guardar_en_db(path: Path, datos: list[dict[str, Any]]) -> None:
    # TODO: inserta datos en SQLite
    pass


# =========================================================================================
#  PRUEBA GUIADA
# =========================================================================================
# ! Haz la prueba en este orden para detectar antes dónde se rompe el flujo si
# cometes un error.
# TODO:
# 1. genera el CSV
# 2. leelo
# 3. calcula resumen
# 4. exporta JSON
# 5. guarda en SQLite


# =========================================================================================
#  RETO FINAL
# =========================================================================================
# TODO FINAL:
# - filtrar por categoria
# - exportar top productos
# - anadir validacion de filas invalidas
# - anadir 2 tests con pytest
