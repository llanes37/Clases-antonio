# =========================================================================================
#  CLASE 17 - GRADLE DESDE CERO (ALUMNO)
#  -----------------------------------------------------------------------------------------
#  Esta version esta pensada para practicar:
#    * lectura de wrapper
#    * interpretacion de build.gradle.kts
#    * generacion de tareas custom
#    * validacion basica con Python
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica  ·  # NOTE: apunte util  ·  # // deprecado
# =========================================================================================

from __future__ import annotations

from pathlib import Path
from textwrap import dedent


BUILD_GRADLE_KTS = dedent(
    """
    plugins {
        id("application")
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        testImplementation(kotlin("test"))
    }
    """
).strip()


def extraer_version_wrapper(texto: str) -> str | None:
    # TODO:
    # Busca una linea con distributionUrl y devuelve la version de Gradle.
    # Ejemplo esperado: si aparece gradle-8.7-bin.zip -> devolver "8.7"
    pass


def generar_tarea_custom(nombre: str) -> str:
    # TODO:
    # Devuelve un bloque tasks.register("nombre") con un println dentro.
    pass


# =========================================================================================
#  PRACTICA 1 · WRAPPER
# =========================================================================================

# * Comprueba si existe este archivo:
#   gradle/wrapper/gradle-wrapper.properties
#
# TODO:
# Si existe:
# - leelo
# - intenta extraer la version
# - muestra el resultado


# =========================================================================================
#  PRACTICA 2 · CHECKLIST DE BUILD
# =========================================================================================

# TODO:
# Crea 4 comprobaciones sobre BUILD_GRADLE_KTS:
# - plugin application
# - repositories
# - dependencies
# - mavenCentral
#
# Muestra para cada una: OK o FALTA


# =========================================================================================
#  PRACTICA 3 · TAREA CUSTOM
# =========================================================================================

# * Usa tu funcion generar_tarea_custom("saludo")
# ? Imprime el bloque generado para pegarlo luego en build.gradle.kts


# =========================================================================================
#  ASSERTS RAPIDOS
# =========================================================================================

# TODO:
# Escribe 3 asserts utiles:
# - uno para extraer_version_wrapper
# - uno para generar_tarea_custom
# - uno para verificar que BUILD_GRADLE_KTS contiene repositories


# =========================================================================================
#  AUTOEVALUACION FINAL
# =========================================================================================

# TODO FINAL:
# 1. Genera una tarea verificarTodo.
# 2. Haz un checklist de build script.
# 3. Simula leer un wrapper.properties con version 8.x.
# 4. Explica en comentario por que gradlew es mejor que depender de una instalacion global.
