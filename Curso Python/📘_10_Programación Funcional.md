# 🐍 Clase 10 de Python — Programación Funcional (lambda, map/filter/reduce, any/all, zip, sorted) + IA

**Autor:** Joaquín Rodríguez — *Guía didáctica práctica y orientada a colecciones*
**Objetivo global:** Dominar los **patrones funcionales esenciales** en Python para procesar colecciones de forma **clara, compacta y expresiva**:

* **`lambda`** para funciones pequeñas.
* **`map` / `filter` / `reduce`** como tuberías de transformación.
* Utilidades **`any` / `all` / `zip` / `sorted(key=...)`**.
* **Laboratorio IA** con prompts listos y **autoevaluación** integradora.

> 🎨 **Convención Better Comments**: `# !` importante · `# *` definición · `# ?` idea · `# TODO:` práctica · `# NOTE:` apunte · `# //` deprecado

---

## 🧭 Cómo usar este material

1. Ejecuta `10_Programación Funcional.py` y usa el **menú** (opciones **1–6**).
2. En cada sección: **lee la teoría**, ejecuta la **demo**, completa la **ZONA DEL ALUMNO (TODO)**.
3. Al final, haz la **Autoevaluación** (informe de ventas funcional).

**Conmutadores del script**

* `RUN_INTERACTIVE`: pide datos reales (`True`) o usa **valores por defecto** (`False`).
* `PAUSE`: pausa entre secciones.
* `IA_DEMO`: activa una mini‑demo en la sección IA.

**Utilidades del script**

* `safe_input(prompt, caster, default)` → lectura **robusta** con casting + valores por defecto.
* `encabezado(titulo)` y `print_firma()` para presentación.

---

## 🧩 Mapa del temario (menú del programa)

1. `lambda` (funciones pequeñas en una línea)
2. `map` / `filter` / `reduce` (tuberías funcionales)
3. `any` / `all` / `zip` / `sorted(key=...)` (utilidades clave)
4. Laboratorio IA (procesamiento de colecciones)
5. Autoevaluación final (informe de ventas)
6. Ejecutar TODO (1→5)

---

## SECCIÓN 1 · `lambda` (funciones pequeñas en una línea)

### 🎯 Objetivos

* Entender la forma y el **uso idiomático** de `lambda` en Python.
* Practicar `lambda` como **argumento** de otras funciones (`key`, `map`, `filter`).

### 🧠 Teoría en claro

```py
# Forma general
tarea = lambda args: expresión  # devuelve el resultado de la expresión
```

**Cuándo usarla**: funciones **muy cortas**, “de usar y tirar”, especialmente como `key=` en `sorted` o en transformaciones simples con `map`/`filter`.

**Cuándo NO**: si la lógica crece, añade ramas/validaciones o reutilización → define una función con `def` y docstring.

### 👀 Demo guiada

* `cuadrado = lambda x: x*x`
* `iva = lambda base, p=21: round(base*(1+p/100), 2)`
* `nombre_completo = lambda n,a: f"{n.strip().title()} {a.strip().title()}"`
* Uso de `lambda` en `sorted(lista, key=...)` para ordenar **por edad** y **por nombre** en una lista de dicts.

### 🛠️ ZONA DEL ALUMNO · TODO — **Formateo express**

1. Define `titulo = lambda s: s.strip().title()`.
2. Con `sucios = ["   peDro", "ana   ", "  ZAida "]`, ordénalos con `sorted(sucios, key=titulo)` y muestra el resultado.

> 💡 **Tip:** Si necesitas **composición** (encadenar pequeñas funciones), considera funciones auxiliares con `def` para que el código sea legible.

---

## SECCIÓN 2 · `map` / `filter` / `reduce` (en profundidad)

### 🎯 Objetivos

* Construir **pipelines**: transformar → filtrar → resumir.
* Limpiar datos “sucios” y totalizar colecciones de forma funcional.

### 🧠 Teoría en claro

* `map(f, iterable)` → aplica `f` a cada elemento → **transformación**.
* `filter(pred, iterable)` → mantiene los elementos con `pred(elem) == True` → **selección**.
* `functools.reduce(func, iterable, init)` → acumula en un **único valor** (suma/producto/concatenación/mezcla).

