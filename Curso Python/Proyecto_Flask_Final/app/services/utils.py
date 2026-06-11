"""Utilidades de ejemplo (programación funcional y helpers).
Incluye map/filter y manejo de excepciones simples.

# * Estas funciones son puras (no tienen efectos secundarios significativos),
#   ideales para testear y para entender programación funcional en Python.
"""
from functools import reduce
from typing import Iterable, List, Dict, Any, Optional

# * Funciones puras de utilidad

def mayusculas(lista_strings: Iterable[str]) -> List[str]:
    """Convierte todos los elementos en mayúsculas usando map.

    Ejemplo:
        mayusculas(["a","b"]) -> ["A","B"]
    """
    return list(map(lambda s: s.upper(), lista_strings))


def filtra_publicados(cursos: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filtra cursos publicados (bool).

    Espera diccionarios con clave 'publicado'. Si no está, asume True.
    """
    return list(filter(lambda c: c.get("publicado", True), cursos))


def total_palabras(cursos: Iterable[Dict[str, Any]]) -> int:
    """Cuenta palabras totales en descripciones usando reduce."""
    return reduce(lambda acc, c: acc + len(c.get("descripcion", "").split()), cursos, 0)


# * Manejo básico de excepciones

def seguro_dividir(a: float, b: float) -> Optional[float]:
    """Divide controlando división por cero.

    Retorna None si b==0 para evitar un error no manejado.
    """
    try:
        return a / b
    except ZeroDivisionError:
        # ! Evitar explotar la app: devolvemos None o un mensaje controlado
        return None
