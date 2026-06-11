# Guía práctica de SQLAlchemy (estilo docente)

Esta guía acompaña al material de clase y al script `12_BBDD con SqlAlchemy.py`.
La idea es ofrecer explicaciones claras, ejemplos seguros y tareas prácticas ordenadas para que el alumno complete.

Usa la convención de Better Comments del curso:

* `# *` explicación / definición
* `# !` advertencia / pitfall
* `# ?` nota o alternativa
* `# TODO:` práctica para el alumno

---

## Objetivos de la unidad

- Entender el patrón Engine + Declarative Base + Session.
- Definir modelos (clases) que representen tablas y campos.
- Realizar operaciones CRUD usando la API ORM de SQLAlchemy.
- Manejar errores y transacciones con rollback.
- Exportar y preparar datos para CSV/JSON (opcional).

## Requisitos

Instala SQLAlchemy si aún no está disponible:

```sh
pip install SQLAlchemy
```

Python 3.8+ recomendado. Para ejecutar los ejemplos locales usamos SQLite (`sqlite:///academia.db`).

---

## Mapa del temario (lo que verás en clase / en el script)

1. Conceptos y motivación (ORM)
2. Engine y Base declarativa
3. Modelo ejemplo: `Usuario`
4. Crear tablas (`create_all`) y abrir sesión
5. CRUD con `Session` y `with` (insert/read/filter/update/delete)
6. Manejo de errores y rollback
7. Exportar resultados (CSV/JSON) — práctica opcional
8. Laboratorio IA + Autoevaluación

---

## 1) ¿Qué es un ORM y por qué usar SQLAlchemy?  # *

Breve: un ORM permite mapear tablas a clases Python, lo que facilita trabajar con datos como objetos,
reduce errores de concatenación SQL y facilita el cambio de motor (SQLite → Postgres) sin reescribir lógica.

## 2) Engine y Base declarativa — ejemplo comentado  # *

```py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DB_URL = 'sqlite:///academia.db'
engine = create_engine(DB_URL, echo=False, future=True)  # echo=True para debug
Base = declarative_base()
```

# ? Por qué `future=True`: prepara la API más moderna y evita warnings en versiones recientes.

## 3) Modelo de ejemplo: `Usuario` — explicación y buenas prácticas  # *

```py
from sqlalchemy import Column, Integer, String, DateTime, func

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    nombre = Column(String(50))
    apellido1 = Column(String(50))
    apellido2 = Column(String(50))
    creado = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Usuario id={self.id} username={self.username!r}>"
```

# ! Evita definir `default=datetime.now()` sin `server_default` si quieres que la BD gestione el valor.

## 4) Crear tablas y preparar sesiones  # *

```py
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# Crear tablas (no borra nada existente)
Base.metadata.create_all(engine)
```

Usa `with SessionLocal() as session:` para asegurar cierre automático de la sesión.

## 5) CRUD: ejemplos comentados (usa `with`)  # *

### Insertar

```py
with SessionLocal() as session:
    u = Usuario(username='jvazara', nombre='Jose', apellido1='Vázquez')
    session.add(u)
    session.commit()
```

### Leer (SELECT)

```py
with SessionLocal() as session:
    usuarios = session.query(Usuario).all()
    for u in usuarios:
        print(u.username, u.nombre)
```

### Filtrar y ordenar

```py
with SessionLocal() as session:
    res = session.query(Usuario).filter(Usuario.nombre.ilike('J%')).order_by(Usuario.id.desc()).all()
```

### Actualizar

```py
with SessionLocal() as session:
    u = session.query(Usuario).filter_by(username='jvazara').first()
    if u:
        u.nombre = 'José Ignacio'
        session.commit()
```

### Eliminar

```py
with SessionLocal() as session:
    u = session.query(Usuario).filter_by(username='ssanubi').first()
    if u:
        session.delete(u)
        session.commit()
```

## 6) Manejo de errores y transacciones  # *

Siempre captura errores de SQLAlchemy y haz rollback cuando sea necesario:

```py
from sqlalchemy.exc import SQLAlchemyError

with SessionLocal() as session:
    try:
        # operaciones de escritura
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print('⚠️ Error de BD:', e)
```

## 7) Exportar resultados (CSV / JSON) — práctica opcional  # ?

Extrae filas y escribe CSV o JSON tal y como hacemos en la unidad de SQLite.

## 8) Laboratorio IA — Prompt kit y ejercicio guiado  # *

Usa este prompt en la sección de Laboratorio del script para pedir a la IA que genere código de apoyo:

"Eres profesor de Python. Genera un script SQLite usando SQLAlchemy que:
- Cree `academia.db` y las tablas `usuarios(id, username, nombre, apellido1, apellido2)` y `cursos(id,nombre,profesor)`.
- Inserte 5 usuarios y 3 cursos.
- Liste usuarios y cursos, muestre usuarios por curso (si hay relación).
- Actualice y elimine registros con ejemplos.
Solo código Python, con transacciones seguras y `with SessionLocal()`.
"

### Idea práctica para la clase

- Pega el código generado por la IA en tu zona de pruebas.
- Añade validaciones y `print()` resumidos (nº filas) al final.

---

## Autoevaluación (sugerida para entregar)

1. Crea `academia.db` y la tabla `usuarios` con el modelo del curso.
2. Inserta 3 usuarios diferentes.
3. Lista todos los usuarios y exporta a `usuarios.csv`.
4. Actualiza el nombre de uno y elimina otro.
5. Implementa manejo de errores (simula una inserción inválida y captura la excepción).

Rúbrica: CRUD correcto (50%), manejo de errores (25%), exportación CSV (25%).

---

## Apéndice — buenas prácticas rápidas

- Usa `SessionLocal()` con `with` para asegurar cierre.
- Evita `drop_all()` en ejemplos: no se debe borrar datos en demos.
- Prefiere `server_default=func.now()` para marcas de tiempo cuando sea posible.
- Para relaciones, estudia `relationship` y `ForeignKey` en módulos siguientes.

---

Si quieres que deje aquí también un ejemplo resuelto de mini‑CLI (auto‑evaluación) para el profesor, lo añado; la versión alumno permanecerá como plantilla con TODOs.

