# 📘 Guía Maestra del Curso de Python

**Autor:** Joaquín Rodríguez

Esta guía fija la estructura oficial del curso. Su función es simple: que el camino principal se vea claro y que el material extra no compita con él.

## 1. Identidad del curso

Este curso mantiene una idea muy concreta:

- explicación práctica en directo
- scripts con menú para enseñar paso a paso
- laboratorio IA para ampliar sin romper el nivel
- versión `(alumno)` para practicar con autonomía

Eso no cambia. Lo que sí se ordena aquí es **cómo se reparte el material**.

## 2. Cómo se organiza la carpeta

La carpeta del curso se divide en tres capas reales:

### Raíz = troncal

La raíz contiene el camino principal del curso.

Aquí están las unidades numeradas, la teoría principal y los proyectos base. Cuando alguien abre la carpeta, debe entender de un vistazo cuál es la ruta oficial.

### `practicas/`

`practicas/` no sustituye el temario. Sirve para repasar bloques enteros con ejercicios más realistas.

Bloques actuales:

- `practicas/🧪_01_05_fundamentos_aplicados.*`
- `practicas/🧪_06_08_poo_y_calidad.*`
- `practicas/🧪_09_13_datos_y_automatizacion.*`
- `practicas/🧪_14_16_web_y_apis_aplicadas.*`

### `evaluacion/`

`evaluacion/` tampoco enseña contenido nuevo. Sirve para comprobar si un bloque ya se sostiene sin demasiado apoyo.

Bloques actuales:

- `evaluacion/📝_10_evaluacion_fundamentos.*`
- `evaluacion/📝_13_evaluacion_datos_y_calidad.*`
- `evaluacion/📝_16_evaluacion_web_y_apis.*`

## 3. Regla visual del curso

La convención oficial queda así:

- `📘_` = documentación didáctica
- `🧪_` = práctica integrada
- `📝_` = evaluación
- `(alumno)` = versión para resolver

Esto permite distinguir rápido:

- qué es teoría
- qué es práctica
- qué es evaluación
- y qué archivo debe tocar el alumno

## 4. Patrón recomendado por unidad

Una unidad troncal ideal sigue esta estructura:

- `NN_tema.py`
- `NN_tema(alumno).py`
- `📘_NN_tema(explicacion).md` o `📘_NN_tema.md`

Y dentro del contenido conviene mantener siempre esta secuencia:

1. objetivo
2. explicación breve
3. menú o demo guiada
4. práctica
5. laboratorio IA
6. autoevaluación o reto

## 5. Ruta oficial del curso

La ruta principal recomendada es esta:

### Base de Python

1. `00_setup_entorno_y_buenas_practicas.*`
2. `01_variable.*`
3. `01_cadenas_operadores.*`
4. `02_condicionales.*`
5. `03_bucles.*`
6. `04_funciones.*`
7. `05_listas_diccionarios_bucles_anidados.*`

### Python estructurado

8. `06_Programación Orientada a Objetos.*`
9. `07_Manejo de Excepciones.*`
10. `08_modulos y librerias.*`
11. `09_EntradaSalida de Archivos.*`
12. `10_Programación Funcional.*`
13. `11_automatizacion_tareas_sistema.*`
14. `12_Introducción a Bases de Datos.*`
15. `12_BBDD con SqlAlchemy.*`
16. `13_testing_y_calidad.*`

### Python web

17. `14_flask_tutorial.*`
18. `14_flask_parte2_sesiones_y_seguridad.*`
19. `15_django_tutorial.*`
20. `16_consumo_apis_http.*`
21. `17_gradle_desde_cero.*` `(opcional)`

### Proyectos

- `Proyecto_Flask_Basico/`
- `Proyecto_Flask_Auth_Migraciones/`
- `Proyecto_Flask_Final/`
- `django_pf/`

## 6. Cómo se conectan troncal, prácticas y evaluación

La lógica correcta del curso es esta:

1. primero se estudia el bloque troncal
2. después se hace la práctica integrada del bloque
3. por último se usa la evaluación como cierre

Ejemplo:

- el alumno estudia `01` a `05`
- luego hace `practicas/🧪_01_05_fundamentos_aplicados.*`
- y finalmente puede pasar a `evaluacion/📝_10_evaluacion_fundamentos.*`

Este patrón evita dos errores comunes:

- convertir la práctica en examen
- o usar la evaluación antes de que el bloque esté consolidado

## 7. Qué queda fuera del tronco

No todo el material debe vivir en la raíz.

Quedan fuera del tronco:

- prácticas integradas por bloques
- evaluaciones formales
- materiales auxiliares que no forman parte del recorrido principal

La regla es sencilla:

si un archivo no enseña la secuencia oficial del tema, no debería competir visualmente con la ruta principal.

## 8. Cambio importante ya aplicado

La antigua unidad de testing salió del tronco y se sustituyó por:

- `13_testing_y_calidad.py`
- `13_testing_y_calidad(alumno).py`
- `📘_13_testing_y_calidad(explicacion).md`

Esto era importante porque el curso ya tenía proyectos con más nivel que aquella unidad. Ahora el bloque 13 queda mucho más alineado con el resto.

## 9. Cómo usar el curso en clase

Secuencia recomendada:

### Antes de la sesión

- leer el `📘_*.md`
- decidir qué partes del menú se van a enseñar
- elegir si habrá práctica o solo demo

### Durante la sesión

- usar el script del profesor
- avanzar por bloques con el menú
- adaptar `RUN_INTERACTIVE`, `PAUSE` e `IA_DEMO` al ritmo del grupo

### Después de la sesión

- entregar el archivo `(alumno)`
- mandar la lectura del `📘_*.md`
- y, si toca, enlazar con `practicas/` o `evaluacion/`

## 10. Qué debe transmitir esta estructura

El curso queda bien cuando:

- la raíz enseña la ruta principal
- `practicas/` refuerza sin mezclar
- `evaluacion/` mide sin confundir
- y la documentación se reconoce de inmediato

Esa es la estructura oficial del curso a partir de ahora.
