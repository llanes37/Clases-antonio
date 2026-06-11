# =========================================================================================
#  🧪 PRACTICA INTEGRADA 06_08 · POO Y CALIDAD
#  ---------------------------------------------------------------------------------------
#  📘 En esta práctica trabajarás:
#    * clases y objetos con estado
#    * excepciones como reglas de negocio
#    * una clase coordinadora con sentido
#    * un flujo simple de biblioteca por consola
#
#  🎯 Objetivo docente:
#    * pasar de datos sueltos a objetos
#    * entender por qué cierta lógica debe vivir dentro de una clase
#    * reforzar orden y calidad sin hacer una aplicación enorme
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica ·  # NOTE: apunte útil   ·  # // evitar
# =========================================================================================

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Callable

RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True


# =========================================================================================
#  SECCION 0 · UTILIDADES DE CLASE
# =========================================================================================
def print_firma() -> None:
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Pagina web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")


def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass


def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
    # * Lee datos de menú sin romper la demostración si el input falla.
    if not RUN_INTERACTIVE:
        return default
    try:
        raw = input(prompt)
        if raw.strip() == "":
            return default
        return caster(raw)
    except (ValueError, EOFError):
        print("! Entrada no valida; usando valor por defecto.")
        return default


def encabezado(titulo: str) -> None:
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


# =========================================================================================
#  SECCION 1 · EXCEPCIONES Y MODELOS
# =========================================================================================
class LibroNoDisponibleError(Exception):
    # * Se lanza cuando un libro no se puede prestar o devolver como se espera.
    pass


class UsuarioNoEncontradoError(Exception):
    # * Se lanza cuando la operación menciona un usuario no registrado.
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
#  SECCION 2 · LOGICA PRINCIPAL
# =========================================================================================
class Biblioteca:
    # * Clase central de la práctica.
    # ! Aquí vive la lógica importante del sistema: altas, préstamos,
    # devoluciones e historial.
    def __init__(self) -> None:
        self.libros: dict[str, Libro] = {}
        self.usuarios: dict[str, Usuario] = {}
        self.historial: list[str] = []

    def registrar_libro(self, libro: Libro) -> None:
        self.libros[libro.codigo] = libro
        self.historial.append(f"{date.today()} ALTA_LIBRO {libro.codigo}")

    def registrar_usuario(self, usuario: Usuario) -> None:
        # NOTE: guardar en minúsculas simplifica la búsqueda por nombre.
        self.usuarios[usuario.nombre.lower()] = usuario
        self.historial.append(f"{date.today()} ALTA_USUARIO {usuario.nombre}")

    def prestar(self, codigo: str, nombre_usuario: str) -> None:
        # ! Primero validamos identidad del usuario y estado del libro; solo
        # después cambiamos datos.
        usuario = self.usuarios.get(nombre_usuario.lower())
        if usuario is None:
            raise UsuarioNoEncontradoError(f"Usuario no encontrado: {nombre_usuario}")

        libro = self.libros.get(codigo)
        if libro is None or not libro.disponible:
            raise LibroNoDisponibleError(f"Libro no disponible: {codigo}")

        libro.disponible = False
        usuario.prestamos.append(codigo)
        self.historial.append(f"{date.today()} PRESTAMO {codigo} -> {usuario.nombre}")

    def devolver(self, codigo: str, nombre_usuario: str) -> None:
        # ! La devolución también tiene reglas: no todo vale por existir un libro.
        usuario = self.usuarios.get(nombre_usuario.lower())
        if usuario is None:
            raise UsuarioNoEncontradoError(f"Usuario no encontrado: {nombre_usuario}")

        libro = self.libros.get(codigo)
        if libro is None:
            raise LibroNoDisponibleError(f"Libro inexistente: {codigo}")

        if codigo in usuario.prestamos:
            usuario.prestamos.remove(codigo)
        libro.disponible = True
        self.historial.append(f"{date.today()} DEVOLUCION {codigo} -> {usuario.nombre}")

    def resumen(self) -> None:
        encabezado("RESUMEN DE BIBLIOTECA")
        disponibles = [libro for libro in self.libros.values() if libro.disponible]
        prestados = [libro for libro in self.libros.values() if not libro.disponible]
        print(f"Libros totales:       {len(self.libros)}")
        print(f"Libros disponibles:   {len(disponibles)}")
        print(f"Libros prestados:     {len(prestados)}")
        print(f"Usuarios registrados: {len(self.usuarios)}")

    def ranking_autores(self) -> None:
        encabezado("RANKING DE AUTORES")
        conteo = Counter(libro.autor for libro in self.libros.values())
        for autor, total in conteo.most_common():
            print(f"- {autor}: {total} libro(s)")


