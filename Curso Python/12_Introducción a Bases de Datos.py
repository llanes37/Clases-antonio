# =========================================================================================
#  🐍 PYTHON CLASE 12 — BASES DE DATOS CON SQLITE (Relacionales + CRUD básico + IA)
#  ────────────────────────────────────────────────────────────────────────────────────────
#  📘 En esta clase aprenderás:
#    * Qué es una base de datos relacional (tablas, filas, columnas, claves primarias)
#    * Cómo funciona SQL (lenguaje de consultas estructurado)
#    * Conexión a SQLite con Python (sin instalar nada extra)
#    * Crear tablas, insertar datos, leer registros, actualizarlos y eliminarlos (CRUD)
#    * Consultas con filtros WHERE
#    * Manejo de excepciones con sqlite3.Error
#    * Exportar resultados a CSV y JSON
#    * Laboratorio IA (prompts guiados para generar un mini-CRUD con exportación)
#    * Autoevaluación final
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica  ·  # NOTE: apunte útil   ·  # // deprecado
# =========================================================================================

import sqlite3
from pathlib import Path
import csv, json

# * Configuración general ---------------------------------------------------------------
DB_FILE = "alumnos.db"
RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True   # * Activa una demo breve dentro del Laboratorio IA

# * Firma del curso ----------------------------------------------------------------------
def print_firma():
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Página web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")

# * Utilidades ---------------------------------------------------------------------------
def pause(msg="Pulsa Enter para continuar..."):
    if not PAUSE: return
    try: input(msg)
    except EOFError: pass

def encabezado(titulo: str):
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)

# =========================================================================================
#  SECCIÓN 1 · Conceptos básicos de Bases de Datos Relacionales
# =========================================================================================
def seccion_1():
    encabezado("SECCIÓN 1 · Conceptos básicos")

    # * TEORÍA
    # -----------------------------------------------------------------
    # Una BASE DE DATOS RELACIONAL:
    # - Es una colección organizada de datos estructurados en TABLAS.
    # - Cada tabla tiene COLUMNAS (atributos) y FILAS (registros).
    # - Cada fila representa un objeto o entidad (ej: un alumno).
    # - Cada columna define qué dato guarda (ej: nombre, edad).
    #
    # 🔹 Clave primaria (PRIMARY KEY):
    # - Identifica de manera ÚNICA a cada fila.
    # - Ejemplo: el DNI de una persona o un ID autoincrementado.
    #
    # 🔹 Ejemplo de tabla ALUMNOS:
    # +----+----------+------+ 
    # | id | nombre   | edad |
    # +----+----------+------+ 
    # | 1  | Ana      | 25   |
    # | 2  | Luis     | 30   |
    # +----+----------+------+ 
    # -----------------------------------------------------------------

    # TODO: (Tema: TU EJEMPLO)
    # Imagina una tabla llamada PROFESORES con (id, nombre, asignatura).
    # Dibuja en consola cómo se vería con 2 registros de ejemplo.

# =========================================================================================
#  SECCIÓN 2 · Conexión a SQLite y creación de tabla
# =========================================================================================
def seccion_2():
    encabezado("SECCIÓN 2 · Conexión y creación de tabla")

    # * TEORÍA
    # -----------------------------------------------------------------
    # SQLite es una base de datos MUY LIGERA integrada en Python.
    # - No requiere instalación ni servidor: guarda todo en un único archivo .db.
    # - Ideal para proyectos pequeños o medianos y para aprender SQL.
    #
    # 🔹 Flujo básico en Python:
    # 1. Conectar → sqlite3.connect("archivo.db")
    # 2. Crear cursor → conexion.cursor()
    # 3. Ejecutar SQL → cursor.execute("...")
    # 4. Confirmar cambios → conexion.commit()
    # 5. Cerrar conexión → conexion.close()
    # -----------------------------------------------------------------

    # * Conectar o crear base de datos
    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    # * Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

    print(f"✅ Base de datos lista en {Path(DB_FILE).resolve()}")

    # TODO: (Tema: OTRA TABLA)
    # Crea una tabla CURSOS (id, nombre, profesor).

