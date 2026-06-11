# Guía rápida: Better Comments en este proyecto

Este repo usa el estilo “Better Comments” para resaltar ideas clave en los comentarios, útil para aprender más rápido.

- # TODO: tareas pendientes o mejoras sugeridas
- # ! Importante/Advertencia: puntos críticos a vigilar
- # ? Pregunta/Explicación: aclaraciones didácticas
- # * Idea clave/Nota positiva: buenas prácticas o resúmenes

Ejemplos en el código:
- `app/__init__.py`: explica el patrón factory y `instance_relative_config`.
- `app/errors.py`: cómo decidimos si responder JSON o HTML.
- `app/services/utils.py`: funciones puras con map/filter/reduce y tipos.
- `app/blueprints/api.py`: validación de payload y control de transacciones.

Consejos para leer el código:
- Busca `# !` para ver advertencias que no debes ignorar.
- Lee `# ?` para entender por qué se hace algo de una manera.
- Revisa `# TODO:` para ideas de práctica o ampliación.
