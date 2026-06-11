# =========================================================================================
#  🧪 PRACTICA INTEGRADA 01_05 · FUNDAMENTOS APLICADOS
#  ---------------------------------------------------------------------------------------
#  📘 En esta práctica trabajarás:
#    * listas y diccionarios como estructura principal
#    * condicionales para validar operaciones
#    * bucles para recorrer y mostrar información
#    * funciones pequeñas y reutilizables
#    * un menú simple que conecte todo el flujo
#
#  🎯 Objetivo docente:
#    * repasar la base del curso con un caso útil
#    * consolidar validaciones sencillas
#    * enseñar a pensar en flujo, no solo en sintaxis suelta
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica ·  # NOTE: apunte útil   ·  # // evitar
# =========================================================================================

from __future__ import annotations

from typing import Any, Callable

RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True


# =========================================================================================
#  SECCION 0 · UTILIDADES DE CLASE
# =========================================================================================
# * Estas funciones no son el foco del bloque, pero dan a la práctica el mismo
#   estilo de uso que el resto del curso.
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
    # * Lee datos de consola y aplica conversión segura.
    # NOTE:
    # - `input()` siempre devuelve texto
    # - casi siempre hay que convertir
    # - conviene tener un valor por defecto para no romper la demo
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
#  SECCION 1 · DATOS BASE
# =========================================================================================
# * Usamos una lista de diccionarios porque ese es justo el nivel que queremos
#   practicar en este bloque. Todavía no hace falta POO.
INVENTARIO_INICIAL = [
    {"id": 1, "nombre": "Teclado", "categoria": "perifericos", "precio": 29.99, "stock": 8},
    {"id": 2, "nombre": "Raton", "categoria": "perifericos", "precio": 15.50, "stock": 12},
    {"id": 3, "nombre": "Monitor", "categoria": "pantallas", "precio": 189.00, "stock": 4},
    {"id": 4, "nombre": "Cable HDMI", "categoria": "accesorios", "precio": 8.25, "stock": 20},
]


# =========================================================================================
#  SECCION 2 · OPERACIONES BASICAS
# =========================================================================================
def clonar_inventario() -> list[dict[str, Any]]:
    # * Devuelve una copia para no modificar el conjunto inicial.
    return [producto.copy() for producto in INVENTARIO_INICIAL]


def buscar_producto(items: list[dict[str, Any]], producto_id: int) -> dict[str, Any] | None:
    # * Busca un producto por id y devuelve `None` si no existe.
    for producto in items:
        if producto["id"] == producto_id:
            return producto
    return None


def listar_productos(items: list[dict[str, Any]]) -> None:
    # * Presenta el estado actual del inventario.
    encabezado("INVENTARIO ACTUAL")
    if not items:
        print("No hay productos.")
        return

    for producto in items:
        print(
            f"[{producto['id']}] {producto['nombre']:<15} | cat={producto['categoria']:<12}"
            f" | precio={producto['precio']:>7.2f} EUR | stock={producto['stock']:>3}"
        )


def agregar_producto(items: list[dict[str, Any]]) -> None:
    # * Da de alta un producto nuevo con validación básica.
    encabezado("ALTA DE PRODUCTO")

    # NOTE: generar ids automáticamente evita errores manuales y refuerza la
    # idea de "siguiente identificador disponible".
    nuevo_id = max((producto["id"] for producto in items), default=0) + 1

    nombre = safe_input("Nombre: ", str, "Nuevo producto").strip()
    categoria = safe_input("Categoria: ", str, "otros").strip().lower()
    precio = safe_input("Precio: ", float, 10.0)
    stock = safe_input("Stock inicial: ", int, 1)

    if precio < 0 or stock < 0:
        print("! Precio y stock no pueden ser negativos.")
        return

    items.append(
        {
            "id": nuevo_id,
            "nombre": nombre or f"Producto {nuevo_id}",
            "categoria": categoria or "otros",
            "precio": round(precio, 2),
            "stock": stock,
        }
    )
    print("Producto agregado correctamente.")


