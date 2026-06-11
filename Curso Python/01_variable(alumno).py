# =========================================================================================
#  🧑‍🎓 PYTHON · PLANTILLA DEL ALUMNO — Clase 1
#  Tema: Variables, Entradas, Listas/Diccionarios y Operadores (+ Autoevaluación)
#  Cómo usar este archivo:
#   1) Lee cada sección (Objetivos + Guía) y completa las ZONAS DEL ALUMNO (TODO).
#   2) Ejecuta este archivo y usa el menú para probar tus soluciones.
#   3) Las "Pruebas rápidas" NO corrigen, solo te ayudan a comprobar resultados básicos.
# =========================================================================================

# -----------------------------------------------------------------------------------------
# RESUMEN Y TEORÍA CLAVE
# -----------------------------------------------------------------------------------------
# * Propósito: aquí practicas escribiendo código desde cero. Cada sección tiene:
#   - Teoría breve y clave (qué es lo importante).
#   - Pistas de implementación (cómo abordarlo).
#   - Un ejercicio corto para que lo programes tú.
# ? Consejo: evita copiar/pegar; escribe y comenta tu solución. Activa el menú con RUN_INTERACTIVE=True.
# -----------------------------------------------------------------------------------------

from typing import Any, Callable

# * Conmutadores de ejecución ----------------------------------------------------------------
# Cambia RUN_INTERACTIVE a True para usar el menú y elegir secciones. Ponlo en False para ejecutar todo de golpe (sin menú).
RUN_INTERACTIVE = True   # True: menú interactivo; False: ejecuta todo seguido sin preguntar
PAUSE = False            # Pausa entre secciones (útil en clase)

# * Utilidades --------------------------------------------------------------------------------
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
	"""
	Convierte la entrada al tipo deseado; si falla o no hay input, devuelve 'default'.
	Si RUN_INTERACTIVE=False, devuelve directamente el valor por defecto.
	"""
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

# (Sin auto-tests) — Este archivo está pensado para que practiques escribiendo tu propio código.

# Pequeña utilidad disponible para la autoevaluación (puedes usarla si te ayuda)
def resumen_final(nombre: str, n_tareas: int, total_compra: float) -> str:
	"""Devuelve la línea resumen final con formato estándar."""
	return f"Usuario {nombre} | Tareas:{n_tareas} | Total compra:{total_compra:.2f} €"

# =========================================================================================
#  SECCIÓN 1 · Variables básicas y f-strings
# =========================================================================================
def seccion_1_variables():
	encabezado("SECCIÓN 1 · Variables básicas y f-strings")
	print("Objetivo: crear variables y mostrarlas formateadas con f-strings.\n")

	# * Teoría clave
	# * Una variable almacena un valor y su nombre la referencia. Tipos comunes: str, int, float, bool.
	# * f-strings: f"Texto {variable}" permiten formateo legible y seguro.

	# ? Cómo funciona el ejercicio
	# - Crea las variables pedidas, elige valores reales o de prueba.
	# - Muestra todo en una línea usando un f-string.
	#
	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Crea estas variables con tus propios valores:
	#   - usuario (str)
	#   - ciudad (str)
	#   - puntos (int)
	#   - activo (bool)
	# Muestra la línea exactamente con este formato (ajusta valores):
	#   "Usuario <usuario> de <ciudad> | Puntos: <puntos> | Activo: <activo>"
	# Pistas:
	# - Elige nombres de variables descriptivos.
	# - Practica distintos tipos (str, int, bool) y usa un f-string para presentarlo en una línea.

	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 · Entrada segura (input) + mini-cálculos
