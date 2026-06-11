# =========================================================================================
#  PYTHON CLASE 13 - TESTING Y CALIDAD
#  -----------------------------------------------------------------------------------------
#  En esta clase practicaras:
#    * Pensar casos de prueba antes de programar
#    * assert como comprobacion rapida
#    * pytest como herramienta principal del curso
#    * Casos borde y errores esperados
#    * Funciones faciles de probar (sin efectos colaterales innecesarios)
#    * Debugging con prints utiles, breakpoints y trazas sencillas
#    * Laboratorio IA y autoevaluacion final
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica  ·  # NOTE: apunte util  ·  # // deprecado
# =========================================================================================

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

# * Configuracion general ---------------------------------------------------------------
# ? Mismo patron del resto del curso: permite clase en vivo, demo grabada y laboratorio IA.
RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True


def print_firma() -> None:
    # * Firma visual para mantener coherencia con las otras unidades del curso.
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Pagina web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")


def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    # ? En clase puede venir bien pausar entre bloques; en ejecución rápida se desactiva.
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass


def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
    # * Entrada segura: si no hay input o falla el cast, usamos un valor por defecto.
    # ! Esto evita romper la demo en entornos sin stdin o cuando el alumno se equivoca.
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


def encabezado(titulo: str) -> None:
    # * Cabecera homogénea para separar secciones del menú.
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


def es_email_valido(email: str) -> bool:
    # * Ejemplo deliberadamente simple para poder hablar de testing sin distraernos con regex.
    # ? La idea docente aquí no es construir el "validador perfecto", sino probar reglas claras.
    email = email.strip()
    return "@" in email and "." in email.split("@")[-1] and " " not in email


def aplicar_descuento(precio: float, descuento_pct: float) -> float:
    # * Función pura: misma entrada => misma salida, sin prints ni input ni ficheros.
    # ? Este tipo de función es la más cómoda para testear con assert o pytest.
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not 0 <= descuento_pct <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    return round(precio * (1 - descuento_pct / 100), 2)


def media_segura(numeros: list[float]) -> float | None:
    # * Caso borde clásico: lista vacía.
    # ! Precisamente por eso esta función es buena para enseñar diseño de pruebas.
    if not numeros:
        return None
    return round(sum(numeros) / len(numeros), 2)


@dataclass
class Pedido:
    # * Mini objeto de dominio para no quedarnos solo en funciones sueltas.
    # ? Así el alumno también ve cómo testear cambios de estado en objetos.
    cliente: str
    total: float
    pagado: bool = False

    def marcar_pagado(self) -> None:
        # * Método simple y fácilmente verificable.
        self.pagado = True


# =========================================================================================
#  SECCION 1 · Pensar casos de prueba
# =========================================================================================
def seccion_1() -> None:
    encabezado("SECCION 1 · Pensar casos de prueba")

    # * IDEA CLAVE:
    #   Un alumno suele ejecutar una vez y pensar "funciona".
    #   Un test obliga a concretar:
    #   - qué entrada uso,
    #   - qué salida espero,
    #   - y qué pasa en casos incómodos.
    print("Una prueba buena comprueba comportamiento, no solo ejecucion.")
    print("Pregunta base: que deberia pasar con datos validos, invalidos y borde?")

    casos = [
        ("email valido", es_email_valido("ana@example.com"), True),
        ("email sin arroba", es_email_valido("anaexample.com"), False),
        ("email con espacios", es_email_valido("ana @example.com"), False),
    ]
    for nombre, obtenido, esperado in casos:
        print(f"{nombre:20} -> obtenido={obtenido} esperado={esperado}")

    # TODO: (Tema: CASOS BORDE)
    # Anade 3 casos mas para la funcion es_email_valido():
    #   - email vacio
    #   - email con subdominio
    #   - email sin punto tras la arroba


# =========================================================================================
#  SECCION 2 · assert rapido y funciones faciles de probar
# =========================================================================================
def seccion_2() -> None:
    encabezado("SECCION 2 · assert rapido y funciones faciles de probar")

    # * assert es perfecto para enseñanza rápida:
    #   - resultado esperado claro,
    #   - feedback inmediato,
    #   - cero ceremonia.
    # ! No sustituye una batería seria de tests, pero sí entrena la mentalidad correcta.
    assert aplicar_descuento(100, 20) == 80.0
    assert media_segura([10, 20, 30]) == 20.0
    assert media_segura([]) is None

    print("assert ejecutados correctamente.")
    print("Idea clave: cuanto menos dependa la funcion de input(), print() o ficheros,")
    print("mas facil sera probarla con seguridad.")

    # TODO: (Tema: IVA)
    # Crea precio_con_iva(base, iva) y escribe al menos 3 asserts manuales.