**Notas prácticas**

* En Python, **comprensiones** suelen ser **más legibles** que `map`/`filter` sencillos. Úsalos cuando realmente aporten claridad.
* Para sumar, prefiere **`sum()`** a `reduce` (más claro). `reduce` brilla en acumulaciones **no triviales**.

### 👀 Demos guiadas

1. **Limpieza y total de precios**

   * Limpia strings (`strip`, `replace`) → filtra numéricos → conviértelos a `float` → totalízalos con `reduce`.
2. **Pipeline en notas**

   * Sube +0.5 a todas (máx. 10), **filtra** aprobados y calcula **media** con `reduce/len`.
3. **Construcción de cadena**

   * Une `['hola','mundo','python']` en una frase con `reduce`.

### 🛠️ ZONA DEL ALUMNO · TODO — **Facturas**

Dada `lineas = [{"desc":"A","precio":3.5,"uds":2}, ...]`:

1. Calcula **importe línea** = `precio*uds` (con `map`).
2. **Filtra** importes > 20 (con `filter`).
3. **Suma** el total (con `reduce`) y muestra con 2 decimales.

> 💡 **Tip:** Encadena pasos en variables intermedias **con nombre** para mejorar legibilidad (evita una sola línea demasiado densa).

---

## SECCIÓN 3 · `any` / `all` / `zip` / `sorted(key=...)` (utilidades clave)

### 🎯 Objetivos

* Validar colecciones con **`any`** (¿hay alguno?) y **`all`** (¿son todos?).
* **Parear** listas con `zip` y dominar `sorted` con claves múltiples.

### 🧠 Teoría en claro

* `any(iterable)` → `True` si **algún** elemento es verdadero.
* `all(iterable)` → `True` si **todos** lo son.
* `zip(a,b,...)` → recorre en paralelo y devuelve tuplas (trunca a la menor longitud).
* `sorted(lista, key=func, reverse=False)` → **ordenación estable** por clave. Para **múltiples claves**: `key=lambda x: (clave1, clave2)`.

### 👀 Demos guiadas

* Comprobar si hay **algún 10** y si **todas** las notas son ≥ 5.
* Parear `cursos` y `plazas` con `zip` en línea formateada.
* Ordenación **multi‑clave** (`categoria`, `precio`) y **Top‑N** (`reverse=True` + slicing).

> 💡 **Atajo**: para claves extraídas de diccionarios o tuplas, también puedes usar `operator.itemgetter('clave')`. Aquí usamos `lambda` por didáctica.

### 🛠️ ZONA DEL ALUMNO · TODO — **Validación y ranking**

Con `notas = [7, 5, 9, 6, 10]` y `alumnos = ["Ana","Luis","Mara","Paco","Rita"]`:

1. `all(n >= 5 for n in notas)` → ¿todos aprobados?
2. `any(n == 10 for n in notas)` → ¿hay algún 10?
3. Muestra parejas “`Nombre: Nota`” con `zip`.
4. Ordena por **nota desc** y muestra el **Top‑3**.

---

## SECCIÓN 4 · Laboratorio IA (procesamiento de colecciones)

### 🎯 Objetivos

* Pedir a la IA un script de **35–50 líneas** que explote `map/filter/reduce`, `sorted`, `any/all`.
* Practicar el patrón **pipeline** con datos de **ventas** o **notas**.

### 🧰 Prompt Kit (copia/pega y ejecuta)

1. **Generación**

   > “Eres profesor de Python. Genera un programa de 35–50 líneas que use:
   > • `map/filter/reduce` para limpiar y resumir ventas (precio, uds)
   > • `sorted(key=...)` para ranking de productos
   > • `any/all` para validaciones
   > Devuelve **SOLO código Python**, sin librerías.”
2. **Alternativo**

   > “Crea un **analizador de notas** con subida de 0.5 (map), filtro de aprobados (filter), media con reduce, Top‑3 con sorted y una línea final tipo dashboard.”
3. **Mejora**

   > “Refactoriza usando **lambdas** y funciones pequeñas. Manténlo **< 50 líneas**.”

