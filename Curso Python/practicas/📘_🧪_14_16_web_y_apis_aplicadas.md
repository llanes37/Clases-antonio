# 📘 Práctica Integrada 14_16 · Web y APIs Aplicadas

## Qué se quiere afianzar con esta práctica

Este bloque no pretende enseñar todo Flask. Su objetivo es más concreto:

- entender qué es un endpoint
- recibir y devolver JSON con criterio
- validar una petición antes de modificar datos
- responder con códigos HTTP coherentes
- pensar como servidor y también como cliente

## Por qué este bloque importa

Muchos alumnos entienden las rutas cuando las ven en clase, pero no interiorizan todavía el contrato completo de una API:

- qué entra
- qué se valida
- qué se devuelve
- con qué código
- y cómo se consume esa respuesta

## Relación con el temario

- Tema 14: rutas y lógica web con Flask
- Tema 15: pensamiento de aplicación web estructurada
- Tema 16: consumo de APIs HTTP

## Flujo pedagógico del ejercicio

La práctica está construida para enseñar esta secuencia:

1. healthcheck
2. listado de productos
3. detalle de producto
4. creación de pedido
5. error de autenticación
6. consulta de pedidos creados

## Qué debería demostrar el alumno

Al terminar este bloque debería poder:

- distinguir entre ruta de lectura y ruta de cambio
- validar un payload JSON antes de tocar estado
- usar `200`, `201`, `400`, `401`, `404` y `409` con sentido
- leer un `status_code` y no solo el cuerpo JSON
- explicar qué parte de la lógica pertenece al servidor y cuál al cliente

## Qué mirar al corregir

- si cada ruta tiene una responsabilidad clara
- si el payload se valida de forma temprana
- si el stock se modifica solo cuando corresponde
- si los errores devuelven códigos coherentes
- si el cliente interpreta bien respuesta y error

## Errores frecuentes

- aceptar datos inválidos sin comprobarlos
- descontar stock antes de validar todo
- responder siempre `200`
- mezclar autenticación, validación y negocio
- ignorar el `status_code` al consumir la API

## Buenas preguntas de repaso

- ¿Qué debería devolver `/health` y por qué?
- ¿Cuándo corresponde usar `404` y cuándo `409`?
- ¿Qué parte de la lógica pertenece al servidor?
- ¿Qué debería hacer siempre el cliente después de recibir una respuesta?

## Señal de que el bloque está maduro

El bloque está bien trabajado cuando el alumno:

- entiende la historia completa de una petición
- valida antes de modificar estado
- usa códigos HTTP con criterio
- y puede razonar tanto desde el lado servidor como desde el lado cliente

## Buenas ampliaciones

Buenas ampliaciones para este punto:

- endpoint para actualizar stock
- filtros por nombre o precio mínimo
- separación de servidor y cliente en módulos
- tests con `pytest`

Malas ampliaciones:

- JWT real
- permisos complejos
- base de datos pesada
- convertir la práctica en un ecommerce completo

## Qué lugar ocupa dentro del curso

Es la mejor antesala para los proyectos Flask del curso porque remata la progresión de `practicas/` con mentalidad cliente-servidor real.
