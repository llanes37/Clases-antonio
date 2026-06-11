# =========================================================================================
#  🧑‍🎓 PYTHON · PLANTILLA DEL ALUMNO — Clase 2
#  Tema: Condicionales (if/elif/else), lógicos and/or/not, truthy/falsy, ternario y match
#  Cómo usar este archivo:
#   1) Lee cada sección (Objetivos + Guía) y completa las ZONAS DEL ALUMNO (TODO).
#   2) Ejecuta este archivo y usa el menú para probar tus soluciones.
#   3) No hay soluciones ejemplo dentro de las secciones: escribe tu propio código.
# =========================================================================================

from typing import Any, Callable

# * Conmutadores de ejecución -------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menú interactivo; False: ejecuta TODO una vez y sale
PAUSE = False            # Pausa tras cada sección (útil en clase)

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

# =========================================================================================
#  SECCIÓN 1 · if básico (una condición)
# =========================================================================================
def seccion_1_if_basico():
	encabezado("SECCIÓN 1 · if básico (una condición)")
	print("Objetivo: tomar una decisión con una única condición y buena indentación.\n")

	# * Teoría clave
	# * Estructura mínima:
	#   if condicion:
	#       bloque_si_verdadero
	# * Comparadores: > < >= <= == !=   · Recuerda: el bloque lo marca la indentación (4 espacios).

	# ? Cómo funciona el ejercicio
	# - Pide (o fija) la edad (int).
	# - Si edad >= 18, imprime "Mayor de edad"; si no, no imprimas nada.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa la lógica anterior. Sugerencia:
	# edad = safe_input("Edad: ", int, default=17)
	# if edad >= 18:
	#     print("Mayor de edad")
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 · if / elif / else (ramas múltiples)
# =========================================================================================
def seccion_2_if_elif_else():
	encabezado("SECCIÓN 2 · if / elif / else (ramas múltiples)")
	print("Objetivo: encadenar condiciones y ejecutar solo la primera que se cumpla.\n")

	# * Teoría clave
	# * Se evalúa de arriba a abajo; en cuanto una rama True se ejecuta, las demás se ignoran.

	# ? Cómo funciona el ejercicio
	# - Pide un color (str): rojo/amarillo/verde (normaliza con .lower()).
	# - Si rojo → "Para"; elif amarillo → "Precaución"; elif verde → "Adelante"; else → "Color no válido".
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa el "Semáforo" según el enunciado.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 · Condiciones anidadas + normalización
# =========================================================================================
def seccion_3_anidadas():
	encabezado("SECCIÓN 3 · Condiciones anidadas + normalización")
	print("Objetivo: tomar decisiones más específicas con if dentro de if.\n")

	# * Teoría clave
	# * Puedes anidar if para mensajes más concretos. Normaliza texto: .strip().lower()

	# ? Cómo funciona el ejercicio
	# - Mini acceso a evento: pide edad (int) y si tiene_entrada (s/n).
	# - Si edad >= 18 y tiene_entrada → "Acceso concedido".
	# - Si no, usa if anidados para indicar el/los motivos (menor de edad, falta de entrada).
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa la lógica solicitada usando if anidados y normalización con .strip().lower().
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · Operadores lógicos: and / or / not + truthy/falsy
# =========================================================================================
def seccion_4_logicos():
	encabezado("SECCIÓN 4 · Lógicos and/or/not + truthy/falsy")
	print("Objetivo: combinar condiciones y entender valores verdaderos/falsos.\n")

	# * Teoría clave
	# * and → ambas verdaderas; or → alguna verdadera; not → invierte.
	# * Falsy: 0, 0.0, "", [], {}, (), set(), None, False. Lo demás tiende a True.

	# ? Cómo funciona el ejercicio
	# - Descuento tienda: pide es_estudiante (s/n) y total (float).
	# - Si es_estudiante and total >= 20 → 10% de descuento; si no → 0%.
	# - Muestra total final y el motivo (p.ej., "no cumple mínimo").
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Aplica and/or/not para calcular el descuento y mostrar el resultado.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 · Ternario y match/case (opcional)
# =========================================================================================
def seccion_5_combinada():
	encabezado("SECCIÓN 5 · Ternario y match/case (opcional)")
	print("Objetivo: decisiones compactas con ternario y múltiples casos con match.\n")

	# * Teoría clave
	# * Ternario: msg = "alto" if valor > 0 else "bajo"
	# * match/case (Python 3.10+): múltiples casos legibles, con case _ como comodín.

	# ? Cómo funciona el ejercicio
	# - Con ternario: dado un total (float), define msg_envio = "Envío gratis" si total>=30, si no "Envío 3.99€".
	# - Con match (Python 3.10+): con opcion 1–3 imprime: 1 Altas, 2 Bajas, 3 Consultas, otro No válido.
	#
	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# Implementa el ternario y el bloque match/case según el enunciado.
	# -------------------------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 6 · Autoevaluación final (mini‑proyecto)
