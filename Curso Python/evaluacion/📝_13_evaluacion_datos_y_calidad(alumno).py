# =========================================================================================
#  EVALUACION 13 · DATOS Y CALIDAD (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  Objetivo:
#    * modelar tickets con claridad
#    * centralizar logica en una clase
#    * usar una excepcion propia
#    * exportar datos a JSON
#    * guardar informacion en SQLite
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: tarea    ·  # NOTE: apunte util   ·  # // evitar
#
#  Orden recomendado:
#    1) modelo
#    2) gestor
#    3) exportacion
#    4) SQLite
# =========================================================================================

from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "tickets_evaluacion.json"
DB_PATH = BASE_DIR / "tickets_evaluacion.db"


# =========================================================================================
#  SECCION 1 · EXCEPCION Y MODELO
# =========================================================================================
class TicketNoEncontradoError(Exception):
    # TODO OPCIONAL:
    # - puedes dejarla vacia
    # - o anadir un docstring corto si quieres explicarla mejor
    pass


@dataclass
class Ticket:
    id: int
    titulo: str
    prioridad: str
    resuelto: bool = False


# =========================================================================================
#  SECCION 2 · LOGICA PRINCIPAL
# =========================================================================================
class GestorTickets:
    def __init__(self) -> None:
        # TODO:
        # - crear una lista vacia para guardar tickets
        pass

    def agregar_ticket(self, ticket: Ticket) -> None:
        # TODO:
        # - anadir el ticket recibido a la lista interna
        pass

    def buscar_ticket(self, ticket_id: int) -> Ticket | None:
        # TODO:
        # - recorrer la lista de tickets
        # - devolver el ticket si coincide el id
        # - devolver None si no existe
        pass

    def resolver_ticket(self, ticket_id: int) -> None:
        # TODO:
        # - buscar el ticket
        # - si no existe, lanzar TicketNoEncontradoError
        # - si existe, marcarlo como resuelto
        # ! El cambio de estado solo debe ocurrir despues de validar.
        pass

    def resumen(self) -> dict[str, Any]:
        # TODO:
        # - calcular total de tickets
        # - calcular cuantos estan resueltos
        # - calcular cuantos quedan pendientes
        pass


# =========================================================================================
#  SECCION 3 · EXPORTACION A JSON
# =========================================================================================
def exportar_json(tickets: list[Ticket], path: Path) -> None:
    # TODO:
    # - abrir el archivo en modo escritura
    # - convertir cada ticket con `asdict`
    # - guardar el resultado como JSON
    # NOTE:
    # `ensure_ascii=False` ayuda si quieres conservar tildes y texto natural.
    pass


# =========================================================================================
#  SECCION 4 · PERSISTENCIA EN SQLITE
# =========================================================================================
def inicializar_db(path: Path) -> None:
    # TODO:
    # - abrir conexion SQLite
    # - crear tabla tickets si no existe
    pass


def guardar_en_db(tickets: list[Ticket], path: Path) -> None:
    # TODO:
    # - asegurar que la tabla exista
    # - limpiar la tabla si quieres rehacer la demo
    # - insertar cada ticket
    # ! Convierte `resuelto` a entero para guardarlo con claridad.
    pass


# =========================================================================================
#  SECCION 5 · FLUJO FINAL
# =========================================================================================
# TODO:
# 1. crear un gestor
# 2. anadir al menos 3 tickets
# 3. resolver uno de ellos
# 4. mostrar resumen
# 5. exportar JSON
# 6. guardar en SQLite
#
# NOTE:
# Esta evaluacion quiere ver separacion de capas. Si todo queda mezclado en una
# sola funcion, justo se pierde lo mas valioso del bloque.
