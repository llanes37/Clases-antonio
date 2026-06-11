# Clase 00 de Python - Setup del entorno y buenas practicas

**Autor:** Joaquín Rodríguez  
**Objetivo global:** Preparar al alumno para trabajar con Python de forma **ordenada, reproducible y profesional** desde el principio. En esta unidad aprenderá a comprobar su instalación de Python, validar `pip`, entender qué es un **entorno virtual**, crear un `requirements.txt`, montar una **estructura mínima de proyecto** y aplicar **buenas prácticas** sencillas pero importantes.

---

## Cómo usar este material

1. **Lee primero este documento** para entender el porqué de cada paso.
2. **Ejecuta** `00_setup_entorno_y_buenas_practicas.py` para ver la explicación guiada con ejemplos.
3. **Completa** `00_setup_entorno_y_buenas_practicas(alumno).py` rellenando las zonas `TODO`.
4. Usa esta unidad como **base de trabajo** para el resto del curso: Flask, bases de datos, testing y proyectos finales dependen de que el entorno esté bien preparado.

> **Idea pedagógica:** este tema no busca “programar mucho”, sino evitar errores futuros. Un alumno que entiende bien `venv`, `pip` y la estructura de proyecto suele tener menos bloqueos durante el curso.

---

## Qué aprenderás exactamente

- Saber qué versión de Python estás ejecutando realmente.
- Diferenciar entre **Python del sistema** y **Python del proyecto**.
- Verificar si `pip` está asociado al Python correcto.
- Entender por qué se usa un **entorno virtual** en casi todos los proyectos reales.
- Crear un `requirements.txt` con dependencias importantes.
- Organizar una carpeta de proyecto con `README`, código principal y tests.
- Aplicar buenas prácticas básicas de legibilidad y estructura.

---

## SECCIÓN 1 · Versión de Python y diagnóstico básico

### Objetivos

- Comprobar qué versión de Python está usando la terminal.
- Identificar el ejecutable real de Python.
- Validar si `pip` funciona correctamente.

### Teoría en claro

Antes de instalar librerías o ejecutar scripts, conviene comprobar **qué Python estás usando**. En muchos equipos puede haber varias instalaciones:

- Python de Microsoft Store
- Python instalado manualmente
- Python dentro de un entorno virtual
- Python usado por un IDE

Los elementos clave aquí son:

- `platform.python_version()` → versión legible de Python.
- `sys.executable` → ruta exacta del ejecutable en uso.
- `sys.version_info` → versión estructurada (major, minor, micro).
- `python -m pip --version` → comprueba que `pip` está ligado a ese Python.

### Demo guiada

El script del profesor muestra:

- versión de Python,
- implementación (`CPython`, por ejemplo),
- ejecutable real,
- sistema operativo,
- y salida de `pip --version`.

Esto permite responder a una pregunta fundamental:

> “¿Estoy instalando librerías en el Python correcto?”

### Práctica (TODO)

1. Muestra `sys.version_info`.
2. Comprueba con `Path(sys.executable).exists()` si la ruta existe.
3. Indica si la palabra `"python"` aparece en el ejecutable.
4. Escribe una línea final tipo resumen:

```txt
Python OK | Ejecutable válido: True | pip detectado: Sí
```

### Errores típicos

- Tener varias versiones de Python y no saber cuál usa la terminal.
- Ejecutar `pip` global cuando el proyecto necesita el del entorno virtual.
- Confiarse porque “Python funciona” aunque el ejecutable no sea el esperado.

---

## SECCIÓN 2 · Entornos virtuales (`venv`)

### Objetivos

- Entender qué es un entorno virtual.
- Saber crearlo y activarlo.
- Comprender por qué evita conflictos entre proyectos.

### Teoría en claro

Un entorno virtual crea un espacio aislado para:

- el intérprete de Python,
- las librerías instaladas,
- y la configuración del proyecto.

Esto evita que dos proyectos se “pisen” entre sí. Por ejemplo:

- un proyecto puede usar Flask 2.x,
- otro puede usar Flask 3.x,
- y ambos coexistir sin conflicto.

### Comandos más usados

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Demo guiada

El script muestra:

- el comando para crear el entorno,
- la ruta típica de activación,
- y el uso de `python -m pip install -r requirements.txt`.

### Práctica (TODO)

1. Construye con `Path` la ruta de activación del entorno.
2. Muestra esa ruta por pantalla.
3. Indica si existe.
4. Añade una línea que explique qué ocurriría si no existe todavía.

### Idea importante

No pasa nada si `.venv` aún no existe. Eso solo significa que **todavía no has creado el entorno**. El objetivo del ejercicio es aprender a reconocer su estructura.

### Error muy habitual

Pensar que `venv` “instala Python”. No: Python ya debe estar instalado. `venv` crea un **entorno de trabajo** a partir de una instalación existente.

---

## SECCIÓN 3 · Dependencias y `requirements.txt`

### Objetivos

- Comprender para qué sirve un `requirements.txt`.
- Saber crear uno manualmente.
- Relacionarlo con el resto del curso.

### Teoría en claro

`requirements.txt` es un archivo que lista las librerías necesarias del proyecto. Sirve para que otro alumno, profesor o equipo pueda reproducir el entorno con un solo comando:

```powershell
python -m pip install -r requirements.txt
```

Hay dos formas comunes de construirlo:

1. **Manual**
   - útil para cursos y proyectos pequeños,
   - solo incluye dependencias importantes.

2. **Con `pip freeze`**
   - lista todo lo instalado en el entorno,
   - útil cuando quieres replicar exactamente una instalación.

