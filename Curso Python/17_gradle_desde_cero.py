# =========================================================================================
#  PYTHON CLASE 17 - GRADLE DESDE CERO
#  -----------------------------------------------------------------------------------------
#  En esta clase aprenderas a:
#    * Entender que es Gradle y por que usamos el wrapper
#    * Leer un build.gradle(.kts) sin perderte
#    * Identificar plugins, repositorios y dependencias
#    * Ejecutar tareas tipicas como build, test, clean y run
#    * Generar bloques Gradle con ayuda de Python
#    * Usar Python para validar una configuracion de build
#    * Practicar con laboratorio IA y mini reto final
#
#  Better Comments:
#    # ! importante   ·  # * definicion/foco   ·  # ? idea/nota
#    # TODO: practica  ·  # NOTE: apunte util  ·  # // deprecado
# =========================================================================================

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any, Callable

# * Configuracion general ---------------------------------------------------------------
# ? Seguimos el mismo patron del resto del curso para que esta unidad encaje visualmente.
RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True


def print_firma() -> None:
    # * Firma comun del curso.
    print("\n" + "=" * 80)
    print("Autor: joaquin  |  Pagina web: https://clasesonlinejoaquin.es/")
    print("=" * 80 + "\n")


def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass


def safe_input(prompt: str, caster: Callable[[str], Any], default: Any) -> Any:
    # * Entrada segura: ideal para demos o cuando el alumno se equivoca al teclear.
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
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


@dataclass
class GradleTask:
    # * Modelo minimo para mostrar tareas comunes de forma ordenada.
    nombre: str
    comando: str
    descripcion: str

    def resumen(self) -> str:
        return f"{self.nombre:<10} -> {self.descripcion} (cmd: {self.comando})"


BUILD_GRADLE_KTS = dedent(
    """
    plugins {
        id("application")
        id("org.jetbrains.kotlin.jvm") version "1.9.24"
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.1")
        testImplementation(kotlin("test"))
    }

    application {
        mainClass.set("org.example.AppKt")
    }
    """
).strip()


def extraer_version_wrapper(texto: str) -> str | None:
    # * Función simple para practicar parsing sin meter regex complejas.
    for linea in texto.splitlines():
        if "distributionUrl" in linea and "gradle-" in linea:
            try:
                fragmento = linea.split("gradle-")[1]
                return fragmento.split("-")[0]
            except IndexError:
                return None
    return None


def generar_tarea_custom(nombre: str) -> str:
    # * Python como generador de plantillas: muy útil para no repetir bloques a mano.
    return dedent(
        f"""
        tasks.register("{nombre}") {{
            doLast {{
                println("Hola desde {nombre}! Aqui pondrias tu logica custom.")
            }}
        }}
        """
    ).strip()


# =========================================================================================
#  SECCION 1 · Fundamentos de Gradle y wrapper
# =========================================================================================
def seccion_1() -> None:
    encabezado("SECCION 1 · Fundamentos de Gradle y wrapper")

    # * TEORIA
    # Gradle es un sistema de build basado en tareas.
    # ? Lo importante para un alumno principiante no es memorizarlo todo:
    #   basta con entender que:
    #   - el wrapper fija la version,
    #   - build/test/clean/run son tareas frecuentes,
    #   - y build.gradle(.kts) es el archivo central de configuracion.
    wrapper_archivos = [
        "gradlew",
        "gradlew.bat",
        "gradle/wrapper/gradle-wrapper.jar",
        "gradle/wrapper/gradle-wrapper.properties",
    ]
    raiz = Path(".")
    existentes = [p for p in wrapper_archivos if (raiz / p).exists()]
    faltantes = [p for p in wrapper_archivos if p not in existentes]

    print("Archivos del wrapper encontrados:")
    for archivo in existentes:
        print(" -", archivo)

    if faltantes:
        print("Faltan estos archivos:")
        for archivo in faltantes:
            print("   ·", archivo)
    else:
        print("Wrapper completo listo para usar: ./gradlew <tarea>")

    props = raiz / "gradle/wrapper/gradle-wrapper.properties"
    if props.exists():
        contenido = props.read_text(encoding="utf-8")
        version = extraer_version_wrapper(contenido)
        print("Version detectada en wrapper:", version or "no encontrada")
    else:
        print("No se encontro gradle-wrapper.properties en la ruta actual.")

    # TODO: (Tema: CHECKLIST WRAPPER)
    # Muestra un mensaje especial si detectas version 7.x o inferior.


# =========================================================================================
#  SECCION 2 · Anatomia de build.gradle.kts
# =========================================================================================
def seccion_2() -> None:
    encabezado("SECCION 2 · Anatomia de build.gradle.kts")

    # * TEORIA
    # Un build script suele responder a 4 preguntas:
    #   - que plugins usa el proyecto,
    #   - de donde descarga dependencias,
    #   - que dependencias necesita,
    #   - y como arranca o empaqueta la aplicacion.
    print("Ejemplo de build.gradle.kts:\n")
    print(BUILD_GRADLE_KTS)

    checklist = [
        ('id("application")' in BUILD_GRADLE_KTS, "Plugin application declarado"),
        ("repositories" in BUILD_GRADLE_KTS, "Repositorios definidos"),
        ("dependencies" in BUILD_GRADLE_KTS, "Dependencias configuradas"),
        ("mainClass.set" in BUILD_GRADLE_KTS, "Punto de entrada declarado"),
    ]
    print("\nChecklist rapido:")
    for ok, texto in checklist:
        icono = "OK" if ok else "FALTA"
        print(f" - [{icono}] {texto}")

    # TODO: (Tema: COMPARAR DSL)
    # Escribe una mini version en Groovy DSL y compara:
    #   plugins { id 'application' }
    # con la version Kotlin DSL.


