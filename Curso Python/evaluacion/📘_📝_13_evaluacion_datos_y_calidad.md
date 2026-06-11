# 📘 Evaluación 13 · Datos y Calidad

## Qué se pretende medir aquí

Esta evaluación no mide solo si el alumno sabe usar `sqlite3` o sabe crear una clase. Lo que mide de verdad es si puede ordenar un problema intermedio con una estructura razonable.

Bloque implicado:

- POO
- excepciones
- archivos JSON
- SQLite
- organización básica del código

## Qué debería demostrar el alumno

Un alumno que llega bien a este punto debería poder:

- modelar una entidad sencilla con claridad
- construir una clase coordinadora con sentido
- usar una excepción propia cuando el problema es de negocio
- exportar datos sin mezclar lógica y salida
- persistir información de forma simple y ordenada

## Por qué el gestor de tickets funciona bien

El escenario permite evaluar varias cosas a la vez:

- estado de objetos
- búsqueda por identificador
- cambio de estado
- resumen del sistema
- exportación
- persistencia

Además obliga a tomar decisiones de estructura, que es justo lo más interesante de este bloque.

## Estrategia de corrección recomendada

Orden útil:

1. revisar el modelado
2. revisar la clase central
3. comprobar búsqueda y excepción
4. comprobar el resumen
5. revisar JSON
6. revisar SQLite

## Rúbrica orientativa

- 2 puntos: modelo `Ticket` y estado básico
- 2 puntos: clase `GestorTickets` bien construida
- 2 puntos: excepción y cambio de estado correctos
- 2 puntos: exportación JSON válida
- 2 puntos: persistencia SQLite correcta y código claro

## Errores frecuentes

- meter demasiada lógica fuera de la clase central
- usar excepción sin necesidad o no usarla cuando toca
- confundir búsqueda con modificación
- exportar una estructura inconsistente
- guardar mal el booleano en SQLite

## Preguntas orales útiles

- ¿Qué responsabilidad tiene `GestorTickets`?
- ¿Por qué aquí sí compensa una clase?
- ¿Qué diferencia hay entre `buscar_ticket` y `resolver_ticket`?
- ¿Por qué tiene sentido una excepción propia en este caso?

## Señal de aprobado sólido

Hay aprobado fuerte cuando:

- la estructura es clara
- el estado cambia con coherencia
- la excepción está bien situada
- JSON y SQLite reflejan bien los datos
- y el alumno puede justificar la separación en capas

## Qué reforzar si falla

Si esta evaluación cuesta demasiado, suele faltar una de estas tres cosas:

- criterio de modelado
- comprensión del estado y sus cambios
- separación entre lógica y persistencia