# =========================================================================================
def seccion_6_autoevaluacion():
	encabezado("SECCIÓN 6 · Autoevaluación final")
	print("Objetivo: integrar if/elif/else, lógicos, truthy/falsy, ternario y match.\n")

	# TODO: ZONA DEL ALUMNO ---------------------------------------------------------------
	# 1) Entrada/valores: nombre (str), edad (int), importe (float), tipo_cliente ("normal"/"premium").
	# 2) Validación: si not nombre → "Nombre requerido". Si edad<0 o importe<0 → "Valores inválidos".
	# 3) Reglas:
	#    - Si edad < 18 → "No puede comprar".
	#    - Si tipo_cliente=="premium" y importe>=50 → 20% descuento.
	#    - elif tipo_cliente=="normal" y importe>=100 → 10% descuento.
	#    - else → 0%.
	# 4) Ternario: estado_envio = "Envío gratis" si total>=60, si no "Envío 3.99€".
	# 5) match/case: según tipo_cliente imprime un saludo específico.
	# 6) Resumen final (1 línea):
	#    "[OK] <nombre> | edad:<edad> | tipo:<tipo_cliente> | base:<importe:.2f> | desc:<aplicado%> | total:<total:.2f> | <estado_envio>"
	# -------------------------------------------------------------------------------


# =========================================================================================
#  MENÚ para ejecutar tus ejercicios por secciones
# =========================================================================================
def menu():
	# Modo no interactivo: ejecuta TODO una vez y sale (evita bucles infinitos)
	if not RUN_INTERACTIVE:
		seccion_1_if_basico()
		seccion_2_if_elif_else()
		seccion_3_anidadas()
		seccion_4_logicos()
		seccion_5_combinada()
		seccion_6_autoevaluacion()
		return

	# Modo interactivo: menú con bucle y opción de salida
	while True:
		print("\n===== MENÚ DEL ALUMNO · Clase 2 (Condicionales) =====")
		print("  1) if básico")
		print("  2) if / elif / else")
		print("  3) Condiciones anidadas")
		print("  4) Lógicos and/or/not + truthy/falsy")
		print("  5) Ternario y match/case")
		print("  6) Autoevaluación final")
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
			seccion_1_if_basico(); pause()
		elif op == 2:
			seccion_2_if_elif_else(); pause()
		elif op == 3:
			seccion_3_anidadas(); pause()
		elif op == 4:
			seccion_4_logicos(); pause()
		elif op == 5:
			seccion_5_combinada(); pause()
		elif op == 6:
			seccion_6_autoevaluacion(); pause()
		elif op == 7:
			seccion_1_if_basico(); seccion_2_if_elif_else(); seccion_3_anidadas(); seccion_4_logicos(); seccion_5_combinada(); seccion_6_autoevaluacion(); pause()
		else:
			print("! Elige una opción del 0 al 7.")


if __name__ == "__main__":
	menu()

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: EJEMPLO BÁSICO DE CONDICIONES EN PYTHON
# ? ESTA SECCIÓN ENSEÑA CÓMO UTILIZAR CONDICIONES SIMPLES EN UN CONTEXTO DE ADMINISTRACIÓN DE SISTEMAS.
# ? UNA CONDICIÓN SE UTILIZA PARA TOMAR DECISIONES BASADAS EN UNA EXPRESIÓN VERDADERA O FALSA.
# -------------------------------------------------------------------------------------------

# * PEDIR AL USUARIO QUE INTRODUZCA EL USO DE CPU.
# * SI EL USO DE CPU ES MAYOR AL 85%, SE MUESTRA UNA ALERTA, SI NO, SE INDICA QUE TODO ESTÁ NORMAL.

# TODO: ESCRIBE AQUÍ TU CÓDIGO PARA PEDIR EL USO DE CPU Y EVALUAR SI ES MAYOR AL 85%.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: CONDICIONES MÚLTIPLES CON ELIF
# ? EN ESTA SECCIÓN SE UTILIZA ELIF PARA EVALUAR DIFERENTES CONDICIONES.
# ? PODEMOS VERIFICAR SI TANTO EL USO DE CPU COMO EL USO DE MEMORIA ESTÁN POR ENCIMA DE UN UMBRAL.
# -------------------------------------------------------------------------------------------

# * PEDIR AL USUARIO QUE INTRODUZCA EL USO DE MEMORIA.
# * VERIFICAR SI TANTO EL USO DE CPU COMO EL USO DE MEMORIA SON MAYORES AL 85%.
# * USAR ELIF PARA EVALUAR SI UNO DE LOS DOS RECURSOS (CPU O MEMORIA) ESTÁ ALTO.
# * SI AMBOS ESTÁN BAJOS, MOSTRAR UN MENSAJE DE QUE TODO ESTÁ EN ORDEN.

