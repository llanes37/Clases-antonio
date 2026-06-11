from __future__ import annotations

import json
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    import requests
except Exception:
    requests = None

# =========================================================================================
#  PYTHON CLASE 16 - CONSUMO DE APIS HTTP
#  ---------------------------------------------------------------------------------------
#  En esta clase aprenderas:
#    * Que es una API y como pedir datos usando HTTP.
#    * Como hacer peticiones GET con parametros.
#    * Como leer JSON y extraer solo la informacion util.
#    * Como enviar datos en una peticion POST con JSON.
#    * Como manejar errores de red, HTTP y timeouts.
#    * Como construir un mini cliente reutilizable para futuros proyectos.
#
#  Convencion de comentarios (Better Comments):
#    # ! importante   |  # * definicion/foco   |  # ? idea/nota
#    # TODO: practica |  # NOTE: apunte util   |  # // deprecado
# =========================================================================================

# * Configuracion general ---------------------------------------------------------------
RUN_INTERACTIVE = True   # True: pide datos; False: usa valores por defecto
PAUSE = False            # Pausa tras cada opcion del menu
BASE_URL = "https://jsonplaceholder.typicode.com"


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


def http_get(url: str, params: dict[str, Any] | None = None, timeout: int = 10) -> tuple[int, Any]:
    """# * Hace un GET y devuelve (status_code, datos_json)."""
    if requests is not None:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.status_code, response.json()

    if params:
        url = f"{url}?{urlencode(params)}"

    with urlopen(url, timeout=timeout) as response:
        return response.status, json.loads(response.read().decode("utf-8"))


def http_post(url: str, payload: dict[str, Any], timeout: int = 10) -> tuple[int, Any]:
    """# * Hace un POST JSON y devuelve (status_code, datos_json)."""
    if requests is not None:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        return response.status_code, response.json()

    data = json.dumps(payload).encode("utf-8")
    request = Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=timeout) as response:
        return response.status, json.loads(response.read().decode("utf-8"))


# =========================================================================================
#  SECCION 1 · QUE ES UNA API Y PRIMER GET
# =========================================================================================
def seccion_1() -> None:
    encabezado("SECCION 1 · Que es una API y primer GET")

    # * TEORIA
    # Una API permite que un programa hable con otro programa a traves de una URL.
    # En este tema vamos a usar un servicio publico de pruebas: jsonplaceholder.
    #
    # ? Idea importante:
    #   GET se usa para CONSULTAR datos; normalmente no modifica nada.

    # * DEMO
    print("Vamos a pedir un recurso JSON y leer su contenido.")
    try:
        status, data = http_get(f"{BASE_URL}/posts/1")
        print(f"Status : {status}")
        print(f"ID     : {data.get('id')}")
        print(f"Titulo : {data.get('title')}")
        print(f"Cuerpo : {data.get('body')}")
    except Exception as exc:
        print("! No se pudo completar el GET:", exc)

    # TODO: (Tema: OTRO RECURSO)
    # 1) Haz una peticion a /users/1
    # 2) Muestra:
    #    - name
    #    - email
    #    - company.name
    # 3) Si alguna clave no existe, usa .get() para evitar errores.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 2 · GET CON PARAMETROS
# =========================================================================================
def seccion_2() -> None:
    encabezado("SECCION 2 · GET con parametros")

    # * TEORIA
    # Muchas APIs aceptan parametros en la URL para filtrar resultados.
    # Ejemplo:
    #   /posts?userId=1
    #
    # ? Esto permite pedir solo una parte de los datos en lugar de descargarlo todo.

    # * DEMO
    user_id = safe_input("User ID (1 por defecto): ", int, 1)
    try:
        status, data = http_get(f"{BASE_URL}/posts", params={"userId": user_id})
        print(f"Status: {status}")
        print(f"Total registros recibidos: {len(data)}")
        for item in data[:3]:
            print(f"  - ({item['id']}) {item['title']}")
    except Exception as exc:
        print("! Error en GET con parametros:", exc)

    # TODO: (Tema: FILTRO LOCAL)
    # 1) Pide una palabra al usuario (por defecto: "qui").
    # 2) Recorre los titulos recibidos.
    # 3) Muestra solo los titulos que contengan esa palabra.
    # 4) Cuenta cuantos titulos coinciden.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 3 · LEER JSON Y RESUMIR DATOS
