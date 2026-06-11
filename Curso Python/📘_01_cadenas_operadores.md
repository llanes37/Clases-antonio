# 📘 Clase 1.2 — Cadenas de Caracteres y Operadores

**Autor:** Joaquín Rodríguez

Esta clase cubre dos temas fundamentales que van juntos: **manipulación de cadenas de caracteres** y **operadores** (aritméticos, comparación, lógicos y de asignación). Los operadores se usan constantemente con strings y números, así que conviene aprenderlos juntos.

---

## 🧩 Estructura por secciones

El menú del programa ofrece:  
**1) Cadenas** · **2) Operadores aritméticos** · **3) Comparación** · **4) Lógicos y asignación** · **5) Autoevaluación** · **6) Ejecutar todo**.

---

## SECCIÓN 1 · Cadenas de caracteres

Las cadenas de caracteres son secuencias de caracteres que representan texto. Son muy útiles en Python.

### 🎯 Objetivos
- Crear y manipular cadenas.
- Usar **indexación y slicing** para acceder a partes de una cadena.
- Aplicar **métodos de cadenas** (`.upper()`, `.lower()`, `.split()`, `.replace()`, etc.).

### 🧠 Teoría en claro

**Definir cadenas:**
```python
"¡Hola, Mundo!"
'¡Hola, Mundo!'
"45678"
"mi-correo@email.com"
```

**Comillas dentro de cadenas:**
```python
print("Mi asignatura favorita es 'Fundamentos de programación'")
print('Mi asignatura favorita es "Fundamentos de programación"')
```

**Indexación (acceder a caracteres):**
```python
# Cadena:    H o l a 
# Índices:   0 1 2 3
cadena = "Hola"
print(cadena[0])  # H
print(cadena[1])  # o
print(cadena[-1]) # a (último carácter)
```

**Slicing (rebanado de cadenas):**
```python
# variable_con_cadena[inicio:fin:paso]
cadena = "cadenaDeTexto"
print(cadena[2:8])      # deaDeT
print(cadena[0:4])      # cade
print(cadena[0:12:2])   # caeeeto (cada 2 caracteres)
```

**Métodos útiles de cadenas:**
```python
cadena = 'cadenaDeTexto'

# Capitalize: primer carácter mayúscula, resto minúsculas
print(cadena.capitalize())  # Cadenatexto

# Count: contar ocurrencias
print(cadena.count('e'))    # 2

# Find: encontrar posición (índice)
print(cadena.find('e'))     # 4

# Lower: todo minúsculas
print(cadena.lower())       # cadenatexto

# Upper: todo mayúsculas
print(cadena.upper())       # CADENATEXTO

# Replace: reemplazar
print(cadena.replace("e", "i"))  # cadinaDitixto

# Split: dividir en lista
frase = 'Esto es una cadena de texto'
palabras = frase.split(" ")  # ['Esto', 'es', 'una', 'cadena', 'de', 'texto']
print(len(palabras))  # 6 (número de palabras)

# Join: unir lista en cadena
lista = ['Python', 'es', 'genial']
resultado = " ".join(lista)  # 'Python es genial'
```

### 👀 Demo guiada
```python
# Ejemplo: análisis de texto
texto = "Python es increíble"
print(f"Texto: {texto}")
print(f"Mayúsculas: {texto.upper()}")
print(f"Posición de 'increíble': {texto.find('increíble')}")
print(f"Palabras: {texto.split()}")
print(f"Total palabras: {len(texto.split())}")
```

### 🛠️ Práctica (TODO)
1) Crea una cadena con tu nombre, usa indexación para mostrar el primer carácter.
2) Divide una frase en palabras con `.split()` y cuenta cuántas hay.
3) Reemplaza una palabra en una cadena con `.replace()`.
4) Convierte a mayúsculas y minúsculas.

### 🧩 Errores típicos
- **IndexError:** intentar acceder a un índice que no existe.
- **AttributeError:** usar `.metodo()` que no existe en cadenas.

---

## SECCIÓN 2 · Operadores aritméticos

Los operadores aritméticos permiten realizar cálculos matemáticos.

### 🎯 Objetivos
- Usar operadores: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Entender la diferencia entre `/` (división con decimales) y `//` (división entera).

### 🧠 Teoría en claro

```python
# Suma
print(2 + 2)        # 4

# Resta
print(10 - 2 - 5)   # 3

# Multiplicación
print(8 * 3)        # 24

# División (siempre devuelve float)
print(30 / 6)       # 5.0

# División entera (devuelve int)
print(21 // 5)      # 4

# Módulo (resto de la división)
print(21 % 5)       # 1

# Potencia
print(2 ** 3)       # 8
```

### 👀 Demo guiada
```python
# Ejemplo: cálculos prácticos
precio = 15.99
cantidad = 3
total = precio * cantidad
print(f"Precio unitario: ${precio}")
print(f"Cantidad: {cantidad}")
print(f"Total: ${total:.2f}")
print(f"IVA (21%): ${total * 0.21:.2f}")
```

### 🛠️ Práctica (TODO)
1) Calcula el área de un rectángulo (largo × ancho).
2) Calcula el resto de dividir dos números.
3) Calcula el resultado de una potencia.
4) Realiza una operación con 3 números diferentes.

---

## SECCIÓN 3 · Operadores de comparación

