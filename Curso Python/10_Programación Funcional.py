# =========================================================================================
#  🐍 PYTHON CLASE 10 — PROGRAMACIÓN FUNCIONAL ESENCIAL
#  ────────────────────────────────────────────────────────────────────────────────────────
#  📘 En esta clase practicarás solo lo que más usarás en el día a día:
#    * lambda (funciones pequeñas y expresivas)
#    * map, filter, reduce (procesamiento de colecciones)
#    * any, all, zip, sorted(key=...) (utilidades clave)
#    * Laboratorio IA (colecciones) y Autoevaluación integradora
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica  ·  # NOTE: apunte útil   ·  # // deprecado
# =========================================================================================

from functools import reduce

# * Configuración general ---------------------------------------------------------------
RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True

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

def safe_input(prompt, caster, default):
    if not RUN_INTERACTIVE: return default
    try:
        raw = input(prompt)
        if raw.strip() == "": return default
        return caster(raw)
    except Exception:
        print("! Entrada no válida; usando valor por defecto.")
        return default

def encabezado(titulo: str):
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)

# =========================================================================================
#  SECCIÓN 1 · lambda (funciones pequeñas en una línea)
# =========================================================================================
def seccion_1():
    encabezado("SECCIÓN 1 · lambda")

    # * TEORÍA
    # lambda args: expresión  → devuelve el resultado de la expresión.
    # Úsala cuando la función sea corta y solo la necesites “aquí y ahora”.
    # Ejemplos típicos: key= en sorted, map/filter de una línea, transformaciones puntuales.

    # * DEMO
    cuadrado = lambda x: x * x
    iva      = lambda base, p=21: round(base * (1 + p/100), 2)
    nombre_completo = lambda n, a: f"{n.strip().title()} {a.strip().title()}"

    print("cuadrado(5) =", cuadrado(5))
    print("iva(100) =", iva(100), "| iva(100, 10) =", iva(100, 10))
    print("nombre_completo →", nombre_completo("  ana  ", "  gomez "))

    # Usos con sorted (muy habitual)
    personas = [
        {"nombre": "Ana",  "edad": 19},
        {"nombre": "Luis", "edad": 23},
        {"nombre": "Mara", "edad": 20},
    ]
    print("Orden por edad:", sorted(personas, key=lambda p: p["edad"]))
    print("Orden por nombre:", sorted(personas, key=lambda p: p["nombre"]))

    # TODO: (Tema: FORMATEO EXPRESS)
    # 1) Crea una lambda 'titulo' que reciba un texto y lo devuelva en Título (title()) sin espacios laterales.
    # 2) Crea una lista de nombres “sucios” y ordénalos por su versión “titulada” usando key=titulo.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # titulo = lambda s: ...
    # sucios = ["   peDro", "ana   ", "  ZAida "]
    # print(sorted(sucios, key=titulo))

# =========================================================================================
#  SECCIÓN 2 · map / filter / reduce (en profundidad)
# =========================================================================================
def seccion_2():
    encabezado("SECCIÓN 2 · map / filter / reduce")

    # * TEORÍA
    # map(func, iterable)       → aplica func a cada elemento (transforma)
    # filter(func, iterable)    → mantiene solo los que cumplan la condición (selecciona)
    # reduce(func, iterable, init) → acumula en un valor (suma, producto, concatenación…)

    # * DEMO 1 · Limpieza y totalización de precios
    crudos = ["10.5", "8", "", "x", "3.2", "  4  "]
    limpiar = lambda s: s.strip().replace(",", ".")
    es_num  = lambda s: s.replace(".", "", 1).isdigit()
    precios = list(map(float, filter(es_num, map(limpiar, crudos))))
    total   = reduce(lambda acc, x: acc + x, precios, 0.0)
    print("Precios válidos:", precios, "| Total:", round(total, 2))

    # * DEMO 2 · Pipeline: transformar -> filtrar -> resumir
    estudiantes = [
        {"nombre": "Ana",  "nota": 8.5},
        {"nombre": "Luis", "nota": 4.3},
        {"nombre": "Mara", "nota": 6.1},
        {"nombre": "Paco", "nota": 9.2},
    ]
    # subir 0.5 a todos, filtrar <5, sumar
    subir = lambda n: min(n + 0.5, 10)
    notas_subidas = list(map(lambda e: {**e, "nota": subir(e["nota"])}, estudiantes))
    aprobados = list(filter(lambda e: e["nota"] >= 5, notas_subidas))
    media_aprob = (reduce(lambda acc, e: acc + e["nota"], aprobados, 0.0) / len(aprobados)) if aprobados else 0
    print("Aprobados:", aprobados, "| Media aprobados:", round(media_aprob, 2))

    # * DEMO 3 · Reduce para construir cadenas o dicts
    palabras = ["hola", "mundo", "python"]
    frase = reduce(lambda acc, w: f"{acc} {w}".strip(), palabras, "")
    print("Frase:", frase)

    # TODO: (Tema: FACTURAS)
    # Dada una lista de líneas: {"desc":str,"precio":float,"uds":int},
    # 1) Obtén importes línea = precio*uds (map)
    # 2) Filtra solo las > 20€ (filter)
    # 3) Suma total con reduce (dos decimales)
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # lineas = [
    #   {"desc":"A", "precio": 3.5, "uds": 2},
    #   {"desc":"B", "precio": 10,  "uds": 3},
    #   {"desc":"C", "precio": 2,   "uds": 5},
    # ]
    # ...

