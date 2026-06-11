# Proyecto Flask Final — Curso Python

Este proyecto resume y pone en práctica todos los conceptos vistos en el curso (variables, condicionales, bucles, funciones, POO, excepciones, módulos, ficheros, BBDD con SQLAlchemy, testing, CLI y Flask). Incluye comentarios al estilo Better Comments para facilitar el estudio.

## Objetivos
- Ver un ejemplo real de aplicación web con Flask.
- Practicar CRUD con SQLAlchemy y SQLite.
- Manejar ficheros (subida/descarga).
- Usar utilidades funcionales (map/filter/reduce).
- Gestionar errores y excepciones.
- Ejecutar tareas por CLI con Click/Flask.
- Probar con pytest.

## Estructura del proyecto
```
Proyecto_Flask_Final/
  app/
    __init__.py
    config.py
    extensions.py
    models.py
    errors.py
    services/
      utils.py
      tasks.py
    blueprints/
      main.py
      api.py
      files.py
    templates/
      base.html
      index.html
      cursos.html
    static/
      css/style.css
  tests/
    conftest.py
    test_basic.py
    test_cursos_api.py
  scripts/
    seed.py
  .env.example
  requirements.txt
  EJERCICIOS.md
  run.ps1
  test.ps1
```

## Requisitos previos
- Windows con PowerShell (v5.1 o superior).
- Python 3.10+ instalado y accesible como `python`.

## Instalación y ejecución (Windows PowerShell)
1) Crear y activar entorno virtual, instalar dependencias y arrancar el servidor (automático):

```powershell
# Desde la carpeta del proyecto: cursos/Curso Python/Proyecto_Flask_Final
./run.ps1
```

2) Acceder en el navegador:
- App: http://127.0.0.1:5000/
- API: http://127.0.0.1:5000/api/cursos
 - Health: http://127.0.0.1:5000/api/health

3) Variables de entorno (opcional usando .env):
Copia `.env.example` a `.env` y ajusta a tu gusto.

## Semillas de datos
Puedes crear datos de ejemplo con el comando CLI incluido:

```powershell
$env:FLASK_APP="app:create_app"; $env:APP_ENV="development"; python -m flask seed
```

## Probar (pytest)
```powershell
# Ejecuta todos los tests
./test.ps1
```

## Qué cubre respecto al curso
- Variables/Operadores: Config y pequeñas utilidades.
- Condicionales/Bucles: Lógica en vistas y plantillas (`for`, `if`).
- Funciones: `services/utils.py` y vistas.
- POO: Modelos `Usuario`, `Curso`, `Inscripcion`.
- Excepciones: `errors.py` y manejo en endpoints.
- Módulos/Librerías: Blueprints, servicios, `click` CLI.
- Ficheros: Subida/descarga en `blueprints/files.py`.
- BBDD: SQLAlchemy con SQLite.
- Testing y Debugging: Pytest + configuración de testing.
 - Healthcheck: `/api/health` devuelve estado y conteos.
 - Paginación/consulta opcional: `/api/cursos?q=flask&page=1&per_page=5`.

## Problemas comunes
- No se activa el entorno virtual: Permisos de ejecución. En PowerShell ejecuta como Admin o permite scripts para la sesión actual:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
- Puerto ocupado: Cambia el puerto con `python -m flask run --port 5001`.
- SQLite bloqueado: cierra programas que tengan abierto el `.db`.

## Estilo de comentarios (Better Comments)
- # TODO: tarea pendiente
- # ! Importante/Advertencia
- # ? Duda o explicación
- # * Punto clave

Consulta también: `COMENTARIOS_BETTER_COMMENTS.md` para ver cómo y dónde se usan.

## Cómo compilar/ejecutar
Flask no se compila; se ejecuta:
```powershell
# Arrancar servidor en desarrollo
$env:FLASK_APP="app:create_app"; $env:APP_ENV="development"; python -m flask run
```

## Nota importante sobre plantillas Jinja
- No abras los HTML de `app/templates` directamente en el navegador (no verás Jinja procesado).
- Debes acceder a través de Flask: `/` o `/cursos`.

> Consejo: Mantén dos terminales: una para el servidor y otra para tests/comandos.

## Licencia
Uso educativo.