Los operadores de comparación crean expresiones booleanas (True/False).

### 🎯 Objetivos
- Usar: `>`, `<`, `>=`, `<=`, `==`, `!=`.
- Comparar números y cadenas.
- Encadenar comparaciones.

### 🧠 Teoría en claro

```python
# Mayor que
print(5 > 6)            # False

# Menor que
print(5 < 6)            # True

# Mayor o igual que
print(8 >= 6)           # True

# Menor o igual que
print(5 <= 3)           # False

# Igual a
print(5 == 5)           # True

# No igual a (distinto)
print(5 != 5)           # False

# Comparar cadenas (orden alfabético)
print("Antonio" > "Zacarías")  # False
print("Pepe" < "Pepa")         # False

# Encadenar comparaciones
a = 1
b = 2
c = 3
print(a < b < c)        # True (1<2 AND 2<3)
```

### 👀 Demo guiada
```python
# Ejemplo: comprobación de edad
edad = 20
print(f"¿Tienes 20 años? {edad == 20}")
print(f"¿Eres mayor de 18? {edad >= 18}")
print(f"¿Eres menor de 30? {edad < 30}")
print(f"¿Estás entre 18 y 65? {18 <= edad <= 65}")
```

### 🛠️ Práctica (TODO)
1) Compara dos números y muestra si son iguales.
2) Verifica si un número está entre 10 y 100.
3) Compara dos cadenas alfabéticamente.
4) Encadena 3 comparaciones.

---

## SECCIÓN 4 · Operadores lógicos y asignación

Los operadores lógicos (`and`, `or`, `not`) combinan expresiones. Los de asignación (`+=`, `-=`, etc.) actualizan variables.

### 🎯 Objetivos
- Usar operadores lógicos: `and`, `or`, `not`.
- Usar operadores de asignación: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.

### 🧠 Teoría en claro

**Operadores lógicos:**
```python
# AND: ambas condiciones deben ser True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: al menos una debe ser True
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# NOT: invierte el resultado
print(not True)         # False
print(not False)        # True
```

**Operadores de asignación:**
```python
# Asignación básica
x = 6
print(x)                # 6

# Suma y asigna
x += 15                 # x = x + 15 = 21
print(x)                # 21

# Resta y asigna
x -= 2                  # x = x - 2 = 19
print(x)                # 19

# Multiplica y asigna
x *= 2                  # x = x * 2 = 38
print(x)                # 38

# Módulo y asigna
x %= 3                  # x = x % 3 = 2
print(x)                # 2

# División y asigna
x = 30
x /= 2                  # x = 15.0
print(x)                # 15.0

# División entera y asigna
x //= 2                 # x = 7.0
print(x)                # 7.0

# Potencia y asigna
x **= 2                 # x = 49.0
print(x)                # 49.0
```

### 👀 Demo guiada
```python
# Ejemplo: control de acceso
usuario_autenticado = True
es_admin = False
tiene_permiso = usuario_autenticado and not es_admin

print(f"¿Puede acceder? {tiene_permiso}")  # True

# Ejemplo: acumulador
contador = 0
contador += 1
contador += 1
print(f"Contador: {contador}")  # 2
```

### 🛠️ Práctica (TODO)
1) Usa `and` para verificar si dos condiciones son verdaderas.
2) Usa `or` para verificar si al menos una es verdadera.
3) Usa `not` para invertir un resultado.
4) Usa `+=` para acumular valores en una variable.

---

## 🏁 Autoevaluación final

### 🎯 Proyecto integrador: Analizador de texto

**Enunciado:**
Una persona normal lee 2 palabras por segundo. Un locutor de radio lee 30% más rápido. Crea un programa que:

1. Pida al usuario que inserte un texto.
2. Calcule el número de palabras.
3. Calcule el tiempo que tarda una persona normal en leerlo.
4. Muestre un aviso si tarda más de 30 segundos.
5. Muestre el tiempo que tarda un locutor.

**Salida esperada (ejemplo):**
```
Escribiste 14 palabras, y tardarías 7.0 segundos en leerlo.
El locutor de radio, lo leería en 4.9 segundos.
```

**Requisitos:**
- Usa `.split()` para contar palabras.
- Usa operadores aritméticos para calcular tiempos.
- Usa comparación (`>`) para el aviso.
- Usa f-strings con decimales (`:. 1f`).

### 🛠️ Tareas TODO:
1) Pide entrada de texto al usuario.
2) Divide en palabras y cuéntalas.
3) Calcula el tiempo a 2 palabras/seg.
4) Verifica si es mayor a 30 segundos.
5) Calcula el tiempo del locutor (30% más rápido).
6) Muestra todo formateado.

### 📏 Rúbrica
- **Correcto:** todas las partes funcionan, formato correcto.
- **Excelente:** maneja cadenas vacías, valida entrada, comentarios claros.

---

## 🔎 Tips finales

1. **Cadenas:** `.split()` es tu amigo para dividir texto.
2. **Operadores:** `/` da float, `//` da entero. Elige bien.
3. **Lógicos:** `and` es restrictivo, `or` es permisivo.
4. **Asignación:** `+=` es más legible que `x = x + 1`.

---

*Fin de la clase. Los temas 01_cadenas y 01_operadores están fusionados aquí.*
