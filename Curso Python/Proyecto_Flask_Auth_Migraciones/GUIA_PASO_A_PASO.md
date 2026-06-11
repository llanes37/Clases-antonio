# Guía paso a paso - Proyecto Flask Auth + Migraciones

## 1. Propósito pedagógico

Esta guía no solo explica **cómo ejecutar** el proyecto, sino **cómo enseñarlo**.

El objetivo es que profesor y alumno comprendan:

- qué problema resuelve cada archivo,
- por qué existe cada capa,
- cómo se relacionan sesión, auth, roles y base de datos,
- y por qué las migraciones son un paso necesario cuando el proyecto crece.

---

## 2. Qué hueco cubre dentro del curso

Antes de este proyecto, el bloque Flask ya tenía:

- rutas,
- plantillas,
- CRUD,
- Blueprints,
- servicios,
- tests,
- y proyecto final.

Lo que faltaba era un proyecto cuyo eje central fuera:

- autenticación real,
- control de acceso,
- estado del usuario,
- y migraciones.

Por eso este proyecto existe: para enseñar el salto entre una app “que funciona” y una app “que empieza a parecer profesional”.

---

## 3. Orden recomendado para explicarlo en clase

### Sesión 1

- arquitectura general,
- modelos `User` y `NotaPrivada`,
- registro,
- login,
- logout.

### Sesión 2

- sesión de usuario,
- `before_request`,
- `g.user`,
- `login_required`,
- creación de notas privadas.

### Sesión 3

- rol admin,
- panel admin,
- `admin_required`,
- 403 y control de acceso.

### Sesión 4

- `Flask-Migrate`,
- diferencia entre `create_all()` y migraciones,
- comandos `db init`, `db migrate`, `db upgrade`.

### Sesión 5

- tests,
- ampliaciones,
- ejercicios,
- comparación con el proyecto Flask final.

---

## 4. Lectura guiada del proyecto

## Paso 1 · `app/__init__.py`

### Qué debe entender el alumno

- aquí nace la aplicación Flask,
- se carga la configuración,
- se registran extensiones y blueprints,
- y se carga el usuario desde la sesión.

### Conceptos a remarcar

- factory pattern,
- `instance_relative_config`,
- `before_request`,
- comando CLI `seed-auth`.

### Pregunta didáctica

> ¿Por qué guardar la carga del usuario en `before_request` y no repetir esa lógica en cada vista?

---

## Paso 2 · `app/config.py`

### Qué debe entender el alumno

- no es buena idea mezclar configuración y lógica,
- development, testing y production no tienen los mismos valores,
- la base de datos y la clave secreta deben estar desacopladas del código duro.

### Pregunta didáctica

> ¿Qué problema hay si un proyecto usa siempre la misma base de datos para desarrollo y tests?

---

## Paso 3 · `app/models.py`

### Qué debe entender el alumno

- `User` representa identidad y permisos.
- `NotaPrivada` representa un recurso del usuario.
- la password no se guarda directamente.
- hay relación 1:N entre usuario y notas.

### Conceptos clave

- hash de password,
- relación ORM,
- método de modelo (`is_admin`, `set_password`, `check_password`).

### Pregunta didáctica

> ¿Por qué `role` es una propiedad de negocio y no solo un detalle visual del panel?

---

## Paso 4 · `app/services/auth_utils.py`

### Qué debe entender el alumno

- auth no debe repetirse en todas las vistas,
- los decoradores permiten encapsular reglas,
- `login_required` y `admin_required` son piezas reutilizables.

### Conceptos clave

- `wraps`,
- decoradores personalizados,
- control de acceso backend.

### Pregunta didáctica

> ¿Por qué no basta con esconder el enlace “Admin” en la plantilla?

---

## Paso 5 · `app/blueprints/auth.py`

### Qué debe entender el alumno

- el registro y el login son dos flujos distintos,
- la validación del formulario debe ocurrir en backend,
- el login correcto termina guardando `user_id` en sesión.

### Qué enseñar aquí

- `request.form`
- `flash`
- redirect después de POST
- patrón PRG básico (Post/Redirect/Get)

### Ejercicio de aula

- forzar errores de registro,
- probar un email duplicado,
- probar login correcto e incorrecto.

---

## Paso 6 · `app/blueprints/main.py`

### Qué debe entender el alumno

- una vez autenticado, el usuario puede acceder a su zona privada,
- aquí aparece el valor práctico de la sesión,
- y el proyecto deja de ser solo “auth” para tener una pequeña funcionalidad real.

### Qué enseñar aquí

- `g.user`
- creación de entidad ligada al usuario
- mensajes flash

### Pregunta didáctica

> ¿Por qué una nota privada debe asociarse al usuario en backend y no confiar solo en un campo oculto del formulario?

---

## Paso 7 · `app/blueprints/admin.py`

### Qué debe entender el alumno

- admin no es otro tipo de plantilla, sino otro nivel de permiso,
- un usuario puede existir y estar activo o inactivo,
- cambiar rol cambia el alcance de acceso.

