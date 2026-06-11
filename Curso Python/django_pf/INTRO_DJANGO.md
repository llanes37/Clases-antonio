# Introducción a Django – Historia, filosofía y comparación con Flask

Autor: Joaquín Rodríguez  
Proyecto de referencia: `cursos/Curso Python/django_pf`

---

## 1. ¿Qué es Django?

Django es un framework web de alto nivel para Python. Su objetivo es que puedas pasar de una idea a una aplicación web funcional en muy poco tiempo, sin tener que reinventar piezas básicas como:

- Gestión de usuarios y autenticación.
- Panel de administración.
- Conexión a bases de datos mediante ORM.
- Sistema de plantillas HTML.
- Manejo de formularios, validaciones y seguridad.

Su eslogan clásico es: **“The Web framework for perfectionists with deadlines”**. Es decir: pensado para quien quiere hacer las cosas bien, pero sin perder tiempo en picar infraestructura desde cero.

---

## 2. Breve historia de Django

- **Origen periodístico**: nace a principios de los 2000 en la redacción del periódico *Lawrence Journal‑World* (Kansas, EE. UU.), para construir sitios de noticias rápidamente.
- **Creadores principales**: Adrian Holovaty y Simon Willison, entre otros desarrolladores.
- **Código abierto**: en 2005 se libera como proyecto open source; en 2008 aparece la versión 1.0.
- **Fundación Django**: desde 2008 existe la Django Software Foundation (DSF), que coordina el desarrollo y la comunidad.
- **Evolución**: hoy Django se usa para proyectos muy diversos:
  - Portales de noticias, redes sociales, intranets, backends de APIs, paneles de administración internos, etc.

En resumen: surgió de una necesidad muy práctica (producir mucho contenido web rápido) y se consolidó como un framework maduro, estable y mantenido por una comunidad grande.

---

## 3. Filosofía de Django: “baterías incluidas”

Django sigue varias ideas clave:

1. **Baterías incluidas**  
   Trae muchas herramientas integradas:
   - ORM para bases de datos relacionales.
   - Sistema de plantillas.
   - Panel de administración auto‑generado.
   - Sistema de formularios y validaciones.
   - Autenticación (login, logout, permisos).
   - Seguridad por defecto (CSRF, XSS, Clickjacking, etc.).

2. **Patrón MVT (Model–View–Template)**  
   Similar a MVC, pero con terminología propia:
   - Model: representa los datos (tablas) mediante clases Python.
   - View: recibe la petición, aplica lógica y prepara la respuesta.
   - Template: define cómo se presenta la información (HTML).

3. **DRY (Don’t Repeat Yourself)**  
   Intenta evitar duplicar lógica. Ejemplo clásico: defines tus modelos una vez y el admin, formularios y validaciones se aprovechan de ellos.

4. **Coherencia y convenciones**  
   Estructura de proyecto y nombres relativamente estándar, lo que hace más fácil entrar en proyectos ajenos.

---

## 4. Django vs Flask (cuándo usar cada uno)

En este curso tienes proyectos de Flask y de Django. No es para “elegir uno y descartar el otro”, sino para entender sus perfiles:

### 4.1 Flask en pocas palabras

- Micro‑framework minimalista.
- Solo define lo esencial: rutas, vistas, plantillas Jinja2.
- El resto se añade con extensiones (ORM, formularios, auth, etc.).
- Ideal para:
  - APIs pequeñas.
  - Prototipos rápidos.
  - Proyectos donde quieres control total sobre cada pieza.

### 4.2 Django en pocas palabras

- Framework “completo” (baterías incluidas).
- Trae ORM, admin, auth, formularios, internacionalización, etc.
- Estructura más marcada (proyecto + apps).
- Ideal para:
  - Aplicaciones con varios módulos (usuarios, cursos, pagos, etc.).
  - Proyectos en equipo, donde las convenciones ayudan.
  - Casos donde necesitas un admin usable desde el primer día.

### 4.3 Resumen comparativo

| Aspecto         | Flask                                  | Django                                       |
|-----------------|----------------------------------------|----------------------------------------------|
| Filosofía       | Micro, minimalista                     | Baterías incluidas                           |
| Estructura      | Muy libre                              | Proyecto + apps con convención               |
| ORM             | Extensiones (SQLAlchemy, etc.)         | Incluido de serie                            |
| Admin           | Hay extensiones                        | Panel de admin automático                    |
| Tamaño inicial  | Código muy pequeño                     | Más archivos, pero todo integrado            |
| Curva de inicio | Más suave si sabes Python y rutas      | Un poco más empinada, pero bien documentada  |