def vender_producto(items: list[dict[str, Any]]) -> None:
    # * Registra una venta y descuenta stock.
    encabezado("VENTA DE PRODUCTO")
    producto_id = safe_input("ID del producto: ", int, 1)
    cantidad = safe_input("Cantidad vendida: ", int, 1)
    producto = buscar_producto(items, producto_id)

    # ! Buena secuencia para practicar validaciones encadenadas.
    if producto is None:
        print("! No existe ese producto.")
        return
    if cantidad <= 0:
        print("! La cantidad debe ser positiva.")
        return
    if cantidad > producto["stock"]:
        print("! Stock insuficiente.")
        return

    producto["stock"] -= cantidad
    total = round(cantidad * producto["precio"], 2)
    print(f"Venta registrada. Total: {total:.2f} EUR")


def reponer_stock(items: list[dict[str, Any]]) -> None:
    # * Suma unidades a un producto existente.
    encabezado("REPOSICION DE STOCK")
    producto_id = safe_input("ID del producto: ", int, 1)
    cantidad = safe_input("Cantidad a reponer: ", int, 1)
    producto = buscar_producto(items, producto_id)

    if producto is None:
        print("! No existe ese producto.")
        return
    if cantidad <= 0:
        print("! La reposicion debe ser positiva.")
        return

    producto["stock"] += cantidad
    print(f"Nuevo stock: {producto['stock']}")


# =========================================================================================
#  SECCION 3 · ANALISIS Y APOYO
# =========================================================================================
def mostrar_bajo_stock(items: list[dict[str, Any]], limite: int = 5) -> None:
    # * Filtra productos con riesgo de quedarse sin unidades.
    encabezado("PRODUCTOS CON STOCK BAJO")
    bajos = [p for p in items if p["stock"] <= limite]
    if not bajos:
        print("No hay productos en riesgo.")
        return

    for producto in bajos:
        print(f"- {producto['nombre']} -> stock {producto['stock']}")


def mostrar_estadisticas(items: list[dict[str, Any]]) -> None:
    # * Calcula métricas simples del inventario.
    encabezado("ESTADISTICAS RAPIDAS")
    if not items:
        print("Sin datos.")
        return

    total_productos = len(items)
    total_unidades = sum(producto["stock"] for producto in items)
    valor_inventario = sum(producto["stock"] * producto["precio"] for producto in items)
    mas_caro = max(items, key=lambda producto: producto["precio"])

    print(f"Productos distintos: {total_productos}")
    print(f"Unidades totales:   {total_unidades}")
    print(f"Valor inventario:   {valor_inventario:.2f} EUR")
    print(f"Producto mas caro:  {mas_caro['nombre']} ({mas_caro['precio']:.2f} EUR)")


def laboratorio_ia() -> None:
    # * Prompt listo para ampliar la práctica sin romper su escala.
    encabezado("LABORATORIO IA")
    if not IA_DEMO:
        print("Laboratorio IA desactivado.")
        return

    prompt = """
Actua como profesor de Python.
Quiero una mejora para un gestor de inventario por consola que use:
- listas y diccionarios
- condicionales
- bucles
- funciones
Propon 3 mejoras realistas y explica por que sirven para practicar.
No generes un proyecto enorme.
""".strip()
    print(prompt)


def autoevaluacion() -> None:
    # * Lista breve de mejoras para comprobar si el alumno domina el bloque.
    encabezado("AUTOEVALUACION FINAL")
    print("- anadir filtro por categoria")
    print("- permitir actualizar precio")
    print("- mostrar top 3 productos por valor total en stock")


# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu() -> None:
    # * Punto de entrada principal para usar la práctica en directo.
    # NOTE:
    # El menú está ordenado para seguir el ciclo natural del inventario:
    # ver -> anadir -> vender -> reponer -> analizar.
    items = clonar_inventario()
    opciones = {
        "1": ("Listar inventario", lambda: listar_productos(items)),
        "2": ("Agregar producto", lambda: agregar_producto(items)),
        "3": ("Vender producto", lambda: vender_producto(items)),
        "4": ("Reponer stock", lambda: reponer_stock(items)),
        "5": ("Ver bajo stock", lambda: mostrar_bajo_stock(items)),
        "6": ("Ver estadisticas", lambda: mostrar_estadisticas(items)),
        "7": ("Laboratorio IA", laboratorio_ia),
        "8": ("Autoevaluacion final", autoevaluacion),
        "0": ("Salir", None),
    }

    while True:
        print_firma()
        print("PRACTICA INTEGRADA 01_05 · FUNDAMENTOS APLICADOS\n")
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
