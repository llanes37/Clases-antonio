# 📘 Práctica Integrada 09_13 · Datos y Automatización

## Qué hace importante este bloque

Esta práctica se parece mucho más a una tarea de trabajo real que los ejercicios clásicos de sintaxis. El alumno recorre una cadena completa:

- prepara entorno
- genera o lee datos
- convierte tipos
- transforma información
- exporta resultados
- guarda registros en SQLite

## Qué debería demostrar el alumno

Un alumno que llega bien aquí debería poder:

- separar entrada, transformación y salida
- leer datos sin mezclar lectura con lógica de negocio
- construir funciones que luego se puedan probar
- usar SQLite como apoyo sin meter complejidad innecesaria
- entender una automatización como secuencia de pasos

## Relación con el temario

- Tema 09: archivos, rutas, CSV y JSON
- Tema 10: transformación y agregación de datos
- Tema 11: automatización por pasos
- Tema 12: persistencia ligera
- Tema 13: funciones más fáciles de testear

## Por qué la mini ETL está bien elegida

La práctica obliga a tocar varias capas sin dejar de ser manejable:

- hay origen de datos
- hay normalización de tipos
- hay resumen calculado
- hay exportación
- hay persistencia

## Estrategia recomendada de resolución

Orden útil:

1. preparar rutas y carpeta de trabajo
2. generar o leer el CSV
3. convertir tipos correctamente
4. crear la función de transformación
5. exportar a JSON
6. guardar en SQLite
7. consultar el resultado final

## Qué conviene observar al corregir

- si la transformación está separada de la lectura
- si convierte tipos antes de operar
- si el resumen final tiene sentido
- si JSON y SQLite reflejan los datos esperados
- si el alumno identifica qué parte probaría primero

## Errores frecuentes

- olvidar convertir `unidades` o `precio`
- mezclar lectura y cálculo en una sola función
- hacer depender la transformación de `input` o del sistema de archivos
- exportar sin revisar la estructura final
- guardar en SQLite sin preparar antes la tabla

## Buenas preguntas de repaso

- ¿Qué parte del flujo es extracción y cuál es transformación?
- ¿Qué función sería la primera candidata para `pytest`?
- ¿Qué ocurriría si el CSV trae datos corruptos?
- ¿Por qué conviene separar JSON y SQLite en funciones distintas?

## Señal de que el bloque está consolidado

La práctica ha cumplido bien su papel cuando el alumno:

- piensa en flujo de datos y no solo en líneas sueltas
- entiende mejor la separación de responsabilidades
- identifica funciones más puras
- y empieza a justificar por qué un diseño es más mantenible

## Buen uso del laboratorio IA

Buenas ampliaciones:

- filtro por categoría
- validación de filas corruptas
- ranking de productos
- tests con `pytest`

Malas ampliaciones:

- meter Flask dentro de esta práctica
- convertirla en una API
- complicar demasiado la base de datos
