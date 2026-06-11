# Proyecto Flask Auth + Migraciones

Proyecto didáctico para enseñar **autenticación web**, **sesiones**, **roles simples**, **protección de rutas**, **SQLAlchemy** y el flujo de **migraciones reales** con `Flask-Migrate`.

> **Idea central del proyecto:** cubrir el hueco entre “Flask modular” y “proyecto web más profesional”.  
> Aquí el foco no es tanto el CRUD de negocio, sino la **seguridad básica**, el **control de acceso** y la **evolución del esquema de la base de datos**.

---

## 1. Objetivo del proyecto

Este proyecto existe para que el alumno practique una fase muy importante del desarrollo web real:

- registrar usuarios,
- iniciar sesión,
- restringir rutas,
- gestionar roles,
- y entender por qué `db.create_all()` no basta cuando una aplicación crece.

Es el proyecto que introduce, de forma clara y gradual:

- **autenticación**,
- **sesión**,
- **admin simple**,
- y **migraciones**.

---

## 2. Qué enseña exactamente

### Bloque de autenticación

- Registro de usuarios.
- Login y logout con sesión.
- Password hasheada con `werkzeug.security`.
- Carga del usuario logueado en cada petición con `before_request`.

### Bloque de autorización

- Roles simples:
  - `student`
  - `admin`
- Rutas protegidas con:
  - `login_required`
  - `admin_required`

### Bloque de base de datos

- Modelos reales con SQLAlchemy:
  - `User`
  - `NotaPrivada`
- Relaciones básicas entre entidades.
- Estado del usuario (`activo`) y cambios de rol.

### Bloque de migraciones

- Integración de `Flask-Migrate`.
- Compatibilidad con:
  - `flask db init`
  - `flask db migrate`
  - `flask db upgrade`

### Bloque de testing

- Tests base para:
  - registro,
  - login,
  - acceso a rutas privadas,
  - permisos de admin.

---

## 3. Cuándo usar este proyecto dentro del curso

### Momento recomendado

Úsalo **después** de:

- `flask_proyecto_didactico (avanzado)`

y **antes** de:

- `Proyecto_Flask_Final`

### Por qué

Porque este proyecto enseña justo el salto que faltaba:

- pasar de una app modular,
- a una app con **usuarios reales**, **permisos** y **evolución controlada de BD**.

---

## 4. Arquitectura del proyecto

```text
Proyecto_Flask_Auth_Migraciones/
  app/
    __init__.py
    config.py
    extensions.py
    models.py
    errors.py
    services/
      auth_utils.py
    blueprints/
      main.py
      auth.py
      admin.py
    templates/
      base.html
      index.html
      login.html
      register.html
      perfil.html
      admin.html
      403.html
      404.html
      500.html
    static/
      css/style.css
  tests/
    conftest.py
    test_auth.py
    test_roles.py
  .env.example
  requirements.txt
  run.ps1
  test.ps1
  migrate.ps1
  GUIA_PASO_A_PASO.md
  EJERCICIOS.md
```

### Qué hace cada parte

- `app/__init__.py`
  - crea la aplicación,
  - carga configuración,
  - registra blueprints,
  - registra migraciones,
  - carga al usuario desde sesión,
  - y expone `seed-auth`.

- `config.py`
  - separa entornos:
    - development
    - testing
    - production

- `extensions.py`
  - centraliza:
    - `db`
    - `migrate`

- `models.py`
  - define los modelos:
    - `User`
    - `NotaPrivada`

- `services/auth_utils.py`
  - contiene la lógica reutilizable de autenticación y permisos.

- `blueprints/auth.py`
  - registro,
  - login,
  - logout.

- `blueprints/main.py`
  - portada,
  - perfil,
  - creación de notas privadas.

- `blueprints/admin.py`
  - panel protegido por rol admin,
  - activación/desactivación de usuarios,
  - cambio de rol.

---

## 5. Flujo funcional del proyecto

### Caso 1: usuario nuevo

1. Entra en `/register`
2. Rellena:
   - nombre
   - email
   - password
3. Se crea el usuario
4. La password se guarda hasheada
5. Se muestra mensaje flash
6. Se redirige al login

### Caso 2: login

1. El usuario entra en `/login`
2. Introduce email y password
3. El sistema:
   - busca usuario activo,
   - verifica el hash,
   - guarda `user_id` en sesión
4. Se redirige al inicio

### Caso 3: acceso privado

1. El usuario intenta entrar en `/perfil`
2. Si no hay sesión:
   - redirección a login
3. Si hay sesión:
   - se muestra el perfil

### Caso 4: acceso admin

1. El usuario intenta entrar en `/admin`
2. Si no es admin:
   - error 403
