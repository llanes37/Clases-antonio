# =========================================================================================
#  CLASE 13 - TESTING Y CALIDAD (ALUMNO)
#  -----------------------------------------------------------------------------------------
#  Esta version esta pensada para practicar:
#    * reglas de validacion sencillas
#    * funciones faciles de probar
#    * asserts manuales
#    * primeros tests con pytest
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica  ·  # NOTE: apunte util  ·  # // deprecado
# =========================================================================================

from __future__ import annotations


def es_email_valido(email: str) -> bool:
    # * Sugerencia:
    #   trabaja paso a paso y prueba cada regla por separado.
    # ? No busques el validador perfecto; busca uno coherente con las reglas del ejercicio.
    # TODO:
    # 1. limpiar espacios extremos
    # 2. comprobar que hay una arroba
    # 3. comprobar que la parte final contiene un punto
    # 4. evitar espacios internos
    pass


def aplicar_descuento(precio: float, descuento_pct: float) -> float:
    # * Esta funcion es ideal para testing porque:
    #   - tiene una regla clara,
    #   - devuelve un valor,
    #   - y tiene errores esperados.
    # TODO:
    # - si precio < 0 -> ValueError
    # - si descuento fuera de 0..100 -> ValueError
    # - devolver precio final redondeado a 2 decimales
    pass


def media_segura(numeros: list[float]) -> float | None:
    # * Aqui hay un caso borde importante: lista vacia.
    # ! No ignores ese caso; es justo lo que queremos entrenar en esta unidad.
    # TODO:
    # - si la lista esta vacia devuelve None
    # - si no, devuelve la media redondeada a 2 decimales
    pass


class Pedido:
    # * Mini clase para practicar testing de cambio de estado.
    def __init__(self, cliente: str, total: float) -> None:
        self.cliente = cliente
        self.total = total
        self.pagado = False

    def marcar_pagado(self) -> None:
        # ? Si este metodo funciona, el atributo pagado debe pasar de False a True.
        # TODO: cambiar el estado a pagado
        pass


# =========================================================================================
#  ASSERTS RAPIDOS
# =========================================================================================

# * Antes de pytest, usa asserts pequeños para comprobar si tu lógica básica ya funciona.
# TODO:
# Escribe 4 asserts manuales utiles sobre las funciones anteriores.


# =========================================================================================
#  PYTEST - COPIA ESTAS IDEAS EN UN ARCHIVO test_*.py
# =========================================================================================

# * Haz los tests en un archivo separado.
# ? Así practicas la estructura real que luego usarás en proyectos más grandes.
# TODO:
# Crea un archivo aparte con nombre parecido a:
#   test_13_testing_y_calidad.py
#
# y escribe pruebas como estas:
#
# def test_email_valido():
#     assert es_email_valido("ana@example.com") is True
#
# def test_media_vacia():
#     assert media_segura([]) is None
#
# def test_pedido_pagado():
#     pedido = Pedido("Ana", 20)
#     pedido.marcar_pagado()
#     assert pedido.pagado is True
#
# def test_descuento_invalido():
#     import pytest
#     with pytest.raises(ValueError):
#         aplicar_descuento(100, 200)


# =========================================================================================
#  AUTOEVALUACION
# =========================================================================================

# * Objetivo final:
#   no solo programar algo que "parece funcionar",
#   sino demostrarlo con pruebas pequeñas y claras.
# TODO FINAL:
# 1. Crea una funcion precio_con_iva(base, iva).
# 2. Escribe al menos 3 pruebas para ella.
# 3. Piensa un caso borde y un caso de error.
