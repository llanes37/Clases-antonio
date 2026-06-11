# =========================================================================================
#  📘 PYTHON CLASE 1.2 — Cadenas de Caracteres y Operadores
#  ────────────────────────────────────────────────────────────────────────────────────────
#  En esta clase aprenderás:
#    * Indexación y slicing de cadenas.
#    * Métodos útiles de cadenas (.split, .replace, .upper, .lower, etc).
#    * Operadores aritméticos, de comparación, lógicos y de asignación.
#    * Un proyecto integrador: análisis de texto (velocidad de lectura).
# =========================================================================================

from typing import Any, Callable

# * Configuración general ---------------------------------------------------------------
RUN_INTERACTIVE = True   # True: menú interactivo; False: ejecuta todo sin preguntar
PAUSE = False            # Pausa tras cada sección

# * Utilidades --------------------------------------------------------------------------
def print_firma():
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Página web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")

def pause(msg="Pulsa Enter para continuar..."):
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass

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

def encabezado(titulo: str):
    print("\n" + "="*80)
    print(titulo)
    print("="*80)

# =========================================================================================
#  SECCIÓN 1 · CADENAS DE CARACTERES
# =========================================================================================
def seccion_1_cadenas():
    encabezado("SECCIÓN 1 · CADENAS DE CARACTERES")

    # * TEORÍA
    print("Definir cadenas, indexación, slicing y métodos útiles.\n")

    # * DEMO · Definir y manipular cadenas
    print("--- Demo: Definir cadenas ---")
    cadena = "Hola Mundo"
    print(f"Cadena: {cadena}")

    print("\n--- Demo: Indexación ---")
    print(f"Primer carácter [0]: {cadena[0]}")
    print(f"Último carácter [-1]: {cadena[-1]}")
    print(f"Segundo carácter [1]: {cadena[1]}")

    print("\n--- Demo: Slicing ---")
    print(f"Primeros 4 caracteres [0:4]: {cadena[0:4]}")
    print(f"Caracteres del 5 al 10 [5:10]: {cadena[5:10]}")
    print(f"Cada 2 caracteres [0:10:2]: {cadena[0:10:2]}")

    print("\n--- Demo: Métodos útiles ---")
    print(f"Mayúsculas: {cadena.upper()}")
    print(f"Minúsculas: {cadena.lower()}")
    print(f"Capitalizar: {cadena.capitalize()}")
    print(f"Posición de 'Mundo': {cadena.find('Mundo')}")
    print(f"Contar 'o': {cadena.count('o')}")
    print(f"Reemplazar 'Mundo' por 'Python': {cadena.replace('Mundo', 'Python')}")

    frase = "Python es increíble"
    palabras = frase.split()
    print(f"Dividir '{frase}': {palabras}")
    print(f"Total de palabras: {len(palabras)}")

    # TODO: (Tema: MANIPULACIÓN DE CADENAS)
    # Crea un programa que:
    # 1) Pida una cadena de texto al usuario.
    # 2) Muestre: primera letra, última letra, mayúsculas, minúsculas.
    # 3) Divida en palabras y muestre cuántas hay.
    # 4) Reemplace una palabra por otra.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 · OPERADORES ARITMÉTICOS
# =========================================================================================
def seccion_2_aritmeticos():
    encabezado("SECCIÓN 2 · OPERADORES ARITMÉTICOS")

    # * TEORÍA
    print("Suma, resta, multiplicación, división, módulo y potencia.\n")

    # * DEMO
    print("--- Operaciones básicas ---")
    print(f"2 + 2 = {2 + 2}")
    print(f"10 - 3 = {10 - 3}")
    print(f"8 * 3 = {8 * 3}")
    print(f"30 / 6 = {30 / 6}  (división, devuelve float)")
    print(f"21 / 5 = {21 / 5}")
    print(f"21 // 5 = {21 // 5}  (división entera, devuelve int)")
    print(f"21 % 5 = {21 % 5}  (módulo, resto)")
    print(f"2 ** 3 = {2 ** 3}  (potencia)")

    print("\n--- Ejemplo práctico: cálculo de compra ---")
    precio_unitario = 15.99
    cantidad = 3
    total = precio_unitario * cantidad
    iva = total * 0.21
    total_con_iva = total + iva
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${total:.2f}")
    print(f"IVA (21%): ${iva:.2f}")
    print(f"Total: ${total_con_iva:.2f}")

    # TODO: (Tema: CALCULADORA DE OPERACIONES)
    # Pide dos números y muestra:
    # - Suma, resta, multiplicación, división, división entera, módulo, potencia.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 · OPERADORES DE COMPARACIÓN
