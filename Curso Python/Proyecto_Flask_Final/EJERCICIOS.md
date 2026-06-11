# Ejercicios propuestos — Proyecto Flask Final

Estos ejercicios refuerzan cada bloque del curso con tareas prácticas sobre este proyecto.

## 1) Python básico
- Crea una función en `app/services/utils.py` que cuente cuántos cursos tienen más de N palabras en la descripción. Añade tests.
- Implementa una versión segura de conversión a entero que devuelva 0 si falla.

## 2) Condicionales y bucles
- Modifica `templates/cursos.html` para resaltar (con CSS) los cursos no publicados.
- En el índice, muestra un mensaje si hay más de 5 cursos.

## 3) Funciones
- Añade una función `slugify` en `utils.py` y úsala para crear un campo `slug` opcional en `Curso`.

## 4) POO y SQLAlchemy
- Añade al modelo `Curso` un método `publicar()` que marque el curso como publicado y deje traza con fecha.
- Crea un modelo `Categoria` y relación 1-N con `Curso`.

## 5) Excepciones
- Implementa un manejador personalizado para `ValueError` que devuelva 400 en la API.
- Experimento: lanza una excepción en la vista de detalle si el ID es 0 y observa el manejador 500.

## 6) Módulos y librerías
- Crea un blueprint `admin` con una ruta protegida por una variable de entorno simple `ADMIN_KEY`.

## 7) Ficheros
- Limita el tamaño de subida a 1MB solo para imágenes y maneja el error con un mensaje claro.

## 8) Testing
- Cubre con tests el flujo de subida y descarga de ficheros (usa un archivo temporal).
- Añade un test de utilidades que use `mayusculas`, `filtra_publicados` y `total_palabras`.

## 9) CLI
- Crea un comando CLI `flask export-cursos` que exporte a CSV los cursos almacenados.

## 10) Bonus
- Integra `Jinja` con un filtro personalizado `resumen(texto, n_palabras)` y úsalo en plantillas.