# TODO: ESCRIBE AQUÍ TU CÓDIGO PARA EVALUAR EL USO DE CPU Y MEMORIA CON CONDICIONES MÚLTIPLES.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: CONDICIONES ANIDADAS
# ? ESTA SECCIÓN DEMUESTRA CÓMO SE PUEDEN ANIDAR CONDICIONES PARA TOMAR DECISIONES MÁS COMPLEJAS.
# ? SE EVALÚA SI UN SERVIDOR ESTÁ CONECTADO A LA RED Y SI EL USO DE CPU ES ALTO.
# -------------------------------------------------------------------------------------------

# * SOLICITAR AL USUARIO SI EL SERVIDOR ESTÁ CONECTADO A LA RED (SÍ/NO).
# * SI EL SERVIDOR ESTÁ CONECTADO, EVALUAR EL USO DE CPU Y MOSTRAR UNA ALERTA SI ES ALTO.
# * SI NO ESTÁ CONECTADO, INDICAR QUE EL SERVIDOR ESTÁ DESCONECTADO.

# TODO: ESCRIBE AQUÍ TU CÓDIGO PARA EVALUAR EL ESTADO DE LA RED Y EL USO DE CPU USANDO CONDICIONES ANIDADAS.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USO DE OPERADORES DE COMPARACIÓN Y LÓGICOS
# ? LOS OPERADORES LÓGICOS COMO "AND" Y "OR" NOS PERMITEN COMBINAR MÚLTIPLES CONDICIONES.
# ? EN ESTE EJEMPLO, VERIFICAMOS SI EL USO DE CPU Y MEMORIA ESTÁN POR DEBAJO DEL 50%.
# -------------------------------------------------------------------------------------------

# * EVALUAR SI EL USO DE CPU Y EL USO DE MEMORIA ESTÁN POR DEBAJO DEL 50% USANDO "AND".
# * SI SOLO UNO DE LOS RECURSOS ESTÁ POR DEBAJO DEL 50%, USAR "OR" PARA MOSTRARLO.
# * SI NINGUNO ESTÁ POR DEBAJO DEL 50%, INDICAR QUE AMBOS RECURSOS ESTÁN ALTOS.

# TODO: ESCRIBE AQUÍ TU CÓDIGO PARA EVALUAR EL USO DE CPU Y MEMORIA USANDO OPERADORES LÓGICOS.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: EVALUACIÓN COMBINADA
# ? AQUÍ COMBINAMOS EL ESTADO DEL SERVIDOR CON SU SEGURIDAD. SI EL SERVIDOR ESTÁ ACTUALIZADO
# ? Y TIENE RECURSOS BAJOS, ES SEGURO Y EFICIENTE. SI NO TIENE ACTUALIZACIONES, SE MOSTRARÁ UNA ALERTA.
# -------------------------------------------------------------------------------------------

# * PEDIR AL USUARIO SI EL SERVIDOR TIENE ACTUALIZACIONES INSTALADAS (SÍ/NO).
# * VERIFICAR SI EL USO DE CPU Y MEMORIA ESTÁN BAJOS Y SI EL SERVIDOR ESTÁ ACTUALIZADO.
# * SI TIENE RECURSOS ALTOS Y NO TIENE ACTUALIZACIONES, MOSTRAR UNA ALERTA DE ALTO RIESGO.
# * SI ESTÁ ACTUALIZADO Y TIENE RECURSOS BAJOS, MOSTRAR QUE EL SERVIDOR ES SEGURO Y EFICIENTE.

# TODO: ESCRIBE AQUÍ TU CÓDIGO PARA EVALUAR EL ESTADO DEL SERVIDOR Y MOSTRAR EL ESTADO DE SEGURIDAD.


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. SOLICITA EL NOMBRE DEL SERVIDOR Y GUARDALO EN UNA VARIABLE.
# 2. SOLICITA EL USO DE CPU Y EL USO DE MEMORIA DEL SERVIDOR.
# 3. SI EL USO DE CPU O MEMORIA ES MAYOR AL 85%, MUESTRA UNA ALERTA.
# 4. SOLICITA SI EL SERVIDOR TIENE ACTUALIZACIONES INSTALADAS Y GUARDA EL RESULTADO.
# 5. MUESTRA UN RESUMEN FINAL QUE INCLUYA EL NOMBRE DEL SERVIDOR, USO DE CPU, USO DE MEMORIA Y SI ESTÁ ACTUALIZADO.
# 6. SI EL SERVIDOR TIENE RECURSOS ALTOS Y NO TIENE ACTUALIZACIONES, MUESTRA UNA ALERTA DE ALTO RIESGO.
# -------------------------------------------------------------------------------------------

# TODO: ESCRIBE AQUÍ TU CÓDIGO PARA LA AUTOEVALUACIÓN FINAL.
