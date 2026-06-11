# =========================================================================================
#  🐍 PYTHON CLASE 6 (AVANZADO) — PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
#  ──────────────────────────────────────────────────────────────────────────────────────
#  🎯 En esta clase practicarás (nivel avanzado):
#    * Dunder avanzados: __repr__/__str__/__eq__/__hash__/orden total y __slots__
#    * Ciclo de vida del objeto: __new__/__init__/__del__ (cuándo usarlos)
#    * Dataclasses avanzadas: frozen, order, slots, default_factory, post_init
#    * Herencia múltiple, MRO y mixins con super() cooperativo
#    * ABC (clases abstractas) y Protocols (duck typing con tipos)
#    * Properties avanzadas y Descriptores (validación reutilizable) y cached_property
#    * Iterables/Iteradores y Context Managers (__enter__/__exit__/contextlib)
#    * Sobrecarga de operadores y protocolo de contenedores (__len__/__contains__/__getitem__)
#    * Genéricos con TypeVar/Generic y factorías/classmethod
#    * Enums y patrones de diseño (Strategy) vía composición e inyección de dependencias
#    * Copias (shallow/deep), inmutabilidad y dataclasses.replace
#    * Laboratorio IA (POO avanzado) y Autoevaluación final
#
#  ✅ Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica  ·  # NOTE: apunte útil   ·  # // deprecado
# =========================================================================================

from __future__ import annotations

from dataclasses import dataclass, field, asdict, replace
from enum import Enum, auto
from functools import total_ordering, cached_property
from typing import Any, List, Dict, Optional, Iterable, Iterator, TypeVar, Generic, Protocol, runtime_checkable, Callable
import copy

# * Configuración general ---------------------------------------------------------------
RUN_INTERACTIVE = True   # True: pedir datos al usuario; False: usar valores por defecto
PAUSE = False            # Pausa tras cada opción del menú
IA_DEMO = True           # Demo corta en Laboratorio IA

# * Firma del curso ----------------------------------------------------------------------
def print_firma():
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Página web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")

# * Utilidades comunes -------------------------------------------------------------------
def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass

def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
    """# * Convierte la entrada; si falla o no hay input, devuelve 'default'."""
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

def encabezado(titulo: str) -> None:
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


# =========================================================================================
#  SECCIÓN 1 — Dunder avanzados y ciclo de vida (__repr__/__eq__/__hash__/__slots__/__new__)
# =========================================================================================
def seccion_1():
    encabezado("SECCIÓN 1 — Dunder avanzados y ciclo de vida")

    # * TEORÍA
    # __repr__: representación inequívoca (debug). __str__: legible para humanos.
    # __eq__/__hash__: igualdad y hash deben ser coherentes; si hay __eq__ define también __hash__ o usa dataclass.
    # Orden: usar @total_ordering implementando al menos __eq__ y un comparador (<, <=, >, >=).
    # __slots__: optimiza memoria y evita atributos dinámicos.
    # __new__: creación (antes de __init__). Útil para singletons/inmutables (p.ej. tuplas/str).

    @total_ordering
    class Punto:
        __slots__ = ("x", "y")  # ! restringe atributos y reduce memoria

        def __new__(cls, x: float, y: float):
            obj = super().__new__(cls)
            return obj

        def __init__(self, x: float, y: float):
            self.x = float(x)
            self.y = float(y)

        def __repr__(self) -> str:
            return f"Punto(x={self.x}, y={self.y})"

        def __str__(self) -> str:
            return f"({self.x:.2f}, {self.y:.2f})"

        def __eq__(self, other: Any) -> bool:
            if not isinstance(other, Punto):
                return NotImplemented
            return (self.x, self.y) == (other.x, other.y)

        def __lt__(self, other: Any) -> bool:
            if not isinstance(other, Punto):
                return NotImplemented
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

        def __hash__(self) -> int:  # coherente con __eq__
            return hash((self.x, self.y))

    a, b, c = Punto(1, 2), Punto(1, 2), Punto(0, 3)
    print("repr:", repr(a), "| str:", str(a))
    print("eq/hash:", a == b, hash(a) == hash(b))
    print("orden:", sorted([a, c, b]))

    # TODO: (Tema: VECTOR)
    # Implementa un Vector2D con __add__, __sub__, __mul__(por escalar) y __abs__(módulo).
    # Asegura __repr__/__str__ claros y __eq__/__hash__ coherentes.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 2 — Dataclasses avanzadas (frozen/order/slots/default_factory/post_init)
