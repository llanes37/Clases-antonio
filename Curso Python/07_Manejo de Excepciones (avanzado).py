# =========================================================================================
#  "YO! PYTHON CLASE 7 (AVANZADO) - MANEJO DE EXCEPCIONES PLUS"
#  -----------------------------------------------------------------------------
#  Practicaras:
#    * Jerarquia de excepciones personalizadas y buenas practicas de mensajes
#    * Manejo avanzado: raise from, captura selectiva, reintentos con decorador
#    * Context managers (with) seguros y manejo de recursos
#    * Logging basico para registrar errores
#    * Validaciones reutilizables y helpers didacticos
#    * Laboratorio: mini pipelines robustos y JSON seguro
#    * Autoevaluacion con tablero final de resultados
#
#  Better Comments:
#    # ! importante   |  # * definicion/foco   |  # ? idea/nota
#    # TODO: practica |  # NOTE: apunte util   |  # // deprecado
# =========================================================================================

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Optional, Type, TypeVar

# =========================================================================================
#  CONFIGURACION / LOGGING
# =========================================================================================
# * RUN_INTERACTIVE controla si pedimos datos al usuario o usamos defaults
RUN_INTERACTIVE = True  # * Al activar se piden datos reales en consola
# ? PAUSE habilita pausas entre secciones para clases guiadas
PAUSE = False           # ? Cambia a True si quieres pausar tras cada seccion

# * Logger sencillo a consola para seguir advertencias y errores sin breakpoints
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("excepciones_avanzado")


def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass


# =========================================================================================
#  EXCEPCIONES PERSONALIZADAS (jerarquia)
# =========================================================================================
class AppError(Exception):
    """Base de errores de negocio en este modulo."""


class EntradaVacia(AppError):
    """Entrada faltante o vacia."""


class ValorFueraDeRango(AppError):
    """Valor numerico fuera de rango permitido."""


class ArchivoInvalido(AppError):
    """Errores relacionados con archivos/JSON."""


# =========================================================================================
#  HELPERS: safe_input, validate, retry
# =========================================================================================
T = TypeVar("T")


def safe_input(prompt: str, caster: Callable[[str], T], default: T) -> T:
    """Convierte input a tipo; devuelve default si hay error."""
    # ! Siempre atrapa excepciones comunes y deja un fallback limpio para la app
    if not RUN_INTERACTIVE:
        return default
    try:
        raw = input(prompt)
        if raw.strip() == "":
            raise EntradaVacia("Entrada vacia")
        return caster(raw)
    except AppError as e:
        logger.warning("Entrada vacia: %s", e)
    except Exception as e:
        logger.warning("Fallo de conversion: %s", e)
    return default


def validate_positive(value: float, field: str) -> float:
    """Valida que value sea positivo."""
    # * Reutiliza esta validacion para mantener mensajes business-friendly
    if value <= 0:
        raise ValorFueraDeRango(f"{field} debe ser positivo, recibido {value}")
    return value


def retry(attempts: int = 3, exceptions: tuple[Type[BaseException], ...] = (Exception,)):
    """Decorador de reintento simple (sin multiplicador de tiempo)."""
    # ! Solo reintenta los errores listados para no esconder bugs distintos

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_err: Optional[BaseException] = None
            for intento in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    last_err = err
                    logger.warning("Intento %s/%s fallo: %s", intento, attempts, err)
            assert last_err is not None
            raise last_err

        return wrapper

    return decorator


