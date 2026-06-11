# =========================================================================================
#  PRACTICA INTEGRADA 14_16 · WEB Y APIS APLICADAS
#  ---------------------------------------------------------------------------------------
#  En esta practica trabajaras:
#    * una mini API Flask con varias rutas
#    * respuestas JSON con estructura clara
#    * validacion de payload y cabeceras
#    * codigos HTTP con significado real
#    * consumo de la API desde un cliente de prueba
#
#  Objetivo docente:
#    * repasar la parte web sin irse a un proyecto enorme
#    * entender el ciclo cliente -> servidor -> respuesta
#    * practicar validacion y contrato de API
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica ·  # NOTE: apunte util   ·  # // evitar
# =========================================================================================

from __future__ import annotations

from typing import Any, Callable

from flask import Flask, jsonify, request

RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True
API_KEY = "curso-python-demo"


# =========================================================================================
#  SECCION 0 · UTILIDADES DE CLASE
# =========================================================================================
# * Igual que en otras practicas, dejamos unas ayudas pequenas para mantener el
#   mismo estilo de uso en clase: firma, pausa, entradas seguras y cabeceras.
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
    # * Lee texto desde consola y lo convierte de forma segura.
    # NOTE:
    # Esta utilidad no es el centro del tema web, pero evita que la demostracion
    # se rompa por un error trivial de entrada.
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
#  SECCION 1 · ESTADO Y APOYO DE NEGOCIO
# =========================================================================================
# * En esta practica guardamos todo en memoria para centrarnos en:
#   - rutas
#   - validacion
#   - JSON
#   - codigos HTTP
# * La persistencia real ya se trabaja en otros bloques del curso.
def crear_estado_inicial() -> dict[str, Any]:
    return {
        "productos": [
            {"id": 1, "nombre": "Curso Flask", "precio": 39.99, "stock": 8},
            {"id": 2, "nombre": "Pack APIs", "precio": 24.50, "stock": 12},
            {"id": 3, "nombre": "Mentoria Web", "precio": 89.00, "stock": 4},
        ],
        "pedidos": [],
        "ultimo_pedido_id": 0,
    }


STATE = crear_estado_inicial()


def resetear_estado() -> None:
    # * Recupera el catalogo original para poder repetir la demo varias veces.
    global STATE
    STATE = crear_estado_inicial()


def buscar_producto(producto_id: int) -> dict[str, Any] | None:
    # * Localiza un producto por id.
    # NOTE:
    # Esta funcion separa la busqueda de la ruta Flask, lo cual hace el codigo
    # mas legible y mas facil de reutilizar.
    for producto in STATE["productos"]:
        if producto["id"] == producto_id:
            return producto
    return None


def validar_api_key(headers: dict[str, Any]) -> bool:
    # * Mini validacion para introducir autenticacion basica.
    # ! Esto no pretende ser seguridad de produccion.
    # Sirve para ensenar que algunas rutas requieren contexto adicional.
    return headers.get("X-API-Key") == API_KEY


