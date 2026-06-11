# =========================================================================================
#  🧑‍🎓 PYTHON · PLANTILLA DEL ALUMNO — Clase 12
#  Tema: Introducción a Bases de Datos con SQLite (CRUD básico) de forma genérica
#  Nota: SQLite viene incluido con Python. No requiere instalación adicional.
# =========================================================================================

from typing import Any, Callable

# * Conmutadores -------------------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menú; False: ejecuta todo una vez y sale
PAUSE = False

# * Utilidades ---------------------------------------------------------------------------
def pause(msg: str = "Pulsa Enter para continuar..."):
	if not PAUSE:
		return
	try:
		input(msg)
	except EOFError:
		pass

def encabezado(titulo: str):
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
		print("! Entrada no válida; usando valor por defecto.")
		return default

# =========================================================================================
#  SECCIÓN 1 · Conceptos básicos de BD relacionales y SQLite
# =========================================================================================
def seccion_1_conceptos():
	encabezado("SECCIÓN 1 · Conceptos básicos de BD y SQLite")
	print("Objetivo: entender tablas, filas, columnas, claves primarias y el papel de SQLite.\n")

	# * Teoría breve
	# - Una BD relacional usa tablas con filas (registros) y columnas (campos).
	# - Clave primaria: identifica de forma única a cada registro.
	# - SQLite: motor ligero embebido en Python.

	# ? Cómo funciona el ejercicio
	# - Anota ejemplos de tablas cotidianas (alumnos, productos, pedidos) y sus campos.
	# - No hay código obligatorio aquí; sirve de marco conceptual.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Escribe (en comentarios) 2-3 tablas con 3-4 campos cada una y su clave primaria.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 · Conectar a SQLite y crear cursor
# =========================================================================================
def seccion_2_conexion_cursor():
	encabezado("SECCIÓN 2 · Conectar a SQLite y crear cursor")
	print("Objetivo: abrir una conexión a un .db y obtener un cursor para ejecutar SQL.\n")

	# ? Cómo funciona el ejercicio
	# - Importa sqlite3, crea una conexión a 'escuela.db' (se crea si no existe) y un cursor.
	# - Muestra por pantalla que la conexión se ha realizado.
	# - Cierra la conexión al final de la prueba (cuando proceda).
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa conexión y cursor. Recuerda cerrar la conexión al terminar.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 · CRUD: Create, Read, Update, Delete
# =========================================================================================
def seccion_3_crud_basico():
	encabezado("SECCIÓN 3 · CRUD: Create, Read, Update, Delete")
	print("Objetivo: crear tabla, insertar, leer, actualizar y eliminar registros.\n")

	# ? Cómo funciona el ejercicio
	# - Crea tabla 'alumnos' (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER).
	# - Inserta al menos dos registros.
	# - Lee todos los registros con SELECT *.
	# - Actualiza la edad de un alumno por id.
	# - Elimina un alumno por id.
	# - Aplica commit tras operaciones de escritura y maneja posibles errores.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Escribe las sentencias SQL y ejecútalas con el cursor.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · SELECT y WHERE: consultas filtradas
# =========================================================================================
def seccion_4_select_where():
	encabezado("SECCIÓN 4 · SELECT y WHERE")
	print("Objetivo: recuperar datos filtrados con condiciones.\n")

	# ? Cómo funciona el ejercicio
	# - Consulta todos los alumnos con edad > 20 usando WHERE.
	# - Muestra los resultados por pantalla.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa la consulta y muestra los registros devueltos.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 · Manejo de excepciones (try/except) en BD
# =========================================================================================
def seccion_5_excepciones_bd():
	encabezado("SECCIÓN 5 · Manejo de excepciones en BD")
	print("Objetivo: capturar errores comunes (tabla inexistente, SQL mal formado).\n")

	# ? Cómo funciona el ejercicio
	# - Intenta consultar una tabla que no existe y captura la excepción.
	# - Muestra un mensaje claro sin detener el programa.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Envuelve en try/except una consulta errónea y maneja el error.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 6 · Autoevaluación: mini‑gestor de alumnos (CLI simple)
# =========================================================================================
def seccion_6_autoevaluacion():
	encabezado("SECCIÓN 6 · Autoevaluación: mini‑gestor de alumnos")
	print("Objetivo: crear un pequeño menú para insertar/listar/actualizar/eliminar alumnos.\n")

	# ? Requisitos sugeridos
	# - Conexión a 'escuela.db' y tabla 'alumnos' (si no existe, crearla).
	# - Opciones:
	#   1) Insertar alumno (nombre, edad)
	#   2) Listar alumnos
	#   3) Actualizar edad por id
	#   4) Eliminar por id
	# - Manejo de excepciones y commits en operaciones de escritura.
	# - Cerrar conexión al salir.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa el CLI minimalista respetando los puntos anteriores.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  MENÚ