# =========================================================================================
def seccion_2():
    encabezado("SECCIÓN 2 — Dataclasses avanzado")

    # * TEORÍA
    # @dataclass genera __init__/__repr__/__eq__/__hash__ (opcional) y orden (order=True).
    # frozen=True => inmutable; slots=True => ahorra memoria; default_factory => listas/dicts por defecto.
    # __post_init__ para validaciones.

    @dataclass(frozen=True, order=True, slots=True)
    class Producto:
        precio: float
        nombre: str = field(compare=False)
        etiquetas: List[str] = field(default_factory=list, compare=False)

        def __post_init__(self):
            if self.precio < 0:
                raise ValueError("El precio no puede ser negativo")

    p1 = Producto(2.5, "Cuaderno", ["papelería"])  # inmutable
    p2 = replace(p1, precio=3.0)  # crea copia modificada
    print("p1:", p1, "| p2 (replace):", p2)
    print("asdict:", asdict(p1))

    # TODO: (Tema: FACTURA)
    # Crea @dataclass Factura(numero:int, items:List[Producto]) con total @property (cached_property opcional).
    # Añade método con_iva(%) que devuelve una nueva Factura con precios ajustados (usa replace en productos).
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 3 — Herencia múltiple, MRO y mixins (super() cooperativo)
# =========================================================================================
def seccion_3():
    encabezado("SECCIÓN 3 — Herencia múltiple, MRO y mixins")

    # * TEORÍA
    # MRO: orden de resolución de métodos. super() coopera si todas las clases lo llaman.
    # Mixins: clases pequeñas que añaden comportamiento (no estado obligatorio).

    class LoggerMixin:
        def save_log(self, msg: str) -> None:
            print(f"[LOG] {msg}")

    class Entidad:
        def __init__(self, id_: int, **kw):
            super().__init__(**kw)
            self.id_ = id_

    class TimestampMixin:
        def __init__(self, **kw):
            super().__init__(**kw)
            self._created = "2025-01-01"

    class Usuario(LoggerMixin, TimestampMixin, Entidad):
        def __init__(self, id_: int, nombre: str):
            super().__init__(id_=id_)
            self.nombre = nombre

    u = Usuario(1, "Ana")
    u.save_log(f"Usuario creado id={u.id_} fecha={u._created}")
    print("MRO Usuario:", [c.__name__ for c in Usuario.mro()])

    # TODO: (Tema: MIXINS)
    # Crea un mixin Printable con __repr__ personalizado y úsalo en 2 clases diferentes.
    # Comprueba el MRO y que super() coopera en toda la jerarquía.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 4 — ABC (abstract base classes) y Protocols (duck typing tipado)
# =========================================================================================
def seccion_4():
    encabezado("SECCIÓN 4 — ABC y Protocols")

    # * TEORÍA
    # ABC: obligan a implementar ciertos métodos. Protocols: verifican estructura (interfaces implícitas).

    from abc import ABC, abstractmethod

    class Recurso(ABC):
        @abstractmethod
        def abrir(self) -> None: ...
        @abstractmethod
        def cerrar(self) -> None: ...

    class ArchivoLocal(Recurso):
        def __init__(self, ruta: str):
            self.ruta = ruta
        def abrir(self) -> None:
            print(f"Abriendo {self.ruta}")
        def cerrar(self) -> None:
            print(f"Cerrando {self.ruta}")

    @runtime_checkable
    class SoportaLen(Protocol):
        def __len__(self) -> int: ...

    def mide(x: SoportaLen) -> int:
        return len(x)

    f = ArchivoLocal("/tmp/demo.txt")
    f.abrir(); f.cerrar()
    print("mide(list)", mide([1,2,3]))

    # TODO: (Tema: PROTOCOL)
    # Define un Protocol Formateable con método formatea() y crea 2 clases que lo satisfacen sin heredar.
    # Añade una función que acepte Formateable y demuéstralo con ambas clases.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 5 — Properties avanzadas y Descriptores (validación reusable)