3. Si sí lo es:
   - accede al panel

---

## 6. Arranque rápido

### Opción 1: automática con PowerShell

```powershell
./run.ps1
```

Este script:

- crea `.venv` si no existe,
- instala dependencias,
- copia `.env.example` a `.env` si hace falta,
- y arranca Flask.

---

## 7. Arranque manual paso a paso

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
$env:FLASK_APP="app:create_app"
$env:APP_ENV="development"
python -m flask run
```

Abre:

```text
http://127.0.0.1:5000/
```

---

## 8. Cómo preparar las migraciones

### Primer uso

```powershell
$env:FLASK_APP="app:create_app"
python -m flask db init
python -m flask db migrate -m "init auth"
python -m flask db upgrade
```

### Seed de usuarios demo

```powershell
python -m flask seed-auth
```

### Credenciales demo

- `admin@demo.local` / `admin123`
- `alumno@demo.local` / `alumno123`

> **Nota didáctica:** las credenciales son simples porque esto es un entorno de aula, no un despliegue real.

---

## 9. Rutas principales

| Ruta | Método | Qué hace |
|------|--------|----------|
| `/` | GET | Portada del proyecto |
| `/register` | GET/POST | Registro de usuario |
| `/login` | GET/POST | Inicio de sesión |
| `/logout` | GET | Cierre de sesión |
| `/perfil` | GET | Zona privada |
| `/notas/crear` | POST | Crea una nota privada |
| `/admin` | GET | Panel admin |
| `/admin/toggle/<id>` | POST | Activa/desactiva usuario |
| `/admin/role/<id>` | POST | Cambia rol |

---

## 10. Modelos del proyecto

### `User`

Campos principales:

- `nombre`
- `email`
- `password_hash`
- `role`
- `activo`
- `created_at`

### `NotaPrivada`

Campos principales:

- `titulo`
- `contenido`
- `created_at`
- `user_id`

### Qué se pretende enseñar con estos modelos

No se ha elegido un dominio complejo a propósito. La idea es que el alumno concentre la atención en:

- usuarios,
- permisos,
- sesión,
- y relación con un recurso privado sencillo.

---

## 11. Qué debe entender el alumno al estudiar este proyecto

### 1. Password segura

La password **no se guarda en texto plano**.  
Se transforma en un hash y luego se compara usando funciones seguras.

### 2. Sesión

Una sesión no es “estar logueado mágicamente”, sino guardar un identificador en una cookie firmada por Flask.

### 3. Permisos

Una ruta protegida no depende de ocultar un botón en HTML, sino de comprobar permisos en el backend.

### 4. Migraciones

Cuando cambian los modelos:

- no basta con borrar la base y crearla otra vez,
- hay que aplicar cambios de esquema de forma controlada.

---

## 12. Testing

Para ejecutar tests:

```powershell
./test.ps1
```

O manualmente:

```powershell
python -m pytest tests -q
```

### Qué cubren ahora los tests

- registro y login,
- redirección si no hay sesión,
- acceso admin correcto,
- y acceso prohibido para usuarios sin rol admin.

---

## 13. Errores comunes

### “No module named flask_migrate”

Instala dependencias:

```powershell
pip install -r requirements.txt
```

### “flask db” no funciona

Asegúrate de tener:

```powershell
$env:FLASK_APP="app:create_app"
```

### El panel admin da 403

Eso significa que el usuario ha iniciado sesión, pero **no tiene rol admin**.

### No aparecen usuarios demo

Ejecuta:

```powershell
python -m flask seed-auth
```

---

## 14. Qué mejorar después

Este proyecto ya es útil y enseñable, pero se puede ampliar con:

- recuperación de password,
- cambio de password,
- edición de perfil,
- CSRF más explícito,
- validación más fuerte,
- API protegida,
- timestamps adicionales,
- y migraciones más avanzadas.

---

## 15. Material complementario

- [GUIA_PASO_A_PASO.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Auth_Migraciones/GUIA_PASO_A_PASO.md)
- [EJERCICIOS.md](/c:/Users/MediaMarktVillaverde/Desktop/ClasesOnlineJoaquin/cursos/Curso%20Python/Proyecto_Flask_Auth_Migraciones/EJERCICIOS.md)

---

## 16. Conclusión

`Proyecto_Flask_Auth_Migraciones` es el proyecto que faltaba para dejar la ruta Flask mucho más equilibrada.  
No compite con `Proyecto_Flask_Final`; lo prepara.

En una frase:

> si `Proyecto_Flask_Final` integra mucho contenido del curso, este proyecto enseña el salto clave hacia **auth + permisos + migraciones**, que es uno de los puntos más importantes del desarrollo web real.