# =========================================================================================
def menu():
	if not RUN_INTERACTIVE:
		seccion_1_conceptos()
		seccion_2_conexion_cursor()
		seccion_3_crud_basico()
		seccion_4_select_where()
		seccion_5_excepciones_bd()
		seccion_6_autoevaluacion()
		return

	while True:
		print("\n===== MENÚ DEL ALUMNO · Clase 12 (SQLite) =====")
		print("  1) Conceptos")
		print("  2) Conexión y cursor")
		print("  3) CRUD básico")
		print("  4) SELECT y WHERE")
		print("  5) Excepciones en BD")
		print("  6) Autoevaluación (CLI)")
		print("  7) Ejecutar TODO (1→6)")
		print("  0) Salir")
		try:
			op = int(input("Opción: "))
		except Exception:
			print("! Opción no válida.")
			continue

		if op == 0:
			print("¡Hasta la próxima!")
			break
		elif op == 1:
			seccion_1_conceptos(); pause()
		elif op == 2:
			seccion_2_conexion_cursor(); pause()
		elif op == 3:
			seccion_3_crud_basico(); pause()
		elif op == 4:
			seccion_4_select_where(); pause()
		elif op == 5:
			seccion_5_excepciones_bd(); pause()
		elif op == 6:
			seccion_6_autoevaluacion(); pause()
		elif op == 7:
			seccion_1_conceptos(); seccion_2_conexion_cursor(); seccion_3_crud_basico(); seccion_4_select_where(); seccion_5_excepciones_bd(); seccion_6_autoevaluacion(); pause()
		else:
			print("! Elige una opción del 0 al 7.")


if __name__ == "__main__":
	menu()

# **Introducción a Bases de Datos con Python para Alumnos**

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: Conceptos Básicos de Bases de Datos Relacionales
# -------------------------------------------------------------------------------------------
# - Una base de datos relacional almacena datos en tablas que contienen filas (registros) y columnas (campos).
# - Las bases de datos relacionales utilizan claves primarias para identificar de manera única cada fila.
# - SQL (Structured Query Language) es el lenguaje utilizado para interactuar con las bases de datos.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: Introducción a SQLite y su uso con Python
# -------------------------------------------------------------------------------------------
# - SQLite es una base de datos ligera que está integrada en Python. No requiere instalación adicional.
# - Puedes usar SQLite para crear, leer, actualizar y eliminar registros en una base de datos.
# -------------------------------------------------------------------------------------------

# TODO: Crea una conexión a una base de datos SQLite y un cursor para ejecutar sentencias SQL.
# ? Recuerda que si la base de datos no existe, SQLite la creará automáticamente.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: Operaciones CRUD (Create, Read, Update, Delete)
# -------------------------------------------------------------------------------------------
# - Create: Insertar nuevos datos en una tabla.
# - Read: Leer datos de la tabla.
# - Update: Actualizar datos existentes.
# - Delete: Eliminar registros de una tabla.
# -------------------------------------------------------------------------------------------

# TODO: Crea una tabla llamada 'alumnos' con tres columnas: id (entero, clave primaria), nombre (texto) y edad (entero).

# TODO: Inserta al menos dos registros en la tabla 'alumnos' utilizando una sentencia INSERT.

# TODO: Crea una consulta SQL para leer todos los registros de la tabla 'alumnos'.

# TODO: Crea una consulta SQL para actualizar la edad de un alumno específico en la tabla.

# TODO: Crea una consulta SQL para eliminar un alumno de la tabla 'alumnos'.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: Consultas Básicas con SELECT y WHERE
# -------------------------------------------------------------------------------------------
# - La instrucción SELECT se utiliza para consultar datos en una tabla.
# - WHERE se utiliza para filtrar los resultados de una consulta.
# -------------------------------------------------------------------------------------------

# TODO: Realiza una consulta SQL para seleccionar todos los alumnos cuya edad sea mayor a 20.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: Manejo de Excepciones en Operaciones con Bases de Datos
# -------------------------------------------------------------------------------------------
# - Al trabajar con bases de datos, pueden ocurrir errores. Para manejarlos, utilizamos try-except.
# -------------------------------------------------------------------------------------------

# TODO: Utiliza un bloque try-except para manejar posibles errores al realizar una consulta a una tabla inexistente.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: Autoevaluación Final
# -------------------------------------------------------------------------------------------
# - Crea un programa que permita a un usuario interactuar con una base de datos de alumnos:
#   1. Inserta nuevos alumnos.
#   2. Muestra una lista de todos los alumnos.
#   3. Actualiza la información de un alumno.
#   4. Elimina un alumno.
# - Usa las operaciones CRUD y asegúrate de manejar las excepciones correctamente.
# -------------------------------------------------------------------------------------------
