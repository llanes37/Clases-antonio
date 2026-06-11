# Guía paso a paso — Proyecto Flask Final

Esta guía explica cada archivo y decisión, con foco didáctico (nivel básico).

## 1. Estructura general
- `app/`: código de la aplicación
  - `__init__.py`: función `create_app` que crea y configura Flask
  - `config.py`: clases de configuración por entorno
  - `extensions.py`: inicialización de extensiones (SQLAlchemy)
  - `models.py`: modelos de datos (Usuario, Curso, Inscripcion)
  - `errors.py`: manejadores de errores 404/500
  - `services/`: utilidades y comandos CLI
  - `blueprints/`: módulos de rutas (main, api, files)
  - `templates/` y `static/`: vistas y recursos
- `tests/`: pruebas con pytest
- `scripts/`: scripts auxiliares (semillas)
- `requirements.txt`: dependencias
- `.env.example`: ejemplo de variables de entorno
- `run.ps1`: script para instalar y ejecutar en Windows

## 2. Flujo de arranque
1) PowerShell ejecuta `run.ps1` -> crea `.venv`, instala requirements y arranca Flask.
2) Flask ejecuta `create_app()` en `app/__init__.py`.
3) Carga configuración desde `app/config.py` leyendo `APP_ENV`.
4) Inicializa la BD (SQLite) y crea tablas si no existen.
5) Registra blueprints y manejadores de errores.

## 3. Modelos (POO)
- `Usuario`: nombre, email y relación N-M con `Curso` a través de `Inscripcion`.
- `Curso`: título, descripción y flag `publicado`; método `to_dict` para API.
- `Inscripcion`: tabla intermedia con fecha.

## 4. Blueprints
- `main.py`: páginas HTML `"/"` e `"/cursos"` renderizando plantillas.
- `api.py`: API REST para cursos con endpoints CRUD JSON.
- `files.py`: subida/descarga de ficheros a `instance/uploads`.

## 5. Plantillas (Jinja)
- `base.html`: layout básico con cabecera y navegación.
- `index.html`: muestra cursos publicados.
- `cursos.html`: lista cursos y permite crear uno vía `fetch` a la API.

## 6. Servicios
- `utils.py`: ejemplos de map/filter/reduce y manejo sencillo de excepciones.
- `tasks.py`: comando `flask seed` para poblar la base de datos.

## 7. Errores y depuración
- En `errors.py` se devuelve HTML o JSON según la ruta o cabeceras.
- En desarrollo, Flask muestra traza de errores en consola (útil para debugging).

## 8. Pruebas (pytest)
- `tests/conftest.py` crea una app de testing con SQLite en memoria.
- `test_basic.py` verifica que la página principal carga.
- `test_cursos_api.py` valida el CRUD de la API.

## 9. Variables de entorno
- Copia `.env.example` a `.env` para personalizar `SECRET_KEY`, `DATABASE_URL` o `APP_ENV`.

## 10. Siguientes pasos
- Realiza los ejercicios de `EJERCICIOS.md`.
- Explora SQLAlchemy: consultas, filtros, relaciones.
- Añade validaciones y formularios (WTForms) si deseas profundizar.
