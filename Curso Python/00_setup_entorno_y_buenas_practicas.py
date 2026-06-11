from __future__ import annotations

import platform
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

# =========================================================================================
#  PYTHON CLASE 00 - SETUP DEL ENTORNO Y BUENAS PRACTICAS
#  ---------------------------------------------------------------------------------------
#  En esta clase aprenderas:
#    * Como comprobar que version de Python estas usando realmente.
#    * Como verificar si pip funciona y desde donde se ejecuta.
#    * Que es un entorno virtual y por que conviene usarlo en cada proyecto.
#    * Como crear un requirements.txt con dependencias del proyecto.
#    * Como organizar una estructura minima de proyecto y escribir codigo mas limpio.
#    * Como aplicar buenas practicas sencillas desde el principio del curso.
#
#  Convencion de comentarios (Better Comments):
#    # ! importante   |  # * definicion/foco   |  # ? idea/nota
#    # TODO: practica |  # NOTE: apunte util   |  # // deprecado
# =========================================================================================

# * Configuracion general ---------------------------------------------------------------
RUN_INTERACTIVE = True   # True: pide datos al usuario; False: usa valores por defecto
PAUSE = False            # Pausa tras cada opcion del menu


# * Utilidades --------------------------------------------------------------------------
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
    """# * Lee, convierte y devuelve un valor; si falla, usa un valor por defecto."""
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