# =========================================================================================
def seccion_5():
    encabezado("SECCIÓN 5 — Properties avanzadas y Descriptores")

    # * TEORÍA
    # property: control de acceso/validación. cached_property: calcula una vez. Descriptores: __get__/__set__/__delete__.

    class NonEmptyStr:
        def __set_name__(self, owner, name):
            self.private = f"_{name}"
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            return getattr(obj, self.private, "")
        def __set__(self, obj, value):
            v = str(value)
            if not v.strip():
                raise ValueError("No puede ser vacío")
            setattr(obj, self.private, v)

    class Usuario:
        nombre = NonEmptyStr()
        def __init__(self, nombre: str, saldo: float = 0.0):
            self.nombre = nombre
            self._saldo = float(saldo)

        @property
        def saldo(self) -> float:
            return self._saldo

        @saldo.setter
        def saldo(self, value: float) -> None:
            v = float(value)
            if v < 0:
                raise ValueError("Saldo negativo")
            self._saldo = v

        @cached_property
        def nombre_mayus(self) -> str:
            print("(calculando nombre_mayus una sola vez)")
            return self.nombre.upper()

    u = Usuario("ana", 10)
    print("nombre:", u.nombre, "| nombre_mayus:", u.nombre_mayus, "/", u.nombre_mayus)

    # TODO: (Tema: DESCRIPTOR VALIDADOR)
    # Crea un descriptor RangoFloat(min,max) y úsalo en una clase Cuenta para validar saldo e interés.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 6 — Iterables/Iteradores y Context Managers
# =========================================================================================
def seccion_6():
    encabezado("SECCIÓN 6 — Iterables/Iteradores y Context Managers")

    # * TEORÍA
    # Iterables: implementan __iter__ que devuelve un iterador. Iteradores: __next__.
    # Context manager: __enter__/__exit__ o @contextmanager.

    class RangoDescendente:
        def __init__(self, start: int, stop: int):
            self.start = start
            self.stop = stop
        def __iter__(self) -> Iterator[int]:
            n = self.start
            while n >= self.stop:
                yield n
                n -= 1

    from contextlib import contextmanager
    @contextmanager
    def abrir(nombre: str):
        print("[abrir]", nombre)
        try:
            yield f"<recurso:{nombre}>"
        finally:
            print("[cerrar]", nombre)

    print(list(RangoDescendente(5, 2)))
    with abrir("demo") as r:
        print("usando", r)

    # TODO: (Tema: TIMER)
    # Implementa un context manager Timer (clase o @contextmanager) que mida duración de un bloque.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 7 — Sobrecarga de operadores y protocolo de contenedores
# =========================================================================================
def seccion_7():
    encabezado("SECCIÓN 7 — Operadores y contenedores")

    # * TEORÍA
    # __len__, __contains__, __iter__, __getitem__ (soporta slices), __setitem__, __delitem__.

    class Bolsa:
        def __init__(self):
            self._datos: List[str] = []
        def __len__(self) -> int:
            return len(self._datos)
        def __contains__(self, item: str) -> bool:
            return item in self._datos
        def __iter__(self) -> Iterator[str]:
            return iter(self._datos)
        def __getitem__(self, idx):
            return self._datos[idx]
        def add(self, x: str) -> None:
            self._datos.append(x)

    b = Bolsa(); b.add("a"); b.add("b"); b.add("c")
    print("len:", len(b), "contains 'b':", 'b' in b, "slice:", b[:2])

    # TODO: (Tema: MATRIZ)
    # Implementa Matriz2D respaldada por lista de listas con __getitem__/__setitem__ para m[i,j].
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 8 — Genéricos (TypeVar/Generic) y factorías con classmethod
# =========================================================================================
T = TypeVar('T')
def seccion_8():
    encabezado("SECCIÓN 8 — Genéricos y factorías")

    class Caja(Generic[T]):
        def __init__(self, valor: T):
            self.valor = valor
        def __repr__(self):
            return f"Caja({self.valor!r})"
        @classmethod
        def desde_texto(cls, s: str) -> "Caja[str]":
            return cls(s)

    c1 = Caja[int](10)
    c2 = Caja.desde_texto("hola")
    print(c1, c2)

    # TODO: (Tema: REPOSITORIO GENÉRICO)
    # Crea Repo[T] con métodos add/get_all y úsalo con T=Producto (de la sección 2).
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 9 — Enums y patrón Strategy (composición + DI)
# =========================================================================================
def seccion_9():
    encabezado("SECCIÓN 9 — Enums y Strategy")

    class EstadoPedido(Enum):
        PENDIENTE = auto()
        PAGADO = auto()
        ENVIADO = auto()

    @dataclass(slots=True)
    class Linea:
        nombre: str
        unidades: int
        precio: float
        @property
        def total(self) -> float:
            return round(self.unidades * self.precio, 2)

    class EstrategiaPrecio(Protocol):
        def total(self, lineas: List[Linea]) -> float: ...

    class PrecioNormal:
        def total(self, lineas: List[Linea]) -> float:
            return round(sum(l.total for l in lineas), 2)

    class PrecioConDescuento:
        def __init__(self, descuento: float = 0.1):
            self.descuento = float(descuento)
        def total(self, lineas: List[Linea]) -> float:
            bruto = sum(l.total for l in lineas)
            return round(bruto * (1 - self.descuento), 2)

    @dataclass
    class Pedido:
        lineas: List[Linea]
        estrategia: EstrategiaPrecio
        estado: EstadoPedido = EstadoPedido.PENDIENTE
        def total(self) -> float:
            return self.estrategia.total(self.lineas)
        def pagar(self) -> None:
            self.estado = EstadoPedido.PAGADO

    pedido = Pedido([Linea("Cuaderno", 2, 2.5), Linea("Bolígrafo", 1, 1.2)], PrecioConDescuento(0.2))
    print("total:", pedido.total(), "estado:", pedido.estado.name)
    pedido.pagar(); print("pagado -> estado:", pedido.estado.name)

    # TODO: (Tema: ESTRATEGIAS)
    # Añade PrecioConIVA(%) y PrecioBlackFriday(descuento fijo por línea) y compáralos con PrecioNormal.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 10 — Copias (shallow/deep), inmutabilidad y dataclasses.replace
