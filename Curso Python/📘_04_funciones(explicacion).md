# 🐍 Clase 4 de Python — Funciones (`def`, `return`, parámetros, \*args/\*\*kwargs, scope, docstrings) + IA

**Autor:** Joaquín Rodríguez — *Guía didáctica para principiantes*
**Objetivo global:** Aprender a crear y usar funciones en Python: definición con `def`, parámetros, valores de retorno, argumentos variables, alcance de variables, docstrings, funciones como datos, y cerrar con un laboratorio de IA + autoevaluación final.

---

## 🧭 Cómo usar este material

1. Ejecuta `04_funciones.py` y usa el menú (opciones **1–10**).
2. Lee la teoría, revisa las demos, completa las zonas **TODO**.
3. Finaliza con la **Autoevaluación** para consolidar todo.

> 💡 **Tip docente:** Recuérdales que las funciones son “bloques de código reutilizables” y que usar buenos nombres + docstrings es clave para proyectos reales.

---

## 🧩 Mapa del temario (menú del programa)

1. `def` y `return` (básico)
2. Parámetros y retorno múltiple (unpacking)
3. Argumentos por defecto y keyword args
4. `*args` y `**kwargs` (parámetros variables)
5. Ámbito (scope) y buenas prácticas
6. Docstrings y type hints
7. Funciones como datos (lambda, key) \[opcional]
8. Laboratorio IA (mini-librería de utilidades)
9. Autoevaluación final
10. Ejecutar TODO (1→9)

---

## SECCIÓN 1 · `def` y `return` (básico)

### 🎯 Objetivos

* Declarar funciones con `def`.
* Usar `return` para devolver valores.

### 🧠 Teoría

```py
def nombre_funcion(par1, par2):
    <bloque>
    return valor  # opcional
```

* Si no hay `return`, devuelve `None`.

### 👀 Demo guiada

```py
def saludar(nombre: str) -> str:
    return f"Hola, {nombre} 👋"

def suma(a: float, b: float) -> float:
    return a + b

print(saludar("Ana"))
print("2 + 3 =", suma(2, 3))
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Define `area_rect(base, altura)` que devuelva `base*altura`.
* Pide/captura base y altura y muestra el área con 2 decimales.

---

## SECCIÓN 2 · Parámetros y retorno múltiple (unpacking)

### 🎯 Objetivos

* Retornar múltiples valores en una tupla.
* Desempaquetar en variables.

### 👀 Demo guiada

```py
def estadisticas(nums):
    L = list(nums)
    return min(L), max(L), sum(L)/len(L)

minimo, maximo, media = estadisticas([5, 7, 9, 2, 10])
print(minimo, maximo, media)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Función `resumen_notas(lista) -> (aprobados, suspensos, media)` y prueba con `[4, 6, 8, 3, 9]`.

---

## SECCIÓN 3 · Argumentos por defecto y keyword args

### 🎯 Objetivos

* Definir valores por defecto.
* Llamar funciones con `nombre=valor` para mayor claridad.

### 👀 Demo guiada

```py
def crear_usuario(nombre: str, rol: str="invitado", activo: bool=True):
    return {"nombre": nombre, "rol": rol, "activo": activo}

print(crear_usuario("Lucía"))
print(crear_usuario(nombre="Ana", rol="admin", activo=False))
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Implementa `precio_final(base, iva=21, descuento=0)` → total con IVA y menos descuento.
* Prueba: `precio_final(100)`, `precio_final(100, iva=10, descuento=5)`.

---

## SECCIÓN 4 · `*args` y `**kwargs`

### 🎯 Objetivos

* Aceptar número variable de argumentos.
* Diferenciar entre `*args` (tupla) y `**kwargs` (diccionario).

### 👀 Demo guiada

```py
def suma_todo(*nums):
    return sum(nums)

print(suma_todo(1,2,3,4))


def describir(**datos):
    return ", ".join(f"{k}={v}" for k,v in datos.items())

print(describir(nombre="Alicia", edad=20))
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Crea `logger(*mensajes, nivel="INFO")` que imprima `[NIVEL] msg` para cada mensaje.
* Ejemplo: `logger("Inicio", "Cargando", nivel="DEBUG")`.

---

## SECCIÓN 5 · Ámbito (scope) y buenas prácticas

### 🎯 Objetivos

* Entender variables locales y evitar abusar de `global`.
* Devolver nuevos valores en lugar de modificar globales.

### 👀 Demo guiada

```py
def incrementar(c):
    return c + 1

c = 0
for _ in range(3):
    c = incrementar(c)
print("Contador:", c)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Función `agregar_saldo(saldo, cantidad)` que devuelva nuevo saldo.
* Simula varias operaciones y muestra el saldo final.

---

## SECCIÓN 6 · Docstrings y type hints

### 🎯 Objetivos

* Documentar funciones con **docstrings**.
* Usar **type hints** para mayor claridad.

### 👀 Demo guiada

```py
def area_circulo(r: float) -> float:
    """Calcula el área de un círculo
    Parámetros:
      r (float): radio
    Retorna:
      float: área aproximada
    """
    return 3.14159 * r * r