### Dependencias mínimas recomendadas para este curso

```txt
flask
sqlalchemy
pytest
requests
```

### Demo guiada

El script del profesor:

- enseña una lista mínima,
- ejecuta `pip freeze`,
- y muestra las primeras líneas como ejemplo real.

### Práctica (TODO)

1. Crea una lista de dependencias mínimas.
2. Guárdala en `requirements_curso.txt`.
3. Muestra la ruta absoluta del fichero creado.
4. Extra: lee después el archivo y vuelve a imprimir su contenido.

### Buen criterio didáctico

Para un curso, suele ser mejor empezar con un `requirements.txt` **pequeño y claro** antes de enseñar un `pip freeze` enorme.

---

## SECCIÓN 4 · Estructura básica de un proyecto

### Objetivos

- Pasar de “scripts sueltos” a “proyecto organizado”.
- Entender qué carpetas y archivos mínimos conviene crear.

### Estructura sugerida

```txt
proyecto_demo/
  README.md
  main.py
  tests/
    test_demo.py
```

### Teoría en claro

Aunque un proyecto sea pequeño, conviene separar:

- **código principal**,
- **documentación**,
- **pruebas**.

Esto ayuda a:

- entender mejor qué hace el proyecto,
- trabajar con orden,
- y facilitar correcciones o ampliaciones.

### Demo guiada

El script del profesor presenta una estructura recomendada y deja planteada la creación de:

- `demo_proyecto_python/`
- `tests/`
- `README.md`
- `app.py`

### Práctica (TODO)

1. Crea la carpeta principal.
2. Crea la subcarpeta `tests`.
3. Crea un `README.md` con una descripción corta.
4. Crea `app.py` con un `print("Hola proyecto")`.
5. Extra: añade `tests/test_basico.py`.

### Reflexión importante

Este paso puede parecer simple, pero cambia la mentalidad del alumno:

> deja de trabajar solo con ejercicios sueltos y empieza a pensar en proyectos reales.

---

## SECCIÓN 5 · Buenas prácticas de código

### Objetivos

- Introducir reglas simples de legibilidad y organización.
- Enseñar a separar lógica y ejecución.

### Reglas básicas

- Usa nombres claros: `precio_unitario`, no `pu`.
- Crea funciones pequeñas.
- Evita repetir código.
- Separa la lógica del flujo principal.
- Usa:

```python
if __name__ == "__main__":
    ...
```

en scripts ejecutables.

### Ejemplo sencillo

```python
def calcular_total(precio, unidades):
    return precio * unidades

if __name__ == "__main__":
    print(calcular_total(10, 3))
```

### Qué enseña realmente este ejemplo

- la función hace una sola cosa,
- se puede reutilizar,
- y el bloque principal controla la ejecución del script.

### Práctica (TODO)

Convierte este flujo en una función:

1. pedir precio,
2. pedir unidades,
3. calcular total,
4. imprimir total.

Extra:

- llama a la función desde `if __name__ == "__main__":`
- mejora los nombres de variables para que sean claros.

### Error habitual

Meter toda la lógica directamente al principio del archivo, sin funciones. Eso funciona en ejercicios pequeños, pero escala mal muy rápido.

---

## Autoevaluación final · Mini proyecto de arranque

### Objetivos

- Integrar entorno, dependencias, estructura y buenas prácticas en una actividad pequeña.

### Tareas

1. Muestra tu versión de Python y verifica si `pip` funciona.
2. Genera `requirements_demo.txt` con varias dependencias.
3. Crea `proyecto_demo` con:
   - `README.md`
   - `main.py`
   - `tests/test_demo.py`
4. Escribe en `main.py` una función `saludar(nombre)`.
5. Llama a esa función desde un bloque principal.
6. Explica en 3 líneas por qué usar un entorno virtual reduce problemas.

### Rúbrica rápida

- **Correcto**: el alumno crea archivos, entiende el entorno y organiza el proyecto.
- **Bien**: además separa lógica y ejecución.
- **Excelente**: usa nombres claros, escribe estructura limpia y justifica bien el uso de `venv`.

---

## Apéndice A · Diferencia entre script y proyecto

### Script

- un solo archivo,
- una tarea concreta,
- útil para ejercicios rápidos.

### Proyecto

- varios archivos o carpetas,
- dependencias,
- documentación,
- posibilidad de crecer.

**Conclusión:** el curso empieza con scripts, pero debe terminar enseñando también a pensar en proyectos.

---

## Apéndice B · Checklist del alumno antes de seguir con el curso

- [ ] Sé qué Python estoy usando.
- [ ] Sé comprobar si `pip` funciona.
- [ ] Entiendo qué es `.venv`.
- [ ] Sé para qué sirve `requirements.txt`.
- [ ] Sé crear una estructura básica de proyecto.
- [ ] Entiendo el uso de `if __name__ == "__main__":`.

---

## Retos extra

1. Crea un archivo `config.py` dentro del proyecto demo.
2. Añade una función en `main.py` y otra en un segundo módulo.
3. Crea un `README.md` un poco más completo con instrucciones de ejecución.
4. Añade una prueba mínima en `tests/test_demo.py`.
5. Explica la diferencia entre instalar una librería globalmente o en `venv`.

---

## Qué has aprendido

- Cómo diagnosticar tu instalación de Python.
- Cómo entender y usar `pip`.
- Qué es un entorno virtual y por qué importa.
- Cómo crear un fichero de dependencias.
- Cómo empezar un proyecto limpio y ordenado.
- Cómo aplicar buenas prácticas desde el inicio del curso.
