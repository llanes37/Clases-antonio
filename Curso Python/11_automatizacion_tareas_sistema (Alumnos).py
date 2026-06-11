# =========================================================================================
#  🧑‍🎓 PYTHON · PLANTILLA DEL ALUMNO — Clase 11
#  Tema: Automatización básica de tareas del sistema (Windows) con Python de forma segura
#  Nota: Mantén los ejemplos genéricos y NO ejecutes acciones destructivas (apagar/reiniciar).
# =========================================================================================

from typing import Any, Callable

# * Conmutadores -------------------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menú; False: ejecuta todo una vez
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
#  SECCIÓN 1 · Información básica del sistema (platform)
# =========================================================================================
def seccion_1_info_sistema():
	encabezado("SECCIÓN 1 · Información básica del sistema (platform)")
	print("Objetivo: obtener nombre del SO, versión y procesador de forma genérica.\n")

	# ? Cómo funciona el ejercicio
	# - Usa el módulo 'platform' para mostrar: system(), release(), version(), machine(), processor().
	# - Muestra la información en varias líneas legibles.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Importa platform y muestra los datos mencionados.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 · Variables de entorno y directorios (os)
# =========================================================================================
def seccion_2_os_ambiente():
	encabezado("SECCIÓN 2 · Variables de entorno y directorios (os)")
	print("Objetivo: leer variables de entorno y rutas en Windows.\n")

	# ? Cómo funciona el ejercicio
	# - Usa os.getenv para leer, por ejemplo, USERNAME y USERPROFILE.
	# - Muestra el directorio actual y cambia temporalmente a otro (si procede), luego vuelve.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Importa os, lee 2-3 variables de entorno y muestra rutas relevantes.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 · Ejecutar comandos de sistema de forma segura (subprocess)
# =========================================================================================
def seccion_3_subprocess_comandos():
	encabezado("SECCIÓN 3 · Ejecutar comandos de sistema de forma segura (subprocess)")
	print("Objetivo: invocar comandos como 'systeminfo' o 'tasklist' y capturar su salida.\n")

	# ? Cómo funciona el ejercicio
	# - Usa subprocess.run([...], capture_output=True, text=True) para ejecutar un comando.
	# - Muestra (parte de) la salida en pantalla sin saturar la consola.
	# - Comandos de ejemplo: 'systeminfo', 'tasklist' (Windows) o equivalentes.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Importa subprocess, ejecuta un comando y muestra las primeras n líneas de la salida.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · Simular acciones sensibles (shutdown) sin ejecutarlas
# =========================================================================================
def seccion_4_simular_acciones():
	encabezado("SECCIÓN 4 · Simular acciones sensibles (shutdown) sin ejecutarlas")
	print("Objetivo: construir el comando de reinicio/apagado como cadena pero NO ejecutarlo.\n")

	# ? Cómo funciona el ejercicio
	# - Construye el comando 'shutdown /r /t 0' (reinicio inmediato) como string, pero solo imprímelo.
	# - Explica por pantalla por qué no se ejecuta automáticamente.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Crea una variable con el comando de ejemplo y muéstrala en consola.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 · Autoevaluación: Monitor básico periódico a archivo
# =========================================================================================
def seccion_5_autoevaluacion():
	encabezado("SECCIÓN 5 · Autoevaluación: Monitor básico periódico a archivo")
	print("Objetivo: cada N segundos, obtener info y guardarla en un log de texto.\n")

	# ? Requisitos sugeridos (ajústalos a tu nivel)
	# - Cada 10 segundos durante 1-3 iteraciones (no infinito):
	#   · Ejecuta 'systeminfo' o un comando corto y guarda un resumen (p.ej., fecha/hora + 1-3 líneas).
	#   · O bien usa 'tasklist' y guarda un recuento de procesos.
	# - Usa time.sleep para el intervalo y datetime.now para sellar fecha/hora.
	# - Escribe en 'monitor.log' (modo 'a') para ir acumulando mediciones.
	# - Maneja excepciones por si falla el comando.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa la rutina descrita arriba con seguridad (pocas iteraciones, sin bucles infinitos).
	# -------------------------------------------------------------------------------