# =========================================================================================
def seccion_3_comparacion():
    encabezado("SECCIÓN 3 · OPERADORES DE COMPARACIÓN")

    # * TEORÍA
    print("Mayor que, menor que, igual, distinto, etc.\n")

    # * DEMO
    print("--- Comparaciones numéricas ---")
    print(f"5 > 6 = {5 > 6}")
    print(f"5 < 6 = {5 < 6}")
    print(f"8 >= 6 = {8 >= 6}")
    print(f"5 <= 3 = {5 <= 3}")
    print(f"5 == 5 = {5 == 5}")
    print(f"5 != 5 = {5 != 5}")

    print("\n--- Comparaciones con cadenas (orden alfabético) ---")
    print(f"'Antonio' > 'Zacarías' = {'Antonio' > 'Zacarías'}")
    print(f"'Pepe' < 'Pepa' = {'Pepe' < 'Pepa'}")

    print("\n--- Encadenar comparaciones ---")
    a, b, c = 1, 2, 3
    print(f"1 < 2 < 3 = {a < b < c}")
    print(f"1 >= 2 > 3 = {a >= b > c}")

    print("\n--- Ejemplo: verificación de edad ---")
    edad = 25
    print(f"¿Tienes 25 años? {edad == 25}")
    print(f"¿Eres mayor de 18? {edad >= 18}")
    print(f"¿Eres menor de 65? {edad < 65}")
    print(f"¿Estás entre 18 y 65? {18 <= edad <= 65}")

    # TODO: (Tema: COMPARADOR DE NÚMEROS)
    # Pide dos números y muestra:
    # - Si son iguales, cuál es mayor, cuál es menor.
    # - Si el primero está entre 10 y 100.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 · OPERADORES LÓGICOS Y ASIGNACIÓN
# =========================================================================================
def seccion_4_logicos_asignacion():
    encabezado("SECCIÓN 4 · OPERADORES LÓGICOS Y ASIGNACIÓN")

    # * TEORÍA
    print("AND, OR, NOT y operadores de asignación compuesta.\n")

    # * DEMO · Lógicos
    print("--- Operador AND ---")
    print(f"True and True = {True and True}")
    print(f"True and False = {True and False}")
    print(f"False and False = {False and False}")

    print("\n--- Operador OR ---")
    print(f"True or True = {True or True}")
    print(f"True or False = {True or False}")
    print(f"False or False = {False or False}")

    print("\n--- Operador NOT ---")
    print(f"not True = {not True}")
    print(f"not False = {not False}")

    print("\n--- Ejemplo lógico: acceso a aplicación ---")
    usuario_autenticado = True
    es_premium = False
    puede_acceder = usuario_autenticado and (es_premium or True)
    print(f"¿Puede acceder? {puede_acceder}")

    # * DEMO · Asignación compuesta
    print("\n--- Operadores de asignación compuesta ---")
    x = 6
    print(f"x = {x}")
    x += 15
    print(f"x += 15  →  x = {x}")
    x -= 2
    print(f"x -= 2   →  x = {x}")
    x *= 2
    print(f"x *= 2   →  x = {x}")
    x %= 3
    print(f"x %= 3   →  x = {x}")

    x = 30
    x /= 2
    print(f"x = 30; x /= 2  →  x = {x}")
    x //= 2
    print(f"x //= 2  →  x = {x}")
    x **= 2
    print(f"x **= 2  →  x = {x}")

    # TODO: (Tema: COMBINACIÓN DE OPERADORES)
    # Pide dos números y muestra:
    # - Si ambos son positivos (AND).
    # - Si al menos uno es mayor a 50 (OR).
    # - Si no es igual a 10 (NOT).
    # - Modifica un número con +=, -=, *=.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  AUTOEVALUACIÓN FINAL: ANALIZADOR DE TEXTO
# =========================================================================================
def autoevaluacion():
    encabezado("AUTOEVALUACIÓN FINAL · Analizador de Texto")

    print("Proyecto: Calcula velocidad de lectura de un texto.\n")

    # TODO: (Tema: ANALIZADOR DE LECTURA)
    # Una persona normal lee 2 palabras/segundo.
    # Un locutor lee 30% más rápido.
    #
    # Tu programa debe:
    # 1) Pedir un texto al usuario.
    # 2) Contar palabras con .split().
    # 3) Calcular tiempo (palabras / 2).
    # 4) Si > 30 seg, mostrar aviso "¡Menudo testamento!"
    # 5) Calcular tiempo locutor (tiempo * 0.7).
    # 6) Mostrar todo con f-strings y 1 decimal.
    #
    # Salida esperada:
    # "Escribiste 14 palabras, y tardarías 7.0 segundos en leerlo."
    # "¡Menudo testamento!"  (solo si > 30)
    # "El locutor de radio, lo leería en 4.9 segundos."
    #
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu():
    while True:
        print_firma()
        print("MENÚ · Elige una opción")
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
            print_firma()
            break
        elif op == 1: seccion_1_cadenas(); pause()
        elif op == 2: seccion_2_aritmeticos(); pause()
        elif op == 3: seccion_3_comparacion(); pause()
        elif op == 4: seccion_4_logicos_asignacion(); pause()
        elif op == 5: autoevaluacion(); pause()
        elif op == 6:
            seccion_1_cadenas(); seccion_2_aritmeticos(); seccion_3_comparacion(); seccion_4_logicos_asignacion(); autoevaluacion(); pause()
        else:
            print("! Elige una opción del 0 al 6.")

# =========================================================================================
#  EJECUCIÓN
# =========================================================================================
if __name__ == "__main__":
    menu()