# =========================================================================================
#  SECCIÓN 3 · any / all / zip / sorted(key=...) (utilidades clave)
# =========================================================================================
def seccion_3():
    encabezado("SECCIÓN 3 · any / all / zip / sorted(key=...)")

    # * TEORÍA
    # any(iterable) → True si ALGUNO es True        (detectar existencia)
    # all(iterable) → True si TODOS son True        (validar conjunto)
    # zip(a,b,...)  → itera pares/tuplas en paralelo
    # sorted(lista, key=func, reverse=False) → ordenación potente con key

    # * DEMO 1 · Validaciones rápidas
    notas = [6, 7.5, 4, 8]
    print("¿Hay algún 10?  →", any(n == 10 for n in notas))
    print("¿Todos >=5?     →", all(n >= 5 for n in notas))

    # * DEMO 2 · Juntar listas con zip
    cursos = ["Python", "Git", "SQL"]
    plazas = [15, 10, 20]
    for curso, p in zip(cursos, plazas):
        print(f"{curso:8} → {p:>3} plazas")

    # * DEMO 3 · Ordenación por claves múltiples (truco muy usado)
    # Primero por 'categoria', luego por 'precio' ascendente
    productos = [
        {"nombre": "cuaderno", "precio": 2.5, "categoria": "papelería"},
        {"nombre": "pendrive", "precio": 9.9, "categoria": "tech"},
        {"nombre": "marcador", "precio": 1.8, "categoria": "papelería"},
        {"nombre": "carpeta",  "precio": 3.6, "categoria": "papelería"},
    ]
    orden_multi = sorted(productos, key=lambda p: (p["categoria"], p["precio"]))
    print("Orden multi-clave:", orden_multi)

    # * DEMO 4 · Top-N con sorted y slicing
    top2 = sorted(productos, key=lambda p: p["precio"], reverse=True)[:2]
    print("Top 2 caros:", top2)

    # TODO: (Tema: VALIDACIÓN Y RANKING)
    # Dada la lista notas = [7, 5, 9, 6, 10]:
    # 1) Usa all() para comprobar si todas son >=5.
    # 2) Usa any() para comprobar si hay algún 10.
    # 3) Dada lista alumnos = ["Ana","Luis","Mara","Paco","Rita"], muestra pareadas con zip “Nombre: Nota”.
    # 4) Ordena (nombre, nota) por nota desc con sorted y muestra el top 3.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # ...

# =========================================================================================
#  SECCIÓN 4 · Laboratorio IA (procesamiento de colecciones)
# =========================================================================================
def seccion_4_ia():
    encabezado("SECCIÓN 4 · Laboratorio IA (colecciones)")

    # * PROMPT KIT (copia/pega en ChatGPT)
    # 1) PROMPT BREVE:
    #    "Eres profesor de Python. Genera un programa de 35–50 líneas que use:
    #     - map/filter/reduce para limpiar y resumir ventas (precio, uds)
    #     - sorted(key=...) para ranking de productos
    #     - any/all para validaciones
    #     Devuelve SOLO código Python, sin librerías."
    #
    # 2) PROMPT ALTERNATIVO:
    #    "Crea un analizador de notas con:
    #     - subida de 0.5 (map), filtro de aprobados (filter),
    #     - media con reduce, top-3 con sorted,
    #     - línea final tipo dashboard."
    #
    # 3) PROMPT DE MEJORA:
    #    "Refactoriza usando lambdas y funciones pequeñas. Manténlo <50 líneas."

    if IA_DEMO:
        precios = [10, 3.5, 6]
        total = reduce(lambda a, b: a + b, precios, 0)
        print("Demo IA → total:", total)

    # TODO: (Tema: PROGRAMA PROPUESTO POR IA)
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def mi_programa_ia():
    #     pass
    # mi_programa_ia()

# =========================================================================================
#  AUTOEVALUACIÓN FINAL (mezcla de todo)
# =========================================================================================
def autoevaluacion():
    encabezado("AUTOEVALUACIÓN FINAL · Informe de ventas funcional")

    # TODO: (ENUNCIADO)
    # Tienes una lista de dicts: {"producto":str,"precio":float,"uds":int}
    # 1) Normaliza nombres (lambda: title/strip) y calcula importes = precio*uds (map).
    # 2) Filtra importes < 20 (filter).
    # 3) Total con reduce (dos decimales).
    # 4) Ordena por importe desc (sorted key=lambda) y muestra el TOP-3 (zip si quieres parear).
    # 5) Usa any/all para:
    #    - ¿hay algún producto con importe 0?
    #    - ¿todos los precios > 0?
    # 6) Línea final tipo dashboard:
    #    "Líneas:<n> | Filtradas:<m> | Total:<€> | Top:<nombre-importe>"
    #
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------

# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu():
    while True:
        print_firma()
        print("MENÚ · Elige una opción")
        print("  1) lambda")
        print("  2) map / filter / reduce")
        print("  3) any / all / zip / sorted")
        print("  4) Laboratorio IA (colecciones)")
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
        elif op == 1: seccion_1(); pause()
        elif op == 2: seccion_2(); pause()
        elif op == 3: seccion_3(); pause()
        elif op == 4: seccion_4_ia(); pause()
        elif op == 5: autoevaluacion(); pause()
        elif op == 6:
            seccion_1(); seccion_2(); seccion_3(); seccion_4_ia(); autoevaluacion(); pause()
        else:
            print("! Elige una opción del 0 al 6.")

# =========================================================================================
#  EJECUCIÓN
# =========================================================================================
if __name__ == "__main__":
    menu()