# =========================================================================================
def seccion_3() -> None:
    encabezado("SECCION 3 · Leer JSON y resumir datos")

    # * TEORIA
    # JSON suele convertirse en:
    # - dict si el objeto es unico
    # - list[dict] si la API devuelve varios registros
    #
    # ! No es buena idea imprimirlo todo sin mas:
    #   conviene resumir la informacion importante.

    # * DEMO
    try:
        status, data = http_get(f"{BASE_URL}/users")
        print(f"Status: {status}")
        print("Resumen de usuarios:")
        for user in data[:5]:
            print(f"  - {user['name']} | {user['email']} | {user['address']['city']}")
    except Exception as exc:
        print("! Error al leer JSON:", exc)

    # TODO: (Tema: LISTA RESUMIDA)
    # 1) Crea una lista de diccionarios con esta forma:
    #      {"nombre": ..., "email": ..., "ciudad": ...}
    # 2) Recorre la nueva lista y muestrala.
    # 3) Extra: ordena alfabeticamente por nombre antes de imprimir.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 4 · POST JSON
# =========================================================================================
def seccion_4() -> None:
    encabezado("SECCION 4 · POST JSON")

    # * TEORIA
    # POST se usa para enviar datos al servidor.
    # En muchas APIs se manda un cuerpo JSON.
    #
    # ? En jsonplaceholder el POST es simulado, pero nos sirve para practicar.

    # * DEMO
    payload = {
        "title": "Curso Python APIs",
        "body": "Probando una peticion POST desde Python",
        "userId": 99,
    }

    try:
        status, data = http_post(f"{BASE_URL}/posts", payload)
        print(f"Status: {status}")
        print("Respuesta JSON:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as exc:
        print("! Error en POST:", exc)

    # TODO: (Tema: TU PAYLOAD)
    # 1) Construye tu propio payload con:
    #    - title
    #    - body
    #    - userId
    # 2) Envialo a /posts
    # 3) Muestra el status y el JSON devuelto
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCION 5 · ERRORES, TIMEOUT Y CLIENTE SENCILLO
# =========================================================================================
def seccion_5() -> None:
    encabezado("SECCION 5 · Errores, timeout y cliente sencillo")

    # * TEORIA
    # Cuando trabajamos con APIs pueden fallar varias cosas:
    # - error de red
    # - error HTTP (404, 500...)
    # - timeout
    # - JSON inesperado
    #
    # ! Por eso conviene encapsular las peticiones en funciones reutilizables.

    # * DEMO
    print("Buenas practicas:")
    print("  - usar timeout")
    print("  - comprobar codigo HTTP")
    print("  - manejar errores de red")
    print("  - validar claves del JSON")

    try:
        status, data = http_get(f"{BASE_URL}/todos/1", timeout=5)
        print(f"OK GET /todos/1 -> {status} | title={data.get('title')}")
    except HTTPError as exc:
        print("! Error HTTP:", exc)
    except URLError as exc:
        print("! Error de red:", exc)
    except Exception as exc:
        print("! Error inesperado:", exc)

    # TODO: (Tema: CLIENTE REUTILIZABLE)
    # Crea una funcion obtener_json(url, params=None) que:
    # 1) haga GET
    # 2) use timeout
    # 3) devuelva [] o {} si falla
    # 4) imprima un mensaje de error claro
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  AUTOEVALUACION FINAL
# =========================================================================================
def autoevaluacion() -> None:
    encabezado("AUTOEVALUACION FINAL · Mini cliente de API")

    # TODO: (Tema: PROYECTO INTEGRADOR DE API)
    # 1) Haz un GET a /users y muestra nombre + email de 3 usuarios.
    # 2) Haz un GET a /posts?userId=1 y cuenta cuantos posts llegan.
    # 3) Haz un POST a /posts con un payload propio.
    # 4) Crea una funcion cliente_get(url, params=None).
    # 5) Maneja errores con try/except y timeout.
    # 6) Extra: guarda algun resultado en un archivo JSON local.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  MENU PRINCIPAL
# =========================================================================================
def menu() -> None:
    while True:
        print_firma()
        print("MENU · Elige una opcion")
        print("  1) Primer GET")
        print("  2) GET con parametros")
        print("  3) Leer JSON")
        print("  4) POST JSON")
        print("  5) Errores y cliente sencillo")
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
