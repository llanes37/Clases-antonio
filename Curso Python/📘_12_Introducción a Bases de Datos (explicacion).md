# 🐍 Clase 12 de Python — Bases de Datos con **SQLite** (Objetivos ampliados + código comentado)

**Autor:** Joaquín Rodríguez — *Guía didáctica práctica, pensada a fondo*

---

## 🎯 Objetivos de aprendizaje detallados (qué harás y por qué)

* **Modelar datos en tablas**: entender filas/columnas, **PRIMARY KEY autoincremental** y cuándo usar `NOT NULL`. Decidir tipos en SQLite (affinity: `INTEGER`, `TEXT`, `REAL`, `BLOB`) y sus implicaciones.
* **Ciclo de trabajo con `sqlite3`**: abrir **conexión** → crear **cursor** → ejecutar **SQL** → **commit** → **cerrar**. Por qué cada paso es necesario y qué pasa si lo omites.
* **Seguridad con placeholders `?`**: evitar inyección SQL y conversiones incorrectas de tipos; diferenciar `execute()` vs `executemany()`.
* **CRUD completo**: insertar, listar (con `SELECT *` y con proyección `SELECT col1,col2`), actualizar por criterio y borrar de forma segura.
* **Filtrar con `WHERE`**: operadores (`=`, `>`, `>=`, `LIKE`, `AND/OR`), ordenar (`ORDER BY`), y manejar el caso de **cero resultados** con mensajes claros.
* **Errores controlados**: capturar `sqlite3.Error`, explicar el fallo (mensaje y tipo), y **siempre** cerrar la conexión (even if it hurts).
* **Exportar resultados**: crear **CSV** con cabecera y **JSON** legible (`indent` + `ensure_ascii=False`), escogiendo columnas en orden lógico.
* **Buenas prácticas**: `with sqlite3.connect(DB) as con` (autocommit/rollback), `con.row_factory = sqlite3.Row` para acceder por nombre, `PRAGMA foreign_keys = ON` cuando haya relaciones.

> 🎨 **Convención de comentarios en el código:**
> `# *` qué hace la línea · `# !` advertencia/pitfall · `# ?` idea/variante · `# TODO:` práctica para ti.

---

## 🧩 Mapa del temario

1. Conceptos relacionales básicos
2. Conexión + creación de tabla
3. CRUD (Create/Read/Update/Delete)
4. SELECT con WHERE
5. Manejo de errores
6. Exportar a CSV/JSON
7. Laboratorio IA
8. Autoevaluación

---

## 1) Conceptos relacionales básicos

* **Tabla** = conjunto de **filas** (registros) con **columnas** (campos).
* **PK** (primary key) identifica de forma **única** una fila; usamos `INTEGER PRIMARY KEY AUTOINCREMENT` para un id consecutivo.
* **Tipos en SQLite** (affinity): no son rígidos como en otros motores, pero **debes validar** en la app.

**Mini‑tabla**

```
+----+----------+------+
| id | nombre   | edad |
+----+----------+------+
| 1  | Ana      | 25   |
| 2  | Luis     | 30   |
+----+----------+------+
```

---

## 2) Conexión + creación de tabla (DDL) — **código comentado**

```py
# * Conectamos/creamos la base de datos (archivo .db en el directorio actual)
# ! Si el archivo no existe, SQLite lo crea al conectar.
import sqlite3
from pathlib import Path

DB_FILE = "alumnos.db"
con = sqlite3.connect(DB_FILE)     # * abrir conexión
cur = con.cursor()                  # * crear cursor para ejecutar SQL

# * DDL: crear tabla si no existe.
# ! AUTOINCREMENT garantiza un id único; NOT NULL evita registros incompletos.
cur.execute('''
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

con.commit()                        # * confirmamos los cambios
con.close()                         # * cerramos SIEMPRE la conexión
print(f"✅ Base lista en {Path(DB_FILE).resolve()}")
```

**Por qué así:**

* `connect()` → crea/abre el archivo `.db`.
* `cursor()` → objeto que ejecuta sentencias SQL.
* `commit()` → hace persistentes los cambios (si no, podrías perderlos).
* `close()` → libera recursos y cierra el fichero.

---

## 3) CRUD completo — **código comentado**

```py
import sqlite3
DB_FILE = "alumnos.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()

# * CREATE (INSERT)
# ! Placeholders (?) evitan inyección SQL y manejan tipos correctamente.
alumnos_nuevos = [("Ana", 25), ("Luis", 30)]
cur.executemany("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", alumnos_nuevos)
con.commit()  # * confirmamos inserciones

# * READ (SELECT)
# ? Usar columnas explícitas hace el código más estable ante cambios de esquema
cur.execute("SELECT id, nombre, edad FROM alumnos ORDER BY id")
for id_, nombre, edad in cur.fetchall():
    print(f"id={id_} | nombre={nombre} | edad={edad}")

# * UPDATE: cambiamos edad de Ana
cur.execute("UPDATE alumnos SET edad=? WHERE nombre=?", (26, "Ana"))
print("Filas actualizadas:", cur.rowcount)  # * feedback
con.commit()

# * DELETE: eliminamos a Luis
cur.execute("DELETE FROM alumnos WHERE nombre=?", ("Luis",))
print("Filas eliminadas:", cur.rowcount)
con.commit()

con.close()  # * cerramos conexión
```

**Claves de lectura:**

* `executemany()` es más eficiente para varias filas.
* `rowcount` da una idea del impacto de `UPDATE/DELETE`.
* Ordenar en el `SELECT` te ahorra trabajo luego.

---

## 4) SELECT con WHERE — **código comentado**

