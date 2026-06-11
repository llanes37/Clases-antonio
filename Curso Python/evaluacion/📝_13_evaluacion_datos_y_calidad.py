# =========================================================================================
#  EVALUACION 13 · DATOS Y CALIDAD
#  ---------------------------------------------------------------------------------------
#  En esta evaluacion se comprueba si el alumno puede:
#    * modelar una entidad simple con claridad
#    * centralizar la logica en una clase con sentido
#    * expresar reglas de negocio con una excepcion propia
#    * exportar datos a JSON
#    * persistir informacion en SQLite sin mezclarlo todo
#
#  Objetivo docente:
#    * medir organizacion de codigo, no solo que "funcione"
#    * comprobar si el alumno ya separa modelo, logica y persistencia
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: tarea    ·  # NOTE: apunte util   ·  # // evitar
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
# * Esta excepcion permite distinguir un fallo de negocio de un problema tecnico.
class TicketNoEncontradoError(Exception):
    pass


# * El modelo es pequeno a proposito: suficiente para evaluar POO sin ruido.
@dataclass
class Ticket:
    id: int
    titulo: str
    prioridad: str
    resuelto: bool = False


# =========================================================================================
#  SECCION 2 · LOGICA DE NEGOCIO
# =========================================================================================
class GestorTickets:
    # * Esta clase concentra el comportamiento principal del ejercicio.
    # NOTE:
    # Si la solucion acaba con todo mezclado fuera de la clase, justo se pierde
    # lo que la evaluacion quiere medir.
    def __init__(self) -> None:
        self.tickets: list[Ticket] = []

    def agregar_ticket(self, ticket: Ticket) -> None:
        self.tickets.append(ticket)

    def buscar_ticket(self, ticket_id: int) -> Ticket | None:
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        return None

    def resolver_ticket(self, ticket_id: int) -> None:
        # * Primero se busca; solo despues se modifica estado.
        ticket = self.buscar_ticket(ticket_id)
        if ticket is None:
            raise TicketNoEncontradoError(f"Ticket no encontrado: {ticket_id}")
        ticket.resuelto = True

    def resumen(self) -> dict[str, Any]:
        # * Resumen minimo pero suficiente para validar coherencia del sistema.
        total = len(self.tickets)
        resueltos = sum(ticket.resuelto for ticket in self.tickets)
        pendientes = total - resueltos
        return {"total": total, "resueltos": resueltos, "pendientes": pendientes}


# =========================================================================================
#  SECCION 3 · EXPORTACION A JSON
# =========================================================================================
def exportar_json(tickets: list[Ticket], path: Path) -> None:
    # * Convierte objetos a un formato de intercambio sencillo.
    # ? Aqui se ve si el alumno entiende el paso objeto -> diccionario -> JSON.
    with path.open("w", encoding="utf-8") as fh:
        json.dump([asdict(ticket) for ticket in tickets], fh, indent=2, ensure_ascii=False)


# =========================================================================================
#  SECCION 4 · PERSISTENCIA EN SQLITE
# =========================================================================================
def inicializar_db(path: Path) -> None:
    # * Prepara la tabla donde guardaremos tickets.
    with sqlite3.connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                prioridad TEXT NOT NULL,
                resuelto INTEGER NOT NULL
            )
            """
        )
        conn.commit()


def guardar_en_db(tickets: list[Ticket], path: Path) -> None:
    # * Inserta la coleccion en SQLite de forma clara.
    # ! Antes de insertar, la tabla debe existir.
    inicializar_db(path)
    with sqlite3.connect(path) as conn:
        conn.execute("DELETE FROM tickets")
        conn.executemany(
            "INSERT INTO tickets (id, titulo, prioridad, resuelto) VALUES (?, ?, ?, ?)",
            [(ticket.id, ticket.titulo, ticket.prioridad, int(ticket.resuelto)) for ticket in tickets],
        )
        conn.commit()


# =========================================================================================
#  SECCION 5 · DEMOSTRACION FINAL DEL PROFESOR
# =========================================================================================
def demo_profesor() -> None:
    gestor = GestorTickets()
    gestor.agregar_ticket(Ticket(1, "Error al iniciar sesion", "alta"))
    gestor.agregar_ticket(Ticket(2, "Actualizar logo", "media"))
    gestor.agregar_ticket(Ticket(3, "Cambiar texto del footer", "baja"))

    gestor.resolver_ticket(1)

    print("Resumen:", gestor.resumen())
    exportar_json(gestor.tickets, JSON_PATH)
    guardar_en_db(gestor.tickets, DB_PATH)
    print("JSON generado en:", JSON_PATH)
    print("SQLite generada en:", DB_PATH)


if __name__ == "__main__":
    demo_profesor()
