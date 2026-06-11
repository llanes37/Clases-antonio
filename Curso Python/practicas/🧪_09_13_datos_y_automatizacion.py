# =========================================================================================
#  🧪 PRACTICA INTEGRADA 09_13 · DATOS Y AUTOMATIZACION
#  ---------------------------------------------------------------------------------------
#  📘 En esta práctica trabajarás:
#    * lectura de CSV
#    * transformación de datos
#    * exportación a JSON
#    * persistencia ligera con SQLite
#    * diseño de funciones fáciles de testear
#
#  🎯 Objetivo docente:
#    * recorrer un flujo de datos casi real de principio a fin
#    * separar extracción, transformación y salida
#    * enseñar por qué algunas funciones son mejores candidatas para `pytest`
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica ·  # NOTE: apunte útil   ·  # // evitar
# =========================================================================================

from __future__ import annotations

import csv
import json
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any, Callable

RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datos_09_13"
CSV_PATH = DATA_DIR / "ventas_demo.csv"
JSON_PATH = DATA_DIR / "resumen_ventas.json"
DB_PATH = DATA_DIR / "ventas.db"


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
    # * Mantiene el menú usable y evita que un error trivial rompa la práctica.
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
#  SECCION 1 · PREPARACION DEL ENTORNO
# =========================================================================================
def asegurar_directorio() -> None:
    # * Prepara la carpeta donde se guardan CSV, JSON y SQLite.
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def generar_csv_demo() -> None:
    # * Genera un pequeño conjunto de ventas para probar todo el flujo.
    asegurar_directorio()
    filas = [
        {"producto": "Teclado", "categoria": "perifericos", "unidades": 3, "precio": 29.99},
        {"producto": "Raton", "categoria": "perifericos", "unidades": 5, "precio": 15.50},
        {"producto": "Monitor", "categoria": "pantallas", "unidades": 2, "precio": 189.00},
        {"producto": "Cable HDMI", "categoria": "accesorios", "unidades": 7, "precio": 8.25},
    ]
    with CSV_PATH.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["producto", "categoria", "unidades", "precio"])
        writer.writeheader()
        writer.writerows(filas)
    print("CSV demo generado en:", CSV_PATH)


