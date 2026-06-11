# 📘 Guía de Proyectos Web - Curso Python

> **Para el profesor:** Esta guía resume todos los proyectos web reales del curso,  
> qué enseña cada uno, en qué orden conviene presentarlos, qué materiales trae y  
> qué huecos quedan todavía por cubrir.  
> **Autor:** Joaquín Rodríguez | **Última actualización:** Marzo 2026

---

## 🗺️ Ruta de Aprendizaje Web (de menos a más)

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  1️⃣  flask_proyecto_didactico           ← Flask en 1 archivo, HTML + JSON   │
│         ↓  (+templates reales, +formularios, +errores, +hooks)              │
│  2️⃣  Proyecto_Flask_Basico              ← Flask + MVC mínimo + SQLite       │
│         ↓  (+Blueprints, +servicios, +API separada)                         │
│  3️⃣  flask_proyecto_didactico (avanzado) ← App factory + Blueprints         │
│         ↓  (+SQLAlchemy real, +CLI, +tests, +subida ficheros)               │
│  4️⃣  Proyecto_Flask_Auth_Migraciones    ← Auth + roles + migraciones        │
│         ↓  (+modelo de proyecto integrador completo)                         │
│  5️⃣  Proyecto_Flask_Final               ← Proyecto Flask completo           │
│                                                                              │
│  🔀 Rama paralela para comparación de framework                              │
│  6️⃣  django_pf                          ← Django MVT + middleware + JSON    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Idea clave de la ruta

- **Flask** se usa como escalera principal para enseñar progresión arquitectónica.
- **Django** se usa como proyecto comparativo y de transición a framework “baterías incluidas”.
- El orden recomendado no es alfabético ni por carpeta: es **pedagógico**.

---

## 📊 Tabla Comparativa

| Proyecto | Nivel | Framework | Arquitectura | Base de datos | API JSON | Tests | Material didáctico |
|----------|:-----:|-----------|--------------|---------------|:--------:|:-----:|--------------------|
| `flask_proyecto_didactico` | ⭐ | Flask | 1 archivo + templates | ❌ | ✅ | ❌ | README |
| `Proyecto_Flask_Basico` | ⭐⭐ | Flask | MVC mínimo + Blueprint | ✅ SQLite | ❌ | ❌ | README + ejercicios |
| `flask_proyecto_didactico (avanzado)` | ⭐⭐⭐ | Flask | App factory + Blueprints + servicio | ⚠️ Memoria / SQLite opcional | ✅ | ❌ | README |
| `Proyecto_Flask_Auth_Migraciones` | ⭐⭐⭐⭐ | Flask | Factory + auth + roles + migrate | ✅ SQLite + Flask-Migrate | ❌ | ✅ pytest | README + guía + ejercicios |
| `Proyecto_Flask_Final` | ⭐⭐⭐⭐ | Flask | Factory + Blueprints + servicios + CLI | ✅ SQLite + SQLAlchemy | ✅ CRUD | ✅ pytest | README + guía + ejercicios |
| `django_pf` | ⭐⭐⭐ | Django | Proyecto + app + MVT + middleware | ⚠️ SQLite preparada | ✅ | ❌ | README + intro + prácticas |

### Leyenda rápida

- **❌** no incluido
- **⚠️** presente de forma parcial, opcional o preparada para ampliar
- **✅** incluido de forma real en el proyecto

---

## 1️⃣ `flask_proyecto_didactico` - Flask paso a paso

> **Cuándo usarlo:** Primera toma de contacto con una mini app web real.  
> Ideal justo después de `14_flask_tutorial.py`, cuando el alumno ya entiende rutas y formularios pero todavía no está listo para una arquitectura más grande.

### 🎯 Qué enseña

