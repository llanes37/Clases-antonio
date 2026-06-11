from __future__ import annotations

from typing import Any, Callable

# =========================================================================================
#  PYTHON · PLANTILLA DEL ALUMNO - CLASE 16
#  Tema: Consumo de APIs HTTP con GET, POST, JSON y manejo basico de errores
#  Nota: la idea de esta plantilla es que practiques peticiones reales y aprendas a
#  resumir datos utiles, no solo a imprimir JSON entero por pantalla.
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
#  SECCION 1 · GET BASICO
# =========================================================================================
def seccion_1_get_basico() -> None:
    encabezado("SECCION 1 · GET basico")
    print("Objetivo: pedir un recurso JSON y mostrar campos concretos.\n")

    # ? Como funciona el ejercicio
    # - Haz una peticion GET a un endpoint sencillo.
    # - Lee el JSON recibido.
    # - Muestra solo algunos campos importantes.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Haz un GET a:
    #   https://jsonplaceholder.typicode.com/posts/1
    # y muestra:
    # - id
    # - title
    # Puedes usar requests o urllib.
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 2 · GET CON PARAMETROS
# =========================================================================================
def seccion_2_get_parametros() -> None:
    encabezado("SECCION 2 · GET con parametros")
    print("Objetivo: usar query params en una peticion.\n")

    # ? Como funciona el ejercicio
    # - Pide datos filtrados a la API.
    # - Cuenta cuantos resultados llegan.
    # - Recorre una parte de la respuesta para mostrarla.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Haz un GET a:
    #   /posts?userId=1
    # y muestra cuantos resultados llegan.
    # Luego imprime los 3 primeros titulos.
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 3 · LEER JSON
# =========================================================================================
def seccion_3_json() -> None:
    encabezado("SECCION 3 · Leer JSON")
    print("Objetivo: recorrer una lista JSON y resumir datos.\n")

    # ? Como funciona el ejercicio
    # - Una API suele devolver una lista de diccionarios.
    # - No hace falta imprimirlo todo: resume lo importante.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Haz un GET a:
    #   /users
    # y muestra nombre, email y ciudad de varios usuarios.
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 4 · POST JSON
# =========================================================================================
def seccion_4_post() -> None:
    encabezado("SECCION 4 · POST JSON")
    print("Objetivo: enviar un payload JSON a una API.\n")

    # ? Como funciona el ejercicio
    # - Construye un diccionario Python.
    # - Envialo como JSON a la API.
    # - Lee la respuesta del servidor.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Haz un POST a:
    #   /posts
    # con un payload propio que incluya title, body y userId.
    # Luego muestra la respuesta JSON.
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 5 · MANEJO DE ERRORES
# =========================================================================================
def seccion_5_errores() -> None:
    encabezado("SECCION 5 · Manejo de errores")
    print("Objetivo: controlar errores de red y respuestas inesperadas.\n")

    # ? Como funciona el ejercicio
    # - Usa try/except para capturar errores de red o HTTP.
    # - Usa timeout para no bloquear el programa.
    # - Devuelve un valor por defecto si falla la peticion.
    #
    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # Crea una funcion obtener_json(url, params=None) que:
    # - haga GET
    # - use timeout
    # - devuelva [] o {} si falla
    # - imprima un error claro
    # -----------------------------------------------------------------------------


# =========================================================================================
#  SECCION 6 · AUTOEVALUACION
# =========================================================================================
def seccion_6_autoevaluacion() -> None:
    encabezado("SECCION 6 · Autoevaluacion")
    print("Objetivo: crear un mini cliente de API.\n")

    # TODO: ZONA DEL ALUMNO --------------------------------------------------------------
    # 1) GET a /users
    # 2) GET a /posts?userId=1
    # 3) POST a /posts
    # 4) funcion cliente_get reutilizable
    # 5) manejo de errores con timeout
    # -----------------------------------------------------------------------------


# =========================================================================================
#  MENU
# =========================================================================================
def menu() -> None:
    if not RUN_INTERACTIVE:
        seccion_1_get_basico()
        seccion_2_get_parametros()
        seccion_3_json()
        seccion_4_post()
        seccion_5_errores()
        seccion_6_autoevaluacion()
        return

    while True:
        print("\n===== MENU DEL ALUMNO · Consumo de APIs =====")
        print("  1) GET basico")
        print("  2) GET con parametros")
        print("  3) Leer JSON")
        print("  4) POST JSON")
        print("  5) Manejo de errores")
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
            seccion_1_get_basico()
            pause()
        elif op == 2:
            seccion_2_get_parametros()
            pause()
        elif op == 3:
            seccion_3_json()
            pause()
        elif op == 4:
            seccion_4_post()
            pause()
        elif op == 5:
            seccion_5_errores()
            pause()
        elif op == 6:
            seccion_6_autoevaluacion()
            pause()
        else:
            print("! Elige una opcion del 0 al 6.")


if __name__ == "__main__":
    menu()