def run(cmd: list[str]) -> tuple[int, str, str]:
    """# * Ejecuta un comando y devuelve codigo de salida, stdout y stderr."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return result.returncode, (result.stdout or "").strip(), (result.stderr or "").strip()
    except Exception as exc:
        return 1, "", str(exc)


# =========================================================================================
#  SECCION 1 · VERSION DE PYTHON Y DIAGNOSTICO BASICO
# =========================================================================================
def seccion_1() -> None:
    encabezado("SECCION 1 · Version de Python y ejecutable")

    # * TEORIA
    # Antes de instalar librerias o ejecutar scripts, conviene saber:
    # - que version exacta de Python se esta usando
    # - donde esta el ejecutable real (sys.executable)
    # - si pip esta asociado a ese mismo Python
    #
    # ? Error tipico de principiantes:
    #   Tener varias versiones de Python instaladas y no saber cual ejecuta la terminal.

    # * DEMO
    print(f"Python version : {platform.python_version()}")
    print(f"Implementacion : {platform.python_implementation()}")
    print(f"Ejecutable     : {sys.executable}")
    print(f"Sistema        : {platform.system()} {platform.release()}")

    code, out, err = run([sys.executable, "-m", "pip", "--version"])
    if code == 0:
        print(f"pip            : {out}")
    else:
        print("pip            : no disponible o con error")
        if err:
            print("Detalle        :", err)

    # TODO: (Tema: DIAGNOSTICO RAPIDO)
    # 1) Muestra sys.version_info completo.
    # 2) Comprueba con Path(sys.executable).exists() si la ruta del ejecutable existe.
    # 3) Indica si la palabra "python" aparece o no dentro de la ruta del ejecutable.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 2 · ENTORNOS VIRTUALES (venv)
# =========================================================================================
def seccion_2() -> None:
    encabezado("SECCION 2 · Entornos virtuales")

    # * TEORIA
    # Un entorno virtual (venv) crea una copia aislada del interprete y sus paquetes.
    # Eso evita mezclar dependencias entre proyectos.
    #
    # ! Idea importante:
    #   Cada proyecto deberia tener su propio entorno virtual si usa librerias externas.

    # * DEMO
    print("Un entorno virtual aisla dependencias de un proyecto.")
    print("\nComandos tipicos:")
    print(f"  {sys.executable} -m venv .venv")
    if platform.system().lower().startswith("win"):
        print(r"  .\.venv\Scripts\Activate.ps1")
    else:
        print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements.txt")

    # TODO: (Tema: RUTA DE ACTIVACION)
    # 1) Construye con Path la ruta del script de activacion del entorno.
    #    - En Windows: .venv/Scripts/Activate.ps1
    #    - En Linux/macOS: .venv/bin/activate
    # 2) Muestra la ruta resultante.
    # 3) Indica si esa ruta existe o no en el proyecto actual.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 3 · DEPENDENCIAS Y requirements.txt
# =========================================================================================
def seccion_3() -> None:
    encabezado("SECCION 3 · Dependencias y requirements.txt")

    # * TEORIA
    # requirements.txt es un archivo de texto que enumera las librerias del proyecto.
    # Permite reproducir el entorno en otro equipo con:
    #   python -m pip install -r requirements.txt
    #
    # ? Dos enfoques habituales:
    #   - escribir un requirements minimo a mano (util para cursos)
    #   - generar uno completo con pip freeze

    # * DEMO
    paquetes_demo = ["flask", "sqlalchemy", "pytest", "requests"]
    print("Ejemplo de requirements minimo:")
    for paquete in paquetes_demo:
        print(f"  {paquete}")

    code, out, err = run([sys.executable, "-m", "pip", "freeze"])
    if code == 0 and out:
        print("\nPrimeras lineas de pip freeze:")
        for linea in out.splitlines()[:10]:
            print(" ", linea)
    else:
        print("\nNo se pudo ejecutar 'pip freeze'.")
        if err:
            print("Detalle:", err)

    # TODO: (Tema: TU requirements MINIMO)
    # 1) Crea una lista con flask, sqlalchemy, pytest y requests.
    # 2) Guardala en requirements_curso.txt usando write_text().
    # 3) Muestra por pantalla la ruta absoluta del archivo creado.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 4 · ESTRUCTURA BASICA DE PROYECTO
# =========================================================================================
def seccion_4() -> None:
    encabezado("SECCION 4 · Estructura basica de un proyecto")

    # * TEORIA
    # Aunque el proyecto sea pequeno, conviene separar:
    # - codigo principal
    # - documentacion (README)
    # - pruebas
    #
    # ? Esto ayuda al alumno a pensar en proyectos, no solo en scripts sueltos.

    # * DEMO
    print("Estructura recomendada:")
    print("  mi_proyecto/")
    print("    app.py")
    print("    utils.py")
    print("    requirements.txt")
    print("    README.md")
    print("    tests/")
    print("      test_basico.py")

    carpeta = Path("demo_proyecto_python")
    print(f"\nCarpeta de ejemplo: {carpeta.resolve()}")

    # TODO: (Tema: CREAR ESTRUCTURA)
    # 1) Crea la carpeta demo_proyecto_python.
    # 2) Dentro crea la subcarpeta tests.
    # 3) Crea README.md con una linea descriptiva.
    # 4) Crea app.py con un print('Hola proyecto').
    # 5) Si quieres subir nivel, crea tambien test_basico.py dentro de tests.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 5 · BUENAS PRACTICAS BASICAS
# =========================================================================================
def seccion_5() -> None:
    encabezado("SECCION 5 · Buenas practicas de codigo")

    # * TEORIA
    # Buenas practicas sencillas que dan mucho valor:
    # - nombres claros
    # - funciones pequenas
    # - evitar repetir codigo
    # - usar bloque principal if __name__ == '__main__'
    #
    # ! No hace falta escribir "codigo profesional complejo":
    #   hace falta escribir codigo claro, entendible y ordenado.

    # * DEMO
    print("Buenas practicas recomendadas:")
    print("  - Usa nombres claros")
    print("  - Divide tareas grandes en funciones pequenas")
    print("  - Evita repetir codigo")
    print("  - Usa if __name__ == '__main__' en scripts ejecutables")
    print("  - Separa datos, logica y salida cuando puedas")

    print("\nEjemplo breve:")
    print("def calcular_total(precio, unidades):")
    print("    return precio * unidades")
    print("")
    print("if __name__ == '__main__':")
    print("    print(calcular_total(10, 3))")

    # TODO: (Tema: REFACTOR SIMPLE)
    # Convierte este flujo en una funcion real:
    #   pedir precio
    #   pedir unidades
    #   calcular total
    #   imprimir total
    #
    # Extra:
    # - llama a la funcion desde if __name__ == '__main__'
    # - usa nombres claros como precio_unitario y numero_unidades
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  AUTOEVALUACION FINAL
# =========================================================================================
def autoevaluacion() -> None:
    encabezado("AUTOEVALUACION FINAL · Setup + estructura + buenas practicas")

    # TODO: (Tema: MINI PROYECTO DE ARRANQUE)
    # 1) Muestra version de Python y verifica si pip funciona.
    # 2) Genera requirements_demo.txt con al menos 3 dependencias.
    # 3) Crea proyecto_demo con README.md, main.py y tests/test_demo.py
    # 4) Escribe en main.py una funcion saludar(nombre) y un bloque principal.
    # 5) Explica en 3 lineas por que usar un entorno virtual reduce problemas.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  MENU PRINCIPAL
# =========================================================================================
def menu() -> None:
    while True:
        print_firma()
        print("MENU · Elige una opcion")
        print("  1) Version de Python y pip")
        print("  2) Entornos virtuales")
        print("  3) Dependencias y requirements.txt")
        print("  4) Estructura basica de proyecto")
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
            print_firma()
            break
        elif op == 1:
            seccion_1()
            pause()
        elif op == 2:
            seccion_2()
            pause()
        elif op == 3:
            seccion_3()
            pause()
        elif op == 4:
            seccion_4()
            pause()
        elif op == 5:
            seccion_5()
            pause()
        elif op == 6:
            autoevaluacion()
            pause()
        else:
            print("! Elige una opcion del 0 al 6.")


if __name__ == "__main__":
    menu()
