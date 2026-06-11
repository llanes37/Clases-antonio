# =========================================================================================
#  🧑‍🎓 PYTHON · PLANTILLA DEL ALUMNO — Clase 1.2
#  Tema: Cadenas de Caracteres y Operadores
#  Cómo usar este archivo:
#   1) Lee cada sección (Objetivos + Guía) y completa las ZONAS DEL ALUMNO (TODO).
#   2) Ejecuta este archivo y usa el menú para probar tus soluciones.
#   3) Evita copiar/pegar: escribe tu código desde cero.
# =========================================================================================

from typing import Any, Callable

# * Conmutadores de ejecución ----------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menú interactivo; False: ejecuta todo
PAUSE = False            # Pausa entre secciones

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
	"""Convierte entrada al tipo deseado; si falla, devuelve 'default'."""
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
#  SECCIÓN 1 · CADENAS DE CARACTERES
# =========================================================================================
def seccion_1_cadenas():
	encabezado("SECCIÓN 1 · CADENAS DE CARACTERES")
	print("Objetivo: dominar indexación, slicing y métodos de cadenas.\n")

	# * Teoría clave
	# * Indexación: accede a caracteres individuales (cadena[0], cadena[-1]).
	# * Slicing: obtén subconjuntos (cadena[inicio:fin:paso]).
	# * Métodos: .upper(), .lower(), .split(), .replace(), .find(), .count(), etc.

	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Crea un programa que:
	# 1) Pida una cadena de texto al usuario (o usa "Python es increíble").
	# 2) Muestre: primera letra [0], última [-1], largo (len()).
	# 3) Convierte a mayúsculas y minúsculas.
	# 4) Divide en palabras con .split() y cuenta cuántas hay.
	# 5) Reemplaza una palabra por otra con .replace().
	#
	# Ejemplo de salida:
	# "Ingresa una cadena: Python es increíble"
	# "Primera letra: P"
	# "Última letra: e"
	# "Largo: 20"
	# "Mayúsculas: PYTHON ES INCREÍBLE"
	# "Palabras: ['Python', 'es', 'increíble'] (3 palabras)"
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 · OPERADORES ARITMÉTICOS
# =========================================================================================
def seccion_2_aritmeticos():
	encabezado("SECCIÓN 2 · OPERADORES ARITMÉTICOS")
	print("Objetivo: practicar suma, resta, multiplicación, división, módulo y potencia.\n")

	# * Teoría clave
	# * +, -, *, / (devuelve float), // (devuelve int), %, **
	# * / siempre da decimales. Usa // para división entera.
	# * % da el resto (módulo).

	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Crea un programa que:
	# 1) Pida dos números al usuario (a y b).
	# 2) Calcule y muestre:
	#    - Suma: a + b
	#    - Resta: a - b
	#    - Multiplicación: a * b
	#    - División: a / b (con 2 decimales)
	#    - División entera: a // b
	#    - Módulo: a % b
	#    - Potencia: a ** b
	#
	# Ejemplo: a=21, b=5
	# "21 + 5 = 26"
	# "21 - 5 = 16"
	# "21 * 5 = 105"
	# "21 / 5 = 4.20"
	# "21 // 5 = 4"
	# "21 % 5 = 1"
	# "21 ** 5 = 4084101"
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 · OPERADORES DE COMPARACIÓN
# =========================================================================================
def seccion_3_comparacion():
	encabezado("SECCIÓN 3 · OPERADORES DE COMPARACIÓN")
	print("Objetivo: dominar comparaciones y expresiones booleanas.\n")

	# * Teoría clave
	# * >, <, >=, <=, ==, !=
	# * Devuelven True o False.
	# * Puedes encadenarlas: 1 < 2 < 3.

	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Crea un programa que:
	# 1) Pida dos números al usuario (a y b).
	# 2) Muestre (con True/False):
	#    - ¿a > b?
	#    - ¿a < b?
	#    - ¿a == b?
	#    - ¿a != b?
	#    - ¿a >= b?
	#    - ¿a <= b?
	# 3) Encadena: ¿0 < a < 100?
	#
	# Ejemplo: a=15, b=25
	# "¿15 > 25? False"
	# "¿15 < 25? True"
	# "¿0 < 15 < 100? True"
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · OPERADORES LÓGICOS Y ASIGNACIÓN
# =========================================================================================
def seccion_4_logicos_asignacion():
	encabezado("SECCIÓN 4 · OPERADORES LÓGICOS Y ASIGNACIÓN")
	print("Objetivo: combinar condiciones con and/or/not y actualizar variables.\n")

	# * Teoría clave
	# * and: ambas deben ser True.
	# * or: al menos una debe ser True.
	# * not: invierte el resultado.
	# * +=, -=, *=, /=, //=, %=, **=: actualiza variables.

	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# Crea un programa que:
	# 1) Pida dos números (a, b).
	# 2) Muestre:
	#    - ¿a > 0 AND b > 0? (and)
	#    - ¿a > 50 OR b > 50? (or)
	#    - ¿NOT a == b? (not)
	# 3) Demuestra operadores compuestos:
	#    - Comienza con x = 10.
	#    - Suma 5 con x += 5.
	#    - Multiplica por 2 con x *= 2.
	#    - Resta 8 con x -= 8.
	#    - Muestra el resultado final.
	#
	# Ejemplo: a=20, b=30
	# "¿20 > 0 AND 30 > 0? True"
	# "¿20 > 50 OR 30 > 50? False"
	# "¿NOT 20 == 30? True"
	# "Demostración de asignación:"
	# "x = 10 → x += 5 → x = 15 → x *= 2 → x = 30 → x -= 8 → x = 22"
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 · AUTOEVALUACIÓN FINAL
# =========================================================================================
def seccion_5_autoevaluacion():
	encabezado("SECCIÓN 5 · AUTOEVALUACIÓN FINAL · Analizador de Texto")
	print("Objetivo: integrar cadenas, operadores aritméticos y comparación.\n")

	# TODO: ZONA DEL ALUMNO -----------------------------------------------------------------
	# PROYECTO INTEGRADOR: Analizador de velocidad de lectura.
	#
	# Una persona normal lee 2 palabras por segundo.
	# Un locutor de radio lee 30% más rápido (es decir, 0.7 del tiempo normal).
	#
	# Tu programa debe:
	# 1) Pedir un texto al usuario (o usar "Escribiste este texto largo y complejo")
	# 2) Dividir en palabras con .split() y contar cuántas hay.
	# 3) Calcular tiempo normal: palabras / 2 (segundos)
	# 4) Si tiempo > 30: mostrar "¡Menudo testamento!"
	# 5) Calcular tiempo locutor: tiempo_normal * 0.7
	# 6) Mostrar todo formateado con 1 decimal.
	#
	# Salida esperada (ejemplo):
	# "Escribiste 12 palabras, y tardarías 6.0 segundos en leerlo."
	# "El locutor de radio, lo leería en 4.2 segundos."
	#
	# Si palabras > 60:
	# "Escribiste 80 palabras, y tardarías 40.0 segundos en leerlo."
	# "¡Menudo testamento!"
	# "El locutor de radio, lo leería en 28.0 segundos."
	#
	# Requisitos:
	# - Usa .split() para contar palabras.
	# - Usa operadores aritméticos (/, *) para calcular tiempos.
	# - Usa comparación (>) para el aviso.
	# - Usa f-strings con :.1f para 1 decimal.
	# ---------------------------------------------------------------------------------------


