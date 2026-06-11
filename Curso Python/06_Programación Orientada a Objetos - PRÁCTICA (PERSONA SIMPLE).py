# =========================================================================================
#  PYTHON — PRÁCTICA (Tema fácil) — Programación Orientada a Objetos
#  (ejercicio) PERSONA SIMPLE — Plantilla guiada SIN CÓDIGO (sólo comentarios y huecos)
#
#  En esta práctica repasarás:
#    * Clases y objetos: atributos y métodos
#    * __init__ y uso de self
#    * Método de instancia que devuelve un string
#
#  Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica  ·  # NOTE: apunte útil   ·  # // deprecado
# =========================================================================================

# * ÍNDICE (ejercicios y partes) ---------------------------------------------------------
# (ejercicio) E1 — Clase Persona (declaración y __init__)
#   (parte) A — Declaración de clase y docstring
#   (parte) B — Constructor __init__(self, nombre, edad)
# (ejercicio) E2 — Método presentar()
#   (parte) C — Implementación del método presentar()
# (ejercicio) E3 — Instanciación y uso
#   (parte) D — Crear objetos y mostrar resultados
# (ejercicio) E4 — Extensiones opcionales (validación / utilidades)
#   (parte) E — Validación básica y método extra
# (extra) Checklist, salida esperada y errores comunes

# =========================================================================================
#  (ejercicio) E1 — Clase Persona (declaración y __init__)
# =========================================================================================
# * OBJETIVO: crear el molde (clase) y preparar sus datos (atributos).
# * REQUISITOS: usar self para guardar nombre (str) y edad (int).

# (parte) A — Declaración de clase y docstring
# TODO: Declara la clase y escribe una docstring breve que explique su propósito.
# Ejemplo de docstring (texto orientativo): "Representa una persona con nombre y edad".
#
# class Persona:
#     """TODO: escribe aquí la descripción de la clase."""
#     # ? Puedes anotar aquí cualquier decisión de diseño (opcional)

# (parte) B — Constructor __init__(self, nombre, edad)
# TODO: Define el constructor y asigna los atributos de instancia.
# - self.nombre = nombre
# - self.edad = edad
# - Conversión/chequeo opcional: int(edad) si necesitas asegurar el tipo
#
#     def __init__(self, nombre: str, edad: int):
#         # TODO: asigna los atributos en self
#         # ! Recuerda: self hace referencia a la instancia
#         # NOTE: puedes validar edad >= 0 como mejora opcional
#         # self.nombre = ...
#         # self.edad = ...

# =========================================================================================
#  (ejercicio) E2 — Método presentar()
# =========================================================================================
# * OBJETIVO: devolver un string con la presentación.
# * FORMATO: "Soy <nombre> y tengo <edad> años"

# (parte) C — Implementación del método presentar()
# TODO: Implementa el método y devuelve el string con f-string o format().
#
#     def presentar(self) -> str:
#         # TODO: devuelve el texto de presentación usando self.nombre y self.edad
#         # return f"Soy {self.nombre} y tengo {self.edad} años"

# =========================================================================================
#  (ejercicio) E3 — Instanciación y uso
# =========================================================================================
# * OBJETIVO: crear dos objetos y mostrar su presentación.
# * DATOS DE PRUEBA sugeridos: ("Ana", 30) y ("Luis", 22)

# (parte) D — Crear objetos y mostrar resultados
# TODO: Crea al menos dos instancias y muestra por pantalla presentar().
#
# # Ejemplo de guion (no implementado):
# # p1 = Persona("Ana", 30)
# # p2 = Persona("Luis", 22)
# # print(p1.presentar())
# # print(p2.presentar())

# =========================================================================================
#  (ejercicio) E4 — Extensiones opcionales (validación / utilidades)
# =========================================================================================
# * OBJETIVO: mejorar la clase con pequeñas utilidades.

# (parte) E — Validación básica y método extra
# TODO (opcional): añade un método es_mayor_de_edad(self) -> bool (>= 18)
# TODO (opcional): valida que edad sea int y no negativa (ValueError si no cumple)
# TODO (opcional): añade __str__ para mostrar "Persona(nombre=<n>, edad=<e>)"
#
#     def es_mayor_de_edad(self) -> bool:
#         # TODO: devuelve True si self.edad >= 18
#         # return ...
#
#     def __str__(self) -> str:
#         # TODO: devuelve una representación amigable de la persona
#         # return f"Persona(nombre={self.nombre}, edad={self.edad})"

# =========================================================================================
#  (extra) Checklist de entrega, salida esperada y errores comunes
# =========================================================================================

# * CHECKLIST -----------------------------------------------------------------------------
# - [ ] La clase Persona existe y tiene docstring
# - [ ] __init__ recibe (nombre, edad) y guarda en atributos de instancia
# - [ ] presentar() devuelve exactamente el texto pedido
# - [ ] Se crean al menos dos instancias y se imprimen sus presentaciones
# - [ ] (Opcional) Validación de edad y método es_mayor_de_edad()

# * SALIDA ESPERADA (orientativa) ---------------------------------------------------------
# Soy Ana y tengo 30 años
# Soy Luis y tengo 22 años
# (Opcional) Ana es mayor de edad: True

# * ERRORES COMUNES ----------------------------------------------------------------------
# - Olvidar self como primer parámetro de los métodos
# - No asignar a atributos de instancia (self.nombre, self.edad) en __init__
# - Construir mal el string en presentar() o no devolverlo (usar print en lugar de return)
# - No crear instancias antes de intentar llamar presentar()

# =========================================================================================
#  ZONA DEL ALUMNO (activa) — Escribe debajo tu solución
#  Consejo: copia las plantillas comentadas de arriba y complétalas.
# =========================================================================================
#
# (Pega aquí tu clase Persona, métodos y pruebas)
#