# =========================================================================================
#  SECCION 3 · DEMO Y OPERACIONES GUIADAS
# =========================================================================================
def crear_demo() -> Biblioteca:
    # * Deja una biblioteca lista para hacer pruebas rápidas.
    biblioteca = Biblioteca()
    for libro in [
        Libro("L001", "Python practico", "Joaquin"),
        Libro("L002", "Clean Code", "Robert C. Martin"),
        Libro("L003", "Automate the Boring Stuff", "Al Sweigart"),
    ]:
        biblioteca.registrar_libro(libro)
    for usuario in [Usuario("Ana"), Usuario("Luis")]:
        biblioteca.registrar_usuario(usuario)
    return biblioteca


def ver_catalogo(biblioteca: Biblioteca) -> None:
    encabezado("CATALOGO")
    for libro in biblioteca.libros.values():
        estado = "disponible" if libro.disponible else "prestado"
        print(f"- {libro.codigo} | {libro.titulo:<28} | {libro.autor:<20} | {estado}")


def operar_prestamo(biblioteca: Biblioteca) -> None:
    encabezado("PRESTAR LIBRO")
    codigo = safe_input("Codigo: ", str, "L001").strip().upper()
    nombre = safe_input("Usuario: ", str, "Ana").strip()
    try:
        biblioteca.prestar(codigo, nombre)
        print("Prestamo realizado.")
    except (LibroNoDisponibleError, UsuarioNoEncontradoError) as exc:
        print("! Error controlado:", exc)


def operar_devolucion(biblioteca: Biblioteca) -> None:
    encabezado("DEVOLVER LIBRO")
    codigo = safe_input("Codigo: ", str, "L001").strip().upper()
    nombre = safe_input("Usuario: ", str, "Ana").strip()
    try:
        biblioteca.devolver(codigo, nombre)
        print("Devolucion registrada.")
    except (LibroNoDisponibleError, UsuarioNoEncontradoError) as exc:
        print("! Error controlado:", exc)


def ver_historial(biblioteca: Biblioteca) -> None:
    encabezado("HISTORIAL")
    if not biblioteca.historial:
        print("Sin movimientos.")
        return
    for linea in biblioteca.historial[-10:]:
        print("-", linea)


# =========================================================================================
#  SECCION 4 · APOYO DOCENTE
# =========================================================================================
def laboratorio_ia() -> None:
    encabezado("LABORATORIO IA")
    if not IA_DEMO:
        print("Laboratorio IA desactivado.")
        return

    prompt = """
Actua como profesor de Python.
Quiero 3 mejoras realistas para una biblioteca por consola orientada a objetos.
Cada mejora debe reforzar:
- poo
- excepciones
- organizacion del codigo
No conviertas el ejercicio en una app gigante.
""".strip()
    print(prompt)


def autoevaluacion() -> None:
    encabezado("AUTOEVALUACION FINAL")
    print("- limitar prestamos maximos por usuario")
    print("- buscar libros por autor")
    print("- anadir estado reservado")
    print("- separar la logica en mas de un modulo")


# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu() -> None:
    # * Menú del bloque de POO y calidad.
    biblioteca = crear_demo()
    opciones = {
        "1": ("Ver catalogo", lambda: ver_catalogo(biblioteca)),
        "2": ("Prestar libro", lambda: operar_prestamo(biblioteca)),
        "3": ("Devolver libro", lambda: operar_devolucion(biblioteca)),
        "4": ("Resumen", lambda: biblioteca.resumen()),
        "5": ("Ranking autores", lambda: biblioteca.ranking_autores()),
        "6": ("Historial", lambda: ver_historial(biblioteca)),
        "7": ("Laboratorio IA", laboratorio_ia),
        "8": ("Autoevaluacion", autoevaluacion),
        "0": ("Salir", None),
    }

    while True:
        print_firma()
        print("PRACTICA INTEGRADA 06_08 · POO Y CALIDAD\n")
        for clave, (texto, _) in opciones.items():
            print(f"[{clave}] {texto}")
        eleccion = safe_input("\nElige una opcion: ", str, "1")
        accion = opciones.get(eleccion, (None, None))[1]
        if eleccion == "0":
            print("Cerrando practica.")
            break
        if accion is None:
            print("! Opcion no valida.")
            pause()
            continue
        accion()
        pause()


if __name__ == "__main__":
    menu()