# =========================================================================================
#  SECCIÓN 3 · Operaciones CRUD (Create, Read, Update, Delete)
# =========================================================================================
def seccion_3():
    encabezado("SECCIÓN 3 · CRUD")

    # * TEORÍA
    # -----------------------------------------------------------------
    # CRUD = Create, Read, Update, Delete → operaciones básicas.
    #
    # - CREATE → Insertar nuevos registros (INSERT INTO).
    # - READ   → Consultar registros (SELECT).
    # - UPDATE → Modificar registros existentes.
    # - DELETE → Eliminar registros.
    #
    # Estas 4 operaciones son el núcleo de cualquier sistema que maneje datos.
    # -----------------------------------------------------------------

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    # * Insertar datos
    cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", ("Ana", 25))
    cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", ("Luis", 30))
    conexion.commit()

    # * Leer datos
    print("📋 Alumnos registrados:")
    cursor.execute("SELECT * FROM alumnos")
    for fila in cursor.fetchall():
        print(fila)

    # * Actualizar datos
    cursor.execute("UPDATE alumnos SET edad=? WHERE nombre=?", (26, "Ana"))
    conexion.commit()
    print("🔄 Edad de Ana actualizada.")

    # * Borrar datos
    cursor.execute("DELETE FROM alumnos WHERE nombre=?", ("Luis",))
    conexion.commit()
    print("🗑 Alumno Luis eliminado.")

    conexion.close()

    # TODO: (Tema: CRUD DE CURSOS)
    # Inserta 2 cursos, muéstralos, actualiza 1 y elimina otro.

# =========================================================================================
#  SECCIÓN 4 · Consultas con SELECT y WHERE
# =========================================================================================
def seccion_4():
    encabezado("SECCIÓN 4 · Consultas con WHERE")

    # * TEORÍA
    # -----------------------------------------------------------------
    # SELECT → sentencia SQL para leer datos de una tabla.
    #
    # Ejemplos:
    # - SELECT * FROM alumnos;
    # - SELECT nombre, edad FROM alumnos;
    # - SELECT * FROM alumnos WHERE edad > 24;
    #
    # WHERE permite filtrar registros con condiciones específicas.
    # -----------------------------------------------------------------

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM alumnos WHERE edad > ?", (24,))
    for fila in cursor.fetchall():
        print("Alumno mayor de 24:", fila)

    conexion.close()

    # TODO: (Tema: FILTRO POR NOMBRE)
    # Selecciona alumnos cuyo nombre empiece por 'A'.

# =========================================================================================
#  SECCIÓN 5 · Manejo de errores
# =========================================================================================
def seccion_5():
    encabezado("SECCIÓN 5 · Manejo de errores")

    # * TEORÍA
    # -----------------------------------------------------------------
    # Al trabajar con bases de datos pueden ocurrir errores:
    # - Tabla inexistente
    # - Violación de restricciones (ej: NOT NULL)
    # - Bloqueos de archivo
    # - Errores de sintaxis en SQL
    #
    # Python ofrece excepciones específicas: sqlite3.Error
    # -----------------------------------------------------------------

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM tabla_inexistente")
    except sqlite3.Error as e:
        print("⚠️ Error capturado:", e)

    conexion.close()

    # TODO: (Tema: ERROR CONTROLADO)
    # Intenta borrar un id que no existe. Captura el error y muéstralo.

# =========================================================================================
#  SECCIÓN 6 · Exportar a CSV y JSON
# =========================================================================================
def seccion_6():
    encabezado("SECCIÓN 6 · Exportar datos")

    # * TEORÍA
    # -----------------------------------------------------------------
    # Muchas veces queremos exportar datos:
    # - CSV → útil en Excel u hojas de cálculo.
    # - JSON → estándar para aplicaciones web/APIs.
    #
    # Python tiene librerías integradas:
    # - csv.writer para crear ficheros CSV
    # - json.dumps para generar texto JSON
    # -----------------------------------------------------------------

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM alumnos")
    datos = cursor.fetchall()

    # Exportar a CSV
    with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nombre", "edad"])
        writer.writerows(datos)

    # Exportar a JSON
    alumnos = [{"id": r[0], "nombre": r[1], "edad": r[2]} for r in datos]
    Path("alumnos.json").write_text(json.dumps(alumnos, indent=2, ensure_ascii=False))

    conexion.close()
    print("✅ Exportados a alumnos.csv y alumnos.json")

    # TODO: (Tema: EXPORTA CURSOS)
    # Exporta la tabla CURSOS a cursos.csv y cursos.json.

