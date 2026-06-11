# 📘 Evaluación 16 · Web y APIs

## Qué pretende medir esta evaluación

Esta evaluación cierra el bloque web básico del curso. No busca una aplicación completa, sino comprobar que el alumno entiende el contrato mínimo de una API bien planteada.

Bloque implicado:

- Flask
- rutas JSON
- validación de peticiones
- códigos HTTP
- consumo de respuestas

## Qué debería demostrar el alumno

Un alumno que domina este tramo debería poder:

- exponer datos por una ruta JSON
- validar entradas antes de modificar estado
- responder con códigos HTTP coherentes
- diferenciar autenticación, validación y negocio
- usar un cliente de prueba para verificar respuestas

## Por qué la API de cursos e inscripciones está bien elegida

El escenario es pequeño, pero completo:

- hay datos a listar
- hay una operación que modifica estado
- hay autenticación básica
- hay varios casos de error

Con eso ya se puede evaluar comprensión web real sin necesidad de un proyecto grande.

## Estrategia de corrección recomendada

Orden útil:

1. comprobar `/health`
2. comprobar el listado de cursos
3. revisar validación de API key
4. revisar validación del payload
5. revisar creación de inscripción
6. comprobar el consumo desde cliente

## Rúbrica orientativa

- 1 punto: healthcheck correcto
- 2 puntos: listado de cursos correcto
- 2 puntos: autenticación y `401`
- 2 puntos: validación del payload y `400`
- 2 puntos: control de curso inexistente o sin plazas
- 1 punto: claridad general y prueba con cliente

## Errores frecuentes

- responder siempre `200`
- no validar `curso_id`
- no comprobar plazas disponibles
- mezclar autenticación, validación y lógica de negocio
- no revisar `status_code` al consumir la API

## Preguntas orales útiles

- ¿Qué diferencia hay entre `400`, `401`, `404` y `409`?
- ¿Qué parte de esta lógica pertenece al servidor?
- ¿Qué parte corresponde al cliente de prueba?
- ¿Por qué conviene validar antes de descontar plazas?

## Señal de aprobado sólido

Hay aprobado fuerte cuando:

- las rutas responden con coherencia
- las validaciones están en orden correcto
- el estado cambia solo cuando debe
- y el alumno sabe leer tanto la petición como la respuesta

## Qué reforzar si falla

Si esta evaluación sale floja, normalmente conviene volver a:

- diseño de rutas pequeñas
- validación temprana
- significado de códigos HTTP
- separación entre servidor y cliente
