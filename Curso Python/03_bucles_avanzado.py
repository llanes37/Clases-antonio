# =========================================================================================
#  PYTHON CLASE 3 AVANZADA — BUCLES AVANZADOS (itertools, generadores, patrones, etc.)
#  ────────────────────────────────────────────────────────────────────────────────────────
#  En esta clase avanzada practicaras:
#    * Itertools (combinations, permutations, product, cycle, chain, groupby)
#    * Generadores con yield (lazy evaluation)
#    * zip() y zip_longest() para iterar en paralelo
#    * Diccionarios: items(), keys(), values() y dict comprehensions
#    * map(), filter() y reduce() con lambdas
#    * Patrones avanzados: sliding window, two pointers, acumuladores
#    * Recursion vs iteracion
#    * Walrus operator (:=) en bucles (Python 3.8+)
#    * Manejo de excepciones dentro de bucles
#    * Optimizacion y buenas practicas
#    * Ejercicios de nivel intermedio-avanzado
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica  ·  # NOTE: apunte util   ·  # // deprecado
# =========================================================================================

from typing import Any, Callable, Generator, Iterator
from functools import reduce
from itertools import (
    combinations, permutations, product, cycle, chain,
    groupby, islice, takewhile, dropwhile, accumulate, zip_longest
)

# * Configuracion general ---------------------------------------------------------------
RUN_INTERACTIVE = True   # True: pedir datos al usuario; False: usar valores por defecto
PAUSE = False            # Pausa tras cada opcion del menu
IA_DEMO = True           # Muestra una demo corta en el Laboratorio IA

# * Firma del curso ----------------------------------------------------------------------
def print_firma():
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Pagina web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")

# * Utilidades comunes -------------------------------------------------------------------
def pause(msg="Pulsa Enter para continuar..."):
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass

def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
    """# * Convierte la entrada al tipo deseado; si falla o no hay input, devuelve 'default'."""
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

def encabezado(titulo: str):
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)

# =========================================================================================
#  SECCION 1 · zip() y zip_longest() (iterar en paralelo)
# =========================================================================================
def seccion_1():
    encabezado("SECCION 1 · zip() y zip_longest() (iterar en paralelo)")

    # * TEORIA
    # zip(iter1, iter2, ...) -> combina elementos de multiples iterables en tuplas.
    # Se detiene cuando el mas corto termina.
    # zip_longest() rellena con un valor (fillvalue) cuando hay diferencia de longitud.

    # * DEMO · zip basico
    nombres = ["Ana", "Luis", "Maria", "Pedro"]
    edades = [25, 30, 22, 28]
    ciudades = ["Madrid", "Barcelona", "Sevilla"]

    print("zip() - se detiene en el mas corto:")
    for nombre, edad, ciudad in zip(nombres, edades, ciudades):
        print(f"  {nombre}, {edad} anos, vive en {ciudad}")

    print("\nzip_longest() - rellena con valor por defecto:")
    for nombre, edad, ciudad in zip_longest(nombres, edades, ciudades, fillvalue="N/A"):
        print(f"  {nombre}, {edad}, {ciudad}")

    # * DEMO · crear diccionario con zip
    claves = ["a", "b", "c"]
    valores = [1, 2, 3]
    diccionario = dict(zip(claves, valores))
    print(f"\nDiccionario creado con zip: {diccionario}")

    # * DEMO · descomprimir con zip(*)
    pares = [(1, "uno"), (2, "dos"), (3, "tres")]
    numeros, palabras = zip(*pares)
    print(f"Descomprimido: numeros={numeros}, palabras={palabras}")

    # TODO: (Tema: NOTAS DE ALUMNOS)
    # Tienes dos listas: alumnos = ["Juan", "Ana", "Pedro"] y notas = [8.5, 9.2, 7.8]
    # Usa zip para mostrar "Alumno: <nombre> - Nota: <nota>" para cada uno.
    # Luego calcula la media de las notas.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # alumnos = ["Juan", "Ana", "Pedro"]
    # notas = [8.5, 9.2, 7.8]
    # for alumno, nota in zip(alumnos, notas):
    #     print(f"Alumno: {alumno} - Nota: {nota}")
    # media = sum(notas) / len(notas)
    # print(f"Media: {media:.2f}")

