# =========================================================================================
#  EJERCICIO FINAL 06 · PROGRAMACION ORIENTADA A OBJETOS (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  Objetivo:
#    * modelar productos con clases
#    * coordinar objetos desde una clase principal
#    * aplicar herencia sencilla con sentido
#    * practicar encapsulacion y validaciones basicas
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica ·  # NOTE: apunte util   ·  # // evitar
#
#  Orden recomendado:
#    1) clase Producto
#    2) clase Cantina
#    3) subclase ProductoEspecial
#    4) AdministradorCantina
#    5) demo final
# =========================================================================================

from __future__ import annotations


# =========================================================================================
#  SECCION 1 · MODELO BASE
# =========================================================================================
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int) -> None:
        # TODO:
        # - guardar nombre
        # - guardar precio
        # - guardar cantidad_disponible
        pass

    def vender(self, cantidad: int) -> bool:
        # TODO:
        # - comprobar que la cantidad sea positiva
        # - comprobar si hay suficiente stock
        # - si todo esta bien, descontar stock
        # - devolver True o False segun corresponda
        # ! Valida primero y modifica el estado solo al final.
        pass

    def mostrar_informacion(self) -> None:
        # TODO:
        # - mostrar nombre
        # - mostrar precio
        # - mostrar cantidad_disponible
        pass


# =========================================================================================
#  SECCION 2 · CLASE PRINCIPAL
# =========================================================================================
class Cantina:
    def __init__(self, nombre_cantina: str) -> None:
        # TODO:
        # - guardar el nombre de la cantina
        # - crear una lista vacia de productos
        pass

    def agregar_producto(self, producto: Producto) -> None:
        # TODO:
        # - anadir el producto a la lista
        # - mostrar un mensaje de confirmacion
        pass

    def mostrar_productos(self) -> None:
        # TODO:
        # - recorrer la lista de productos
        # - llamar a mostrar_informacion() en cada uno
        pass

    def buscar_producto(self, nombre_producto: str) -> Producto | None:
        # TODO:
        # - normalizar el nombre recibido
        # - recorrer los productos
        # - devolver el producto si coincide
        # - devolver None si no existe
        pass

    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        # TODO:
        # - buscar el producto
        # - si no existe, mostrar mensaje
        # - si existe, llamar a vender()
        pass


# =========================================================================================
#  SECCION 3 · HERENCIA Y ESPECIALIZACION
# =========================================================================================
class ProductoEspecial(Producto):
    def __init__(
        self,
        nombre: str,
        precio: float,
        cantidad_disponible: int,
        fecha_caducidad: str,
    ) -> None:
        # TODO:
        # - llamar al constructor de Producto con super()
        # - guardar fecha_caducidad
        pass

    def mostrar_informacion(self) -> None:
        # TODO:
        # - mostrar la informacion del producto
        # - incluir fecha_caducidad
        # NOTE:
        # Este metodo sobrescribe al de la clase base.
        pass


# =========================================================================================
#  SECCION 4 · ENCAPSULACION Y VALIDACION
# =========================================================================================
class AdministradorCantina:
    def __init__(self, nombre: str, clave: str) -> None:
        # TODO:
        # - guardar nombre como atributo privado
        # - guardar clave como atributo privado
        pass

    def verificar_clave(self, clave: str) -> bool:
        # TODO:
        # - comparar la clave recibida con la clave privada
        # - devolver True o False
        pass

    def cambiar_clave(self, nueva_clave: str) -> bool:
        # TODO:
        # - comprobar que tenga al menos 8 caracteres
        # - si cumple, actualizar la clave y devolver True
        # - si no cumple, mostrar mensaje y devolver False
        pass

    def mostrar_resumen(self) -> None:
        # TODO:
        # - mostrar el nombre del administrador
        # ! No muestres la clave privada.
        pass


# =========================================================================================
#  SECCION 5 · DEMO FINAL
# =========================================================================================
# TODO:
# 1. crear una cantina
# 2. anadir productos normales
# 3. anadir un producto especial
# 4. mostrar la lista de productos
# 5. realizar una venta
# 6. mostrar la lista actualizada
# 7. crear un administrador
# 8. verificar y cambiar la clave
#
# NOTE:
# Si resuelves bien este bloque, ya estas usando varias ideas de POO a la vez:
# composicion, herencia, encapsulacion y reparto de responsabilidades.
