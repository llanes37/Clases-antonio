# Flask (Parte 2): Sesiones, Flash, Blueprints y Seguridad bÃ¡sica (CSRF)

**Autor:** JoaquÃ­n RodrÃ­guez  
**ContinuaciÃ³n de:** `14_flask_tutorial.py`  

---

## 1. Objetivo de esta unidad

En esta continuaciÃ³n pasas de â€œrutas sueltasâ€ a una **mini-app mÃ¡s realista**, aprendiendo:

- **Sesiones** (`session`) para recordar al usuario (login simple).
- **Mensajes flash** (`flash`) para feedback (Ã©xito/error).
- **Blueprints** para organizar una app por mÃ³dulos (auth / pÃ¡ginas / API).
- **Seguridad bÃ¡sica**: **CSRF token** en formularios (sin librerÃ­as externas).
- Buenas prÃ¡cticas: `url_for`, redirects, `abort`, `g`, configuraciÃ³n por entorno.

> Esta unidad estÃ¡ pensada para ser **100% didÃ¡ctica y ejecutable en un solo archivo**, igual que el patrÃ³n del curso.

---

## 2. Archivos de la unidad

- `📘_14_flask_parte2_sesiones_y_seguridad(explicacion).md` (este documento)
- `14_flask_parte2_sesiones_y_seguridad.py` (profesor, completo y comentado)
- `14_flask_parte2_sesiones_y_seguridad(alumno).py` (plantilla con TODOs)

---

## 3. Requisitos previos

- Python 3.8+
- Flask instalado:

```bash
pip install flask
```

Conocimientos recomendados:
- HTTP (GET/POST), formularios, JSON
- Lo visto en `14_flask_tutorial.py`

---

## 4. CÃ³mo ejecutar (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install flask
python "cursos/Curso Python/14_flask_parte2_sesiones_y_seguridad.py"
```

Abrir en el navegador:
- `http://127.0.0.1:5000/`

---

## 5. Conceptos clave (explicaciÃ³n corta y Ãºtil)

### 5.1 SesiÃ³n (`session`)
La sesiÃ³n en Flask suele guardarse en una **cookie firmada** (no en el servidor).

- Sirve para guardar datos pequeÃ±os: usuario, preferencias, token CSRFâ€¦
- Requiere `SECRET_KEY`.

**Importante:**
- No guardes datos sensibles â€œen crudoâ€ (contraseÃ±as, tokens reales de producciÃ³n).
- No guardes listas enormes (la cookie crecerÃ¡).

### 5.2 Flash (`flash`)
Mensajes temporales para el usuario:
- â€œLogin correctoâ€
- â€œFalta el nombreâ€
- â€œTarea creadaâ€

Se leen en la siguiente peticiÃ³n (tras redirect).

### 5.3 Blueprints
Permiten separar la app en â€œbloquesâ€:
- `auth` (login/logout)
- `pages` (home/perfil/tareas)
- `api` (JSON endpoints)

### 5.4 CSRF (Cross-Site Request Forgery)
Ataque tÃ­pico:
- Un usuario logueado visita una web maliciosa.
- Esa web dispara un POST a tu app â€œen segundo planoâ€.
- Si tu app no valida un token, ejecuta la acciÃ³n como si fuese el usuario.

SoluciÃ³n bÃ¡sica:
- Generar un token aleatorio por sesiÃ³n.
- Incluirlo como `<input type="hidden" name="csrf_token" ...>`.
- Validarlo en cada POST.

> En proyectos reales se suele usar `Flask-WTF`, pero aquÃ­ lo implementamos â€œa manoâ€ para entenderlo.

---

## 6. PrÃ¡cticas (TODO) recomendadas

### TODO 1 â€” Login con validaciÃ³n
En `14_flask_parte2_sesiones_y_seguridad(alumno).py`:
- Rechaza nombres vacÃ­os.
- Rechaza nombres demasiado cortos (por ejemplo `< 3`).
- Rechaza nombres con espacios si quieres (extra).

### TODO 2 â€” Proteger acciones con CSRF
- AÃ±ade y valida `csrf_token` en:
  - Logout
  - Crear tarea
  - Borrar tarea

### TODO 3 â€” API JSON (POST)
Implementa un endpoint `POST /api/tareas` que:
- Reciba JSON `{"texto": "..."}`.
- Valide que el texto no estÃ© vacÃ­o.
- AÃ±ada la tarea y devuelva JSON con la lista actualizada.

### TODO 4 â€” Reto extra (roles)
AÃ±ade un rol simple:
- Si el usuario es `"admin"`, permite borrar todas las tareas.
- Si no, devuelve `403`.

---

## 7. Mini-rÃºbrica (evaluaciÃ³n rÃ¡pida)

- Funciona el login/logout con sesiÃ³n.
- Formularios protegidos con CSRF.
- Blueprints bien separados (auth/pages/api).
- Validaciones claras y mensajes flash.
- API devuelve cÃ³digos HTTP correctos (200/201/400/401/403).

---

## 8. Siguiente paso natural (despuÃ©s de esta unidad)

Cuando esto te salga fluido, el siguiente salto es:
- Persistencia real con BD (Flask + SQLAlchemy + migraciones).
- AutenticaciÃ³n real (hash de contraseÃ±as, usuarios en BD).
- Testing de la app Flask con `pytest`.