# =========================================================================================
def seccion_10():
    encabezado("SECCIÓN 10 — Copias e inmutabilidad")

    a = {"nums": [1, 2, 3]}
    b = copy.copy(a)      # shallow
    c = copy.deepcopy(a)  # deep
    a["nums"][0] = 99
    print("shallow:", b["nums"], "deep:", c["nums"])

    @dataclass(frozen=True)
    class Config:
        host: str
        port: int

    cfg = Config("localhost", 8080)
    cfg2 = replace(cfg, port=8000)
    print("inmutable:", cfg, "| replace:", cfg2)

    # TODO: (Tema: COPIA PROFUNDA)
    # Define una estructura anidada de objetos y demuestra diferencias entre copy y deepcopy.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 11 — Plugins, factorías y registros (classmethod + registro global)
# =========================================================================================
def seccion_11():
    encabezado("SECCIÓN 11 — Plugins y factorías")

    REGISTRO: Dict[str, type] = {}

    class PluginBase(Protocol):
        def run(self, dato: str) -> str: ...

    def registra(nombre: str):
        def deco(cls: type) -> type:
            REGISTRO[nombre] = cls
            return cls
        return deco

    @registra("upper")
    class PluginUpper:
        def run(self, dato: str) -> str:
            return dato.upper()

    @registra("title")
    class PluginTitle:
        def run(self, dato: str) -> str:
            return dato.title()

    class Fabrica:
        @classmethod
        def crear(cls, nombre: str) -> PluginBase:
            if nombre not in REGISTRO:
                raise KeyError(f"Plugin desconocido: {nombre}")
            return REGISTRO[nombre]()

    p = Fabrica.crear("upper"); print(p.run("hola plugins"))
    p = Fabrica.crear("title"); print(p.run("hola plugins"))

    # TODO: (Tema: NUEVO PLUGIN)
    # Registra un plugin "reverse" y pruébalo. Añade validación para asegurar que implementa run().
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  SECCIÓN 12 — Laboratorio IA (POO avanzado)
# =========================================================================================
def seccion_12_ia():
    encabezado("SECCIÓN 12 — Laboratorio IA (POO avanzado)")

    # * PROMPT KIT (copia/pega en ChatGPT)
    # 1) PROMPT BREVE:
    #    "Eres profesor de Python. Diseña un sistema POO de 60 líneas con:
    #      - ABC para Repositorio, protocolo para Serializable, y dataclasses inmutables.
    #      - Estrategias de precio (Strategy) y un context manager de transacción.
    #      - Demostración con 2 objetos y un registro de plugins. Devuélveme SOLO código Python."
    #
    # 2) PROMPT ALTERNATIVO:
    #    "Crea un mini motor de reglas: Regla (Protocol) y Motor que aplica reglas a eventos.
    #      Incluye una fábrica por nombre y tests básicos inline. 70 líneas máximo."
    #
    # 3) PROMPT DE MEJORA:
    #    "Añade validación via descriptor y cached_property en el flujo. Mantén < 80 líneas."

    # * DEMO opcional
    if IA_DEMO:
        @dataclass(frozen=True)
        class Demo:
            nombre: str
            @property
            def saludo(self) -> str:
                return f"Hola {self.nombre}!"
        print(Demo("Avanzado").saludo)

    # TODO: (Tema: PROGRAMA PROPUESTO POR IA)
    # 1) Pide a ChatGPT el miniproyecto con el PROMPT KIT.
    # 2) Pega el código debajo y ejecútalo desde el menú.
    # 3) Modifícalo a tu gusto.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # def mi_proyecto_ia_avanzado():
    #     # pega aquí el código que te generó la IA
    #     pass
    # mi_proyecto_ia_avanzado()


