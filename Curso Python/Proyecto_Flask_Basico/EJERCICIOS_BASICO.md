# Ejercicios — Proyecto Flask Básico (nivel inicial)

Pequeños retos para mejorar el proyecto y practicar MVC en Flask.

## 1) Mensajes flash (validación)
- Cuando el título esté vacío, en vez de redirigir sin más, muestra un mensaje (flash) en la parte superior.
- Pista: `from flask import flash` y `get_flashed_messages()` en la plantilla.

## 2) Editar curso
- Añade una ruta `GET /editar/<id>` con un formulario para editar título y descripción.
- Añade la ruta `POST /actualizar/<id>` que guarde los cambios.
- Muestra un enlace [editar] junto a cada curso.

## 3) Ordenar por título
- Permite ordenar por título ascendente si se pasa `?orden=titulo` en `/`.
- Si no se pasa nada, ordena por id descendente (como ahora).

## 4) Búsqueda simple
- Añade un input en la parte superior para buscar por título.
- Pista: usa `request.args.get('q')` y un `filter` con `contains` o `ilike`.

## 5) Confirmación al borrar
- Añade confirmación JavaScript `onclick="return confirm('¿Seguro?')"` en el enlace borrar.

## 6) Semillas rápidas (opcional)
- Crea una función en `__init__.py` que inserte 3 cursos de ejemplo si la tabla está vacía.

## 7) CSS externo (opcional)
- Saca el estilo inline a `static/css/style.css` y enlázalo en `base.html`.

## 8) División por blueprints (opcional)
- Si te ves con fuerzas, separa el blueprint en `miniapp/blueprints/main.py` y ajústalo en `__init__.py`.

> Consejo: Después de cada ejercicio, arranca de nuevo y verifica manualmente que funciona.