### Qué enseñar aquí

- panel protegido,
- cambios de estado,
- cambios de rol,
- 403.

### Ejercicio de aula

- entrar con alumno y provocar 403,
- entrar con admin y modificar un usuario.

---

## Paso 8 · Errores y plantillas

### Qué debe entender el alumno

- una aplicación web no está completa si no controla errores,
- 403, 404 y 500 forman parte del comportamiento normal.

### Qué enseñar aquí

- diferencia entre error funcional y error técnico,
- por qué conviene dar una salida controlada al usuario.

---

## 5. Flujo técnico completo de autenticación

## Registro

1. El usuario rellena formulario.
2. El backend valida campos.
3. Se comprueba unicidad de email.
4. Se genera hash.
5. Se guarda el usuario.
6. Se muestra mensaje de éxito.

## Login

1. El usuario envía email y password.
2. Se busca usuario activo.
3. Se compara hash.
4. Si es válido:
   - se guarda `user_id` en sesión
   - se redirige al inicio

## Carga de usuario

1. En cada petición:
   - se lee `session["user_id"]`
   - se consulta el usuario
   - se guarda en `g.user`

## Permisos

1. `login_required`
   - si no hay sesión, redirige a login
2. `admin_required`
   - si no es admin, responde 403

---

## 6. Flujo técnico completo de migraciones

## Antes de las migraciones

Con `db.create_all()` puedes crear tablas iniciales, pero si el modelo cambia:

- no tienes historial,
- no sabes qué cambió,
- y acabas recreando la base manualmente.

## Con migraciones

El flujo correcto es:

```powershell
python -m flask db init
python -m flask db migrate -m "descripcion del cambio"
python -m flask db upgrade
```

### Qué debe entender el alumno

- `init` prepara Alembic,
- `migrate` detecta cambios del modelo,
- `upgrade` los aplica a la base de datos.

### Ejercicio perfecto para esta unidad

Añadir un campo nuevo a `User`, por ejemplo:

- `ultimo_login`

y generar una migración real.

---

## 7. Comandos recomendados para el profesor

### Arranque mínimo

```powershell
./run.ps1
```

### Arranque manual completo

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
$env:FLASK_APP="app:create_app"
$env:APP_ENV="development"
python -m flask db init
python -m flask db migrate -m "init auth"
python -m flask db upgrade
python -m flask seed-auth
python -m flask run
```

### Tests

```powershell
./test.ps1
```

---

## 8. Escenarios de demostración en clase

### Demo 1 · Registro

- registrar un alumno,
- intentar registrar email duplicado,
- ver mensajes flash.

### Demo 2 · Login

- login correcto,
- login incorrecto,
- logout.

### Demo 3 · Zona privada

- acceder a `/perfil` sin sesión,
- acceder con sesión,
- crear nota privada.

### Demo 4 · Panel admin

- entrar como alumno y provocar 403,
- entrar como admin y cambiar un rol.

### Demo 5 · Migraciones

- añadir un campo nuevo al modelo,
- generar migración,
- explicar el fichero de migración.

---

## 9. Errores y bloqueos típicos del alumno

### “No entiendo dónde se guarda la sesión”

Explica que Flask guarda una cookie firmada y que el valor útil para la app es `user_id`.

### “Si oculto el botón Admin ya está protegido”

No. El backend debe verificar permisos siempre.

### “¿Por qué no usamos `create_all()` siempre?”

Porque cuando el modelo cambia necesitas un historial reproducible.

### “¿Por qué el test usa SQLite en memoria?”

Porque es rápido, limpio y no deja residuos.

---

## 10. Qué ampliaría yo después

### Ampliaciones fáciles

- edición de perfil,
- cambio de password,
- editar y borrar notas.

### Ampliaciones medias

- endpoint `/api/me`,
- auditoría simple,
- timestamps de login.

### Ampliaciones avanzadas

- token auth,
- confirmación por email,
- recuperación de password,
- integración de `Flask-Login`,
- CSRF más formal.

---

## 11. Comparación con el resto del bloque Flask

### Frente a `flask_proyecto_didactico`

- aquí ya hay usuarios reales,
- ya hay BD,
- y ya hay permisos.

### Frente a `Proyecto_Flask_Basico`

- aquí el foco no es CRUD básico,
- sino auth y control de acceso.

### Frente a `flask_proyecto_didactico (avanzado)`

- aquí aparece seguridad,
- no solo modularización.

### Frente a `Proyecto_Flask_Final`

- este proyecto especializa el bloque de auth,
- mientras el final integra muchas áreas del curso.

---

## 12. Conclusión docente

Este proyecto ya puede usarse como unidad fuerte del curso.

Si el objetivo es enseñar:

- login,
- sesiones,
- permisos,
- migraciones,

este proyecto ya cumple bien.

Si más adelante quieres subirlo a un nivel todavía más profesional, el siguiente salto natural sería:

- añadir API autenticada,
- o integrar `Flask-Login` y migraciones más ricas.
