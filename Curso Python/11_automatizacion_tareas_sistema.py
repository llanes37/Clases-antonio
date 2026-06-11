# =========================================================================================
#  🐍 PYTHON CLASE 11 — AUTOMATIZACIÓN BÁSICA DE TAREAS EN WINDOWS
#  ────────────────────────────────────────────────────────────────────────────────────────
#  📘 En esta clase verás, de forma simple y práctica:
#    * Cómo obtener información del sistema (platform, variables de entorno)
#    * Cómo ver uso de CPU y memoria con comandos nativos de Windows (WMIC / systeminfo)
#    * Cómo listar procesos en ejecución (tasklist)
#    * Cómo guardar un "snapshot" (foto rápida) del sistema en un .txt
#    * Autoevaluación ligera para reforzar
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica  ·  # NOTE: apunte útil   ·  # // deprecado
# =========================================================================================

import os
import platform
import subprocess
from pathlib import Path
from datetime import datetime

# * Configuración general ---------------------------------------------------------------
RUN_INTERACTIVE = True   # True: pedir datos; False: usar valores por defecto
PAUSE = False            # Pausa tras cada opción

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

def run(cmd: list[str]) -> tuple[int, str, str]:
    """# * Ejecuta un comando y devuelve (returncode, stdout, stderr) en texto."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:
        return 1, "", str(e)

def es_windows() -> bool:
    return platform.system().lower().startswith("win")

# =========================================================================================
#  SECCIÓN 1 · Información del sistema (fácil y directa)
# =========================================================================================
def seccion_1():
    encabezado("SECCIÓN 1 · Información del sistema")

    # * TEORÍA
    # platform.system(), platform.version(), platform.processor()
    # Variables de entorno: os.environ.get("USERNAME"), "COMPUTERNAME", etc.

    if not es_windows():
        print("Este ejemplo está pensado para Windows.")
        return

    nombre_sistema = platform.system()
    version_sistema = platform.version()
    procesador = platform.processor()

    usuario = os.environ.get("USERNAME", "desconocido")
    equipo  = os.environ.get("COMPUTERNAME", "desconocido")

    print(f"SO: {nombre_sistema}  |  Versión: {version_sistema}")
    print(f"Procesador: {procesador}")
    print(f"Usuario: {usuario}  |  Equipo: {equipo}")

    # TODO: (Tema: Carpeta de usuario)
    # Muestra por pantalla la ruta de tu carpeta de usuario (USERPROFILE) y si existe.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # userprofile = os.environ.get("USERPROFILE", "")
    # print("USERPROFILE:", userprofile, "| existe:", Path(userprofile).exists())

# =========================================================================================
#  SECCIÓN 2 · Uso de CPU y Memoria (comandos nativos)
# =========================================================================================
def seccion_2():
    encabezado("SECCIÓN 2 · Uso de CPU y Memoria")

    # * TEORÍA
    # - CPU: WMIC puede devolver el % de uso → wmic cpu get loadpercentage
    # - Memoria: systeminfo tiene datos útiles; también WMIC OS con Free/Total
    #   wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value

    if not es_windows():
        print("Este ejemplo está pensado para Windows.")
        return

    # Uso de CPU
    code, out, err = run(["wmic", "cpu", "get", "loadpercentage"])
    if code == 0 and out:
        print("CPU (WMIC):")
        print(out)
    else:
        print("WMIC no disponible. Intentando PowerShell…")
        code, out, err = run([
            "powershell", "-NoProfile", "-Command",
            "(Get-CimInstance Win32_Processor).LoadPercentage"
        ])
        print(out or err or "No se pudo obtener el uso de CPU.")

    # Memoria física (MB)
    code, out, err = run(["wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize", "/Value"])
    if code == 0 and out:
        print("\nMemoria (WMIC):")
        print(out)
    else:
        print("\nMemoria (systeminfo, líneas relevantes):")
        code, out, err = run(["cmd", "/c", 'systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"'])
        print(out or err or "No se pudo obtener la memoria.")

    # TODO: (Tema: Solo el número)
    # Muestra SOLO el número de porcentaje de CPU (sin encabezados) usando splitlines y isdigit.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # for linea in (out.splitlines() if out else []):
    #     # ejemplo de parsing:
    #     pass

# =========================================================================================
#  SECCIÓN 3 · Procesos en ejecución (tasklist)
# =========================================================================================
def seccion_3():
    encabezado("SECCIÓN 3 · Procesos en ejecución")

    # * TEORÍA
    # tasklist → lista de procesos. Con /FO CSV da formato CSV fácil de leer.

    if not es_windows():
        print("Este ejemplo está pensado para Windows.")
        return

    # Versión simple: mostrar primeras líneas sin liar al alumno
    code, out, err = run(["tasklist"])
    if out:
        lineas = out.splitlines()
        print("\n".join(lineas[:20]))
        print("... (mostrando solo 20 primeras líneas)")
    else:
        print("No se pudo listar procesos:", err)

    # TODO: (Tema: Filtro por nombre)
    # Pide/captura un nombre (por defecto 'python') y muestra solo líneas que lo contengan.
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # nombre = "python"
    # for linea in lineas:
    #     if nombre.lower() in linea.lower():
    #         print(linea)

# =========================================================================================
#  SECCIÓN 4 · Guardar un SNAPSHOT del sistema (texto)
# =========================================================================================
def seccion_4():
    encabezado("SECCIÓN 4 · Snapshot del sistema → archivo .txt")

    if not es_windows():
        print("Este ejemplo está pensado para Windows.")
        return

    salida = Path("snapshot_sistema.txt")
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bloques = []

    # Info básica
    bloques.append(f"=== SNAPSHOT {ahora} ===")
    bloques.append(f"SO={platform.system()}  VERSION={platform.version()}  CPU={platform.processor()}")
    bloques.append(f"USER={os.environ.get('USERNAME','')}  PC={os.environ.get('COMPUTERNAME','')}")

    # CPU
    code, out, err = run(["wmic", "cpu", "get", "loadpercentage"])
    bloques.append("\n[CPU]\n" + (out or err or "No disponible"))

    # Memoria
    code, out, err = run(["wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize", "/Value"])
    bloques.append("\n[MEMORIA]\n" + (out or err or "No disponible"))

    # Procesos (primeras 15 líneas)
    code, out, err = run(["tasklist"])
    if out:
        primeras = "\n".join(out.splitlines()[:15])
        bloques.append("\n[PROCESOS]\n" + primeras + "\n... (15 primeras líneas)")
    else:
        bloques.append("\n[PROCESOS]\n" + (err or "No disponible"))

    salida.write_text("\n".join(bloques), encoding="utf-8")
    print(f"Snapshot guardado en: {salida.resolve()}")

    # TODO: (Tema: Carpeta propia)
    # Guarda el snapshot dentro de una carpeta 'reportes' (créala si no existe) con nombre:
    #   reportes/snapshot_YYYYMMDD_HHMMSS.txt
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------
    # carpeta = Path("reportes"); carpeta.mkdir(exist_ok=True)
    # nombre = datetime.now().strftime("snapshot_%Y%m%d_%H%M%S.txt")
    # (carpeta/nombre).write_text("\n".join(bloques), encoding="utf-8")

# =========================================================================================
#  AUTOEVALUACIÓN FINAL (muy sencilla)
# =========================================================================================
def autoevaluacion():
    encabezado("AUTOEVALUACIÓN · Mini-monitor")

    # TODO: (Enunciado)
    # 1) Crea una función captura_rapida() que:
    #    - obtenga %CPU (WMIC o PowerShell),
    #    - obtenga memoria libre y total (WMIC OS ... /Value),
    #    - guarde una línea en 'mini_log.txt' con formato:
    #      "YYYY-MM-DD HH:MM:SS | CPU:<%> | MemLibre:<MB> / MemTotal:<MB>"
    # 2) Llama a captura_rapida() 3 veces con unos segundos entre cada captura.
    # 3) Abre el archivo y revisa que cada línea tenga datos.
    #
    # --- ZONA DEL ALUMNO -----------------------------------------------------------------

# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu():
    while True:
        print_firma()
        print("MENÚ · Elige una opción")
        print("  1) Información del sistema")
        print("  2) Uso de CPU y Memoria")
        print("  3) Procesos en ejecución")
        print("  4) Guardar snapshot en .txt")
        print("  5) Autoevaluación (enunciado)")
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
        elif op == 5: autoevaluacion(); pause()
        else:
            print("! Elige una opción del 0 al 5.")

# =========================================================================================
#  EJECUCIÓN
# =========================================================================================
if __name__ == "__main__":
    menu()
