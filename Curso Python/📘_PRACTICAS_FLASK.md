# 🌐 PRÁCTICAS GUIADAS — Flask Tutorial

Autor: Joaquín | Página: https://clasesonlinejoaquin.es/

---

## 📋 Índice de Prácticas

1. [Configuración inicial](#configuración-inicial)
2. [Práctica 1: Rutas básicas](#práctica-1-rutas-básicas)
3. [Práctica 2: Rutas con parámetros](#práctica-2-rutas-con-parámetros)
4. [Práctica 3: Formularios POST](#práctica-3-formularios-post)
5. [Práctica 4: Query Strings](#práctica-4-query-strings)
6. [Práctica 5: API JSON](#práctica-5-api-json)
7. [Práctica 6: Manejo de errores](#práctica-6-manejo-de-errores)
8. [Retos avanzados](#retos-avanzados)

---

## Configuración inicial

### Paso 1: Crear entorno virtual

```bash
python -m venv env
```

### Paso 2: Activar (Windows)

```bash
.\env\Scripts\activate
```

### Paso 3: Instalar Flask

```bash
pip install flask
```

### Paso 4: Ejecutar

```bash
python "cursos/Curso Python/14_flask_tutorial.py"
```

### Paso 5: Abrir en navegador

```
http://127.0.0.1:5000/
```

---

## Práctica 1: Rutas básicas

### 🎯 Objetivo

Entender cómo Flask mapea URLs a funciones Python.

### 📝 Tarea

1. Navega a `http://127.0.0.1:5000/`
   - ¿Qué función se ejecuta?
   - ¿Qué devuelve?

2. Navega a `http://127.0.0.1:5000/about`
   - ¿Diferencia con la anterior?

3. **Añade una nueva ruta** en el archivo `14_flask_tutorial.py`:

```python
@app.route("/contacto")
def contacto():
    """📧 Página de contacto."""
    return """
    <h1>Contacto</h1>
    <p>Email: hola@clasesonlinejoaquin.es</p>
    <a href="/">Volver</a>
    """
```

4. Guarda el archivo y recarga el navegador.
5. Visita `http://127.0.0.1:5000/contacto`

**✅ Éxito si**: Ves tu página de contacto personalizada.

---

## Práctica 2: Rutas con parámetros

### 🎯 Objetivo

Recibir valores dinámicos en la URL y usarlos en la respuesta.

### 📝 Tarea

1. Navega a `http://127.0.0.1:5000/saluda/Juan`
   - Cambia "Juan" por tu nombre
   - ¿Ves el cambio en la respuesta?

2. Navega a `http://127.0.0.1:5000/suma/10/20`
   - ¿Cuál es el resultado?
   - Prueba con otros números

3. **Añade una nueva ruta tipada**:

```python
@app.route("/precio/<float:monto>")
def aplicar_descuento(monto: float):
    """💰 Aplica 10% de descuento."""
    descuento = monto * 0.10
    final = monto - descuento
    return f"""
    <h2>Calculadora de descuentos</h2>
    <p>Precio original: ${monto:.2f}</p>
    <p>Descuento 10%: ${descuento:.2f}</p>
    <p><strong>Precio final: ${final:.2f}</strong></p>
    <a href="/">Volver</a>
    """
```

4. Prueba:
   - `http://127.0.0.1:5000/precio/100`
   - `http://127.0.0.1:5000/precio/50.5`
   - `http://127.0.0.1:5000/precio/abc` (¿qué ocurre?)

**✅ Éxito si**: El descuento se calcula correctamente y `abc` devuelve 404.

---

## Práctica 3: Formularios POST

### 🎯 Objetivo

Enviar datos desde HTML usando formularios POST.

### 📝 Tarea

1. En la página principal (`http://127.0.0.1:5000/`), verás el formulario "1️⃣ Formulario (POST)".
2. Escribe tu nombre y envía.
3. Deberías ver: "Hola, <tu nombre>!"

4. **Modifica la ruta `/procesar`** para almacenar datos en una lista:

```python
# ARRIBA de app = Flask(__name__), añade:
historial = []

# En la función procesar(), antes de renderizar:
@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = (request.form.get("nombre") or "").strip()
    if not nombre:
        return redirect(url_for("inicio"))
    
    historial.append(nombre)  # ! Guardar en lista
    
    return render_template_string(RESULTADO_HTML, title="Resultado", nombre=nombre)
```

5. **Crea una nueva ruta para mostrar el historial**:

```python
@app.route("/historial")
def ver_historial():
    """📜 Muestra todos los nombres enviados."""
    items = "".join([f"<li>{n}</li>" for n in historial])
    return f"""
    <h2>Historial de nombres</h2>
    <ul>{items}</ul>
    <a href="/">Volver</a>
    """
```

6. Envía varios nombres y visita `http://127.0.0.1:5000/historial`

**✅ Éxito si**: Ves la lista de todos los nombres enviados.

---

## Práctica 4: Query Strings

### 🎯 Objetivo

Usar parámetros GET (en la URL sin cambiar la ruta).

### 📝 Tarea

1. Navega a `http://127.0.0.1:5000/buscar?q=flask&page=1`
   - Abre DevTools (F12) → Network → verás JSON
   - Modifica `q` y `page`

2. **Crea una ruta de filtrado de estudiantes**:

```python
# ARRIBA, añade lista de estudiantes:
estudiantes_db = [
    {"id": 1, "nombre": "Ada", "edad": 20},
    {"id": 2, "nombre": "Bob", "edad": 22},
    {"id": 3, "nombre": "Carlos", "edad": 19},
    {"id": 4, "nombre": "Diana", "edad": 21},
]

# Ahora, nueva ruta:
@app.route("/api/estudiantes")
def listar_estudiantes():
    """🎓 Lista estudiantes, filtrable por edad mínima."""
    edad_min = int(request.args.get("edad_min", 18))
    filtrados = [e for e in estudiantes_db if e["edad"] >= edad_min]
    return jsonify(total=len(filtrados), estudiantes=filtrados)
```

3. Prueba:
   - `http://127.0.0.1:5000/api/estudiantes`
   - `http://127.0.0.1:5000/api/estudiantes?edad_min=20`
   - `http://127.0.0.1:5000/api/estudiantes?edad_min=22`

**✅ Éxito si**: El filtro funciona y devuelve JSON correcto.

---

## Práctica 5: API JSON

### 🎯 Objetivo

Crear endpoints que reciben y devuelven JSON (sin HTML).

### 📝 Tarea

1. Abre DevTools (F12) → Console
2. Copia y pega este código:

```javascript
fetch('/api/echo?q=hola')
  .then(r => r.json())
  .then(d => console.log(d))
```

3. Deberías ver: `{ok: true, echo: "hola"}`

4. **Prueba POST con JSON**:

```javascript
fetch('/api/saludo', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({nombre: 'Ada'})
})
  .then(r => r.json())
  .then(d => console.log(d))
```

5. **Crea una API de notas**:

```python
# Arriba:
notas = []

# Nueva ruta:
@app.route("/api/notas", methods=["GET", "POST"])
def gestionar_notas():
    """📝 GET: lista notas; POST: añade nota."""
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        titulo = str(data.get("titulo", "")).strip()
        contenido = str(data.get("contenido", "")).strip()
        
        if not titulo or not contenido:
            return jsonify(ok=False, error="Faltan campos"), 400
        
        notas.append({"titulo": titulo, "contenido": contenido})
        return jsonify(ok=True, total=len(notas)), 201
    
    return jsonify(ok=True, notas=notas)
```

6. Prueba (en consola):

```javascript
// GET
fetch('/api/notas').then(r => r.json()).then(d => console.log(d))

// POST
fetch('/api/notas', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({titulo: 'Mi nota', contenido: 'Contenido aquí'})
})
  .then(r => r.json())
  .then(d => console.log(d))

// GET de nuevo (verás la nota añadida)
fetch('/api/notas').then(r => r.json()).then(d => console.log(d))
```

**✅ Éxito si**: Puedes crear notas y recuperarlas vía API JSON.

---

## Práctica 6: Manejo de errores

### 🎯 Objetivo

Entender cómo Flask maneja 404 y 500.

### 📝 Tarea

1. Visita `http://127.0.0.1:5000/ruta-que-no-existe`
   - Verás JSON: `{"error": "Ruta no encontrada (404)", ...}`
   - Este es tu manejador 404

2. Visita `http://127.0.0.1:5000/error-intencional`
   - Se provoca un RuntimeError
   - Ves el traceback (porque debug=True)
   - En producción, sería JSON genérico

3. **Crea una ruta con validación**:

```python
@app.route("/api/validar-email/<email>")
def validar_email(email: str):
    """📧 Valida formato de email."""
    if "@" not in email or "." not in email:
        return jsonify(ok=False, error="Email inválido"), 400
    return jsonify(ok=True, email=email)
```

4. Prueba:
   - `http://127.0.0.1:5000/api/validar-email/user@example.com` → ✅
   - `http://127.0.0.1:5000/api/validar-email/invalido` → ❌ (400)

**✅ Éxito si**: Los errores devuelven código HTTP correcto y JSON descriptivo.

---

## Retos avanzados

### Reto 1: Contador de visitas

```python
# Arriba:
contador = 0

@app.before_request
def contar_visita():
    global contador
    contador += 1

@app.route("/api/stats")
def estadisticas():
    """📊 Devuelve número de visitas."""
    return jsonify(total_visitas=contador)
```

**Tarea**: Visita varias páginas, luego `/api/stats`. ¿Ves el contador incrementarse?

---

### Reto 2: Calculadora mejorada

```python
@app.route("/api/calc/<operacion>/<int:a>/<int:b>")
def calculadora_mejorada(operacion: str, a: int, b: int):
    """🧮 Calculadora con múltiples operaciones."""
    operacion = operacion.lower()
    
    operaciones = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "mult": lambda x, y: x * y,
        "div": lambda x, y: x / y if y != 0 else None,
        "potencia": lambda x, y: x ** y,
    }
    
    if operacion not in operaciones:
        return jsonify(ok=False, error=f"Op '{operacion}' desconocida"), 400
    
    try:
        resultado = operaciones[operacion](a, b)
        return jsonify(ok=True, operacion=operacion, a=a, b=b, resultado=resultado)
    except ZeroDivisionError:
        return jsonify(ok=False, error="División por cero"), 400
```

---

### Reto 3: Sistema de usuarios mock

```python
usuarios = {
    "1": {"id": 1, "nombre": "Ada", "email": "ada@example.com"},
    "2": {"id": 2, "nombre": "Bob", "email": "bob@example.com"},
}

@app.route("/api/usuario/<id>")
def obtener_usuario(id: str):
    """👤 Devuelve usuario por ID."""
    if id not in usuarios:
        return jsonify(ok=False, error="Usuario no encontrado"), 404
    return jsonify(ok=True, usuario=usuarios[id])

@app.route("/api/usuarios", methods=["POST"])
def crear_usuario():
    """➕ Crea un nuevo usuario."""
    data = request.get_json(silent=True) or {}
    nombre = str(data.get("nombre", "")).strip()
    email = str(data.get("email", "")).strip()
    
    if not nombre or not email or "@" not in email:
        return jsonify(ok=False, error="Datos inválidos"), 400
    
    nuevo_id = str(max(int(k) for k in usuarios.keys()) + 1)
    usuarios[nuevo_id] = {"id": int(nuevo_id), "nombre": nombre, "email": email}
    
    return jsonify(ok=True, usuario=usuarios[nuevo_id]), 201
```

---

## 📚 Recursos

- **Documentación Flask**: https://flask.palletsprojects.com/
- **HTTP Status Codes**: https://httpwg.org/specs/rfc9110.html#status.codes
- **JSON**: https://www.json.org/
- **Jinja2 Templates**: https://jinja.palletsprojects.com/

---

## ❓ Preguntas frecuentes

### P: ¿Por qué mi ruta no funciona?
**R**: Verifica que:
1. La URL es exacta (mayúsculas/minúsculas)
2. El servidor está corriendo (sin errores en terminal)
3. Si cambias código, guarda y recarga el navegador (Ctrl+R)

### P: ¿Cómo envío datos en POST desde JavaScript?
**R**: Usa `fetch()`:
```javascript
fetch('/ruta', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({clave: 'valor'})
})
```

### P: ¿Los datos persisten entre reinicios?
**R**: No. Están en memoria RAM. Para persistencia, necesitas una base de datos (SQLite, PostgreSQL, etc.).

### P: ¿Cómo despliego esto en producción?
**R**: Necesitas:
1. Servidor (Heroku, Render, AWS, DigitalOcean, etc.)
2. Base de datos
3. WSGI server (gunicorn, uWSGI)
4. SSL/HTTPS

---

**¡Felicidades! 🎉 Has completado el tutorial de Flask.** Ahora puedes:
- ✅ Crear rutas y endpoints
- ✅ Leer parámetros (URL, query string, formularios, JSON)
- ✅ Devolver HTML y JSON
- ✅ Manejar errores
- ✅ Crear APIs REST básicas

**Próximos pasos**: Flask con base de datos, autenticación, testing, despliegue.

Autor: Joaquín | https://clasesonlinejoaquin.es/
