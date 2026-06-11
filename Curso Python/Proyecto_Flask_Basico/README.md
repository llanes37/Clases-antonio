# Proyecto Flask Básico (MVC mínimo)

Objetivo: entender la estructura mínima de un proyecto Flask con Modelo, Controlador (Blueprint) y Vistas (Jinja).

## Estructura
```
Proyecto_Flask_Basico/
  miniapp/
    __init__.py        # crea la app
    models.py          # MODELO: Curso
    views.py           # CONTROLADOR: rutas
    templates/
      base.html
      index.html       # VISTA
  requirements.txt
  run.ps1              # ejecutar en Windows PowerShell
```

## Ejecutar
```powershell
./run.ps1
```

- App: http://127.0.0.1:5000/

Nota importante:
- No abras `miniapp/templates/*.html` directamente en el navegador; deben renderizarse a través de Flask.
- Accede siempre por las rutas (`/`).

## Conceptos clave (Better Comments)
- # * Idea clave
- # ! Advertencia
- # ? Explicación
- # TODO: Siguiente mejora sugerida

Recursos:
- `COMENTARIOS_BETTER_COMMENTS.md` — Guía rápida de las etiquetas usadas
- `EJERCICIOS_BASICO.md` — Lista de retos sencillos para practicar
