# =========================================================================================
#  PYTHON CLASE 10 · PROGRAMACION FUNCIONAL (ALUMNO)
#  ---------------------------------------------------------------------------------------
#  En esta plantilla trabajaras:
#    * funciones puras
#    * funciones lambda
#    * funciones de orden superior
#    * map, filter y reduce
#    * inmutabilidad
#    * composicion de funciones
#    * recursion
#
#  Objetivo:
#    * practicar el enfoque funcional paso a paso
#    * aprender a transformar datos sin depender de variables globales
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica ·  # NOTE: apunte util   ·  # // evitar
# =========================================================================================

from __future__ import annotations

from functools import reduce


# =========================================================================================
#  SECCION 1 · FUNCIONES PURAS
# =========================================================================================
# * Una funcion pura, para los mismos argumentos, devuelve siempre lo mismo.
# * Ademas, no modifica estado externo.
def suma_pura(a: int, b: int) -> int:
    # TODO:
    # - devolver la suma de `a` y `b`
    # ! No uses prints aqui como resultado principal.
    pass


# =========================================================================================
#  SECCION 2 · FUNCIONES LAMBDA
# =========================================================================================
# * Las lambda sirven para operaciones pequenas y expresivas.
# ? No son mejores "porque si"; se usan cuando la funcion es muy corta.
multiplicar = None
# TODO:
# - convierte `multiplicar` en una lambda que reciba dos numeros
# - debe devolver su producto


# =========================================================================================
#  SECCION 3 · FUNCIONES DE ORDEN SUPERIOR
# =========================================================================================
# * Una funcion de orden superior recibe otra funcion como argumento
#   o devuelve una funcion nueva.
def aplicar_operacion(valor: int, funcion):
    # TODO:
    # - recibir un numero y una funcion
    # - aplicar la funcion al valor recibido
    pass


# =========================================================================================
#  SECCION 4 · MAP, FILTER Y REDUCE
# =========================================================================================
numeros = [1, 2, 3, 4, 5, 6]

# TODO MAP:
# - crear una nueva lista con los numeros al cuadrado
# ? Pista: list(map(...))


# TODO FILTER:
# - crear una nueva lista solo con los numeros pares
# ? Pista: list(filter(...))


# TODO REDUCE:
# - calcular la suma total de `numeros`
# ? Pista: reduce(lambda acumulado, actual: ..., numeros, 0)


# =========================================================================================
#  SECCION 5 · INMUTABILIDAD
# =========================================================================================
# * En enfoque funcional se evita modificar la estructura original.
# * Lo normal es construir una nueva a partir de la anterior.
lista_original = [10, 20, 30]

# TODO:
# - crear `lista_incrementada` sin modificar `lista_original`
# - sumar 1 a cada elemento


# =========================================================================================
#  SECCION 6 · COMPOSICION DE FUNCIONES
# =========================================================================================
def duplicar(n: int) -> int:
    # TODO: devolver el doble
    pass


def sumar_tres(n: int) -> int:
    # TODO: devolver `n + 3`
    pass


def componer_demo(valor: int) -> int:
    # TODO:
    # - combinar `duplicar` y `sumar_tres`
    # - por ejemplo: primero duplicar y luego sumar tres
    pass


# =========================================================================================
#  SECCION 7 · RECURSION
# =========================================================================================
def factorial(n: int) -> int:
    # TODO:
    # - definir caso base
    # - definir caso recursivo
    # ! Si olvidas el caso base, la funcion no termina bien.
    pass


# =========================================================================================
#  AUTOEVALUACION FINAL
# =========================================================================================
# TODO FINAL:
# 1. probar `suma_pura(2, 3)`
# 2. probar la lambda `multiplicar`
# 3. usar `aplicar_operacion` con una funcion sencilla
# 4. mostrar los resultados de map, filter y reduce
# 5. comprobar que `lista_original` no ha cambiado
# 6. probar `componer_demo(5)`
# 7. probar `factorial(5)`
#
# NOTE:
# Una buena resolucion aqui no mezcla todo sin orden. Lo ideal es que cada idea
# quede en su bloque y luego la autoevaluacion las conecte.