| Concepto | Cómo lo ve el alumno |
|----------|----------------------|
| **Flask básico** | `app = Flask(__name__)` en un proyecto real |
| **Templates Jinja2** | `templates/base.html`, `index.html`, `about.html`, `resultado.html` |
| **Formularios POST** | `/procesar` recibe `request.form` |
| **Rutas con parámetros** | `/saluda/<nombre>` y `/suma/<int:a>/<int:b>` |
| **Query strings** | `/buscar?q=...&page=...` |
| **API JSON** | `/api/echo`, `/api/saludo`, `/api/health`, `/api/calculadora/...` |
| **Errores** | handlers 404 y 500 |
| **Hooks** | `before_request` y `after_request` |
| **Better Comments** | flujo comentado para lectura guiada |

### ✅ Estado actual

- README explicando estructura, rutas y ejercicios.
- Proyecto pequeño y muy fácil de arrancar.
- Bueno para demos en clase y prácticas rápidas.
- Sin base de datos ni tests automáticos.

### 📦 Material incluido

- [README.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/flask_proyecto_didactico/README.md)
- [app.py](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/flask_proyecto_didactico/app.py)
- 4 plantillas HTML

### 🧠 Valor didáctico real

Es el mejor proyecto para enseñar:

- ciclo completo petición → ruta → vista → plantilla,
- diferencia entre HTML y JSON,
- validaciones muy básicas,
- y cómo se comporta una app web sin meter todavía base de datos ni capas.

### ⚠️ Limitaciones

- Todo vive en un solo archivo Python.
- No hay persistencia real.
- No hay tests.
- No hay separación arquitectónica fuerte.

---

## 2️⃣ `Proyecto_Flask_Basico` - MVC mínimo con SQLite

> **Cuándo usarlo:** Después del didáctico básico, cuando quieres que el alumno vea un primer proyecto “más serio” pero todavía simple.

### 🎯 Qué enseña

| Concepto | Cómo lo ve el alumno |
|----------|----------------------|
| **MVC mínimo** | modelo `Curso`, controlador `views.py`, vistas Jinja |
| **Blueprint** | `bp = Blueprint('main', __name__)` |
| **App factory básica** | `create_app()` en `miniapp/__init__.py` |
| **SQLite con SQLAlchemy** | `mini_basico.db` en `instance/` |
| **CRUD básico** | listar, crear y borrar cursos |
| **Plantillas reales** | `base.html` + `index.html` |
| **Buenas prácticas iniciales** | estructura en paquete y comentarios docentes |

### ✅ Estado actual

- README claro y breve.
- Ejercicios específicos para ampliarlo.
- Usa SQLAlchemy real.
- Aún no tiene tests ni API JSON.

### 📦 Material incluido

- [README.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Basico/README.md)
- [EJERCICIOS_BASICO.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Basico/EJERCICIOS_BASICO.md)
- [miniapp/__init__.py](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Basico/miniapp/__init__.py)
- [miniapp/views.py](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Basico/miniapp/views.py)
- [miniapp/models.py](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Basico/miniapp/models.py)

### 🧠 Valor didáctico real

Este proyecto sirve como puente perfecto entre:

- “Flask como tutorial”
- y “Flask como mini app real con base de datos”

Es pequeño, pero ya obliga a entender:

- creación de app,
- modelo persistente,
- vistas separadas,
- commit en base de datos,
- patrón de trabajo MVC muy básico.

### ⚠️ Limitaciones

- El CRUD está incompleto: no incluye edición todavía.
- No tiene API.
- No tiene tests.
- La arquitectura sigue siendo mínima.

---

## 3️⃣ `flask_proyecto_didactico (avanzado)` - MVC ligero con Blueprints

> **Cuándo usarlo:** Cuando el alumno ya entiende Flask básico y quieres enseñar cómo dividir una app por responsabilidades sin saltar aún al proyecto final completo.

### 🎯 Qué enseña

| Concepto | Cómo lo ve el alumno |
|----------|----------------------|
| **App factory** | `create_app()` y configuración separada |
| **Blueprints** | uno para web y otro para API |
| **Servicio/controlador** | `controllers/items.py` como capa CRUD |
| **Modelo simple** | `Item` como dataclass / entidad ligera |
| **Formularios + API** | HTML y JSON conviven en el mismo proyecto |
| **Arquitectura modular** | `routes/`, `controllers/`, `templates/` |
| **Persistencia opcional** | `items_sqlite.py` como salto a SQLite |

