# 🐍 Clase 11 de Python — Automatización básica de tareas en **Windows** (platform, entorno, `subprocess`, WMIC/PowerShell, `tasklist`, snapshot)

**Autor:** Joaquín Rodríguez — *Guía didáctica, pensada a fondo y lista para clase*
**Objetivo global:** Aprender a **inspeccionar y automatizar** tareas sencillas del sistema Windows con Python: leer **información del sistema** y **variables de entorno**, consultar **CPU y memoria** con comandos nativos (WMIC / PowerShell / `systeminfo`), **listar procesos** con `tasklist`, **guardar snapshots** de diagnóstico y diseñar una **autoevaluación práctica**.

> 🎨 **Convención Better Comments** que usa el proyecto: `# !` importante · `# *` definición/foco · `# ?` idea/nota · `# TODO:` práctica · `# NOTE:` apunte · `# //` deprecado

---

## 🧭 Cómo usar este material

1. Ejecuta `11_automatizacion_tareas_sistema.py` para ver el **menú** (opciones **0–5**).
2. Recorre cada sección: **teoría breve**, **demo guiada** y **ZONA DEL ALUMNO (TODO)** para practicar.
3. El script ya trae utilidades (`safe_input`, `encabezado`, `pause`, `run`, `es_windows`) y **conmutadores**:

   * `RUN_INTERACTIVE`: `True` pide datos reales; `False` usa **valores por defecto** (no bloquea).
   * `PAUSE`: `True` añade pausa tras cada sección (ideal en directo).
4. Al final, completa la **Autoevaluación** creando un mini‑monitor con log periódico.

> ⚠️ **Requisito**: estas demos están enfocadas a **Windows**. En otros SO, el script imprime un aviso y omite la sección.

---

## 🧩 Mapa del temario (menú del programa)

1. Información del sistema (platform + entorno)
2. Uso de CPU y memoria (WMIC / PowerShell / `systeminfo`)
3. Procesos en ejecución (`tasklist`)
4. Snapshot del sistema → `.txt`
5. Autoevaluación (mini‑monitor)
6. Salir

---

## Utilidades incluidas (ya en el script)

* `print_firma()` · `encabezado(titulo)` · `pause()`
* `safe_input(prompt, caster, default)` → lectura **robusta** con casting y **fallback**.
* `run(cmd: list[str]) -> (returncode, stdout, stderr)` → envoltorio de `subprocess.run` con **captura** de salida, **texto** y **timeout** (20 s).
* `es_windows()` → detección rápida del SO.

> 💡 **Patrón**: en vez de `os.system(...)`, usamos `subprocess.run` para **capturar** stdout/stderr, comprobar código de salida y **evitar** inyecciones.

---

## SECCIÓN 1 · Información del sistema (rápida y útil)

### 🎯 Objetivos

* Leer datos básicos con `platform` y **variables de entorno** con `os.environ`.

### 🧠 Teoría en claro

* `platform.system()` / `platform.version()` / `platform.processor()`
* Entorno típico de Windows: `USERNAME`, `COMPUTERNAME`, `USERPROFILE`.

### 👀 Demo guiada

* Muestra SO, versión y CPU; más **usuario** y **equipo** desde el entorno.

### 🛠️ ZONA DEL ALUMNO · TODO — **Carpeta de usuario**

1. Lee `USERPROFILE` con `os.environ.get("USERPROFILE", "")`.
2. Con `Path(userprofile).exists()`, imprime si **existe** esa ruta.
3. (Opcional) Lanza una advertencia si no existe.

> 🧩 **Idea**: añade al final de la sección una línea que imprima el **tamaño** (en bytes) de `USERPROFILE` usando `sum(p.stat().st_size ...)` sobre algunos subdirectorios (¡cuidado con el coste!).

---

## SECCIÓN 2 · Uso de CPU y de Memoria (comandos nativos)

### 🎯 Objetivos

* Obtener **carga de CPU** y **memoria libre/total** con herramientas del SO.
* Probar **alternativas** si WMIC no está disponible.

### 🧠 Teoría en claro

* **CPU (WMIC)**: `wmic cpu get loadpercentage`
* **Memoria (WMIC)**: `wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value`
* **Alternativas PowerShell** (si WMIC no existe):

  * CPU: `(Get-CimInstance Win32_Processor).LoadPercentage`
  * Memoria: `(Get-CimInstance Win32_OperatingSystem) | Select FreePhysicalMemory, TotalVisibleMemorySize`
* **`systeminfo`** + `findstr` sirve como **plan C** para memoria disponible/total.

### 👀 Demo guiada

* Ejecuta WMIC; si falla, intenta PowerShell.
* Muestra los bloques de salida en crudo y luego las **líneas relevantes**.

### 🛠️ ZONA DEL ALUMNO · TODO — **Solo el porcentaje**

1. Tras invocar CPU, procesa `stdout` con `.splitlines()` y **filtra** la línea que sea un **número** (`str.isdigit()`).
2. Imprime `CPU:<n>%` (solo el número).
3. Para memoria, las métricas WMIC vienen en **KB**: convierte a **MB** (divide por 1024, redondea a 0 decimales).

> 🧪 **Tip**: al parsear WMIC en `/Value`, separa por `'='` y convierte con `int()`; protege con `try/except`.

---

## SECCIÓN 3 · Procesos en ejecución (`tasklist`)

### 🎯 Objetivos

* Listar procesos y **filtrar** por nombre de forma simple.

### 🧠 Teoría en claro

