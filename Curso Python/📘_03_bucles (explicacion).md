# 🐍 Clase 3 de Python — Bucles (`for`, `while`, `range`, `enumerate`, `break/continue/else`, comprensiones) + IA

**Autor:** Joaquín Rodríguez — *Guía didáctica para principiantes*
**Objetivo global:** Practicar el uso de bucles en Python (`for`, `while`, `range`, `enumerate`), controlar el flujo con `break`/`continue`/`else`, crear bucles anidados, usar comprensiones de listas y aplicar todo en un laboratorio con IA + autoevaluación final.

---

## 🧭 Cómo usar este material

1. Ejecuta `03_bucles.py` y usa el menú (opciones **1–10**).
2. Estudia la **teoría**, prueba las **demos**, completa los **TODO** en la ZONA DEL ALUMNO.
3. Termina con la **Autoevaluación final**.

> 💡 **Tip docente:** anima al alumnado a probar **casos límite** (listas vacías, 0, negativos, etc.) para entender mejor los bucles.

---

## 🧩 Mapa del temario (menú del programa)

1. `for` básico (listas)
2. `range()` (secuencias numéricas)
3. `enumerate()` (índice + valor)
4. `while` (condición)
5. `break`, `continue` y `for-else`
6. Bucles anidados (tablas)
7. Comprensiones de listas (opcional)
8. Laboratorio IA (bucles creativos)
9. Autoevaluación final
10. Ejecutar TODO (1→9)

---

## SECCIÓN 1 · `for` básico (recorrer listas)

### 🎯 Objetivos

* Entender la sintaxis del bucle `for` en colecciones.
* Practicar con listas.

### 🧠 Teoría

```py
for <elemento> in <colección>:
    <bloque>
```

Recorre cada elemento en orden.

### 👀 Demo guiada

```py
frutas = ["manzana", "plátano", "pera"]
for f in frutas:
    print(f"Fruta: {f}")
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Crea lista `nombres = ["Ana", "Luis", "María"]` y muestra “Hola, <nombre>” para cada uno.

---

## SECCIÓN 2 · `range()` (secuencias numéricas)

### 🎯 Objetivos

* Generar secuencias numéricas.
* Usar `range(inicio, fin, paso)` para contar o repetir.

### 👀 Demo guiada · Suma 1..n

```py
n = 5
total = 0
for i in range(1, n+1):
    total += i
print(f"Suma 1..{n} = {total}")
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Pide un número `t` (por defecto 4) y muestra su tabla de multiplicar del 1 al 10.

---

## SECCIÓN 3 · `enumerate()` (índice + valor)

### 🎯 Objetivos

* Numerar elementos de una colección.
* Evitar llevar un contador manual.

### 👀 Demo guiada

```py
lista_compra = ["pan", "leche", "huevos"]
for idx, item in enumerate(lista_compra, start=1):
    print(f"{idx}. {item}")
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Crea lista `tareas = ["pagar", "estudiar", "entrenar"]` y muéstralas numeradas desde 1.

---

## SECCIÓN 4 · `while` (condición)

### 🎯 Objetivos

* Ejecutar un bloque repetidamente mientras la condición sea True.
* Evitar bucles infinitos.

### 👀 Demo guiada · PIN con 3 intentos

```py
PIN_CORRECTO = "1234"
intentos = 0
autenticado = False
while intentos < 3 and not autenticado:
    pin = input("PIN: ")
    autenticado = (pin == PIN_CORRECTO)
    intentos += 1
print("Acceso", "concedido" if autenticado else "denegado")
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Imprime los números del 1 al 5 usando `while`.

---

## SECCIÓN 5 · `break`, `continue` y `for-else`

### 🎯 Objetivos

* Controlar el flujo dentro de un bucle.
* Usar `for-else` como “no encontrado”.

### 🧠 Teoría

* `break`: termina el bucle inmediatamente.
* `continue`: salta a la siguiente iteración.
* `for ... else`: el bloque `else` se ejecuta solo si el bucle **no** se interrumpió con `break`.

### 👀 Demo guiada

```py
# for-else
nums = [3, 7, 10, 12]
objetivo = 9
for d in nums:
    if d == objetivo:
        print("Encontrado")
        break
else:
    print("No encontrado")

# continue
numeros = [5, -2, 4, -1, 6]
positivos = []
for n in numeros:
    if n < 0:
        continue
    positivos.append(n)
print("Solo positivos:", positivos)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Recorre lista `datos = [1, 3, -2, 5, 0, 4]`.

  * Suma solo positivos.
  * Si aparece `0`, corta con `break`.
  * Muestra el total acumulado.

---

## SECCIÓN 6 · Bucles anidados (tablas)

### 🎯 Objetivos

* Usar bucles dentro de otros.
* Generar tablas o cuadrículas.

### 👀 Demo guiada · Tabla 3x3

```py
for fila in range(1, 4):
    linea = []
    for col in range(1, 4):
        linea.append(fila * col)
    print(linea)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Pide `filas` y `columnas` y dibuja una cuadrícula de `*` de ese tamaño.