### ✅ Estado actual

- README correcto con instalación, rutas y ejercicios.
- Arquitectura más madura que el didáctico básico.
- Incluye alternativa SQLite opcional.
- Sin tests automáticos integrados.

### 📦 Material incluido

- [README.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/flask_proyecto_didactico%20(avanzado)/README.md)
- [app.py](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/flask_proyecto_didactico%20(avanzado)/app.py)
- `proyecto_avanzado/__init__.py`
- `config.py`
- `models.py`
- `controllers/items.py`
- `controllers/items_sqlite.py`
- `routes/web.py`
- `routes/api.py`
- 4 plantillas

### 🧠 Valor didáctico real

Es el proyecto más útil para enseñar **arquitectura Flask intermedia**:

- cómo crecer desde un solo archivo,
- cómo separar HTML de API,
- cómo aislar lógica de negocio,
- y cómo preparar el salto a persistencia real.

### ⚠️ Limitaciones

- La persistencia por defecto sigue siendo en memoria.
- SQLite está como ampliación opcional, no como núcleo.
- No trae tests ni CLI.

---

## 4️⃣ `Proyecto_Flask_Auth_Migraciones` - Auth, roles y evolución de esquema

> **Cuándo usarlo:** Después del proyecto avanzado con Blueprints y antes del proyecto final completo.  
> Es el proyecto ideal para enseñar seguridad básica, sesiones y por qué las migraciones existen.

### 🎯 Qué enseña

| Concepto | Cómo lo ve el alumno |
|----------|----------------------|
| **Autenticación** | registro, login y logout con sesión |
| **Passwords seguras** | hash con `werkzeug.security` |
| **Roles simples** | `student` y `admin` |
| **Rutas protegidas** | `login_required` y `admin_required` |
| **Panel admin básico** | gestión de roles y activación de usuarios |
| **SQLAlchemy real** | modelos `User` y `NotaPrivada` |
| **Migraciones** | proyecto preparado para `flask db migrate` / `upgrade` |
| **Testing** | tests de auth y permisos |
| **Mensajes flash** | feedback visual al usuario |

### ✅ Estado actual

- Proyecto nuevo creado específicamente para cubrir el hueco de auth + migraciones.
- Tiene README, guía paso a paso y ejercicios.
- Incluye tests base.
- Está preparado para `Flask-Migrate`.

### 📦 Material incluido

- [README.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Auth_Migraciones/README.md)
- [GUIA_PASO_A_PASO.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Auth_Migraciones/GUIA_PASO_A_PASO.md)
- [EJERCICIOS.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Auth_Migraciones/EJERCICIOS.md)
- `.env.example`
- `run.ps1`
- `test.ps1`
- `migrate.ps1`
- modelos, blueprints, templates y tests

### 🧠 Valor didáctico real

Este proyecto cubre uno de los saltos más importantes del desarrollo web:

- pasar de una app funcional
- a una app con control de acceso y evolución de base de datos.

Es el mejor proyecto del bloque para explicar:

- por qué no se guardan passwords en texto plano,
- cómo funciona una sesión,
- qué significa tener permisos por rol,
- y por qué `create_all()` no basta cuando la aplicación crece.

### ⚠️ Limitaciones

- No tiene API JSON como foco principal.
- No incluye recuperación de password ni email de confirmación.
- Las migraciones están preparadas, pero no se entrega un historial generado completo.

---

## 5️⃣ `Proyecto_Flask_Final` - Proyecto integrador completo

> **Cuándo usarlo:** Al final del bloque Flask o como proyecto integrador del curso completo de Python.

### 🎯 Qué enseña

