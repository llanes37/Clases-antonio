from __future__ import annotations

from typing import Any, Callable

# =========================================================================================
#  PYTHON · PLANTILLA DEL ALUMNO - CLASE 00
#  Tema: Setup del entorno y buenas practicas para empezar bien el curso
#  Idea: aqui NO se trata de resolver algoritmos dificiles, sino de aprender a trabajar
#  con un entorno limpio, una estructura minima y codigo mas ordenado.
# =========================================================================================

# * Conmutadores -------------------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menu interactivo; False: ejecuta todo una vez
PAUSE = False


# * Utilidades ---------------------------------------------------------------------------
def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass


def encabezado(titulo: str) -> None:
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
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


# =========================================================================================
#  SECCION 1 · VERSION DE PYTHON Y EJECUTABLE
# =========================================================================================
def seccion_1_info_python() -> None:
    encabezado("SECCION 1 · Version de Python y ejecutable")
    print("Objetivo: mostrar version de Python, ejecutable y datos basicos.\n")

    # ? Como funciona el ejercicio
    # - Importa sys y platform.
    # - Muestra la version de Python y la ruta del ejecutable.
    # - Muestra tambien sys.version_info para ver mayor, menor y micro.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Importa sys y platform.
    # Muestra:
    # - platform.python_version()
    # - sys.executable
    # - sys.version_info
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 2 · ENTORNOS VIRTUALES
# =========================================================================================
def seccion_2_venv() -> None:
    encabezado("SECCION 2 · Entornos virtuales")
    print("Objetivo: entender como se crea y activa un entorno virtual.\n")

    # ? Como funciona el ejercicio
    # - Usa Path para construir la ruta del script de activacion.
    # - Piensa en dos posibles sistemas:
    #   * Windows -> .venv/Scripts/Activate.ps1
    #   * Linux/macOS -> .venv/bin/activate
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Construye con Path la ruta de activacion del entorno.
    # Luego imprime:
    # - la ruta
    # - si existe
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 3 · requirements.txt
# =========================================================================================
def seccion_3_requirements() -> None:
    encabezado("SECCION 3 · requirements.txt")
    print("Objetivo: crear un archivo de dependencias de ejemplo.\n")

    # ? Como funciona el ejercicio
    # - Crea una lista de strings con nombres de librerias.
    # - Une la lista con saltos de linea.
    # - Guarda el contenido en requirements_demo.txt.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Crea una lista con:
    #   flask
    #   sqlalchemy
    #   pytest
    #   requests
    # Guardala en requirements_demo.txt con write_text().
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 4 · ESTRUCTURA BASICA DE PROYECTO
# =========================================================================================
def seccion_4_estructura() -> None:
    encabezado("SECCION 4 · Estructura basica de proyecto")
    print("Objetivo: crear una estructura minima de proyecto.\n")

    # ? Como funciona el ejercicio
    # - Crea una carpeta principal.
    # - Dentro crea otra carpeta tests.
    # - Crea README.md y main.py.
    # - Piensa en ello como el esqueleto de un proyecto real.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Crea:
    #   proyecto_demo/
    #   proyecto_demo/tests/
    #   proyecto_demo/README.md
    #   proyecto_demo/main.py
    # Usa Path.mkdir() y write_text().
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 5 · BUENAS PRACTICAS
# =========================================================================================
def seccion_5_buenas_practicas() -> None:
    encabezado("SECCION 5 · Buenas practicas")
    print("Objetivo: escribir una funcion limpia y reutilizable.\n")

    # ? Como funciona el ejercicio
    # - Escribe una funcion pequena con un nombre claro.
    # - Evita meter todo el codigo a nivel global.
    # - Llama a tu funcion desde el bloque principal.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Escribe una funcion saludar(nombre) que devuelva un texto.
    # Luego llamala desde:
    #   if __name__ == '__main__':
    #       ...
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 6 · AUTOEVALUACION
# =========================================================================================
def seccion_6_autoevaluacion() -> None:
    encabezado("SECCION 6 · Autoevaluacion")
    print("Objetivo: juntar setup, archivos y buenas practicas.\n")

    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # 1) Muestra version de Python.
    # 2) Crea requirements_demo.txt.
    # 3) Crea proyecto_demo con README.md y main.py.
    # 4) Escribe una funcion propia en main.py.
    # 5) Explica en comentarios por que usar venv es util.
    # -----------------------------------------------------------------------------


# =========================================================================================
#  MENU
# =========================================================================================
def menu() -> None:
    if not RUN_INTERACTIVE:
        seccion_1_info_python()
        seccion_2_venv()
        seccion_3_requirements()
        seccion_4_estructura()
        seccion_5_buenas_practicas()
        seccion_6_autoevaluacion()
        return

    while True:
        print("\n===== MENU DEL ALUMNO · Setup del entorno =====")
        print("  1) Version de Python")
        print("  2) Entornos virtuales")
        print("  3) requirements.txt")
        print("  4) Estructura de proyecto")
        print("  5) Buenas practicas")
        print("  6) Autoevaluacion")
        print("  0) Salir")
        try:
            op = int(input("Opcion: "))
        except Exception:
            print("! Opcion no valida.")
            continue

        if op == 0:
            print("Hasta la proxima.")
            break
        elif op == 1:
            seccion_1_info_python()
            pause()
        elif op == 2:
            seccion_2_venv()
            pause()
        elif op == 3:
            seccion_3_requirements()
            pause()
        elif op == 4:
            seccion_4_estructura()
            pause()
        elif op == 5:
            seccion_5_buenas_practicas()
            pause()
        elif op == 6:
            seccion_6_autoevaluacion()
            pause()
        else:
            print("! Elige una opcion del 0 al 6.")


if __name__ == "__main__":
    menu()