# =========================================================================================
def seccion_2_input_y_calculos():
	encabezado("SECCIÓN 2 · Entrada segura (input) + mini-cálculos")
	print("Objetivo: leer unidades y precio de forma robusta y calcular el total.\n")

	# * Teoría clave
	# * input() devuelve str; convierte con int()/float() para cálculos. Usa safe_input() para fallback.

	# ? Cómo funciona el ejercicio
	# - Pide (o usa valores por defecto) los kilómetros.
	# - Convierte a millas y muestra el resultado con 2 decimales.
	#
	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Conversor sencillo: pide kilómetros (float) y conviértelos a millas.
	# 1 km = 0.621371. Muestra el resultado con 2 decimales.
	# Sugerencia: usa safe_input("¿Kilómetros? ", float, default=10.0)
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 · Listas y Diccionarios
# =========================================================================================
def seccion_3_colecciones():
	encabezado("SECCIÓN 3 · Listas y Diccionarios")
	print("Objetivo: practicar operaciones básicas con listas y diccionarios.\n")

	# * Teoría clave
	# * Lista: colección ordenada, mutable. Operaciones: append(), pop(), slices.
	# * Diccionario: mapa clave→valor, útil para representar objetos (alumno, contacto).

	# ? Cómo funciona el ejercicio
	# - Crea una lista de tareas y modifica (append).
	# - Crea/actualiza un diccionario 'contacto' y muestra sus campos.
	#
	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# 1) Agenda de tareas: crea una lista 'tareas' con 3 strings. Añade 1 más.
	#    Muestra: total de tareas, la primera y la última.
	# 2) Contacto: crea un diccionario 'contacto' con nombre, telefono, email.
	#    Actualiza 'telefono' y añade 'ciudad'. Muestra el resultado final.
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · Operadores (aritméticos, comparación, lógicos, asignación)
# =========================================================================================
def seccion_4_operadores():
	encabezado("SECCIÓN 4 · Operadores")
	print("Objetivo: usar operadores aritméticos, de comparación y lógicos.\n")

	# * Teoría clave
	# * Aritméticos: + - * / // % **  · Comparación: > < >= <= == !=
	# * Lógicos: and / or / not. Asignación compuesta para actualizar variables.

	# ? Cómo funciona el ejercicio
	# - Pide dos números y calcula operaciones básicas y comparaciones.
	# - Muestra los resultados claramente; maneja división por cero.
	#
	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Calculadora mini: pide dos números (usa safe_input) y muestra:
	# - +, -, *, /, //, %, **
	# - 3 comparaciones (>, <, ==)
	# - Una combinación lógica (por ejemplo: a>0 and b>0)
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 · Autoevaluación final (Proyecto integrador)
# =========================================================================================
def seccion_5_autoevaluacion():
	encabezado("SECCIÓN 5 · Autoevaluación final")
	print("Objetivo: integrar variables, entrada segura, colecciones y operadores.\n")

	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# 1) Variables: nombre_usuario (str), edad (int), ciudad (str), activo (bool).
	# 2) Entrada y cálculo: unidades (int), precio (float), total = unidades * precio.
	# 3) Lista 'tareas': 3 iniciales + 1 añadida; muestra total, primera y última.
	# 4) Diccionario 'perfil': nombre, edad, ciudad, activo; añade 'puntos'.
	# 5) Operadores: con dos números, muestra suma, resta y una comparación.
	# 6) Resumen final (1 línea):
	#    "Usuario <nombre> | Tareas:<n> | Total compra:<importe> €"
	# ---------------------------------------------------------------------------------------

	# (Sin auto-tests): escribe y ejecuta tu solución completa.


# =========================================================================================
#  MENÚ para ejecutar tus ejercicios por secciones
# =========================================================================================
def menu():
	# Modo no interactivo: ejecuta TODO una vez y sale (evita bucles infinitos)
	if not RUN_INTERACTIVE:
		seccion_1_variables()
		seccion_2_input_y_calculos()
		seccion_3_colecciones()
		seccion_4_operadores()
		seccion_5_autoevaluacion()
		return

	# Modo interactivo: menú con bucle y opción de salida
	while True:
		print("\n===== MENÚ DEL ALUMNO · Clase 1 =====")
		print("  1) Variables básicas")
		print("  2) Entrada segura + cálculos")
		print("  3) Listas y Diccionarios")
		print("  4) Operadores")
		print("  5) Autoevaluación final")
		print("  7) Ejecutar TODO (1→5)")
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
			seccion_1_variables(); pause()
		elif op == 2:
			seccion_2_input_y_calculos(); pause()
		elif op == 3:
			seccion_3_colecciones(); pause()
		elif op == 4:
			seccion_4_operadores(); pause()
		elif op == 5:
			seccion_5_autoevaluacion(); pause()
		elif op == 7:
			seccion_1_variables(); seccion_2_input_y_calculos(); seccion_3_colecciones(); seccion_4_operadores(); seccion_5_autoevaluacion(); pause()
		else:
			print("! Elige una opción del 0 al 7.")


if __name__ == "__main__":
	menu()