| Concepto | Cómo lo ve el alumno |
|----------|----------------------|
| **App factory real** | configuración por entorno y carpetas `instance/` |
| **Blueprints** | `main`, `api`, `files` |
| **SQLAlchemy real** | modelos `Usuario`, `Curso`, `Inscripcion` |
| **CRUD API completo** | listar, detalle, crear, actualizar y borrar cursos |
| **Relaciones POO + BD** | muchos-a-muchos mediante `Inscripcion` |
| **Subida/descarga ficheros** | `files.py` con `upload` y `download` |
| **Servicios reutilizables** | utilidades y tareas CLI |
| **CLI** | comando de seed |
| **Testing** | pytest con app en modo testing |
| **Config por entorno** | desarrollo, testing, producción |

### ✅ Estado actual

- Es el proyecto más completo del bloque web Python.
- Tiene README, guía paso a paso, ejercicios y tests.
- Ya se parece a un proyecto real de portfolio docente.

### 📦 Material incluido

- [README.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Final/README.md)
- [GUIA_PASO_A_PASO.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Final/GUIA_PASO_A_PASO.md)
- [EJERCICIOS.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Final/EJERCICIOS.md)
- `.env.example`
- `run.ps1`
- `test.ps1`
- 3 blueprints
- 5 tests Python
- modelos y servicios

### 🧠 Valor didáctico real

Es el proyecto que mejor integra todo el curso:

- Python base,
- funciones,
- POO,
- excepciones,
- módulos,
- bases de datos,
- testing,
- Flask.

Si hubiera que enseñar **un solo proyecto “serio” del bloque Flask**, este sería el elegido.

### ⚠️ Limitaciones

- No incluye autenticación real de usuarios.
- No hay migraciones formales (se usa `create_all()`).
- No hay panel admin ni roles completos.

---

## 6️⃣ `django_pf` - Django fácil completo (rama comparativa)

> **Cuándo usarlo:** Cuando el alumno ya ha visto Flask y quieres compararlo con Django sin entrar todavía en un proyecto empresarial grande.

### 🎯 Qué enseña

| Concepto | Cómo lo ve el alumno |
|----------|----------------------|
| **Estructura de proyecto Django** | `manage.py`, `settings.py`, `urls.py`, app `core` |
| **MVT** | vistas, templates y rutas al estilo Django |
| **Formularios POST** | `request.POST` y render de resultado |
| **Query strings** | `request.GET` |
| **API JSON** | `JsonResponse` |
| **Middleware** | `RequestLogMiddleware` con tiempo de respuesta |
| **Errores 404/500** | handlers registrados en el proyecto |
| **Comparación Flask vs Django** | misma idea didáctica con otro framework |

### ✅ Estado actual

- Buen README.
- Introducción histórica y conceptual a Django.
- Prácticas guiadas bastante completas.
- No incluye tests automáticos.
- La BD está preparada, pero el foco actual no es el ORM.

### 📦 Material incluido

- [README.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/django_pf/README.md)
- [INTRO_DJANGO.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/django_pf/INTRO_DJANGO.md)
- [PRACTICAS_DJANGO_PF.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/django_pf/PRACTICAS_DJANGO_PF.md)
- `manage.py`
- configuración `djpf/`
- app `core/`
- middleware propio
- 4 plantillas

### 🧠 Valor didáctico real

No es un proyecto para sustituir la ruta Flask, sino para responder esta pregunta:

> “¿Cómo cambia la misma idea cuando el framework ya trae más estructura y más piezas de serie?”

Muy útil para:

- comparar frameworks,
- enseñar MVT,
- introducir middleware y estructura Django,
- y preparar el salto a ORM, auth y admin.

### ⚠️ Limitaciones

- No explota aún el ORM de Django de forma protagonista.
- No trae tests.
- No hay login, admin ni modelos potentes como eje principal.

---

## 💡 Orden de presentación recomendado en clase

### Ruta recomendada para Flask

1. **`flask_proyecto_didactico`**
   - para ver el flujo entero sin distraerse con arquitectura.
2. **`Proyecto_Flask_Basico`**
   - para introducir persistencia real con SQLite y SQLAlchemy.
