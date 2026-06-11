# =========================================================================================
#  📗 PYTHON CLASE 1.2 — Cadenas y Operadores (NO AVANZADO, MUY COMENTADO)
#  * TIP: Este archivo usa marcadores compatibles con la extensión 'Better Comments'
#  ───────────────────────────────────────────────────────────────────────────────────────-
#  Este archivo mantiene la estructura didáctica del material original pero
#  con comentarios ampliados y explicaciones paso a paso ("better comments").
#  * USO: marcadores como '# !' (IMPORTANTE), '# ?' (PREGUNTA), '# *' (HIGHLIGHT),
#  *      '# TODO:' (TAREA), '# NOTE:' (NOTA) ayudan a colorear en el editor.
#  Objetivo: que los alumnos entiendan cada línea y cada idea sin necesidad
#  de documentación externa. No se incluyen tests ni versiones avanzadas.
# =========================================================================================

from typing import Any, Callable

# * CONFIGURACIÓN GENERAL
# ? RUN_INTERACTIVE: si True, el script pedirá entradas al usuario
# ? PAUSE: si True, hará una pausa entre secciones para revisar resultados
# ! Cambia estas variables para ejecutar en clase o en modo automatizado
RUN_INTERACTIVE = True   # Cambia a False para ejecutar sin pedir input
PAUSE = False            # Cambiar a True si quieres pausar entre secciones

# * UTILIDADES PEQUEÑAS (para reutilizar y mejorar la legibilidad)
# * Estas funciones hacen el código más limpio y evitan repetir código
# NOTE: son puntos clave para enseñar buenas prácticas (funciones pequeñas y legibles)
# ? Usa estas funciones para demostrar la ventaja de abstraer lógica repetida

def print_firma() -> None:
    """Imprime firma y separador (útil para que el output quede ordenado)."""
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Página web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")


def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    """Pausa la ejecución si PAUSE == True.

    - Evita que el alumno pierda la salida al ejecutar todo de golpe.
    - Si PAUSE es False, esta función no hace nada y evita condicionales en el
      resto del código.
    """
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        # En entornos sin stdin, simplemente continuamos.
        pass


def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
    """Lee una entrada y la convierte al tipo deseado.

    - prompt: mensaje para el usuario.
    - caster: función que convierte string -> tipo (int, float, str, ...).
    - default: si el usuario deja vacío o hay error, devolvemos este valor.

    Ejemplo: safe_input('Edad: ', int, 18)
    """
    if not RUN_INTERACTIVE:
        # En modo no interactivo devolvemos valor por defecto para evitar bloqueos.
        return default
    try:
        raw = input(prompt)
        if raw.strip() == "":
            print("Entrada vacía; usando valor por defecto.")
            return default
        return caster(raw)
    except (ValueError, EOFError):
        print("¡Entrada no válida! Usando valor por defecto.")
        return default

# =========================================================================================
# SECCIÓN 1 · Cadenas de caracteres (explicación paso a paso)
# =========================================================================================