---

## SECCIÓN 7 · Comprensiones de listas (opcional)

### 🎯 Objetivos

* Crear listas nuevas de forma concisa.
* Usar condición opcional para filtrar.

### 👀 Demo guiada

```py
nums = [1, 2, 3, 4, 5]
cuadrados = [x*x for x in nums]
pares = [x for x in nums if x % 2 == 0]
print("Cuadrados:", cuadrados)
print("Pares:", pares)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Dada `precios = [10, 3.5, 20]`, crea lista `con_iva` aplicando 21% (redondeo 2 decimales).

---

## SECCIÓN 8 · Laboratorio IA (bucles creativos)

### 🎯 Objetivos

* Pedir a la IA programas con bucles.
* Practicar prompts y mejoras.

### 🧰 Prompt Kit

1. **Generación**

   > “Eres profesor de Python. Genera un programa de 25–40 líneas que use `for/while`, `range/enumerate` y `break/continue`. Tema: **‘carrito de la compra con descuentos por volumen’**. Variables en español, comentarios con `# *` y `# TODO`. Sin librerías ni clases. Devuelve SOLO código Python.”

2. **Alternativo**

   > “Crea un minijuego **‘Adivina el número’**: número secreto (usar fijo si no hay random), hasta 5 intentos, pistas mayor/menor. Usa `while` y `break`.”

3. **Mejora**

   > “Optimiza el código con `enumerate` y un resumen final en una línea. Mantén 30–40 líneas.”

### 👀 Demo rápida (IA\_DEMO=True)

```py
suma_pares = sum([n for n in range(1, 11) if n % 2 == 0])
print("Suma de pares 1..10:", suma_pares)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Pide a la IA con el Prompt Kit, pega el código en `mi_programa_ia()`.
* Ejecútalo desde el menú.
* Modifícalo con validaciones extra o resúmenes.

---

## SECCIÓN 9 · Autoevaluación final

### 🎯 Objetivos

* Integrar todos los tipos de bucles en un proyecto pequeño.

### 🛠️ Enunciado

1. Menú en bucle `while` con opciones:

   1. Añadir tarea
   2. Listar tareas (numeradas con `enumerate`)
   3. Eliminar por número
   4. Mostrar cuántas tareas tienen más de N caracteres
   5. Tabla de multiplicar de un número
   6. Salir

2. Usa `range`/`enumerate` donde corresponda. Evita bucles infinitos.

3. Opcional: usa `for-else` para avisar si no se encuentra un índice al eliminar.

4. Resumen final en 1 línea:
   `"Total tareas:<n> | Largas:<m> | Última acción:<texto>"`

### 📏 Rúbrica rápida

* **Correcto**: menú funcional, bucles aplicados.
* **Excelente**: mensajes claros, validaciones, código limpio.

---

## APÉNDICE A · Patrones útiles

* **Bucle con acumulador:**

```py
total = 0
for x in lista:
    total += x
```

* **While con contador de intentos:**

```py
intentos = 0
while intentos < 3:
    ...
    intentos += 1
```

* **For-else para búsqueda:**

```py
for x in lista:
    if x == objetivo:
        break
else:
    print("No encontrado")
```

---

## APÉNDICE B · Buenas prácticas

* Evita bucles infinitos (`while True`) sin condición de salida clara.
* Usa `enumerate` en lugar de contadores manuales.
* Prefiere **comprensiones** para construir listas simples.
* Añade comentarios **Better Comments** para guiar el aprendizaje.

---

## APÉNDICE C · Retos extra

1. **Primos**: genera los números primos del 1 al 50 usando bucles.
2. **Matriz identidad**: imprime una matriz identidad NxN con bucles anidados.
3. **Secuencia Fibonacci** con `while` hasta superar 1000.
4. **Filtrado con comprensiones**: de una lista de nombres, crea otra solo con los que tienen más de 5 letras.

---

## ✅ Qué has aprendido

* Usar `for` y `while` de forma segura.
* Trabajar con `range()` y `enumerate()`.
* Controlar el flujo con `break`, `continue`, `for-else`.
* Crear bucles anidados para tablas/cuadrículas.
* Usar comprensiones de listas para construir colecciones.
* Aplicar todo en un **mini-proyecto integrador** con menú.

---