# =========================================================================================
#  SECCION 2 · Diccionarios: items(), keys(), values()
# =========================================================================================
def seccion_2():
    encabezado("SECCION 2 · Iterando sobre diccionarios")

    # * TEORIA
    # dict.keys()   -> iterador de claves
    # dict.values() -> iterador de valores
    # dict.items()  -> iterador de pares (clave, valor)
    # ! CUIDADO: No modificar un dict mientras iteras sobre el (usar copia o list())

    # * DEMO · items()
    inventario = {"manzanas": 50, "naranjas": 30, "peras": 25, "uvas": 0}

    print("Inventario completo:")
    for producto, cantidad in inventario.items():
        estado = "AGOTADO" if cantidad == 0 else f"{cantidad} uds"
        print(f"  {producto}: {estado}")

    # * DEMO · filtrar mientras iteras (creando nueva estructura)
    disponibles = {k: v for k, v in inventario.items() if v > 0}
    print(f"\nProductos disponibles: {disponibles}")

    # * DEMO · ordenar por valor
    print("\nOrdenado por cantidad (mayor a menor):")
    for prod, cant in sorted(inventario.items(), key=lambda x: x[1], reverse=True):
        print(f"  {prod}: {cant}")

    # * DEMO · dict comprehension con transformacion
    precios_base = {"pan": 1.20, "leche": 0.95, "huevos": 2.50}
    precios_iva = {k: round(v * 1.21, 2) for k, v in precios_base.items()}
    print(f"\nPrecios con IVA: {precios_iva}")

    # TODO: (Tema: CONTADOR DE PALABRAS)
    # Dada una frase, crea un diccionario que cuente cuantas veces aparece cada palabra.
    # Luego muestra las palabras ordenadas por frecuencia.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # frase = "el gato y el perro y el pajaro"
    # palabras = frase.lower().split()
    # contador = {}
    # for palabra in palabras:
    #     contador[palabra] = contador.get(palabra, 0) + 1
    # for palabra, cuenta in sorted(contador.items(), key=lambda x: x[1], reverse=True):
    #     print(f"{palabra}: {cuenta}")