# =========================================================================================
#  SECCIÓN 7 · Laboratorio IA (mini-CRUD generado por IA)
# =========================================================================================
def seccion_7_ia():
    encabezado("SECCIÓN 7 · Laboratorio IA (mini-CRUD con exportación)")

    # * TEORÍA
    # -----------------------------------------------------------------
    # Objetivo del Lab IA:
    # - Practicar pedir ayuda a una IA (ChatGPT) para crear un mini-CRUD completo,
    #   pegando el código generado en la ZONA DEL ALUMNO y ejecutándolo desde este menú.
    # - Ver cómo la IA puede acelerar tareas repetitivas (crear tablas, inserts, queries,
    #   exportar datos) manteniendo buenas prácticas (parámetros ?, commits, cierre de conexión).
    # -----------------------------------------------------------------

    # * PROMPT KIT (copia/pega en ChatGPT)
    # -----------------------------------------------------------------
    # 1) PROMPT BREVE (tienda de productos):
    #    "Eres profesor de Python. Genera un script SQLite (40–60 líneas) que:
    #     - Cree 'tienda.db' y la tabla productos(id INTEGER PK AUTOINCREMENT,
    #       nombre TEXT NOT NULL, precio REAL NOT NULL, stock INTEGER NOT NULL).
    #     - Inserte al menos 5 productos.
    #     - Liste todos los productos ordenados por precio DESC.
    #     - Busque productos con stock < 5.
    #     - Actualice el stock de un producto por nombre.
    #     - Exporte los productos a 'productos.csv' y 'productos.json'.
    #     Solo código Python estándar (sqlite3, csv, json)."
    #
    # 2) PROMPT ALTERNATIVO (academia):
    #    "Crea 'academia.db' y las tablas alumnos(id, nombre, edad) y cursos(id, nombre).
    #     Inserta datos, muestra top-3 alumnos por edad y exporta alumnos a CSV/JSON.
    #     Solo código Python estándar. 45–60 líneas."
    #
    # 3) PROMPT DE MEJORA:
    #    "Refactoriza para usar funciones pequeñas (conectar, crear_tabla, insertar, listar)
    #     y manejo de errores básico (try/except sqlite3.Error). Mantén <70 líneas."
    # -----------------------------------------------------------------

    # * DEMO opcional para inspirar (no crea archivos reales aquí)
    if IA_DEMO:
        print("💡 IA_DEMO → idea de flujo: conectar → crear tabla → inserts → SELECT con WHERE → exportar CSV/JSON.")

    # TODO: (Tema: PROGRAMA PROPUESTO POR IA)
    # 1) Pídele a la IA el código con el PROMPT KIT (elige uno).
    # 2) Pega el código dentro de la función 'mi_script_ia()'.
    # 3) Ejecuta 'mi_script_ia()' desde aquí para probarlo.
    #
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def mi_script_ia():
    #     # Pega aquí el código que te generó la IA
    #     pass
    #
    # mi_script_ia()

# =========================================================================================
#  AUTOEVALUACIÓN FINAL (ejercicio completo)
# =========================================================================================
def autoevaluacion():
    encabezado("AUTOEVALUACIÓN FINAL")

    # * ENUNCIADO
    # -----------------------------------------------------------------
    # EJERCICIO PROPUESTO:
    # 1) Crea una nueva base 'sistema_escuela.db'.
    # 2) Crea tabla CURSOS (id, nombre, profesor).
    # 3) Inserta 3 cursos.
    # 4) Muestra todos los cursos.
    # 5) Actualiza el nombre de uno.
    # 6) Elimina otro.
    # 7) Exporta los cursos a CSV y JSON.
    #
    # * Nota metodológica:
    #   Puedes apoyarte en la SECCIÓN 7 (Laboratorio IA) para que la IA te genere
    #   esqueletos de funciones y luego personalizarlos.
    # -----------------------------------------------------------------

    # --- ZONA DEL ALUMNO -----------------------------------------------------------------

# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu():
    while True:
        print_firma()
        print("MENÚ · Bases de Datos")
        print("  1) Conceptos básicos")
        print("  2) Conexión + Crear tabla")
        print("  3) CRUD")
        print("  4) Consultas con WHERE")
        print("  5) Manejo de errores")
        print("  6) Exportar a CSV y JSON")
        print("  7) Laboratorio IA (mini-CRUD)")
        print("  8) Autoevaluación")
        print("  0) Salir")

        try:
            op = int(input("Opción: "))
        except Exception:
            print("! Opción no válida.")
            continue

        if op == 0:
            print("¡Hasta la próxima!")
            print_firma()
            break
        elif op == 1: seccion_1(); pause()
        elif op == 2: seccion_2(); pause()
        elif op == 3: seccion_3(); pause()
        elif op == 4: seccion_4(); pause()
        elif op == 5: seccion_5(); pause()
        elif op == 6: seccion_6(); pause()
        elif op == 7: seccion_7_ia(); pause()
        elif op == 8: autoevaluacion(); pause()
        else:
            print("! Elige una opción del 0 al 8.")

# =========================================================================================
#  EJECUCIÓN
# =========================================================================================
if __name__ == "__main__":
    menu()
