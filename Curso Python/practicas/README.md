# Prácticas Integradas por Bloques

## Qué función cumple esta carpeta

`practicas/` existe para cubrir una transición muy concreta del curso:

- el temario enseña piezas aisladas
- el archivo `(alumno)` permite practicar una pieza concreta
- `practicas/` obliga a combinar varias piezas dentro de un problema más completo

Su valor no está en añadir “más ejercicios”. Su valor está en obligar al alumno a pensar en flujo, orden y criterio cuando ya no tiene el problema troceado por temas.

## Qué no es esta carpeta

`practicas/` no debe usarse como:

- sustituto del temario
- examen encubierto
- colección de ejercicios de relleno
- zona para meter temas nuevos que aún no se han explicado

Si una práctica introduce demasiadas ideas nuevas a la vez, deja de reforzar y empieza a confundir.

## Relación exacta con el resto del curso

La secuencia sana del curso es esta:

1. estudiar el bloque del temario
2. resolver la versión `(alumno)` del tema cuando corresponda
3. pasar a la práctica integrada del bloque
4. cerrar con evaluación solo cuando la práctica ya no necesita mucho apoyo

Esa progresión evita dos errores muy comunes:

- practicar demasiado pronto
- evaluar antes de que el bloque esté estable

## Cómo se recomienda usar cada práctica

Secuencia recomendada en clase o como tarea:

1. leer la guía `📘_...md` para entender el sentido del bloque
2. intentar la versión `(alumno)` sin abrir la resuelta
3. resolver primero la parte estructural del problema
4. revisar validaciones, casos borde y salida final
5. comparar con la versión profesor solo al final
6. cerrar con una mejora pequeña o con laboratorio IA

La práctica pierde bastante valor si el alumno abre la solución completa antes de intentar organizar su propio enfoque.

## Convención de nombres

- `🧪_` = práctica integrada por bloques
- `(alumno)` = versión para resolver
- `📘_` = guía didáctica del bloque

Ejemplo:

- `🧪_09_13_datos_y_automatizacion.py`
- `🧪_09_13_datos_y_automatizacion(alumno).py`
- `📘_🧪_09_13_datos_y_automatizacion.md`

## Qué debe tener una práctica buena

Una práctica de esta carpeta debería:

- reforzar un bloque coherente del temario
- usar un escenario entendible y reconocible
- tener un tamaño razonable para clase o tarea
- obligar a tomar decisiones, no solo a copiar
- permitir mejoras pequeñas al final
- tener versión resuelta, versión alumno y guía

Lo que conviene evitar:

- prácticas gigantes
- contextos demasiado artificiales
- complejidad metida por lucimiento
- cambios de alcance que rompan el nivel del bloque

## Bloques actuales

### `🧪_01_05_fundamentos_aplicados`

Refuerza la base del curso con un inventario en memoria y obliga a recorrer, buscar, validar y modificar estructuras simples.

### `🧪_06_08_poo_y_calidad`

Refuerza POO, excepciones y organización del código mediante una mini biblioteca con préstamos y devoluciones.

### `🧪_09_13_datos_y_automatizacion`

Refuerza archivos, transformación de datos, automatización, SQLite y diseño de funciones más fáciles de probar.

### `🧪_14_16_web_y_apis_aplicadas`

Refuerza Flask, JSON, validación, códigos HTTP y consumo de API con una mini aplicación cliente-servidor.

## Ruta recomendada dentro de la carpeta

Orden recomendado:

1. `🧪_01_05_fundamentos_aplicados`
2. `🧪_06_08_poo_y_calidad`
3. `🧪_09_13_datos_y_automatizacion`
4. `🧪_14_16_web_y_apis_aplicadas`

## Cómo detectar si una práctica ha cumplido su función

La práctica está bien aprovechada si el alumno:

- sabe explicar el flujo completo sin leer línea a línea
- identifica qué temas se están mezclando
- detecta errores razonables por su cuenta
- propone una mejora realista sin romper el nivel
- depende menos del patrón exacto del tema original

## Cómo corregirlas con criterio

Lo útil es revisar:

- si la estructura global tiene sentido
- si las validaciones están en el orden correcto
- si reutiliza funciones o repite lógica innecesariamente
- si la salida final es coherente
- si el alumno puede explicar lo que ha hecho

## Qué ampliaciones sí encajan

Buenas ampliaciones:

- filtros
- validaciones nuevas
- pequeñas estadísticas
- separación en más funciones
- pequeños tests

Malas ampliaciones:

- meter frameworks sin necesidad
- cambiar por completo el tipo de ejercicio
- inflar la práctica hasta volverla proyecto

## Cierre

Esta carpeta está bien diseñada cuando tiene pocas prácticas, pero bien escogidas, claramente alineadas con bloques del curso y capaces de servir como puente entre temario y evaluación.