3. **`flask_proyecto_didactico (avanzado)`**
   - para enseñar modularización, blueprints y servicios.
4. **`Proyecto_Flask_Auth_Migraciones`**
   - para enseñar sesiones, roles, permisos y migraciones.
5. **`Proyecto_Flask_Final`**
   - para integrar todo en un proyecto serio.

### Ruta recomendada para Django

1. enseñar Flask primero,
2. luego comparar con **`django_pf`**,
3. y solo después entrar en `15_django_tutorial.py` o en ampliaciones de ORM/admin.

---

## 📁 Estructura actual del bloque web Python

```text
Curso Python/
│
├── flask_proyecto_didactico/              ← 1️⃣ Flask en 1 archivo + templates
│   ├── app.py
│   ├── README.md
│   └── templates/
│
├── Proyecto_Flask_Basico/                 ← 2️⃣ MVC mínimo + SQLite
│   ├── miniapp/
│   ├── README.md
│   ├── EJERCICIOS_BASICO.md
│   └── requirements.txt
│
├── flask_proyecto_didactico (avanzado)/   ← 3️⃣ App factory + Blueprints
│   ├── app.py
│   ├── README.md
│   └── proyecto_avanzado/
│
├── Proyecto_Flask_Auth_Migraciones/       ← 4️⃣ Auth + roles + migraciones
│   ├── app/
│   ├── tests/
│   ├── README.md
│   ├── GUIA_PASO_A_PASO.md
│   ├── EJERCICIOS.md
│   └── requirements.txt
│
├── Proyecto_Flask_Final/                  ← 5️⃣ Proyecto Flask completo
│   ├── app/
│   ├── tests/
│   ├── scripts/
│   ├── README.md
│   ├── GUIA_PASO_A_PASO.md
│   ├── EJERCICIOS.md
│   └── requirements.txt
│
├── django_pf/                             ← 6️⃣ Rama comparativa en Django
│   ├── manage.py
│   ├── djpf/
│   ├── core/
│   ├── README.md
│   ├── INTRO_DJANGO.md
│   └── PRACTICAS_DJANGO_PF.md
│
└── 📘_GUIA_PROYECTOS_WEB_PYTHON.md        ← 📖 Este fichero
```

---

## ✅ Estado global del bloque

| Proyecto | README | Guía extra | Ejercicios | Tests | BD real | API JSON |
|---|---|---|---|---|---|---|
| `flask_proyecto_didactico` | ✅ | ❌ | ⚠️ en README | ❌ | ❌ | ✅ |
| `Proyecto_Flask_Basico` | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |
| `flask_proyecto_didactico (avanzado)` | ✅ | ❌ | ⚠️ en README | ❌ | ⚠️ opcional | ✅ |
| `Proyecto_Flask_Auth_Migraciones` | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| `Proyecto_Flask_Final` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `django_pf` | ✅ | ✅ intro + prácticas | ✅ | ❌ | ⚠️ preparada | ✅ |

---

## 🔎 Qué hace cada proyecto en una frase

- **`flask_proyecto_didactico`**: enseña Flask “desde dentro” en formato muy lineal y fácil de explicar.
- **`Proyecto_Flask_Basico`**: enseña el primer CRUD real con Flask + SQLAlchemy + MVC mínimo.
- **`flask_proyecto_didactico (avanzado)`**: enseña cómo modularizar Flask con Blueprints y una capa de servicio.
- **`Proyecto_Flask_Auth_Migraciones`**: enseña autenticación, roles y el salto didáctico a migraciones reales.
- **`Proyecto_Flask_Final`**: enseña una app Flask bastante completa con CRUD API, archivos, CLI y tests.
- **`django_pf`**: enseña la misma familia de ideas pero bajo la estructura propia de Django.

---

## 🚧 Qué falta todavía y por qué

### 1. En Flask ya no falta el bloque de autenticación

Ese hueco queda cubierto ahora con:

- `Proyecto_Flask_Auth_Migraciones`