print(area_circulo(2))
print(area_circulo.__doc__)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Escribe `precio_con_descuento(precio: float, descuento: float=10) -> float` con docstring.
* Imprime la docstring para comprobar.

---

## SECCIÓN 7 · Funciones como datos (lambda, key) \[opcional]

### 🎯 Objetivos

* Usar funciones como argumentos.
* Practicar con `lambda` para operaciones simples.

### 👀 Demo guiada

```py
frutas = ["kiwi", "manzana", "plátano", "uva"]
ordenadas = sorted(frutas, key=lambda s: len(s))
print(ordenadas)
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Convierte lista `palabras = ["hola","adios","python"]` a mayúsculas con `map(lambda s: s.upper(), palabras)`.

---

## SECCIÓN 8 · Laboratorio IA (mini-librería)

### 🎯 Objetivos

* Aprender a **pedir a la IA** mini-librerías con varias funciones.
* Integrar código generado y mejorarlo.

### 🧰 Prompt Kit

1. **Generación**

   > “Eres profesor de Python. Genera una mini-librería (30–45 líneas) con:
   >
   > * 4 funciones: `calcular_total(carrito, iva=21, descuento=0)`, `normalizar_texto(s)`, `filtrar_mayores(lista, umbral)`, `formatear_ticket(lineas)`.
   >   Incluye docstrings y type hints. Demostración mínima al final. Devuelve SOLO código Python.”

2. **Alternativo**

   > “Crea utilidades para **agenda de tareas**: `add_tarea(lista,texto)`, `remove_tarea(lista,idx)`, `listar(lista)`, `resumen(lista)` con demo pequeña. SOLO código Python.”

3. **Mejora**

   > “Mejora el código con \*args/\*\*kwargs en alguna función y añade 2 validaciones simples. Manténlo <45 líneas.”

### 👀 Demo opcional

```py
def total_demo(carrito, iva=21):
    return round(sum(carrito) * (1 + iva/100), 2)

print(total_demo([10, 5.5, 3]))
```

### 🛠️ ZONA DEL ALUMNO · TODO

* Pide a la IA un código con el Prompt Kit y pégalo en `mi_libreria()`.
* Ejecútalo y mejora con validaciones o extras.

---

## SECCIÓN 9 · Autoevaluación final

### 🎯 Objetivos

* Integrar todas las técnicas de funciones en un proyecto.

### 🛠️ Enunciado

Implementa y prueba:

1. `add_item(carrito, nombre, precio, unidades=1) -> list`
2. `total_carrito(carrito, iva=21, descuento=0) -> float`
3. `resumen_carrito(carrito) -> (num_items, unidades_totales, total_sin_iva)`
4. `crear_perfil(nombre, rol="invitado", **extra) -> dict`
5. `aplicar_bono(total, *bonos) -> float` (cada bono es un % de descuento)

### 📋 Requisitos

* Usa docstrings y type hints en al menos 2 funciones.
* Usa \*args/\*\*kwargs en al menos una.
* Evita globales, devuelve valores nuevos.
* Salida final estilo dashboard:
  `"Items:<n> | Unidades:<u> | Total:<€> | Perfil:<rol> | Bonos:<aplicados>"`

### 📏 Rúbrica

* **Correcto**: funciones bien definidas y probadas.
* **Excelente**: validaciones, docstrings claros, resultados bien formateados.

---

## APÉNDICE A · Patrones útiles

* **Función con retorno múltiple:**

```py
def min_max_media(L):
    return min(L), max(L), sum(L)/len(L)
```

* \**Uso de *args:**

```py
def media(*nums):
    return sum(nums)/len(nums)
```

* \*\*Uso de **kwargs:**

```py
def config(**opciones):
    return opciones
```

---

## APÉNDICE B · Buenas prácticas

* Nombres claros y descriptivos.
* Añade docstrings para funciones reutilizables.
* Evita `global`, devuelve siempre valores nuevos.
* Usa type hints para claridad en proyectos grandes.

---

## APÉNDICE C · Retos extra

1. Función `es_primo(n)` con docstring y type hints.
2. `contar_palabras(texto)` que devuelva diccionario {palabra: frecuencia}.
3. `apply_funcs(lista, funcs)` que aplique lista de funciones a cada elemento.
4. `ordenar_dicc(dic, key_func)` para ordenar por clave de función.

---

## ✅ Qué has aprendido

* Definir funciones con `def` y `return`.
* Usar parámetros, valores por defecto y keyword args.
* Manejar `*args` y `**kwargs`.
* Comprender el scope y buenas prácticas.
* Documentar funciones con docstrings y type hints.
* Usar funciones como datos (`lambda`, `key`).
* Integrar todo en un mini-proyecto con autoevaluación.

---