**Idea clave**: Flask te enseña “las tripas” de una app web ligera. Django te enseña cómo organizar un proyecto completo de forma profesional.

---

## 5. Estructura típica de un proyecto Django

En este curso tenemos el proyecto `django_pf`, que refleja bastante bien la estructura estándar:

```text
django_pf/
├── manage.py              # Lanzador de comandos (runserver, migrate, etc.)
├── djpf/                  # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py        # Ajustes globales (DEBUG, BD, apps, templates…)
│   ├── urls.py            # Rutas raíz del proyecto
│   ├── wsgi.py            # Punto de entrada WSGI
│   └── asgi.py            # Punto de entrada ASGI
└── core/                  # App principal (equivalente a “módulo” funcional)
    ├── __init__.py
    ├── apps.py            # Configuración de la app
    ├── middleware.py      # Middleware propio (logs, cabeceras)
    ├── views.py           # Vistas (HTML + API JSON + errores)
    ├── urls.py            # Rutas de la app
    └── templates/
        ├── base.html      # Layout común
        ├── index.html     # Página principal
        ├── about.html     # Información del proyecto
        └── resultado.html # Respuesta del formulario
```

Puntos importantes:

- Un **proyecto** Django puede contener varias **apps** (`core`, `blog`, `cursos`, etc.).  
- Cada app se centra en un concepto (ej. cursos, usuarios, blog) y agrupa:
  - `models.py`: modelos de datos.
  - `views.py`: vistas.
  - `urls.py`: rutas propias.
  - `templates/` y `static/`: presentación.
- `manage.py` es el punto de entrada para todas las tareas administrativas.

---

## 6. Flujo de una petición en Django

Simplificando, lo que pasa cuando visitas una URL es:

1. El navegador hace una petición a `/algo/`.
2. Django pasa esa petición por el **middleware** (seguridad, sesiones, logs…).
3. El enrutador (`urls.py`) busca qué vista corresponde a la ruta.
4. La vista:
   - Lee datos (query string, cuerpo, sesión…).
   - Opcional: consulta o modifica la base de datos a través de los modelos.
   - Prepara un contexto (`dict` de datos) y elige un template o JSON.
5. Se renderiza el template o se construye el `JsonResponse`.
6. La respuesta vuelve a pasar por el middleware (por ejemplo, para añadir cabeceras).
7. Django envía la respuesta final al navegador/cliente.

En el proyecto `django_pf` puedes seguir este flujo mirando:

- Middleware: `core/middleware.py`
- Enrutador raíz: `djpf/urls.py`
- Rutas de la app: `core/urls.py`
- Vistas: `core/views.py`
- Templates: `core/templates/*.html`

---

## 7. Cómo encaja Django en este curso Python

En el curso ya has visto:

- Programación estructurada y modular en Python.
- Control de flujo (condicionales, bucles).
- Funciones, colecciones, errores.
- Un tutorial completo de Flask.

Django te permite:

- Aplicar todo lo anterior en un contexto de **aplicación web estructurada**.
- Ver un proyecto que se parece mucho a lo que se usa en empresas:
  - Configuración por módulos.
  - Separación de responsabilidades (config, rutas, vistas, plantillas, middleware…).
  - Posibilidad de crecer hacia:
    - Modelos y base de datos reales.
    - Panel de administración.
    - APIs REST más complejas (con Django REST Framework).

La idea de `django_pf` es servir como “puente” entre el proyecto de Flask y una app Django más grande, sin abrumar al alumno, pero permitiendo extenderlo con:

- Modelos (`Curso`, `Alumno`, etc.).
- Autenticación.
- Tests.
- Despliegue real.

---

## 8. Siguientes pasos sugeridos

Si ya entiendes esta introducción:

1. Lee el archivo `django_pf/README.md` para ver qué hace cada parte del proyecto.  
2. Recorre `core/views.py` y `core/urls.py` para relacionar rutas con vistas.  
3. Usa `PRACTICAS_DJANGO_PF.md` como guion de laboratorio para ir ampliando la app.  
4. Cuando estés cómodo, da el salto a:
   - Añadir modelos y usar el ORM.
   - Crear un panel de administración útil.
   - Explorar Django REST Framework para APIs más grandes.

Con esta base te resultará más fácil entender proyectos reales de Django y decidir cuándo te conviene elegirlo frente a Flask u otras alternativas.