# =========================================================================================
#  CONTEXT MANAGER SEGURO (lectura de JSON)
# =========================================================================================
def cargar_json_seguro(path: Path) -> Dict[str, Any]:
    """Lee JSON de forma segura con context manager y errores encadenados."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise ArchivoInvalido(f"No existe el archivo {path}") from e
    except json.JSONDecodeError as e:
        raise ArchivoInvalido(f"JSON invalido en {path}: {e}") from e


# =========================================================================================
#  DATACLASS PARA RESULTADOS
# =========================================================================================
@dataclass
class Resultado:
    ok: bool
    valor: Any = None
    error: Optional[str] = None


# =========================================================================================
#  SECCION 1: raise from y jerarquia
# =========================================================================================
def seccion_1():
    # ? TEORIA (raise from + jerarquia):
    # ? - raise from encadena excepciones manteniendo el traceback original.
    # ? - Define una jerarquia (AppError -> hijos) para capturar reglas de negocio
    # ?   sin atrapar errores del sistema.
    print("\nSECCION 1 >> raise from y jerarquia")

    def leer_entero(texto: str) -> int:
        if texto.strip() == "":
            raise EntradaVacia("Se esperaba un numero, recibimos vacio")
        try:
            return int(texto)
        except ValueError as e:
            # ! Encadenamos para conservar traceback original
            raise ValorFueraDeRango(f"No es entero valido: {texto}") from e

    try:
        valor = leer_entero("abc")
        print("Entero:", valor)
    except AppError as e:
        print("Error de App:", e)
        # ? raise from mantiene el traceback original

    pause()


# =========================================================================================
#  SECCION 2: reintento con decorador
# =========================================================================================
@retry(attempts=3, exceptions=(ValueError,))
def _leer_precio_interactivo() -> float:
    precio = safe_input("Precio (float): ", float, default=-1.0)
    validate_positive(precio, "precio")
    return precio


def seccion_2():
    # ? TEORIA (decorador retry):
    # ? - Envuelve funciones que pueden fallar temporalmente (validaciones, IO).
    # ? - Controla cuantas veces reintenta y que excepciones gatillan el reintento.
    # ? - Evita duplicar bucles de intentos en cada funcion.
    print("\nSECCION 2 >> Reintento con decorador")
    try:
        p = _leer_precio_interactivo()
        print("Precio OK:", p)
    except Exception as e:
        print("Se agoto el reintento:", e)
        # ! Observa como el decorador reintenta y solo falla al agotar intentos
    pause()


# =========================================================================================
#  SECCION 3: context manager y with seguro
# =========================================================================================
def seccion_3():
    # ? TEORIA (context manager):
    # ? - with garantiza liberar recursos aun si hay excepciones.
    # ? - Manejar FileNotFoundError o JSONDecodeError con raise from deja claro el origen.
    # ? - Ideal para archivos, conexiones o locks.
    print("\nSECCION 3 >> Context manager y JSON seguro")
    ruta = Path("datos_demo.json")
    ruta.write_text('{"nombre": "Ada", "edad": 34}', encoding="utf-8")
    try:
        datos = cargar_json_seguro(ruta)
        print("JSON cargado:", datos)
    except ArchivoInvalido as e:
        print("Archivo invalido:", e)
        # * Observa como `raise from` deja claro que el origen fue JSONDecodeError o FileNotFoundError
    finally:
        try:
            ruta.unlink()
        except Exception:
            pass
    pause()


# =========================================================================================
#  SECCION 4: iterables y acumuladores seguros
# =========================================================================================
def media_segura(numeros: Iterable[float]) -> Resultado:
    lista = list(numeros)
    if not lista:
        return Resultado(ok=False, error="Lista vacia")
    try:
        validate_positive(len(lista), "len")
        return Resultado(ok=True, valor=sum(lista) / len(lista))
    except Exception as e:
        return Resultado(ok=False, error=str(e))


def seccion_4():
    # ? TEORIA (dataclass Resultado):
    # ? - Encapsula exito/error sin lanzar excepcion en cada paso.
    # ? - Evita que el flujo didactico se rompa cuando el alumno prueba listas vacias.
    # ? - Permite imprimir dashboards claros con estado.
    print("\nSECCION 4 >> Media segura con Resultado dataclass")
    casos = [[], [1, 2, 3]]
    for caso in casos:
        res = media_segura(caso)
        # ? Resultado contiene ok/error para evitar excepciones sin catch
        if res.ok:
            print("Media:", res.valor)
        else:
            print("Fallo:", res.error)
    pause()


# =========================================================================================
#  SECCION 5: pipeline mini (parse + validar + calcular)
# =========================================================================================
def calcular_total(linea: str) -> float:
    """Linea CSV: nombre, unidades, precio."""
    try:
        nombre, unidades, precio = linea.split(",")
        unidades_i = int(unidades)
        precio_f = float(precio)
        validate_positive(unidades_i, "unidades")
        validate_positive(precio_f, "precio")
        return unidades_i * precio_f
    except ValueError as e:
        raise ValorFueraDeRango(f"Formato invalido o numero no valido: {linea}") from e


def seccion_5():
    # ? TEORIA (pipeline robusto):
    # ? - Divide parseo, validacion y calculo para detectar en que etapa falla.
    # ? - raise from indica si el error viene de conversion o de negocio.
    # ? - Se usa mucho en ETL / parsing de archivos.
    print("\nSECCION 5 >> Pipeline de calculo con raise from")
    lineas = ["Mouse,2,15.5", "Teclado,x,50"]
    for linea in lineas:
        try:
            total = calcular_total(linea)
            print(f"{linea} -> total {total}")
        except AppError as e:
            print("Error de negocio:", e)
            # ! Captura la excepcion personalizada para poder seguir con el siguiente item
    pause()


# =========================================================================================
#  SECCION 6: laboratorio mini JSON seguro
# =========================================================================================
def seccion_6():
    # ? TEORIA (laboratorio JSON):
    # ? - Practica detectar errores comunes en archivos de terceros.
    # ? - Muestra como capturar y reportar sin detener toda la app.
    # ? - Repite el patron try/except/finally de limpieza.
    print("\nSECCION 6 >> Laboratorio JSON seguro con try/except")
    sample = Path("sample_bad.json")
    sample.write_text('{"nombre": "Ada", "edad":}', encoding="utf-8")
    try:
        cargar_json_seguro(sample)
    except ArchivoInvalido as e:
        print("Detectamos JSON roto:", e)
        # * Esta seccion es ideal para que los alumnos prueben distintos JSON invalidos
    finally:
        try:
            sample.unlink()
        except Exception:
            pass
    pause()


# =========================================================================================
#  AUTOEVALUACION
# =========================================================================================
def autoevaluacion():
    print("\nAUTOEVALUACION >> Tablero de flujo robusto")
    # TODO: (Enunciado)
    # 1) Implementa leer_float_reintento(msg, intentos=3) usando retry o un bucle manual.
    # 2) Crea CupnInvalido(AppError) y total_con_cupon(base, unidades, cupon):
    #    - cupon entre 0 y 100, base >0, unidades >0.
    # 3) Disea un contexto abrir_producto(path) que valide JSON con claves requeridas.
    # 4) Imprime un dashboard final: "base=.. | unidades=.. | cupon=.. | total=.. | estado=OK/ERROR".
    # ? Puedes combinar raise/else/finally y asegurar que siempre se muestra el cierre


# =========================================================================================
#  MENU
# =========================================================================================
def menu():
    opciones = {
        "1": seccion_1,
        "2": seccion_2,
        "3": seccion_3,
        "4": seccion_4,
        "5": seccion_5,
        "6": seccion_6,
        "9": autoevaluacion,
    }
    while True:
        print("\n=== MENU AVANZADO EXCEPCIONES ===")
        for k, v in opciones.items():
            print(f" {k}) {v.__name__}")
        print(" 9) autoevaluacion (todo junto)")
        print(" 0) Salir")
        op = input("Opcion: ").strip()
        if op == "0":
            print("Hasta pronto!")
            break
        funcion = opciones.get(op)
        if funcion:
            funcion()
        else:
            print("Elige una opcion valida.")


# =========================================================================================
#  EJECUCION
# =========================================================================================
if __name__ == "__main__":
    menu()