# =========================================================================================
#  SECCION 3 · Tareas habituales
# =========================================================================================
def seccion_3() -> None:
    encabezado("SECCION 3 · Tareas habituales de Gradle")

    # * IDEA CLAVE
    # El alumno no necesita 50 tareas. Necesita reconocer 4 o 5 muy comunes.
    tareas = [
        GradleTask("build", "./gradlew build", "Compila, testea y empaqueta"),
        GradleTask("test", "./gradlew test", "Ejecuta la suite de pruebas"),
        GradleTask("clean", "./gradlew clean", "Limpia artefactos de build"),
        GradleTask("run", "./gradlew run", "Lanza la app si existe plugin application"),
        GradleTask("tasks", "./gradlew tasks", "Lista tareas disponibles"),
    ]

    for tarea in tareas:
        print("-", tarea.resumen())

    print("\nRegla practica:")
    print("- Cuando no sabes por donde empezar: ./gradlew tasks")
    print("- Cuando quieres comprobar calidad minima: ./gradlew test")

    # TODO: (Tema: MAPA DE TAREAS)
    # Añade una tarea mas que te parezca util para Android, Java o Kotlin.


# =========================================================================================
#  SECCION 4 · Generar tareas custom con Python
# =========================================================================================
def seccion_4() -> None:
    encabezado("SECCION 4 · Generar tareas custom con Python")

    # * Python aqui no sustituye a Gradle.
    # ? Lo usamos como asistente para generar plantillas, validar checks o automatizar texto.
    nombre = safe_input("Nombre de tu tarea custom: ", str, "saludo")
    bloque = generar_tarea_custom(nombre)

    print("Bloque generado:\n")
    print(bloque)

    # TODO: (Tema: DEPENDSON)
    # Genera otra tarea llamada verificarTodo que dependa de test y de saludo.


# =========================================================================================
#  SECCION 5 · Validar configuracion con Python
# =========================================================================================
def seccion_5() -> None:
    encabezado("SECCION 5 · Validar configuracion con Python")

    # * Esta parte conecta con la idea central del curso:
    #   usar Python para tareas utiles, incluso aunque el ecosistema principal sea otro.
    checks = {
        "plugin application": 'id("application")' in BUILD_GRADLE_KTS,
        "mavenCentral": "mavenCentral()" in BUILD_GRADLE_KTS,
        "dependencia de test": "testImplementation" in BUILD_GRADLE_KTS,
        "mainClass": "mainClass.set" in BUILD_GRADLE_KTS,
    }
    for nombre, ok in checks.items():
        print(f"- {nombre:<22} -> {'OK' if ok else 'FALTA'}")

    # TODO: (Tema: ASSERTS)
    # Convierte estas comprobaciones en asserts y explica que fallaria si quitas mavenCentral().


# =========================================================================================
#  SECCION 6 · Laboratorio IA
# =========================================================================================
def seccion_6() -> None:
    encabezado("SECCION 6 · Laboratorio IA")

    if not IA_DEMO:
        print("Laboratorio IA desactivado.")
        return

    # * El uso correcto de IA aqui es:
    #   pedir una explicacion comparativa o una plantilla,
    #   no copiar codigo sin entender el build script.
    prompt = """
Actua como profesor de Gradle para principiantes.
Quiero:
1. Explicacion simple de plugins, repositories y dependencies
2. Un ejemplo minimo de build.gradle.kts
3. Una tarea custom sencilla
4. Explicacion corta de cuando usar build, test, clean y run
No uses jerga innecesaria.
""".strip()
    print(prompt)


# =========================================================================================
#  SECCION 7 · Autoevaluacion final
# =========================================================================================
def seccion_7() -> None:
    encabezado("SECCION 7 · Autoevaluacion final")

    print("Mini reto final:")
    print("- Detecta si existe wrapper")
    print("- Lee gradle-wrapper.properties si existe")
    print("- Extrae la version de Gradle")
    print("- Genera una tarea custom llamada saludarEquipo")
    print("- Comprueba con asserts que el build script tiene plugins y dependencies")


# =========================================================================================
#  MENU PRINCIPAL
# =========================================================================================
def menu() -> None:
    opciones = {
        "1": ("Fundamentos y wrapper", seccion_1),
        "2": ("build.gradle.kts", seccion_2),
        "3": ("Tareas habituales", seccion_3),
        "4": ("Tareas custom con Python", seccion_4),
        "5": ("Validar configuracion", seccion_5),
        "6": ("Laboratorio IA", seccion_6),
        "7": ("Autoevaluacion final", seccion_7),
        "0": ("Salir", None),
    }

    while True:
        print_firma()
        print("CLASE 17 · GRADLE DESDE CERO\n")
        for clave, (texto, _) in opciones.items():
            print(f"[{clave}] {texto}")

        eleccion = safe_input("\nElige una opcion: ", str, "1")
        accion = opciones.get(eleccion, (None, None))[1]
        if eleccion == "0":
            print("Cerrando unidad 17.")
            break
        if accion is None:
            print("! Opcion no valida.")
            pause()
            continue
        accion()
        pause()


if __name__ == "__main__":
    menu()
