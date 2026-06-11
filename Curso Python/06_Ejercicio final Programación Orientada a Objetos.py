# =========================================================================================
#  EJERCICIO FINAL 06 · PROGRAMACION ORIENTADA A OBJETOS
#  ---------------------------------------------------------------------------------------
#  En este ejercicio trabajaras:
#    * clases con atributos y metodos
#    * colaboracion entre objetos
#    * herencia sencilla
#    * encapsulacion con atributos privados
#    * validaciones basicas de negocio
#
#  Objetivo docente:
#    * cerrar el bloque de POO con un caso algo mas real
#    * comprobar que el alumno entiende cuando crear clases y como repartir
#      responsabilidad entre ellas
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica ·  # NOTE: apunte util   ·  # // evitar
# =========================================================================================

from __future__ import annotations


# =========================================================================================
#  SECCION 1 · MODELO BASE
# =========================================================================================
# * Un producto conoce su propio estado y sabe ejecutar operaciones pequenas
#   sobre si mismo, como vender o mostrar informacion.
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def vender(self, cantidad: int) -> bool:
        # * Devuelve True si la venta se puede realizar.
        # ! La validacion se hace antes de modificar el estado.
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return False
        if cantidad > self.cantidad_disponible:
            print(f"No hay suficiente cantidad de {self.nombre} para vender.")
            return False

        self.cantidad_disponible -= cantidad
        print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
        return True

    def mostrar_informacion(self) -> None:
        print(
            f"Producto: {self.nombre} | Precio: {self.precio:.2f} EUR | "
            f"Stock: {self.cantidad_disponible}"
        )


# =========================================================================================
#  SECCION 2 · CLASE PRINCIPAL
# =========================================================================================
# * La cantina no sabe vender "por si sola"; coordina a los productos.
# * Esta separacion ayuda a entender responsabilidad por objeto.
class Cantina:
    def __init__(self, nombre_cantina: str) -> None:
        self.nombre_cantina = nombre_cantina
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la cantina {self.nombre_cantina}.")

    def mostrar_productos(self) -> None:
        print(f"Productos en {self.nombre_cantina}:")
        for producto in self.productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre_producto: str) -> Producto | None:
        # * Centralizamos la busqueda para no repetir el mismo bucle varias veces.
        nombre_normalizado = nombre_producto.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_normalizado:
                return producto
        return None

    def realizar_venta(self, nombre_producto: str, cantidad: int) -> None:
        producto = self.buscar_producto(nombre_producto)
        if producto is None:
            print(f"Producto {nombre_producto} no encontrado en la cantina.")
            return
        producto.vender(cantidad)


# =========================================================================================
#  SECCION 3 · HERENCIA Y ESPECIALIZACION
# =========================================================================================
# * La herencia aqui no se usa "porque si", sino porque un producto especial
#   sigue siendo un producto normal con informacion adicional.
class ProductoEspecial(Producto):
    def __init__(
        self,
        nombre: str,
        precio: float,
        cantidad_disponible: int,
        fecha_caducidad: str,
    ) -> None:
        super().__init__(nombre, precio, cantidad_disponible)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_informacion(self) -> None:
        print(
            f"Producto especial: {self.nombre} | Precio: {self.precio:.2f} EUR | "
            f"Stock: {self.cantidad_disponible} | Caduca: {self.fecha_caducidad}"
        )


# =========================================================================================
#  SECCION 4 · ENCAPSULACION Y VALIDACION
# =========================================================================================
# * Esta clase sirve para introducir atributos privados y una validacion minima.
class AdministradorCantina:
    def __init__(self, nombre: str, clave: str) -> None:
        self.__nombre = nombre
        self.__clave = clave

    def verificar_clave(self, clave: str) -> bool:
        return self.__clave == clave

    def cambiar_clave(self, nueva_clave: str) -> bool:
        # ! El cambio no debe hacerse si la nueva clave es demasiado debil.
        if len(nueva_clave) < 8:
            print("La nueva clave debe tener al menos 8 caracteres.")
            return False
        self.__clave = nueva_clave
        print("Clave cambiada con exito.")
        return True

    def mostrar_resumen(self) -> None:
        # * Mostramos solo el nombre para no exponer la clave privada.
        print(f"Administrador activo: {self.__nombre}")


# =========================================================================================
#  SECCION 5 · DEMOSTRACION FINAL
# =========================================================================================
def demo_profesor() -> None:
    # * Este flujo final une todas las piezas del bloque.
    cantina = Cantina("Cantina San Juan Bosco")

    producto1 = Producto("Refresco", 1.50, 100)
    producto2 = Producto("Empanada", 2.00, 50)
    producto3 = ProductoEspecial("Pastel Especial", 10.00, 10, "2026-06-20")

    cantina.agregar_producto(producto1)
    cantina.agregar_producto(producto2)
    cantina.agregar_producto(producto3)

    print("\nLista inicial de productos:")
    cantina.mostrar_productos()

    print("\nRealizando venta de 2 refrescos...")
    cantina.realizar_venta("Refresco", 2)

    print("\nLista de productos despues de la venta:")
    cantina.mostrar_productos()

    admin = AdministradorCantina("Maria", "clave123")
    print("\nVerificando clave inicial:")
    print(admin.verificar_clave("clave123"))

    print("\nCambiando clave del administrador...")
    admin.cambiar_clave("nuevaClaveSegura")

    print("\nVerificando con la nueva clave:")
    print(admin.verificar_clave("nuevaClaveSegura"))
    admin.mostrar_resumen()


if __name__ == "__main__":
    demo_profesor()