### 👀 Demo rápida (si `IA_DEMO=True`)

* Totalizar una lista `precios` con `reduce` en una sola línea.

### 🛠️ ZONA DEL ALUMNO · TODO — **Pega tu mini‑programa**

* Programa y mejora el resultado: separa funciones, añade validaciones y **resumen final**.

---

## AUTOEVALUACIÓN FINAL · Informe de ventas funcional

### 🎯 Objetivos

* Integrar **lambda**, **map/filter/reduce**, **any/all**, **zip**, **sorted** en un informe claro.

### 🛠️ Enunciado

Tienes una lista de dicts `{"producto":str, "precio":float, "uds":int}`:

1. **Normaliza nombres** con `lambda` (`strip`+`title`) y calcula **importes** `precio*uds` (con `map`).
2. **Filtra** las líneas con importe `< 20` (con `filter`).
3. **Totaliza** con `reduce` (dos decimales).
4. **Ordena** por **importe desc** (`sorted(key=lambda ...)`) y muestra el **Top‑3** (puedes usar `zip` para parear nombre‑importe).
5. Usa **`any`** y **`all`** para:

   * ¿Hay **algún** producto con importe **0**?
   * ¿**Todos** los precios son `> 0`?
6. **Resumen final** (una línea):
   `"Líneas:<n> | Filtradas:<m> | Total:<€> | Top:<nombre-importe>"`

### 📏 Rúbrica

* **Correcto**: pipelines claros, validaciones con `any/all`, ordenación correcta.
* **Excelente**: nombres expresivos, pasos intermedios con variables, resumen legible.

---

## APÉNDICE A · Patrones y alternativas idiomáticas

* **Comprensiones** vs `map/filter`: en Python, las comprensiones suelen ser **más legibles**. Ej.:
  `pares = [x for x in nums if x % 2 == 0]`  en lugar de  `list(filter(lambda x: x % 2 == 0, nums))`.
* **`sum`/`min`/`max`** con generadores son preferibles a `reduce` para esos casos:
  `total = sum(x['importe'] for x in lineas)`.
* **Ordenación multi‑clave**: `sorted(datos, key=lambda r: (r['cat'], r['precio']))`.
* **Top‑N**: `sorted(..., reverse=True)[:N]` o `heapq.nlargest(N, datos, key=...)` para colecciones grandes.
* **Evita lambdas complejas**: si la expresión crece, usa `def` con un **nombre descriptivo** y docstring.

---

## APÉNDICE B · Errores comunes (y cómo evitarlos)

* **`reduce` innecesario**: usa `sum` para sumas sencillas.
* **Lambdas largas**: baja la lógica a funciones nombradas.
* **Olvidar normalizar datos** antes de ordenar/filtrar (espacios, mayúsculas, comas por puntos).
* **Pipelines opacos** en una sola línea: separa en pasos con nombres **claros**.
* **Suposiciones con `zip`**: recuerda que trunca a la longitud de la lista **más corta**.

---

## APÉNDICE C · Retos extra (para subir el nivel)

1. **Ranking por grupo**: dada una lista con `categoria`, calcula Top‑2 por categoría (puedes usar `sorted` + bucles o `itertools.groupby`).
2. **Análisis de texto**: de un párrafo, normaliza, separa palabras y devuelve Top‑5 más frecuentes (`sorted` por `(-freq, palabra)`).
3. **Validación de formularios**: con `any/all`, comprueba que todos los campos requeridos no estén vacíos y al menos uno de los opcionales esté presente.
4. **KPI simple**: convierte lecturas de sensores con `map`, filtra fuera de rango con `filter`, y resume con `min/max/sum/len`.

---

## ✅ Qué has aprendido

* Diseñar **pipelines funcionales** con `map/filter/reduce`.
* Ordenar y seleccionar con `sorted(key=...)`, `any/all`, `zip`.
* Usar `lambda` con criterio para transformar/ordenar con claridad.
* Integrar todo en un **informe funcional** de ventas.
* Pedir a la **IA** miniprogramas funcionales y **mejorarlos**.

---