# =========================================================================================
#  SECCION 2 · CONSTRUCCION DE LA API
# =========================================================================================
def crear_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> Any:
        # * Ruta minima para comprobar que el servicio responde.
        return jsonify({"status": "ok", "servicio": "mini-api-cursos"}), 200

    @app.get("/api/productos")
    def listar_productos() -> Any:
        # * Devuelve un catalogo completo y un total.
        # NOTE:
        # Incluir metadatos como `total` acostumbra al alumno a pensar en
        # respuestas utiles para clientes reales.
        return jsonify({"items": STATE["productos"], "total": len(STATE["productos"])}), 200

    @app.get("/api/productos/<int:producto_id>")
    def detalle_producto(producto_id: int) -> Any:
        producto = buscar_producto(producto_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404
        return jsonify(producto), 200

    @app.post("/api/pedidos")
    def crear_pedido() -> Any:
        # ! Este endpoint es el corazon docente del bloque.
        # El orden correcto es:
        # 1) autenticar
        # 2) leer payload
        # 3) validar tipos y reglas
        # 4) comprobar stock
        # 5) modificar estado
        # 6) responder con codigo coherente
        if not validar_api_key(request.headers):
            return jsonify({"error": "API key invalida"}), 401

        payload = request.get_json(silent=True) or {}
        producto_id = payload.get("producto_id")
        cantidad = payload.get("cantidad")
        cliente = str(payload.get("cliente", "")).strip()

        if not isinstance(producto_id, int) or not isinstance(cantidad, int):
            return jsonify({"error": "producto_id y cantidad deben ser enteros"}), 400
        if cantidad <= 0:
            return jsonify({"error": "La cantidad debe ser positiva"}), 400
        if cliente == "":
            return jsonify({"error": "El cliente es obligatorio"}), 400

        producto = buscar_producto(producto_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404
        if cantidad > producto["stock"]:
            return jsonify({"error": "Stock insuficiente"}), 409

        producto["stock"] -= cantidad
        STATE["ultimo_pedido_id"] += 1

        pedido = {
            "id": STATE["ultimo_pedido_id"],
            "cliente": cliente,
            "producto_id": producto["id"],
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "total": round(cantidad * producto["precio"], 2),
        }
        STATE["pedidos"].append(pedido)
        return jsonify(pedido), 201

    @app.get("/api/pedidos")
    def listar_pedidos() -> Any:
        return jsonify({"items": STATE["pedidos"], "total": len(STATE["pedidos"])}), 200

    return app


APP = crear_app()


# =========================================================================================
#  SECCION 3 · CLIENTE DE PRUEBA
# =========================================================================================
# * `test_client()` permite practicar la API sin arrancar un servidor externo.
# * Esto hace el bloque mas docente: todo vive en un unico archivo y se puede
#   demostrar paso a paso desde el menu.
def ver_health(client: Any) -> None:
    encabezado("HEALTHCHECK")
    response = client.get("/health")
    print("Status:", response.status_code)
    print("JSON:", response.get_json())


def listar_productos_api(client: Any) -> None:
    encabezado("LISTADO DE PRODUCTOS")
    response = client.get("/api/productos")
    body = response.get_json()
    print("Status:", response.status_code)

    # NOTE:
    # El cliente no adivina nada; primero consume JSON y despues decide como
    # presentarlo al usuario.
    for item in body["items"]:
        print(f"- [{item['id']}] {item['nombre']} | {item['precio']:.2f} EUR | stock={item['stock']}")


def detalle_producto_api(client: Any) -> None:
    encabezado("DETALLE DE PRODUCTO")
    producto_id = safe_input("ID del producto: ", int, 1)
    response = client.get(f"/api/productos/{producto_id}")
    print("Status:", response.status_code)
    print("JSON:", response.get_json())


def crear_pedido_api(client: Any) -> None:
    encabezado("CREAR PEDIDO")
    producto_id = safe_input("ID del producto: ", int, 1)
    cantidad = safe_input("Cantidad: ", int, 1)
    cliente = safe_input("Cliente: ", str, "Alumno Demo").strip() or "Alumno Demo"

    # * El cliente construye cabeceras y payload igual que una app real.
    response = client.post(
        "/api/pedidos",
        json={"producto_id": producto_id, "cantidad": cantidad, "cliente": cliente},
        headers={"X-API-Key": API_KEY},
    )
    print("Status:", response.status_code)
    print("JSON:", response.get_json())


def probar_error_autenticacion(client: Any) -> None:
    encabezado("ERROR DE AUTENTICACION")
    response = client.post(
        "/api/pedidos",
        json={"producto_id": 1, "cantidad": 1, "cliente": "Sin Token"},
    )
    print("Status:", response.status_code)
    print("JSON:", response.get_json())


def listar_pedidos_api(client: Any) -> None:
    encabezado("LISTADO DE PEDIDOS")
    response = client.get("/api/pedidos")
    body = response.get_json()
    print("Status:", response.status_code)
    if not body["items"]:
        print("Todavia no hay pedidos.")
        return
    for pedido in body["items"]:
        print(
            f"- pedido {pedido['id']} | cliente={pedido['cliente']} | "
            f"{pedido['producto']} x{pedido['cantidad']} | total={pedido['total']:.2f} EUR"
        )


def demo_flujo_completo(client: Any) -> None:
    encabezado("DEMO DE FLUJO COMPLETO")

    # NOTE:
    # Esta opcion compacta la historia completa de la API:
    # catalogo inicial -> pedido -> cambio de stock -> consulta final.
    resetear_estado()
    print("1. Estado reseteado.")
    listar_productos_api(client)

    print("\n2. Se crea un pedido de ejemplo.")
    response = client.post(
        "/api/pedidos",
        json={"producto_id": 1, "cantidad": 2, "cliente": "Demo"},
        headers={"X-API-Key": API_KEY},
    )
    print("Status pedido:", response.status_code)
    print("JSON pedido:", response.get_json())

    print("\n3. Se consulta el catalogo actualizado.")
    listar_productos_api(client)

    print("\n4. Se consultan pedidos registrados.")
    listar_pedidos_api(client)


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
Quiero 3 mejoras realistas para una mini API Flask que use:
- rutas JSON
- validacion de payload
- codigos HTTP
- consumo por cliente
Las mejoras deben seguir siendo pequenas y docentes.
""".strip()
    print(prompt)


def autoevaluacion() -> None:
    encabezado("AUTOEVALUACION FINAL")
    print("- anadir endpoint para actualizar stock")
    print("- anadir filtro por nombre o precio minimo")
    print("- separar servidor y cliente en modulos distintos")
    print("- crear tests con pytest para las rutas principales")


# =========================================================================================
#  MENU PRINCIPAL
# =========================================================================================
def menu() -> None:
    # * Menu del bloque web.
    # NOTE:
    # Mantener el menu ayuda a que esta practica se use igual que una unidad del
    # troncal: se explica, se ejecuta y se repite por partes.
    client = APP.test_client()
    opciones = {
        "1": ("Healthcheck", lambda: ver_health(client)),
        "2": ("Listar productos API", lambda: listar_productos_api(client)),
        "3": ("Detalle de producto", lambda: detalle_producto_api(client)),
        "4": ("Crear pedido", lambda: crear_pedido_api(client)),
        "5": ("Probar error de autenticacion", lambda: probar_error_autenticacion(client)),
        "6": ("Listar pedidos", lambda: listar_pedidos_api(client)),
        "7": ("Demo de flujo completo", lambda: demo_flujo_completo(client)),
        "8": ("Laboratorio IA", laboratorio_ia),
        "9": ("Autoevaluacion", autoevaluacion),
        "0": ("Salir", None),
    }

    while True:
        print_firma()
        print("PRACTICA INTEGRADA 14_16 · WEB Y APIS APLICADAS\n")
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