# =========================================================================================
#  MENÚ
# =========================================================================================
def menu():
	if not RUN_INTERACTIVE:
		seccion_1_info_sistema()
		seccion_2_os_ambiente()
		seccion_3_subprocess_comandos()
		seccion_4_simular_acciones()
		seccion_5_autoevaluacion()
		return

	while True:
		print("\n===== MENÚ DEL ALUMNO · Clase 11 (Automatización Windows) =====")
		print("  1) Info de sistema (platform)")
		print("  2) Entorno y rutas (os)")
		print("  3) Comandos seguros (subprocess)")
		print("  4) Simular acciones (shutdown)")
		print("  5) Autoevaluación: monitor sencillo")
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
			seccion_1_info_sistema(); pause()
		elif op == 2:
			seccion_2_os_ambiente(); pause()
		elif op == 3:
			seccion_3_subprocess_comandos(); pause()
		elif op == 4:
			seccion_4_simular_acciones(); pause()
		elif op == 5:
			seccion_5_autoevaluacion(); pause()
		elif op == 6:
			seccion_1_info_sistema(); seccion_2_os_ambiente(); seccion_3_subprocess_comandos(); seccion_4_simular_acciones(); seccion_5_autoevaluacion(); pause()
		else:
			print("! Elige una opción del 0 al 6.")


if __name__ == "__main__":
	menu()

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: AUTOMATIZACIÓN DE TAREAS DEL SISTEMA EN WINDOWS CON PYTHON
# ? En esta lección vamos a ver cómo podemos interactuar con el sistema operativo Windows usando Python.
# ? Vamos a obtener información básica del sistema, monitorear el uso de CPU y memoria, y ver los procesos en ejecución.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * Ejemplo 1: Obtener información del sistema
# ? Python incluye una librería llamada `platform` que nos permite obtener datos del sistema como el nombre del OS y el procesador.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que obtenga y muestre la información del sistema operativo, la versión y el procesador.

# -------------------------------------------------------------------------------------------
# * Ejemplo 2: Monitorear el uso de CPU y memoria
# ? Usaremos comandos del sistema de Windows a través de Python para monitorear el uso de CPU y memoria.
# ? Para ello, utilizaremos el módulo `os` de Python que nos permite ejecutar comandos en el sistema operativo.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que use el comando de Windows para obtener el porcentaje de uso de la CPU y la memoria física disponible.

# -------------------------------------------------------------------------------------------
# * Ejemplo 3: Ver los procesos en ejecución
# ? Muchas veces es útil saber qué procesos se están ejecutando en el sistema. En Windows, esto se hace con el comando `tasklist`.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que ejecute el comando `tasklist` para mostrar todos los procesos en ejecución en el sistema.

# -------------------------------------------------------------------------------------------
# * Ejemplo 4: Reiniciar el sistema (solo como ejemplo)
# ? En Python, también podemos enviar comandos para apagar o reiniciar el sistema, aunque debemos ser muy cuidadosos con esto.
# ? Como ejemplo, crearemos una función que muestre cómo se reiniciaría el sistema (sin ejecutarlo realmente).
# -------------------------------------------------------------------------------------------

# TODO: Crea una función que simule el comando para reiniciar el sistema pero sin ejecutarlo, usando el comando `shutdown`.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: AUTOEVALUACIÓN FINAL
# -------------------------------------------------------------------------------------------
# * Ejercicio 1: Crear un sistema básico de monitoreo en Python.
# - Debes escribir un programa que cada 10 segundos monitoree el uso de CPU y memoria y guarde los resultados en un archivo de texto.
# - Usa las funciones que has creado para obtener los datos de CPU y memoria.
# - Guarda esos datos en un archivo de texto y añade la fecha y hora de cada medición.
# -------------------------------------------------------------------------------------------

# TODO: Crea una función que monitoree el uso de CPU y memoria cada 10 segundos, y que guarde los resultados en un archivo de registro.