```py
import sqlite3
DB_FILE = "alumnos.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()

# * WHERE con parámetro posicional
# ! Evita concatenar f-strings con valores; usa ( ? )
min_edad = 24
cur.execute(
    "SELECT id, nombre, edad FROM alumnos WHERE edad > ? ORDER BY edad DESC",
    (min_edad,)
)
resultados = cur.fetchall()

if not resultados:
    print("(sin resultados)")
else:
    for id_, nombre, edad in resultados:
        print(f"Mayor de {min_edad} → id={id_}, nombre={nombre}, edad={edad}")

con.close()
```

**Notas:** `LIKE 'A%'` para nombres que empiezan por A; combina **`AND`/`OR`** para filtros compuestos.

---

## 5) Manejo de errores — **código comentado**

```py
import sqlite3
DB_FILE = "alumnos.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()

try:
    # * Forzamos un error consultando una tabla que no existe
    cur.execute("SELECT * FROM tabla_inexistente")
except sqlite3.Error as e:
    # ! Captura genérica de errores de SQLite: sintaxis, tablas/columnas inexistentes, etc.
    print("⚠️ Error:", e.__class__.__name__, "→", e)
finally:
    # * Cerramos siempre, ocurra o no ocurra error
    con.close()
```

**Buenas prácticas:** captura el error, informa con claridad y asegúrate de **cerrar recursos**.

---

## 6) Exportar a CSV/JSON — **código comentado**

```py
import sqlite3, csv, json
from pathlib import Path

DB_FILE = "alumnos.db"
con = sqlite3.connect(DB_FILE)
cur = con.cursor()

# * Elegimos columnas y orden
cur.execute("SELECT id, nombre, edad FROM alumnos ORDER BY id")
datos = cur.fetchall()  # * lista de tuplas

# * CSV (Excel‑friendly): newline='' + UTF‑8 para acentos
with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "nombre", "edad"])  # * cabecera
    w.writerows(datos)                        # * filas

# * JSON (web/API): lista de dicts legible
alumnos = [{"id": r[0], "nombre": r[1], "edad": r[2]} for r in datos]
Path("alumnos.json").write_text(
    json.dumps(alumnos, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

con.close()
print("✅ Exportados a alumnos.csv y alumnos.json")
```

**Decisiones:** en CSV ponemos cabecera **humana**; en JSON usamos claves cortas y `indent` para facilitar la lectura.

---

## 7) Laboratorio IA — Mini‑agenda escolar (SQLite + CSV/JSON)

**Prompt Kit (copia/pega y ejecuta)**

1. *Generación*:

   > “Eres profesor de Python. Crea un mini‑sistema con **SQLite** (40–55 líneas) con tabla `alumnos(id, nombre, edad)` y tabla `cursos(id, nombre, profesor)`. Incluye funciones `insertar_*`, `listar_*` y `matricular(alumno_id, curso_id)` (tabla intermedia). Exporta `alumnos` a **CSV** y **JSON**. **Solo código Python**.”
2. *Alternativo*:

   > “Haz un **gestor de inventario**: `productos(id, nombre, precio)`, `ventas(id, producto_id, uds)` con **FOREIGN KEY** y `PRAGMA foreign_keys=ON`. Top‑3 productos por ventas.”
3. *Mejora*:

   > “Refactoriza con `with sqlite3.connect(DB) as con` y `con.row_factory = sqlite3.Row`. Usa placeholders en todas las consultas. Mantén < 60 líneas.”

**👉 Tu tarea**: pega el código en tu zona de práctica, ejecútalo, añade **validaciones** y un **resumen final** (nº filas, etc.).

---

## 8) Autoevaluación — “Sistema Escuela” paso a paso

1. Crea `sistema_escuela.db`.
2. Tabla `CURSOS(id, nombre, profesor)`.
3. Inserta **3** cursos.
4. Lista todos los cursos.
5. Actualiza el nombre de uno.
6. Elimina otro.
7. Exporta a **CSV** y **JSON**.
8. (Opcional) `ALUMNOS(id, nombre, edad)` y tabla intermedia `MATRICULAS(alumno_id, curso_id)` con `FOREIGN KEY`.

**Rúbrica**

* **Correcto**: CRUD + export correcto.
* **Excelente**: filtros/ordenaciones, manejo de errores claro, funciones bien nombradas.

---

## Apéndice A — `with`, transacciones y `row_factory`

```py
import sqlite3
DB = "alumnos.db"

with sqlite3.connect(DB) as con:        # * COMMIT automático si no hay excepciones
    con.row_factory = sqlite3.Row        # * filas accesibles por nombre
    cur = con.cursor()
    cur.execute("INSERT INTO alumnos(nombre,edad) VALUES(?,?)", ("Eva", 22))
    nuevo_id = cur.lastrowid             # * id autogenerado
    print("Nuevo id:", nuevo_id)
```

---

## Apéndice B — Índices, FKs y diseño

* Índices: `CREATE INDEX idx_alumnos_nombre ON alumnos(nombre)` para acelerar búsquedas por nombre.
* Claves foráneas: activa `PRAGMA foreign_keys=ON` cuando relaciones tablas.
* Normalización: evita datos duplicados; usa tablas relacionadas.

---

## ✅ Qué te llevas

* Diseñar tablas con criterios claros (PK, NOT NULL).
* Conectar y trabajar con `sqlite3` siguiendo el ciclo correcto.
* CRUD seguro con placeholders y commits a tiempo.
* Filtrar con `WHERE` y ordenar resultados.
* Exportar a **CSV/JSON** con codificación y formato legible.
* Tratar errores sin romper la app y cerrar recursos.
* Buenas prácticas: `with`, `row_factory`, \`PR