# =========================================================================================
#  SECCION 3 · pytest como herramienta principal
# =========================================================================================
def seccion_3() -> None:
    encabezado("SECCION 3 · pytest como herramienta principal")

    # * Este bloque sustituye la antigua orientación excesivamente básica de la unidad vieja.
    # ? Aquí fijamos la herramienta principal del curso cuando ya hablamos de pruebas reales.
    ejemplo = r'''
def test_aplicar_descuento_basico():
    assert aplicar_descuento(200, 25) == 150.0

def test_media_vacia_devuelve_none():
    assert media_segura([]) is None

def test_descuento_fuera_de_rango():
    import pytest
    with pytest.raises(ValueError):
        aplicar_descuento(50, 200)
'''
    print("EJEMPLO DE TEST CON PYTEST:\n")
    print(ejemplo.strip())
    print("\nComando habitual:")
    print("  pytest -q")
    print("\nConsejo didactico:")
    print("  empieza por tests cortos, con nombres muy literales y un solo objetivo.")

    # TODO: (Tema: PYTEST)
    # Escribe una prueba para es_email_valido() y otra para Pedido.marcar_pagado().


# =========================================================================================
#  SECCION 4 · Errores esperados y casos borde
# =========================================================================================
def seccion_4() -> None:
    encabezado("SECCION 4 · Errores esperados y casos borde")

    # * Importante: un buen test no solo verifica éxitos.
    # ! También confirma que el código falla cuando debe fallar.
    try:
        aplicar_descuento(-5, 10)
    except ValueError as exc:
        print("Error esperado detectado:", exc)

    ejemplos = [
        ("precio cero", aplicar_descuento(0, 10)),
        ("descuento cero", aplicar_descuento(100, 0)),
        ("descuento cien", aplicar_descuento(100, 100)),
    ]
    for nombre, resultado in ejemplos:
        print(f"{nombre:18} -> {resultado}")

    # TODO: (Tema: RAISES)
    # Comprueba con pytest.raises que aplicar_descuento falla si el descuento es -1.


# =========================================================================================
#  SECCION 5 · Debugging util
# =========================================================================================
def seccion_5() -> None:
    encabezado("SECCION 5 · Debugging util")

    # ? Este ejemplo es intencionadamente simple:
    #   queremos enseñar cuándo un print temporal ayuda y cuándo estorba.
    numeros = [5, 15, 25]
    objetivo = safe_input("Numero a buscar: ", int, 15)

    print("[DEBUG] lista actual:", numeros)
    print("[DEBUG] objetivo:", objetivo)

    if objetivo in numeros:
        print("Encontrado.")
    else:
        print("No encontrado.")

    print("\nConsejo:")
    print("- Usa prints cortos y temporales.")
    print("- Si el bug es dificil, usa breakpoint() en el punto exacto.")
    print("- No dejes debugging ruidoso en la version final.")


# =========================================================================================
#  SECCION 6 · Laboratorio IA
# =========================================================================================
def seccion_6() -> None:
    encabezado("SECCION 6 · Laboratorio IA")

    if not IA_DEMO:
        print("Laboratorio IA desactivado.")
        return

    # * El laboratorio IA aquí tiene un uso concreto:
    #   generar mejores casos de prueba, no "resolver el tema".
    # ! Si la IA propone casos absurdos o no ejecutables, se descartan.
    prompt = """
Actua como revisor de tests en Python.
Te doy una funcion y quiero:
1. 5 casos de prueba utiles
2. 2 casos borde
3. 1 ejemplo con pytest.raises si aplica
4. una breve explicacion de por que esos tests importan
No cambies la firma de la funcion.
    """.strip()
    print(prompt)


# =========================================================================================
#  SECCION 7 · Autoevaluacion final
# =========================================================================================
def seccion_7() -> None:
    encabezado("SECCION 7 · Autoevaluacion final")

    # * El cierre de la unidad obliga a unir:
    #   - reglas de negocio,
    #   - validacion,
    #   - y pruebas.
    print("Mini proyecto sugerido:")
    print("- Funcion: normalizar_usuario(nombre, email)")
    print("- Reglas: limpiar espacios, nombre en title case, email en minusculas")
    print("- Escribe tests para casos validos, vacios e invalidos")
    print("- Extra: crea una clase Ticket con estado abierto/cerrado y prueba su flujo")


# =========================================================================================
#  MENU PRINCIPAL
# =========================================================================================
def menu() -> None:
    # * Mantenemos el patrón de menú porque forma parte de la identidad didáctica del curso.
    opciones = {
        "1": ("Pensar casos de prueba", seccion_1),
        "2": ("assert y funciones puras", seccion_2),
        "3": ("pytest", seccion_3),
        "4": ("Casos borde y errores", seccion_4),
        "5": ("Debugging", seccion_5),
        "6": ("Laboratorio IA", seccion_6),
        "7": ("Autoevaluacion final", seccion_7),
        "0": ("Salir", None),
    }

    while True:
        print_firma()
        print("CLASE 13 · TESTING Y CALIDAD\n")
        for clave, (texto, _) in opciones.items():
            print(f"[{clave}] {texto}")

        eleccion = safe_input("\nElige una opcion: ", str, "1")
        accion = opciones.get(eleccion, (None, None))[1]
        if eleccion == "0":
            print("Cerrando unidad 13.")
            break
        if accion is None:
            print("! Opcion no valida.")
            pause()
            continue
        accion()
        pause()


if __name__ == "__main__":
    # * Punto de entrada principal para la clase en vivo.
    menu()
