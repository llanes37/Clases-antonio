# =========================================================================================
#  🧑‍🎓 PYTHON · PLANTILLA DEL ALUMNO — Clase 12 (ORM)
#  Tema: Bases de Datos con SQLAlchemy (ORM) — Engine, Declarative Base, Modelos, Sesiones,
#        CRUD y manejo de errores, de forma genérica y segura
#  Nota: SQLAlchemy no forma parte de la librería estándar. Instálalo con:
#        pip install SQLAlchemy
# =========================================================================================

from typing import Any, Callable

# * Conmutadores -------------------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menú; False: ejecuta TODO una vez y sale
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

def seccion_3_modelo():
	encabezado("SECCIÓN 3 · Declarative Base y Modelo")
	print("Objetivo: definir la Base y un modelo sencillo (Alumno) con columnas id, nombre, edad.\n")

	# * Teoría breve
	# - Base = declarative_base() · todos los modelos heredan de Base.
	# - Un modelo define __tablename__ y Column(...) por cada campo.

	# ? Cómo funciona el ejercicio
	# - Define la clase Alumno(Base) con: id INTEGER PK autoincrement, nombre TEXT, edad INTEGER.
	# - Opcional: añade una columna creado (DateTime) con default=func.now().
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# from sqlalchemy.orm import declarative_base
	# from sqlalchemy import Column, Integer, String
	# Base = declarative_base()
	# class Alumno(Base):
	#     __tablename__ = 'alumnos'
	#     id = Column(Integer, primary_key=True, autoincrement=True)
	#     nombre = Column(String(50), nullable=False)
	#     edad = Column(Integer, nullable=False)
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · Crear tablas con Base.metadata.create_all(engine)
# =========================================================================================
def seccion_4_create_all():
	encabezado("SECCIÓN 4 · Crear tablas con create_all")
	print("Objetivo: materializar los modelos en la base de datos.\n")

	# * Teoría breve
	# - Base.metadata.create_all(engine) crea las tablas definidas por los modelos.

	# ? Cómo funciona el ejercicio
	# - Invoca create_all tras definir Base y los modelos.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Base.metadata.create_all(engine)
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 · CRUD con ORM: Create, Read, Filter, Update, Delete
# =========================================================================================
def seccion_5_crud():
	encabezado("SECCIÓN 5 · CRUD con ORM")
	print("Objetivo: practicar inserciones, consultas, filtros, actualizaciones y borrados.\n")

	# * Teoría breve
	# - Create: session.add(obj); session.commit()
	# - Read: session.query(Modelo).all() / .filter(Modelo.campo == valor)
	# - Update: modificar atributos del objeto y commit
	# - Delete: session.delete(obj) y commit

	# ? Cómo funciona el ejercicio
	# - Inserta dos alumnos; lista todos; filtra por condición (edad > 20); actualiza uno; borra otro.
	# - Muestra por pantalla los resultados de cada operación.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Escribe aquí las operaciones ORM usando la sesión creada en la sección 2.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 6 · Manejo de errores y transacciones (rollback)
# =========================================================================================
def seccion_6_errores():
	encabezado("SECCIÓN 6 · Manejo de errores y transacciones")
	print("Objetivo: capturar excepciones de SQLAlchemy y asegurar rollback/cierre.\n")

	# * Teoría breve
	# - Captura SQLAlchemyError (from sqlalchemy.exc import SQLAlchemyError).
	# - En except: session.rollback(); en finally: session.close().

	# ? Cómo funciona el ejercicio
	# - Fuerza un error sencillo (p.ej., insertar un tipo incorrecto) y comprueba el manejo.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# from sqlalchemy.exc import SQLAlchemyError
	# try:
	#     # operación que puede fallar
	#     session.commit()
	# except SQLAlchemyError as e:
	#     print("⚠️ Error:", e)
	#     session.rollback()
	# finally:
	#     session.close()
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 7 · Autoevaluación: mini‑gestor ORM (CLI simple)
# =========================================================================================
def seccion_7_autoevaluacion():
	encabezado("SECCIÓN 7 · Autoevaluación: mini‑gestor ORM (CLI)")
	print("Objetivo: construir un pequeño menú para insertar/listar/actualizar/eliminar Alumno vía ORM.\n")

	# ? Requisitos sugeridos
	# - Reutiliza engine/Base/SessionLocal/Alumno.
	# - Menú:
	#   1) Insertar alumno (nombre, edad)
	#   2) Listar alumnos
	#   3) Actualizar edad por id
	#   4) Eliminar por id
	# - Manejo de excepciones con rollback y cierre.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa aquí el CLI minimalista usando la sesión y el modelo ORM.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  MENÚ
# =========================================================================================
def menu():
	if not RUN_INTERACTIVE:
		seccion_1_intro()
		seccion_2_engine_session()
		seccion_3_modelo()
		seccion_4_create_all()
		seccion_5_crud()
		seccion_6_errores()
		seccion_7_autoevaluacion()
		return

	while True:
		print("\n===== MENÚ DEL ALUMNO · Clase 12 (SQLAlchemy ORM) =====")
		print("  1) Introducción ORM/SQLAlchemy")
		print("  2) Engine y Session")
		print("  3) Declarative Base y Modelo")
		print("  4) Crear tablas (create_all)")
		print("  5) CRUD con ORM")
		print("  6) Errores y transacciones")
		print("  7) Autoevaluación (CLI)")
		print("  8) Ejecutar TODO (1→7)")
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
			seccion_1_intro(); pause()
		elif op == 2:
			seccion_2_engine_session(); pause()
		elif op == 3:
			seccion_3_modelo(); pause()
		elif op == 4:
			seccion_4_create_all(); pause()
		elif op == 5:
			seccion_5_crud(); pause()
		elif op == 6:
			seccion_6_errores(); pause()
		elif op == 7:
			seccion_7_autoevaluacion(); pause()
		elif op == 8:
			seccion_1_intro(); seccion_2_engine_session(); seccion_3_modelo(); seccion_4_create_all(); seccion_5_crud(); seccion_6_errores(); seccion_7_autoevaluacion(); pause()
		else:
			print("! Elige una opción del 0 al 8.")


if __name__ == "__main__":
	menu()