# =========================================================================================
#  MENÚ para ejecutar tus ejercicios por secciones
# =========================================================================================
def menu():
	# Modo no interactivo: ejecuta TODO una vez
	if not RUN_INTERACTIVE:
		seccion_1_cadenas()
		seccion_2_aritmeticos()
		seccion_3_comparacion()
		seccion_4_logicos_asignacion()
		seccion_5_autoevaluacion()
		return

	# Modo interactivo: menú con bucle
	while True:
		print("\n===== MENÚ DEL ALUMNO · Clase 1.2 Cadenas y Operadores =====")
		print("  1) Cadenas de caracteres")
		print("  2) Operadores aritméticos")
		print("  3) Operadores de comparación")
		print("  4) Operadores lógicos y asignación")
		print("  5) Autoevaluación final")
		print("  6) Ejecutar TODO (1→5)")
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
			seccion_1_cadenas(); pause()
		elif op == 2:
			seccion_2_aritmeticos(); pause()
		elif op == 3:
			seccion_3_comparacion(); pause()
		elif op == 4:
			seccion_4_logicos_asignacion(); pause()
		elif op == 5:
			seccion_5_autoevaluacion(); pause()
		elif op == 6:
			seccion_1_cadenas(); seccion_2_aritmeticos(); seccion_3_comparacion(); seccion_4_logicos_asignacion(); seccion_5_autoevaluacion(); pause()
		else:
			print("! Elige una opción del 0 al 6.")


if __name__ == "__main__":
	menu()