def seccion_1_cadenas() -> None:
    """Demuestra indexación, slicing y métodos básicos de cadenas.

    Comentarios (mejorados):
    - Indexación: acceder a caracteres individuales con corchetes y un índice.
    - Slicing: obtener subcadenas con [inicio:fin:paso].
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 1 · CADENAS DE CARACTERES")
    print("=" * 80)

    # * EJEMPLO BÁSICO: definimos una cadena y mostramos operaciones comunes.
    cadena = "Hola Mundo"
    print(f"Cadena: {cadena}")

    # ! Indexación (IMPORTANTE): siempre empieza en 0
    print(f"Primer carácter [0]: {cadena[0]}  # 'H'")
    print(f"Último carácter [-1]: {cadena[-1]}  # 'o' (índice negativo)" )

    # * Slicing: obtener subcadenas (no incluye el índice 'fin')
    print(f"Primeros 4 caracteres [0:4]: {cadena[0:4]}  # 'Hola'")
    print(f"Desde 5 hasta el final [5:]: {cadena[5:]}  # 'Mundo'")
    print(f"Cada 2 caracteres [0:10:2]: {cadena[0:10:2]}  # 'Hl ud' dependiendo del texto")

    # * MÉTODOS ÚTILES: transformaciones inmutables (devuelven nueva cadena)
    print(f"Mayúsculas: {cadena.upper()}  # 'HOLA MUNDO'")
    print(f"Minúsculas: {cadena.lower()}  # 'hola mundo'")
    print(f"Reemplazar 'Mundo' por 'Python': {cadena.replace('Mundo','Python')}")

    # División en palabras: split() sin argumentos separa por espacios
    frase = "Python es increíble"
    palabras = frase.split()
    print(f"Dividir '{frase}': {palabras}  # Lista de palabras")
    print(f"Total de palabras: {len(palabras)}")

    # ? EJERCICIO PROPUESTO (guía): intenta implementar lo siguiente
    print("\n-- EJERCICIO PROPUESTO: crea un programa que pida una cadena y muestre:")
    print("   * primera letra, última letra, versión en mayúsculas y minúsculas")
    print("   * cuántas palabras tiene y sustituir una palabra por otra")

    # Zona del alumno: dejamos TODO para que el alumno lo implemente en clase
    # TODO: implementar la práctica guiada de manipulación de cadenas

# =========================================================================================
# SECCIÓN 2 · Operadores aritméticos (con ejemplos claros)
# =========================================================================================

def seccion_2_aritmeticos() -> None:
    print("\n" + "=" * 80)
    print("SECCIÓN 2 · OPERADORES ARITMÉTICOS")
    print("=" * 80)

    # * Comentario: mostramos operaciones básicas y resultados esperando que
    # * el alumno lea y modifique para practicar.
    a = 2 + 2
    b = 10 - 3
    c = 8 * 3
    d = 30 / 6  # división -> float
    e = 21 // 5  # división entera
    f = 21 % 5  # resto
    g = 2 ** 3  # potencia

    print(f"2 + 2 = {a}")
    print(f"10 - 3 = {b}")
    print(f"8 * 3 = {c}")
    print(f"30 / 6 = {d}  (división flotante)")
    print(f"21 // 5 = {e}  (división entera)")
    print(f"21 % 5 = {f}  (módulo)")
    print(f"2 ** 3 = {g}  (potencia)")

    # Ejemplo práctico: calculadora simple (puedes pedir números al alumno)
    precio_unitario = 15.99
    cantidad = 3
    subtotal = precio_unitario * cantidad
    iva = subtotal * 0.21
    total = subtotal + iva
    print("\n-- Ejemplo compra:")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (21%): ${iva:.2f}")
    print(f"Total: ${total:.2f}")

    # TODO: práctica: pide dos números y calcula todas las operaciones básicas

# =========================================================================================
# SECCIÓN 3 · Operadores de comparación
# =========================================================================================

def seccion_3_comparacion() -> None:
    print("\n" + "=" * 80)
    print("SECCIÓN 3 · OPERADORES DE COMPARACIÓN")
    print("=" * 80)

    print("Comparaciones simples:")
    print(f"5 > 6 = {5 > 6}")
    print(f"5 < 6 = {5 < 6}")
    print(f"5 == 5 = {5 == 5}")
    print(f"5 != 5 = {5 != 5}")

    # NOTE: Comparación de cadenas usa orden lexicográfico (alfabético)
    print(f"'Antonio' > 'Zacarías' = {'Antonio' > 'Zacarías'}  # cuidado con mayúsculas y acentos")

    # Encadenar comparaciones: útil y legible
    a, b, c = 1, 2, 3
    print(f"1 < 2 < 3 = {a < b < c}")

    # Ejercicio simple: pedir dos números y determinar cuál es mayor
    # TODO: implementar validador de entrada y comparar los números

# =========================================================================================
# SECCIÓN 4 · Operadores lógicos y de asignación
# =========================================================================================

def seccion_4_logicos_asignacion() -> None:
    print("\n" + "=" * 80)
    print("SECCIÓN 4 · OPERADORES LÓGICOS Y ASIGNACIÓN")
    print("=" * 80)

    # Operadores lógicos básicos
    print(f"True and False = {True and False}")
    print(f"True or False = {True or False}")
    print(f"not True = {not True}")

    # * EJEMPLO: control de acceso (como en aplicaciones reales)
    usuario_autenticado = True
    es_admin = False
    puede_acceder = usuario_autenticado and (es_admin or True)
    print(f"¿Puede acceder? {puede_acceder}")

    # Operadores de asignación compuesta (atajos para actualizar variables)
    x = 6
    x += 15
    x *= 2
    x %= 3
    print(f"Ejemplo de asignación compuesta → x = {x}")

    # TODO: práctica: pide dos números y aplica AND, OR, NOT y operadores compuestos

# =========================================================================================
# AUTOEVALUACIÓN FINAL: ANALIZADOR DE TEXTO (versión simple)
# =========================================================================================

def autoevaluacion() -> None:
    """Proyecto final: calcula la velocidad de lectura (versión simple).

    Reglas simplificadas:
    - Una persona normal lee 2 palabras/segundo.
    - El locutor lee 30% más rápido.

    Salidas (ejemplo):
    "Escribiste 14 palabras, y tardarías 7.0 segundos en leerlo."  (1 decimal)
    "¡Menudo testamento!"  (si > 30s)
    "El locutor de radio, lo leería en 4.9 segundos."  (1 decimal)

    Nota: esta implementación es sencilla y pensada para que el alumno la
    lea y entienda cada paso antes de extenderla.
    """
    print("\n" + "=" * 80)
    print("AUTOEVALUACIÓN FINAL · Analizador de Texto")
    print("=" * 80)

    # ? Pedimos el texto al alumno. Si está vacío, avisamos y salimos.
    try:
        texto = input("Escribe un texto: ").strip()
    except EOFError:
        # En algunos entornos (ej. automated run) no hay stdin
        texto = ""

    if texto == "":
        print("No escribiste nada.")
        return

    # Contar palabras usando split (método sencillo y suficiente para la clase)
    palabras = texto.split()
    n = len(palabras)

    # Cálculo de tiempos
    tiempo = n / 2.0
    tiempo_locutor = tiempo * 0.7

    # Salida con formatado y 1 decimal
    print(f"Escribiste {n} palabras, y tardarías {tiempo:.1f} segundos en leerlo.")
    if tiempo > 30:
        print("¡Menudo testamento!")
    print(f"El locutor de radio, lo leería en {tiempo_locutor:.1f} segundos.")

# =========================================================================================
# MENÚ PRINCIPAL (igual estructura que en el material original)
# =========================================================================================

def menu() -> None:
    """Muestra un menú simple para navegar por las secciones.

    Detalle: está pensado para uso en clase; el alumno puede ejecutar cada
    sección desde el menú para ver ejemplos en acción.
    """
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

        # Leemos opción con try/except para evitar crash por entrada inválida
        try:
            op = int(input("Opción: "))
        except Exception:
            print("¡Opción no válida! Elige un número del 0 al 6.")
            continue

        if op == 0:
            print("¡Hasta la próxima!")
            print_firma()
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
            autoevaluacion(); pause()
        elif op == 6:
            # Ejecutamos todo seguido (útil para demos rápidas en clase)
            seccion_1_cadenas(); seccion_2_aritmeticos(); seccion_3_comparacion(); seccion_4_logicos_asignacion(); autoevaluacion(); pause()
        else:
            print("¡Elige una opción del 0 al 6!")

# =========================================================================================
# EJECUCIÓN PRINCIPAL
# =========================================================================================

if __name__ == "__main__":
    # Si RUN_INTERACTIVE está en False, se podría ejecutar todo automáticamente.
    if not RUN_INTERACTIVE:
        seccion_1_cadenas(); seccion_2_aritmeticos(); seccion_3_comparacion(); seccion_4_logicos_asignacion(); autoevaluacion()
    else:
        menu()