# =========================================================================================
#  AUTOEVALUACIÓN FINAL (avanzado)
# =========================================================================================
def autoevaluacion():
    encabezado("AUTOEVALUACIÓN FINAL (avanzado) — Marketplace POO")

    # TODO: (ENUNCIADO)
    # Implementa un mini Marketplace con componentes reutilizando conceptos avanzados:
    #
    # 1) Producto @dataclass(frozen=True, order=True, slots=True) con etiquetas (default_factory=list).
    # 2) Catalogo que actúa como contenedor: __len__/__contains__/__iter__/__getitem__ (por id).
    # 3) Precios via Strategy: Normal, ConDescuento(%), ConIVA(%). Inyección en Pedido.
    # 4) Pedido con líneas (dataclass Linea) + Estado(Enum). Método pagar() que fija estado.
    # 5) Cliente base (ABC o Protocol: tiene nombre y saldo) y ClienteVIP con 10% extra descuento.
    # 6) Descriptor NonEmptyStr para validar nombre de cliente y property para saldo (no negativo).
    # 7) Añade Repo[Producto] genérico con add/get_all y factoría classmethod desde dict.
    # 8) Demostración final: crea 3 productos, dos clientes (normal/VIP), un pedido con estrategia
    #    y muestra un dashboard: "Cliente:<nom> Saldo:<€> | VIP:<nom> Saldo:<€> | Items:<len> Total:<€> Estado:<estado>"
    #
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------


# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu():
    while True:
        print_firma()
        print("MENÚ — Elige una opción (Avanzado)")
        print("  1) Dunder avanzados y ciclo de vida")
        print("  2) Dataclasses avanzado")
        print("  3) Herencia múltiple y mixins")
        print("  4) ABC y Protocols")
        print("  5) Properties y Descriptores")
        print("  6) Iterables y Context Managers")
        print("  7) Operadores y contenedores")
        print("  8) Genéricos y factorías")
        print("  9) Enums y Strategy")
        print(" 10) Copias e inmutabilidad")
        print(" 11) Plugins y factorías")
        print(" 12) Laboratorio IA (POO avanzado)")
        print(" 13) Autoevaluación final")
        print(" 14) Ejecutar TODO (1–13)")
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
        elif op == 4: seccion_4(); pause()
        elif op == 5: seccion_5(); pause()
        elif op == 6: seccion_6(); pause()
        elif op == 7: seccion_7(); pause()
        elif op == 8: seccion_8(); pause()
        elif op == 9: seccion_9(); pause()
        elif op == 10: seccion_10(); pause()
        elif op == 11: seccion_11(); pause()
        elif op == 12: seccion_12_ia(); pause()
        elif op == 13: autoevaluacion(); pause()
        elif op == 14:
            seccion_1(); seccion_2(); seccion_3(); seccion_4(); seccion_5(); seccion_6();
            seccion_7(); seccion_8(); seccion_9(); seccion_10(); seccion_11(); seccion_12_ia(); autoevaluacion(); pause()
        else:
            print("! Elige una opción del 0 al 14.")


# =========================================================================================
#  EJECUCIÓN
# =========================================================================================
if __name__ == "__main__":
    menu()