# =========================================================================================
#  SECCION 2 · EXTRACCION Y TRANSFORMACION
# =========================================================================================
def leer_ventas_csv(path: Path) -> list[dict[str, Any]]:
    # * Lee un CSV y convierte texto a tipos útiles.
    # ! Leer datos no es solo abrir un archivo: también es normalizarlos.
    with path.open("r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        datos = []
        for fila in reader:
            datos.append(
                {
                    "producto": fila["producto"],
                    "categoria": fila["categoria"],
                    "unidades": int(fila["unidades"]),
                    "precio": float(fila["precio"]),
                }
            )
        return datos


def transformar_ventas(datos: list[dict[str, Any]]) -> dict[str, Any]:
    # * Resume la información en una función fácil de testear.
    # NOTE: esta es la mejor candidata para `pytest` porque no depende de
    # consola ni de archivos.
    total_facturacion = round(sum(item["unidades"] * item["precio"] for item in datos), 2)
    total_unidades = sum(item["unidades"] for item in datos)
    top_producto = max(datos, key=lambda item: item["unidades"] * item["precio"])
    conteo_categorias = Counter(item["categoria"] for item in datos)

    return {
        "total_facturacion": total_facturacion,
        "total_unidades": total_unidades,
        "top_producto": {
            "nombre": top_producto["producto"],
            "facturacion": round(top_producto["unidades"] * top_producto["precio"], 2),
        },
        "categorias": dict(conteo_categorias),
    }


def guardar_resumen_json(resumen: dict[str, Any], path: Path) -> None:
    # * Exporta una vista resumida del proceso para inspección humana.
    asegurar_directorio()
    with path.open("w", encoding="utf-8") as fh:
        json.dump(resumen, fh, indent=2, ensure_ascii=False)
    print("Resumen exportado a JSON en:", path)


# =========================================================================================
#  SECCION 3 · SQLITE
# =========================================================================================
def inicializar_db(path: Path) -> None:
    # * Crea la tabla base si no existe.
    asegurar_directorio()
    with sqlite3.connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT NOT NULL,
                categoria TEXT NOT NULL,
                unidades INTEGER NOT NULL,
                precio REAL NOT NULL
            )
            """
        )
        conn.commit()


def guardar_en_db(path: Path, datos: list[dict[str, Any]]) -> None:
    # * Carga datos limpios en SQLite.
    # NOTE: borramos primero el contenido para que cada demo arranque desde un
    # estado conocido y el alumno pueda comparar resultados.
    inicializar_db(path)
    with sqlite3.connect(path) as conn:
        conn.execute("DELETE FROM ventas")
        conn.executemany(
            "INSERT INTO ventas (producto, categoria, unidades, precio) VALUES (?, ?, ?, ?)",
            [(item["producto"], item["categoria"], item["unidades"], item["precio"]) for item in datos],
        )
        conn.commit()
    print("Datos guardados en SQLite en:", path)


def top_productos_db(path: Path) -> list[tuple[str, float]]:
    inicializar_db(path)
    with sqlite3.connect(path) as conn:
        filas = conn.execute(
            """
            SELECT producto, SUM(unidades * precio) AS facturacion
            FROM ventas
            GROUP BY producto
            ORDER BY facturacion DESC
            LIMIT 3
            """
        ).fetchall()
    return [(fila[0], round(float(fila[1]), 2)) for fila in filas]


def mostrar_top_productos_db(path: Path) -> None:
    encabezado("TOP PRODUCTOS DESDE SQLITE")
    # ? Esta salida ayuda a que el alumno vea valor práctico en guardar los
    # datos y no perciba SQLite como un paso decorativo.
    filas = top_productos_db(path)
    if not filas:
        print("No hay datos cargados en la base de datos.")
        return
    for producto, facturacion in filas:
        print(f"- {producto}: {facturacion:.2f} EUR")


def resumen_texto(resumen: dict[str, Any]) -> None:
    encabezado("RESUMEN DE VENTAS")
    print(f"Facturacion total: {resumen['total_facturacion']:.2f} EUR")
    print(f"Unidades totales:  {resumen['total_unidades']}")
    print(
        "Top producto:      "
        f"{resumen['top_producto']['nombre']} ({resumen['top_producto']['facturacion']:.2f} EUR)"
    )
    print("Categorias:")
    for categoria, total in resumen["categorias"].items():
        print(f"- {categoria}: {total}")


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
Quiero 3 mejoras realistas para una mini ETL que use:
- CSV
- JSON
- SQLite
- funciones faciles de testear
No la conviertas en un proyecto gigante.
""".strip()
    print(prompt)


def autoevaluacion() -> None:
    encabezado("AUTOEVALUACION FINAL")
    print("- filtrar ventas por categoria")
    print("- exportar top productos a otro JSON")
    print("- anadir validaciones de filas invalidas")
    print("- escribir un archivo de tests con pytest")


# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu() -> None:
    # * Menú didáctico del bloque de datos.
    # NOTE: la secuencia de opciones está pensada para respetar el flujo ETL:
    # generar -> leer -> transformar -> exportar -> persistir -> consultar.
    opciones = {
        "1": ("Generar CSV demo", generar_csv_demo),
        "2": ("Procesar CSV", lambda: resumen_texto(transformar_ventas(leer_ventas_csv(CSV_PATH)))),
        "3": (
            "Exportar resumen JSON",
            lambda: guardar_resumen_json(transformar_ventas(leer_ventas_csv(CSV_PATH)), JSON_PATH),
        ),
        "4": ("Cargar datos en SQLite", lambda: guardar_en_db(DB_PATH, leer_ventas_csv(CSV_PATH))),
        "5": ("Consultar top productos desde DB", lambda: mostrar_top_productos_db(DB_PATH)),
        "6": ("Laboratorio IA", laboratorio_ia),
        "7": ("Autoevaluacion", autoevaluacion),
        "0": ("Salir", None),
    }

    while True:
        print_firma()
        print("PRACTICA INTEGRADA 09_13 · DATOS Y AUTOMATIZACION\n")
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
        if eleccion != "1" and not CSV_PATH.exists():
            print("No existe CSV demo. Se genera primero.")
            generar_csv_demo()
        accion()
        pause()


if __name__ == "__main__":
    menu()