* `tasklist` devuelve una tabla; también puedes formatear en CSV con `/FO CSV`.
* Para filtrar sin Python: `tasklist | findstr /I python`.

### 👀 Demo guiada

* Ejecuta `tasklist` y muestra **las 20 primeras líneas** para no saturar la consola.

### 🛠️ ZONA DEL ALUMNO · TODO — **Filtro por nombre**

1. Pide/captura un nombre (por defecto, `python`).
2. Recorre `lineas` y **muestra** solo las que contengan ese texto (ignora mayúsculas/minúsculas con `.lower()`).
3. (Opcional) Repite usando el modo **CSV** y separa columnas por comas.

> 🧩 **Idea**: crea una lista de dicts con `{nombre, pid, memoria}` a partir del CSV y ordénala por memoria descendente.

---

## SECCIÓN 4 · Snapshot del sistema → archivo `.txt`

### 🎯 Objetivos

* Consolidar en un **único reporte**: SO, usuario/equipo, CPU, memoria y procesos (resumen).
* Guardarlo en disco con fecha/hora e **indicaciones** claras.

### 🧠 Teoría en claro

* Usa `datetime.now().strftime("%Y-%m-%d %H:%M:%S")` para el sello.
* Construye el reporte en una lista `bloques` y **úne** con `"\n".join(bloques)`.

### 👀 Demo guiada

* Crea `snapshot_sistema.txt` con: encabezado (fecha), SO/versión/CPU, usuario/equipo, bloque **\[CPU]**, bloque **\[MEMORIA]**, bloque **\[PROCESOS]** (primeras 15 líneas) y aviso de **recorte**.

### 🛠️ ZONA DEL ALUMNO · TODO — **Carpeta `reportes/` + nombre temporal**

1. Crea carpeta `reportes/` si no existe.
2. Genera archivo `snapshot_YYYYMMDD_HHMMSS.txt`.
3. Escribe el mismo contenido y **muestra la ruta absoluta** al final.

> 💡 **Tip**: con `Path.resolve()` obtienes la **ruta completa** del reporte.

---

## AUTOEVALUACIÓN FINAL · **Mini‑monitor** con log periódico

### 🎯 Objetivos

* Diseñar una función de **captura** que tome CPU y memoria, y **registre** una línea en un log.
* Realizar **N repeticiones** separadas por una espera breve.

### 🛠️ Enunciado

1. Implementa `captura_rapida()` que:

   * Obtenga **%CPU** (WMIC o PowerShell).
   * Obtenga **Memoria libre y total** (WMIC `/Value`).
   * Escriba en `mini_log.txt` una línea:
     `"YYYY-MM-DD HH:MM:SS | CPU:<%> | MemLibre:<MB> / MemTotal:<MB>"`
2. Llama a `captura_rapida()` **3 veces** con `time.sleep(2)` entre llamadas.
3. Abre el archivo y **verifica** que cada línea tiene datos.

### 📏 Rúbrica

* **Correcto**: lectura de CPU/memoria, líneas con sello de tiempo, 3 capturas totales.
* **Excelente**: manejo de **errores** (códigos de salida ≠ 0), función pequeña y clara, y conversión de unidades coherente.

> 🧪 **Plus**: crea `captura_n(n=3, pausa=2)` para configurar número de capturas y segundos entre ellas.

---

## Apéndice A · Alternativas y compatibilidad (WMIC, PowerShell, `systeminfo`)

* **WMIC** está **deprecado** en versiones recientes de Windows, pero suele seguir estando disponible; si no, usa **PowerShell** con `Get-CimInstance`.
* **Plan A**: WMIC → simple y directo.
* **Plan B**: PowerShell → más moderno, algo más verboso.
* **Plan C**: `systeminfo` + `findstr` → rescata datos básicos si lo anterior falla.

> 🔧 **Sugerencia de diseño**: encapsula cada plan (A/B/C) en **funciones** y elige **dinámicamente** la primera que funcione.

---

## Apéndice B · Buenas prácticas de automatización con `subprocess`

* Pasa comandos como **lista** `list[str]` (evita `shell=True` salvo que lo necesites).
* Establece **`timeout`** (ya lo hace `run(...)`) para no colgar la app.
* Usa el **código de salida** para decidir si reintentas con otro método.
* **No bloquees** la UI: agrupa salidas y muestra **resúmenes** (ej. 15–20 líneas de procesos).
* Haz **parsing robusto**: valida que algo es dígito antes de convertir; usa `.partition('=')` con WMIC `/Value`.

---

## Apéndice C · Retos extra (sube el nivel)

1. **Procesos CSV**: invoca `tasklist /FO CSV`, parsea a dicts y guarda el **Top‑10 por memoria** en `procesos_top.csv`.
2. **Alerta simple**: si `CPU > umbral` (ej. 85%), añade una marca `!ALTO USO` en el log.
3. **Programa de limpieza**: crea `limpieza_tmp.ps1` con comandos (borrar temporales) y ejecútalo desde Python (solo si eres admin).
4. **Empaquetado**: guarda el snapshot y el log en `reportes/` con nombre de sesión y fecha.

---

## ✅ Qué has aprendido

* Consultar **información del sistema** y **entorno** desde Python.
* Medir **CPU** y **memoria** usando **comandos nativos** (WMIC/PowerShell) y alternativas.
* **Listar y filtrar procesos** de forma práctica.
* Generar un **snapshot** de diagnóstico legible y guardarlo con marca temporal.
* Diseñar un **mini‑monitor** con `subprocess` y logs.

---
