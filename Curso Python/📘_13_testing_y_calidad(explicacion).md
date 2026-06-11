# 📘 Clase 13 de Python — Testing y Calidad (`assert`, `pytest`, casos borde, debugging)

## 🧭 Cómo usar este material

Esta unidad sustituye al bloque antiguo de testing. El objetivo ya no es solo “ver `unittest` y `pdb`”, sino aprender una forma más profesional de validar código:

- pensar casos de prueba antes de programar,
- escribir funciones fáciles de probar,
- usar `assert` para comprobaciones rápidas,
- y trabajar con **`pytest`** como herramienta principal del curso.

---

## 🎯 Qué aprenderás exactamente

Al terminar esta unidad deberías poder:

- distinguir entre caso normal, caso borde y caso de error,
- escribir pruebas sencillas con `pytest`,
- comprobar excepciones con `pytest.raises`,
- detectar cuándo una función es difícil de testear,
- y depurar fallos de forma ordenada sin llenar el código de `print()` innecesarios.

---

## 🧩 Mapa del temario

1. Casos de prueba y pensamiento de calidad
2. `assert` como verificación rápida
3. `pytest` básico
4. Casos borde y errores esperados
5. Debugging útil
6. Laboratorio IA
7. Autoevaluación final

---

## SECCIÓN 1 · Casos de prueba y pensamiento de calidad

### 🎯 Objetivos

- Entender que testear no es “probar una vez”.
- Separar:
  - caso normal,
  - caso borde,
  - caso erróneo.

### 🧠 Teoría en claro

Un buen test no pregunta solo “¿el programa corre?”. Pregunta:

- ¿da el resultado correcto?
- ¿qué pasa si entra un valor raro?
- ¿qué pasa si la entrada está vacía?
- ¿qué pasa si el dato debería ser inválido?

Ejemplo rápido para una función `media_segura(lista)`:

- Caso normal: `[10, 20, 30]`
- Caso borde: `[5]`
- Caso borde: `[]`
- Caso erróneo: datos no numéricos si tu función no los soporta

### 👀 Demo guiada

Antes de escribir código, anota 4-5 casos en una lista. Ese hábito mejora más que memorizar teoría.

### 🛠️ ZONA DEL ALUMNO · TODO

- Diseña 5 casos para `es_email_valido(email)`.
- Marca cuáles son normales, cuáles borde y cuáles errores.

---

## SECCIÓN 2 · `assert` como verificación rápida

### 🎯 Objetivos

- Usar `assert` para comprobar comportamiento simple.
- Entender sus límites.

### 🧠 Teoría en claro

`assert` sirve para verificaciones rápidas:

```python
assert aplicar_descuento(100, 20) == 80.0
assert media_segura([]) is None
```

Es útil en clase, en demos y en funciones pequeñas. Pero para un proyecto real conviene pasar a `pytest`, porque:

- organiza mejor las pruebas,
- da informes más claros,
- permite agrupar muchos tests,
- y maneja muy bien excepciones, fixtures y parametrización.

### 👀 Demo guiada

- prueba una función pura,
- prueba una lista vacía,
- prueba una excepción esperada.

### 🛠️ ZONA DEL ALUMNO · TODO

- Escribe 4 `assert` útiles para una función de precios.

---

## SECCIÓN 3 · `pytest` básico

### 🎯 Objetivos

- Entender la estructura mínima de un test con `pytest`.
- Aprender el comando de ejecución más habitual.

### 🧠 Teoría en claro

Un test sencillo con `pytest` suele tener esta forma:

```python
def test_aplicar_descuento_basico():
    assert aplicar_descuento(200, 25) == 150.0
```

Para lanzar pruebas:

```bash
pytest -q
```

Para comprobar errores esperados:

```python
import pytest

def test_descuento_invalido():
    with pytest.raises(ValueError):
        aplicar_descuento(50, 200)
```

### 👀 Demo guiada

Piensa siempre en tres grupos:

- una prueba feliz,
- una prueba borde,
- una prueba de error.

### 🛠️ ZONA DEL ALUMNO · TODO

- Crea un archivo `test_13_testing_y_calidad.py`.
- Escribe al menos:
  - 2 tests normales,
  - 1 caso borde,
  - 1 test con `pytest.raises`.

---

## SECCIÓN 4 · Casos borde y errores esperados

### 🎯 Objetivos

- Diferenciar entrada “rara pero válida” de entrada directamente inválida.

### 🧠 Teoría en claro

No todos los fallos son iguales:

- `[]` puede ser un caso borde válido.
- `None` puede ser inválido según la función.
- `-10` puede ser correcto o error, según el dominio.

La calidad mejora cuando la función deja claras sus reglas:

- qué acepta,
- qué devuelve,
- y cuándo lanza excepción.

### 🛠️ ZONA DEL ALUMNO · TODO

- Revisa una función tuya antigua del curso.
- Añade:
  - 2 casos borde,
  - 1 caso de error,
  - y la decisión de si debe devolver algo o lanzar excepción.

---

## SECCIÓN 5 · Debugging útil

### 🎯 Objetivos

- Depurar con más criterio.
- Evitar el abuso de `print()`.

### 🧠 Teoría en claro

Orden recomendado:

1. reproducir el fallo,
2. reducir el caso al mínimo,
3. inspeccionar variables clave,
4. usar `breakpoint()` si hace falta,
5. arreglar,
6. dejar un test que evite la regresión.

La última parte es la importante: si arreglas un bug pero no dejas prueba, el bug puede volver.

### 🛠️ ZONA DEL ALUMNO · TODO

- Coge un ejercicio viejo.
- Provoca un error controlado.
- Localízalo con:
  - un `print()` temporal,
  - o `breakpoint()`.
- Luego elimina el ruido y deja un test.

---

## SECCIÓN 6 · Laboratorio IA

### 🎯 Objetivos

- Usar IA para generar casos de prueba mejores, no para pensar menos.

### 🧰 Prompt Kit recomendado

```text
Actua como revisor de tests en Python.
Te doy una funcion y quiero:
1. 5 casos de prueba utiles
2. 2 casos borde
3. 1 ejemplo con pytest.raises si aplica
4. una breve explicacion de por que esos tests importan
No cambies la firma de la funcion.
```

### Regla importante

No copies pruebas a ciegas. Ejecuta y verifica siempre.

---

## AUTOEVALUACIÓN FINAL · Mini módulo con pruebas

### 🎯 Objetivos

- Combinar lógica, validación y tests.

### 🛠️ Enunciado

Crea un pequeño módulo con:

- `normalizar_usuario(nombre, email)`
- `precio_con_iva(base, iva)`
- una clase `Ticket` con estado abierto/cerrado

Y acompáñalo con pruebas que cubran:

- comportamiento normal,
- casos borde,
- y errores esperados.

### 📏 Rúbrica rápida

- Correctitud: 50%
- Cobertura de casos útiles: 25%
- Claridad de nombres: 15%
- Orden y limpieza: 10%

---

## APÉNDICE A · Qué cambia respecto al bloque antiguo

- `pytest` pasa a ser la referencia principal.
- `unittest` queda como cultura general, no como centro del tema.
- debugging y testing se conectan entre sí.
- se insiste más en calidad real que en ejemplos sueltos.

---

## ✅ Qué has aprendido

- A pensar pruebas con intención.
- A escribir `assert` útiles.
- A empezar con `pytest`.
- A comprobar excepciones.
- A dejar tests después de corregir bugs.
