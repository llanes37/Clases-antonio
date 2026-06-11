# =========================================================================================
#  🧪 PRACTICA INTEGRADA 06_08 · POO Y CALIDAD (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  📘 Objetivo:
#    * construir una mini biblioteca con clases
#    * centralizar reglas en una clase principal
#    * usar excepciones cuando el problema sea de negocio
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica ·  # NOTE: apunte útil   ·  # // evitar
#
#  ? Consejo:
#    aquí importa más pensar bien la estructura que escribir muchas líneas.
# =========================================================================================

from __future__ import annotations

from dataclasses import dataclass, field


# =========================================================================================
#  SECCION 1 · EXCEPCIONES Y MODELOS
# =========================================================================================
class LibroNoDisponibleError(Exception):
    pass


class UsuarioNoEncontradoError(Exception):
    pass


@dataclass
class Libro:
    codigo: str
    titulo: str
    autor: str
    disponible: bool = True


@dataclass
class Usuario:
    nombre: str
    prestamos: list[str] = field(default_factory=list)


# =========================================================================================
#  SECCION 2 · CLASE PRINCIPAL
# =========================================================================================
# ! Debe almacenar el estado de la biblioteca y aplicar las reglas.
# Si aquí mezclas todo sin criterio, el ejercicio pierde su sentido.
class Biblioteca:
    def __init__(self) -> None:
        # TODO: crea libros, usuarios e historial
        pass

    def registrar_libro(self, libro: Libro) -> None:
        # TODO:
        # - guardar el libro en un diccionario por codigo
        # - registrar el movimiento en historial
        pass

    def registrar_usuario(self, usuario: Usuario) -> None:
        # TODO:
        # - guardar usuario por nombre en minusculas
        # - registrar alta en historial
        pass

    def prestar(self, codigo: str, nombre_usuario: str) -> None:
        # TODO:
        # - buscar usuario
        # - buscar libro
        # - lanzar excepciones si hace falta
        # - marcar libro como no disponible
        # - guardar el codigo del libro en prestamos
        # - anadir linea al historial
        pass

    def devolver(self, codigo: str, nombre_usuario: str) -> None:
        # TODO:
        # - localizar usuario y libro
        # - controlar errores si hace falta
        # - quitar el libro de prestamos del usuario
        # - marcar libro como disponible
        # - registrar la devolucion
        pass


# =========================================================================================
#  PRUEBA GUIADA
# =========================================================================================
# NOTE: la prueba no es un adorno. Es la forma de comprobar que tu modelo
# realmente mantiene el estado correcto cuando varias operaciones se encadenan.
# TODO:
# - crea una biblioteca
# - registra libros y usuarios
# - presta un libro
# - intenta prestar el mismo libro otra vez
# - prueba un error controlado con un usuario inexistente


# =========================================================================================
#  RETO FINAL
# =========================================================================================
# TODO FINAL:
# - limite de prestamos
# - busqueda por autor
# - ranking de autores
# - separar la logica en mas de un modulo