Así que la ruta Flask ya tiene:

- introducción,
- MVC mínimo,
- modularización,
- autenticación + migraciones,
- y proyecto final completo.

### 2. Lo que aún falta en Flask es un proyecto con API protegida

Ahora mismo tienes auth web con sesiones, pero no un proyecto cuyo foco sea:

- API JSON autenticada,
- permisos por token o sesión,
- consumo desde frontend o cliente externo.

**Proyecto sugerido a futuro:**  
`Proyecto_Flask_API_Auth`

con:

- `/api/login`
- `/api/me`
- rutas protegidas
- separación clara entre auth web y auth API

### 3. En Django sigue faltando un proyecto donde ORM + admin + auth sean protagonistas

`django_pf` es muy bueno como comparación didáctica, pero aún no es el proyecto Django que mejor enseñaría:

- modelos reales,
- panel admin,
- login,
- relaciones,
- formularios basados en modelo.

**Proyecto sugerido a medio plazo:**  
`django_proyecto_cursos_admin`

con:

- `Curso`, `Alumno`, `Matricula`
- panel admin
- login
- vistas CRUD
- y una pequeña API o exportación

### 4. En ambos frameworks falta un proyecto orientado a despliegue real

No es imprescindible ahora, pero a futuro tendría sentido un proyecto o mini unidad sobre:

- configuración de producción,
- variables de entorno,
- gunicorn / waitress,
- logging,
- y despliegue en Render o similar.

### 1. Falta un proyecto Flask centrado en autenticación real

Ahora mismo tienes:

- Flask básico,
- Flask con API,
- Flask con CRUD,
- Flask final con ficheros y tests,

pero no hay un **proyecto dedicado a login/logout, sesiones, roles y protección de rutas** como núcleo del proyecto.

**Por qué falta:**  
Porque ese es un salto natural entre el proyecto avanzado y el final, y además conecta muy bien con seguridad web real.

### 2. Falta un proyecto Flask con migraciones formales

`Proyecto_Flask_Final` usa `db.create_all()`, que está bien para un curso, pero no muestra el flujo profesional de:

- migraciones,
- evolución del esquema,
- mantenimiento de BD en varios entornos.

**Proyecto sugerido:**  
`Proyecto_Flask_Auth_Migraciones`

que enseñe:

- Flask-Login o sesiones,
- roles simples,
- migraciones con Alembic/Flask-Migrate,
- formularios y validación un poco más seria.

### 3. En Django falta un proyecto “con ORM protagonista”

`django_pf` es muy bueno como comparación de rutas, templates, middleware y JSON, pero aún no es el proyecto ideal para enseñar:

- modelos reales,
- admin,
- relaciones,
- formularios basados en modelos,
- auth.

**Proyecto sugerido a medio plazo:**  
`django_proyecto_cursos_admin`

con:

- `Curso`, `Alumno`, `Matricula`,
- panel admin,
- login,
- listado web,
- API simple o vistas CRUD.

---

## 🧭 Recomendación estratégica

Si solo vas a crear **un** proyecto nuevo en el bloque web Python, el más rentable es este:

### `Proyecto_Flask_Auth_Migraciones`

Porque cubriría justo el hueco más importante entre:

- el proyecto avanzado modular,
- y el proyecto final completo.

Además reforzaría:

- seguridad,
- sesiones,
- estructura real de producción,
- y transición a aplicaciones más profesionales.

---

## 📌 Conclusión docente

El bloque web Python ya está **bastante bien escalonado** y tiene suficiente material para un curso serio:

- una ruta principal de Flask,
- una rama comparativa de Django,
- y un proyecto final claramente más maduro.

Lo que necesita ahora no es más cantidad sin criterio, sino:

1. una **guía unificada** como esta,
2. una mejor señalización de **qué proyecto usar en cada fase**,
3. y cubrir el hueco de **autenticación + migraciones**.

Con eso, el bloque quedaría mucho más redondo y fácil de impartir.

---

*Última actualización: Marzo 2026 - Curso Python*