# =========================================================================================
#  SECCION 3 · Generadores y yield (evaluacion perezosa)
# =========================================================================================
def seccion_3():
    encabezado("SECCION 3 · Generadores y yield (lazy evaluation)")

    # * TEORIA
    # Un generador produce valores uno a uno, sin cargar todo en memoria.
    # Se define con 'yield' en lugar de 'return'.
    # Util para: secuencias infinitas, archivos grandes, procesamiento streaming.

    # * DEMO · generador simple
    def contar_hasta(n: int) -> Generator[int, None, None]:
        """Genera numeros del 1 al n."""
        i = 1
        while i <= n:
            yield i
            i += 1

    print("Generador contar_hasta(5):")
    for num in contar_hasta(5):
        print(f"  {num}", end="")
    print()

    # * DEMO · generador infinito (con limite)
    def fibonacci() -> Generator[int, None, None]:
        """Genera la secuencia de Fibonacci infinitamente."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    print("\nPrimeros 10 numeros de Fibonacci:")
    fib_gen = fibonacci()
    for _ in range(10):
        print(f"  {next(fib_gen)}", end="")
    print()

    # * DEMO · expresion generadora (como list comprehension pero con ())
    cuadrados_gen = (x**2 for x in range(1, 6))
    print(f"\nExpresion generadora de cuadrados: {list(cuadrados_gen)}")

    # * DEMO · yield from (delegar a otro generador)
    def cadena_generadores():
        yield from range(3)
        yield from "ABC"
        yield from [100, 200]

    print(f"yield from multiple: {list(cadena_generadores())}")

    # TODO: (Tema: GENERADOR DE PRIMOS)
    # Crea un generador que produzca numeros primos indefinidamente.
    # Usa islice para obtener los primeros 15 primos.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def es_primo(n):
    #     if n < 2:
    #         return False
    #     for i in range(2, int(n**0.5) + 1):
    #         if n % i == 0:
    #             return False
    #     return True
    #
    # def generador_primos():
    #     n = 2
    #     while True:
    #         if es_primo(n):
    #             yield n
    #         n += 1
    #
    # from itertools import islice
    # primeros_15 = list(islice(generador_primos(), 15))
    # print(f"Primeros 15 primos: {primeros_15}")

# =========================================================================================
#  SECCION 4 · itertools (combinaciones, permutaciones, etc.)
# =========================================================================================
def seccion_4():
    encabezado("SECCION 4 · itertools (herramientas de iteracion)")

    # * TEORIA
    # itertools proporciona iteradores eficientes para operaciones comunes:
    # - combinations(iterable, r): combinaciones de r elementos
    # - permutations(iterable, r): permutaciones de r elementos
    # - product(*iterables): producto cartesiano
    # - cycle(iterable): repite infinitamente
    # - chain(*iterables): concatena iterables
    # - groupby(iterable, key): agrupa elementos consecutivos
    # - islice(iterable, stop): slice para iteradores
    # - takewhile/dropwhile: filtra con condicion

    # * DEMO · combinations y permutations
    letras = ["A", "B", "C"]
    print(f"Combinaciones de 2: {list(combinations(letras, 2))}")
    print(f"Permutaciones de 2: {list(permutations(letras, 2))}")

    # * DEMO · product (producto cartesiano)
    colores = ["rojo", "azul"]
    tallas = ["S", "M", "L"]
    print(f"\nProducto cartesiano (variantes de producto):")
    for color, talla in product(colores, tallas):
        print(f"  {color}-{talla}")

    # * DEMO · cycle (con limite)
    print("\nCycle con limite:")
    turnos = cycle(["Juan", "Ana", "Pedro"])
    for i, jugador in enumerate(turnos):
        if i >= 7:
            break
        print(f"  Turno {i+1}: {jugador}")

    # * DEMO · chain (concatenar)
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista3 = [7, 8, 9]
    concatenada = list(chain(lista1, lista2, lista3))
    print(f"\nChain (concatenar): {concatenada}")

    # * DEMO · groupby
    datos = [("fruta", "manzana"), ("fruta", "pera"), ("verdura", "zanahoria"),
             ("verdura", "lechuga"), ("fruta", "naranja")]
    datos_ordenados = sorted(datos, key=lambda x: x[0])
    print("\nGroupby (agrupacion):")
    for categoria, items in groupby(datos_ordenados, key=lambda x: x[0]):
        productos = [item[1] for item in items]
        print(f"  {categoria}: {productos}")

    # * DEMO · accumulate
    numeros = [1, 2, 3, 4, 5]
    print(f"\nAccumulate (suma acumulada): {list(accumulate(numeros))}")
    print(f"Accumulate (producto): {list(accumulate(numeros, lambda x, y: x * y))}")

    # TODO: (Tema: GENERADOR DE CONTRASENAS)
    # Usa itertools.product para generar todas las contrasenas posibles
    # de 3 caracteres usando solo los digitos 0-9.
    # Cuenta cuantas hay y muestra las primeras 10.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # from itertools import product
    # digitos = "0123456789"
    # contrasenas = product(digitos, repeat=3)
    # lista_contrasenas = ["".join(c) for c in contrasenas]
    # print(f"Total contrasenas: {len(lista_contrasenas)}")
    # print(f"Primeras 10: {lista_contrasenas[:10]}")

# =========================================================================================
#  SECCION 5 · map(), filter() y reduce()
# =========================================================================================
def seccion_5():
    encabezado("SECCION 5 · map(), filter() y reduce()")

    # * TEORIA
    # map(func, iterable): aplica func a cada elemento
    # filter(func, iterable): filtra elementos donde func devuelve True
    # reduce(func, iterable): reduce a un solo valor aplicando func acumulativamente
    # Estas funciones devuelven iteradores (perezosos).

    # * DEMO · map()
    numeros = [1, 2, 3, 4, 5]
    cuadrados = list(map(lambda x: x**2, numeros))
    print(f"map (cuadrados): {cuadrados}")

    # map con multiples iterables
    lista_a = [1, 2, 3]
    lista_b = [10, 20, 30]
    sumas = list(map(lambda a, b: a + b, lista_a, lista_b))
    print(f"map con 2 listas (sumas): {sumas}")

    # * DEMO · filter()
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(f"\nfilter (pares): {pares}")

    # filter con None (elimina valores falsy)
    datos = [0, 1, "", "hola", None, [], [1, 2], False, True]
    truthy = list(filter(None, datos))
    print(f"filter(None, ...) (truthy): {truthy}")

    # * DEMO · reduce()
    numeros = [1, 2, 3, 4, 5]
    suma = reduce(lambda acc, x: acc + x, numeros)
    producto = reduce(lambda acc, x: acc * x, numeros)
    maximo = reduce(lambda acc, x: acc if acc > x else x, numeros)
    print(f"\nreduce (suma): {suma}")
    print(f"reduce (producto): {producto}")
    print(f"reduce (maximo): {maximo}")

    # * DEMO · combinando map, filter, reduce
    # Obtener la suma de los cuadrados de los numeros pares
    numeros = range(1, 11)
    resultado = reduce(
        lambda acc, x: acc + x,
        map(lambda x: x**2,
            filter(lambda x: x % 2 == 0, numeros))
    )
    print(f"\nSuma de cuadrados de pares (1-10): {resultado}")

    # TODO: (Tema: PROCESAMIENTO DE DATOS)
    # Tienes una lista de diccionarios con productos:
    # productos = [
    #     {"nombre": "laptop", "precio": 1000, "stock": 5},
    #     {"nombre": "mouse", "precio": 25, "stock": 0},
    #     {"nombre": "teclado", "precio": 75, "stock": 10},
    #     {"nombre": "monitor", "precio": 300, "stock": 3},
    # ]
    # Usa filter para obtener productos con stock > 0
    # Usa map para aplicar 10% de descuento al precio
    # Usa reduce para calcular el valor total del inventario (precio * stock)
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # productos = [
    #     {"nombre": "laptop", "precio": 1000, "stock": 5},
    #     {"nombre": "mouse", "precio": 25, "stock": 0},
    #     {"nombre": "teclado", "precio": 75, "stock": 10},
    #     {"nombre": "monitor", "precio": 300, "stock": 3},
    # ]
    # disponibles = list(filter(lambda p: p["stock"] > 0, productos))
    # con_descuento = list(map(lambda p: {**p, "precio": p["precio"] * 0.9}, disponibles))
    # valor_total = reduce(lambda acc, p: acc + p["precio"] * p["stock"], disponibles, 0)
    # print(f"Productos disponibles: {[p['nombre'] for p in disponibles]}")
    # print(f"Valor total inventario: {valor_total}")

# =========================================================================================
#  SECCION 6 · Patrones avanzados: Sliding Window
# =========================================================================================
def seccion_6():
    encabezado("SECCION 6 · Patron Sliding Window (ventana deslizante)")

    # * TEORIA
    # El patron sliding window es util para:
    # - Encontrar subarrays/substrings con cierta propiedad
    # - Calcular sumas/promedios moviles
    # - Detectar patrones en secuencias
    # Complejidad: O(n) en lugar de O(n*k) del enfoque ingenuo

    # * DEMO · Suma maxima de k elementos consecutivos
    def max_suma_k_elementos(arr: list, k: int) -> int:
        """Encuentra la suma maxima de k elementos consecutivos."""
        if len(arr) < k:
            return 0

        # Calcular suma de la primera ventana
        suma_ventana = sum(arr[:k])
        max_suma = suma_ventana

        # Deslizar la ventana
        for i in range(k, len(arr)):
            suma_ventana += arr[i] - arr[i - k]  # Anadir nuevo, quitar viejo
            max_suma = max(max_suma, suma_ventana)

        return max_suma

    numeros = [2, 1, 5, 1, 3, 2, 8, 1, 3]
    k = 3
    resultado = max_suma_k_elementos(numeros, k)
    print(f"Array: {numeros}")
    print(f"Suma maxima de {k} elementos consecutivos: {resultado}")

    # * DEMO · Media movil
    def media_movil(arr: list, k: int) -> list:
        """Calcula la media movil de k elementos."""
        if len(arr) < k:
            return []

        resultado = []
        suma_ventana = sum(arr[:k])
        resultado.append(suma_ventana / k)

        for i in range(k, len(arr)):
            suma_ventana += arr[i] - arr[i - k]
            resultado.append(suma_ventana / k)

        return [round(x, 2) for x in resultado]

    datos = [10, 20, 30, 40, 50, 60, 70]
    print(f"\nDatos: {datos}")
    print(f"Media movil (k=3): {media_movil(datos, 3)}")

    # * DEMO · Substring mas largo sin repetir caracteres
    def longest_unique_substring(s: str) -> int:
        """Encuentra la longitud del substring mas largo sin caracteres repetidos."""
        char_index = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length

    texto = "abcabcbb"
    print(f"\nTexto: '{texto}'")
    print(f"Substring mas largo sin repetir: {longest_unique_substring(texto)}")

    # TODO: (Tema: DETECTOR DE PICOS)
    # Implementa una funcion que encuentre todos los "picos" en una lista.
    # Un pico es un elemento mayor que sus dos vecinos.
    # Usa el patron de ventana deslizante de tamano 3.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def encontrar_picos(arr):
    #     picos = []
    #     for i in range(1, len(arr) - 1):
    #         if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
    #             picos.append((i, arr[i]))
    #     return picos
    #
    # datos = [1, 3, 2, 5, 1, 4, 2]
    # print(f"Datos: {datos}")
    # print(f"Picos encontrados: {encontrar_picos(datos)}")

# =========================================================================================
#  SECCION 7 · Patron Two Pointers (dos punteros)
# =========================================================================================
def seccion_7():
    encabezado("SECCION 7 · Patron Two Pointers (dos punteros)")

    # * TEORIA
    # El patron two pointers usa dos indices para recorrer una estructura.
    # Variantes:
    # - Desde extremos opuestos (para arrays ordenados)
    # - Ambos desde el inicio (rapido/lento para ciclos)
    # Complejidad tipica: O(n)

    # * DEMO · Par que suma un objetivo (array ordenado)
    def par_suma_objetivo(arr: list, objetivo: int) -> tuple:
        """Encuentra dos numeros que sumen el objetivo (array ordenado)."""
        izq, der = 0, len(arr) - 1

        while izq < der:
            suma = arr[izq] + arr[der]
            if suma == objetivo:
                return (arr[izq], arr[der])
            elif suma < objetivo:
                izq += 1
            else:
                der -= 1

        return None

    numeros = [1, 2, 4, 6, 8, 10, 12]
    objetivo = 14
    resultado = par_suma_objetivo(numeros, objetivo)
    print(f"Array ordenado: {numeros}")
    print(f"Par que suma {objetivo}: {resultado}")

    # * DEMO · Eliminar duplicados in-place
    def eliminar_duplicados(arr: list) -> int:
        """Elimina duplicados y devuelve la nueva longitud (array ordenado)."""
        if not arr:
            return 0

        pos_escritura = 1
        for pos_lectura in range(1, len(arr)):
            if arr[pos_lectura] != arr[pos_lectura - 1]:
                arr[pos_escritura] = arr[pos_lectura]
                pos_escritura += 1

        return pos_escritura

    arr_duplicados = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"\nArray con duplicados: {arr_duplicados.copy()}")
    nueva_long = eliminar_duplicados(arr_duplicados)
    print(f"Sin duplicados: {arr_duplicados[:nueva_long]}")

    # * DEMO · Es palindromo
    def es_palindromo(s: str) -> bool:
        """Verifica si una cadena es palindromo (ignorando no-alfanumericos)."""
        s = ''.join(c.lower() for c in s if c.isalnum())
        izq, der = 0, len(s) - 1

        while izq < der:
            if s[izq] != s[der]:
                return False
            izq += 1
            der -= 1

        return True

    textos = ["Anita lava la tina", "Hola mundo", "A man a plan a canal Panama"]
    print("\nVerificando palindromos:")
    for texto in textos:
        print(f"  '{texto}': {es_palindromo(texto)}")

    # * DEMO · Detectar ciclo (tortuga y liebre)
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None

    def tiene_ciclo(cabeza: Nodo) -> bool:
        """Detecta si una lista enlazada tiene ciclo."""
        if not cabeza:
            return False

        lento = cabeza
        rapido = cabeza

        while rapido and rapido.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
            if lento == rapido:
                return True

        return False

    # Crear lista con ciclo para demo
    n1, n2, n3, n4 = Nodo(1), Nodo(2), Nodo(3), Nodo(4)
    n1.siguiente = n2
    n2.siguiente = n3
    n3.siguiente = n4
    n4.siguiente = n2  # Ciclo!

    print(f"\nLista enlazada con ciclo: {tiene_ciclo(n1)}")

    # TODO: (Tema: CONTENEDOR CON MAS AGUA)
    # Dado un array de alturas, encuentra el contenedor que puede almacenar mas agua.
    # Area = min(altura[i], altura[j]) * (j - i)
    # Usa two pointers desde los extremos.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def max_agua(alturas):
    #     izq, der = 0, len(alturas) - 1
    #     max_area = 0
    #     while izq < der:
    #         ancho = der - izq
    #         altura = min(alturas[izq], alturas[der])
    #         area = ancho * altura
    #         max_area = max(max_area, area)
    #         if alturas[izq] < alturas[der]:
    #             izq += 1
    #         else:
    #             der -= 1
    #     return max_area
    #
    # alturas = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # print(f"Alturas: {alturas}")
    # print(f"Max agua: {max_agua(alturas)}")

# =========================================================================================
#  SECCION 8 · Walrus Operator (:=) en bucles
# =========================================================================================
def seccion_8():
    encabezado("SECCION 8 · Walrus Operator (:=) en bucles (Python 3.8+)")

    # * TEORIA
    # El operador morsa (:=) asigna y devuelve un valor en la misma expresion.
    # Util para: evitar calculos duplicados, simplificar while loops,
    # asignaciones en comprehensions.

    # * DEMO · while con entrada del usuario
    print("Simulacion de entrada (usando lista predefinida):")
    entradas = ["hola", "mundo", "python", "salir"]
    idx = 0

    def get_input():
        nonlocal idx
        if idx < len(entradas):
            val = entradas[idx]
            idx += 1
            return val
        return "salir"

    while (linea := get_input()) != "salir":
        print(f"  Procesando: {linea.upper()}")

    # * DEMO · evitar calculo duplicado en if
    import re
    texto = "Mi email es ejemplo@test.com y el tuyo?"

    if (match := re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', texto)):
        print(f"\nEmail encontrado: {match.group()}")
    else:
        print("\nNo se encontro email")

    # * DEMO · en list comprehension (filtrar y transformar)
    datos = ["  hola  ", "", "  mundo  ", "   ", "python"]
    # Sin walrus: procesariamos strip() dos veces
    limpios = [stripped for d in datos if (stripped := d.strip())]
    print(f"\nLista limpia (sin vacios): {limpios}")

    # * DEMO · leer bloques de datos
    def leer_en_bloques(datos: list, tamano: int):
        """Simula lectura de datos en bloques."""
        inicio = 0
        while (bloque := datos[inicio:inicio + tamano]):
            yield bloque
            inicio += tamano

    numeros = list(range(1, 12))
    print(f"\nLeyendo en bloques de 3:")
    for bloque in leer_en_bloques(numeros, 3):
        print(f"  Bloque: {bloque}")

    # TODO: (Tema: PROCESAMIENTO CON WALRUS)
    # Lee numeros de una lista hasta encontrar un negativo.
    # Usa walrus operator para asignar y verificar en el while.
    # Calcula la suma de todos los numeros positivos leidos.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # numeros = [5, 3, 8, 2, -1, 4, 6]
    # idx = 0
    # suma = 0
    # while idx < len(numeros) and (num := numeros[idx]) >= 0:
    #     suma += num
    #     idx += 1
    # print(f"Suma hasta encontrar negativo: {suma}")

# =========================================================================================
#  SECCION 9 · Manejo de excepciones en bucles
# =========================================================================================
def seccion_9():
    encabezado("SECCION 9 · Manejo de excepciones en bucles")

    # * TEORIA
    # Los bucles con operaciones que pueden fallar necesitan manejo de errores.
    # Estrategias: try/except dentro del bucle (continuar), fuera (abortar todo),
    # o usar else/finally para cleanup.

    # * DEMO · Procesar lista con errores individuales
    datos = ["10", "20", "treinta", "40", "50.5", "60"]

    print("Procesando datos con errores:")
    resultados = []
    errores = []

    for i, dato in enumerate(datos):
        try:
            numero = int(dato)
            resultados.append(numero)
            print(f"  [{i}] '{dato}' -> {numero}")
        except ValueError:
            errores.append((i, dato))
            print(f"  [{i}] '{dato}' -> ERROR (no es entero)")

    print(f"\nResultados validos: {resultados}")
    print(f"Errores: {errores}")

    # * DEMO · Reintentos con limite
    def operacion_inestable(intento: int) -> str:
        """Simula una operacion que falla las primeras veces."""
        if intento < 3:
            raise ConnectionError(f"Fallo en intento {intento}")
        return "Exito!"

    print("\nOperacion con reintentos:")
    max_intentos = 5
    for intento in range(1, max_intentos + 1):
        try:
            resultado = operacion_inestable(intento)
            print(f"  Intento {intento}: {resultado}")
            break
        except ConnectionError as e:
            print(f"  Intento {intento}: {e}")
            if intento == max_intentos:
                print("  Se agotaron los intentos!")
    else:
        print("  Bucle completado sin break (no deberia pasar aqui)")

    # * DEMO · for-else con excepcion
    def buscar_divisor(n: int, divisores: list) -> int:
        """Busca el primer divisor valido."""
        for d in divisores:
            try:
                if n % d == 0:
                    return d
            except ZeroDivisionError:
                print(f"  Saltando division por cero")
                continue
        return None

    print("\nBuscando divisor de 100:")
    divisores = [0, 7, 3, 5, 2]
    resultado = buscar_divisor(100, divisores)
    print(f"  Primer divisor encontrado: {resultado}")

    # * DEMO · finally para cleanup
    print("\nProcesamiento con cleanup:")
    recursos_abiertos = []

    try:
        for i in range(5):
            recursos_abiertos.append(f"recurso_{i}")
            if i == 3:
                raise RuntimeError("Error simulado!")
            print(f"  Procesando recurso_{i}")
    except RuntimeError as e:
        print(f"  ERROR: {e}")
    finally:
        print(f"  Cleanup: cerrando {len(recursos_abiertos)} recursos")
        recursos_abiertos.clear()

    # TODO: (Tema: VALIDADOR DE DATOS)
    # Crea una funcion que reciba una lista de diccionarios y valide que cada uno
    # tenga las claves "nombre" (str) y "edad" (int positivo).
    # Usa try/except para manejar errores y reporta cuales registros son invalidos.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def validar_registros(registros):
    #     validos = []
    #     invalidos = []
    #     for i, reg in enumerate(registros):
    #         try:
    #             nombre = reg["nombre"]
    #             edad = reg["edad"]
    #             if not isinstance(nombre, str) or not nombre:
    #                 raise ValueError("nombre invalido")
    #             if not isinstance(edad, int) or edad < 0:
    #                 raise ValueError("edad invalida")
    #             validos.append(reg)
    #         except (KeyError, ValueError) as e:
    #             invalidos.append((i, str(e)))
    #     return validos, invalidos
    #
    # registros = [
    #     {"nombre": "Ana", "edad": 25},
    #     {"nombre": "", "edad": 30},
    #     {"nombre": "Luis"},
    #     {"nombre": "Maria", "edad": -5},
    #     {"nombre": "Pedro", "edad": 40},
    # ]
    # v, inv = validar_registros(registros)
    # print(f"Validos: {v}")
    # print(f"Invalidos: {inv}")

# =========================================================================================
#  SECCION 10 · Recursion vs Iteracion
# =========================================================================================
def seccion_10():
    encabezado("SECCION 10 · Recursion vs Iteracion")

    # * TEORIA
    # Recursion: una funcion se llama a si misma. Elegante para problemas divisibles.
    # Iteracion: usa bucles. Mas eficiente en memoria (sin stack de llamadas).
    # Python tiene limite de recursion (~1000). Considerar tail recursion o convertir a iterativo.

    # * DEMO · Factorial recursivo vs iterativo
    def factorial_recursivo(n: int) -> int:
        if n <= 1:
            return 1
        return n * factorial_recursivo(n - 1)

    def factorial_iterativo(n: int) -> int:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    n = 10
    print(f"Factorial de {n}:")
    print(f"  Recursivo: {factorial_recursivo(n)}")
    print(f"  Iterativo: {factorial_iterativo(n)}")

    # * DEMO · Fibonacci con memoizacion
    def fib_memo(n: int, memo: dict = None) -> int:
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

    def fib_iterativo(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    n = 30
    print(f"\nFibonacci de {n}:")
    print(f"  Con memo: {fib_memo(n)}")
    print(f"  Iterativo: {fib_iterativo(n)}")

    # * DEMO · Aplanar lista anidada
    def aplanar_recursivo(lista: list) -> list:
        resultado = []
        for elemento in lista:
            if isinstance(elemento, list):
                resultado.extend(aplanar_recursivo(elemento))
            else:
                resultado.append(elemento)
        return resultado

    def aplanar_iterativo(lista: list) -> list:
        resultado = []
        pila = [lista]
        while pila:
            actual = pila.pop()
            if isinstance(actual, list):
                pila.extend(reversed(actual))
            else:
                resultado.append(actual)
        return resultado

    anidada = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
    print(f"\nLista anidada: {anidada}")
    print(f"  Aplanada (recursivo): {aplanar_recursivo(anidada)}")
    print(f"  Aplanada (iterativo): {aplanar_iterativo(anidada)}")

    # * DEMO · Binary search
    def busqueda_binaria_recursiva(arr: list, objetivo: int, izq: int = 0, der: int = None) -> int:
        if der is None:
            der = len(arr) - 1
        if izq > der:
            return -1
        medio = (izq + der) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            return busqueda_binaria_recursiva(arr, objetivo, medio + 1, der)
        else:
            return busqueda_binaria_recursiva(arr, objetivo, izq, medio - 1)

    def busqueda_binaria_iterativa(arr: list, objetivo: int) -> int:
        izq, der = 0, len(arr) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if arr[medio] == objetivo:
                return medio
            elif arr[medio] < objetivo:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    arr_ordenado = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    objetivo = 11
    print(f"\nBusqueda binaria de {objetivo} en {arr_ordenado}:")
    print(f"  Recursiva: indice {busqueda_binaria_recursiva(arr_ordenado, objetivo)}")
    print(f"  Iterativa: indice {busqueda_binaria_iterativa(arr_ordenado, objetivo)}")

    # TODO: (Tema: SUMA DE DIGITOS)
    # Implementa tanto recursiva como iterativamente una funcion que sume los digitos
    # de un numero hasta obtener un solo digito (ej: 9875 -> 29 -> 11 -> 2)
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def suma_digitos_recursiva(n):
    #     if n < 10:
    #         return n
    #     suma = sum(int(d) for d in str(n))
    #     return suma_digitos_recursiva(suma)
    #
    # def suma_digitos_iterativa(n):
    #     while n >= 10:
    #         n = sum(int(d) for d in str(n))
    #     return n
    #
    # numero = 9875
    # print(f"Suma de digitos de {numero}:")
    # print(f"  Recursiva: {suma_digitos_recursiva(numero)}")
    # print(f"  Iterativa: {suma_digitos_iterativa(numero)}")

# =========================================================================================
#  SECCION 11 · Laboratorio IA (Bucles Avanzados)
# =========================================================================================
def seccion_11_ia():
    encabezado("SECCION 11 · Laboratorio IA (Bucles Avanzados)")

    # * PROMPT KIT (copia/pega en ChatGPT o Claude)
    #
    # 1) PROMPT - GENERADOR DE DATOS:
    #    "Crea un generador en Python que produzca datos de sensores simulados
    #     (temperatura, humedad, timestamp). Incluye funciones para: filtrar lecturas
    #     anomalas, calcular medias moviles, y detectar tendencias. Usa itertools,
    #     generadores y patrones de ventana deslizante. 40-60 lineas, comentarios claros."
    #
    # 2) PROMPT - PROCESADOR DE LOGS:
    #    "Implementa un procesador de archivos de log que use generadores para leer
    #     linea por linea (memoria eficiente). Agrupa errores por tipo usando groupby,
    #     cuenta frecuencias, y genera un resumen. Incluye manejo de excepciones."
    #
    # 3) PROMPT - ALGORITMO DE BUSQUEDA:
    #    "Implementa un algoritmo de busqueda A* simplificado para encontrar el camino
    #     mas corto en una cuadricula. Usa bucles con break/continue, diccionarios para
    #     el grafo, y heapq para la cola de prioridad. Explica la complejidad."
    #
    # 4) PROMPT - PIPELINE DE DATOS:
    #    "Crea un pipeline de procesamiento de datos usando generadores encadenados.
    #     El pipeline debe: 1) Generar numeros, 2) Filtrar, 3) Transformar, 4) Agregar.
    #     Demuestra lazy evaluation y composicion de generadores."

    # * DEMO opcional
    if IA_DEMO:
        print("DEMO: Pipeline de procesamiento con generadores")

        # Generadores encadenados
        def generar_numeros(n):
            for i in range(n):
                yield i

        def filtrar_pares(gen):
            for num in gen:
                if num % 2 == 0:
                    yield num

        def multiplicar(gen, factor):
            for num in gen:
                yield num * factor

        def sumar_acumulado(gen):
            total = 0
            for num in gen:
                total += num
                yield total

        # Componer pipeline
        pipeline = sumar_acumulado(
            multiplicar(
                filtrar_pares(
                    generar_numeros(10)
                ), 3
            )
        )

        print(f"  Pipeline (pares * 3, acumulado): {list(pipeline)}")

    # TODO: (Tema: PROGRAMA IA)
    # 1) Usa uno de los prompts del PROMPT KIT con tu IA favorita.
    # 2) Pega el codigo generado aqui.
    # 3) Ejecutalo y modificalo para entender como funciona.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def mi_programa_ia():
    #     # Pega aqui el codigo generado por la IA
    #     pass
    # mi_programa_ia()

# =========================================================================================
#  AUTOEVALUACION FINAL (mezcla de todo)
# =========================================================================================
def autoevaluacion():
    encabezado("AUTOEVALUACION FINAL · Sistema de Gestion Avanzado")

    # TODO: (ENUNCIADO)
    # Crea un sistema de gestion de inventario avanzado que incluya:
    #
    # 1) ESTRUCTURA DE DATOS:
    #    - Diccionario de productos: {id: {nombre, precio, stock, categoria}}
    #    - Historial de transacciones como generador
    #
    # 2) FUNCIONALIDADES (usa los patrones aprendidos):
    #    a) Agregar/eliminar productos (validacion con excepciones)
    #    b) Buscar productos por categoria (filter + dict comprehension)
    #    c) Aplicar descuentos por categoria (map + itertools.groupby)
    #    d) Calcular valor total del inventario (reduce)
    #    e) Generar reporte de productos bajo stock (generador)
    #    f) Historial de precios con media movil (sliding window)
    #    g) Busqueda binaria de producto por ID (two pointers en lista ordenada)
    #
    # 3) MENU INTERACTIVO:
    #    - while True con break para salir
    #    - Manejo de excepciones para inputs invalidos
    #    - Walrus operator donde sea apropiado
    #
    # 4) RESUMEN FINAL:
    #    - Usar reduce para estadisticas
    #    - Comprension de diccionario para filtros
    #    - enumerate para listados numerados
    #
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # Tu codigo aqui...

    print("Completa el ejercicio de autoevaluacion en la ZONA DEL ALUMNO")
    print("Este ejercicio integra TODOS los conceptos de la clase.")

# =========================================================================================
#  MENU PRINCIPAL
# =========================================================================================
def menu():
    opciones = {
        1: ("zip() y zip_longest()", seccion_1),
        2: ("Iterando sobre diccionarios", seccion_2),
        3: ("Generadores y yield", seccion_3),
        4: ("itertools", seccion_4),
        5: ("map(), filter(), reduce()", seccion_5),
        6: ("Patron Sliding Window", seccion_6),
        7: ("Patron Two Pointers", seccion_7),
        8: ("Walrus Operator (:=)", seccion_8),
        9: ("Excepciones en bucles", seccion_9),
        10: ("Recursion vs Iteracion", seccion_10),
        11: ("Laboratorio IA", seccion_11_ia),
        12: ("Autoevaluacion final", autoevaluacion),
        13: ("Ejecutar TODO (1-12)", None),
    }

    while True:
        print_firma()
        print("MENU · BUCLES AVANZADOS")
        print("-" * 40)
        for num, (desc, _) in opciones.items():
            print(f"  {num:2}) {desc}")
        print("   0) Salir")
        print("-" * 40)

        try:
            op = int(input("Opcion: "))
        except ValueError:
            print("! Opcion no valida.")
            continue

        if op == 0:
            print("Hasta la proxima!")
            print_firma()
            break
        elif op == 13:
            for num in range(1, 13):
                opciones[num][1]()
                pause()
        elif op in opciones:
            opciones[op][1]()
            pause()
        else:
            print("! Elige una opcion del 0 al 13.")

# =========================================================================================
#  EJECUCION
# =========================================================================================
if __name__ == "__main__":
    menu()
