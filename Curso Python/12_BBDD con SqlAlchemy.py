# =========================================================================================
#  🐍 PYTHON CLASE 12 — Bases de Datos con SQLAlchemy (ORM)
#  ────────────────────────────────────────────────────────────────────────────────────────
#  Objetivos en esta clase:
#    * Qué es un ORM y por qué usar SQLAlchemy
#    * Preparar Engine y Base declarativa
#    * Definir un Modelo (tabla) con columnas y claves
#    * Crear la base de datos y abrir Sesiones
#    * CRUD completo con manejo de errores (commit/rollback)
#    * Autoevaluación con un mini‑gestor via ORM
#
#  🎨 Better Comments:
#    # ! importante   ·  # * definición/foco   ·  # ? idea/nota
#    # TODO: práctica  ·  # NOTE: apunte útil   ·  # // deprecado
# =========================================================================================

from datetime import datetime
from typing import Optional

from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# * Configuración general ---------------------------------------------------------------
DB_URL = "sqlite:///academia.db"  # Archivo SQLite local
RUN_INTERACTIVE = True
PAUSE = False

# * Infraestructura ORM -----------------------------------------------------------------
engine = create_engine(DB_URL, echo=False, future=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


# * Utilidades ---------------------------------------------------------------------------
def pause(msg: str = "Pulsa Enter para continuar..."):
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass


def encabezado(titulo: str):
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


# =========================================================================================
#  SECCIÓN 1 · Conceptos: ¿Qué es un ORM? ¿Qué aporta SQLAlchemy?
# =========================================================================================
def seccion_1_conceptos():
    encabezado("SECCIÓN 1 · Conceptos ORM y SQLAlchemy")

    # * TEORÍA
    # -----------------------------------------------------------------
    # Un ORM (Object‑Relational Mapper) permite trabajar con una BD relacional
    # usando clases y objetos en lugar de escribir SQL directo en cada paso.
    #
    # SQLAlchemy proporciona:
    # - Engine: conexión a la BD y gestión del dialecto (SQLite, Postgres, MySQL...).
    # - Base declarativa: clase base para declarar modelos/tablas como clases Python.
    # - Session: unidad de trabajo para persistir cambios (add/commit/delete/rollback).
    # -----------------------------------------------------------------

    # TODO: (Tema: TU RESUMEN)
    # Escribe con tus palabras en 1‑2 líneas qué son: Engine, Base, Session.


# =========================================================================================
#  SECCIÓN 2 · Definir el Modelo (tabla) con la Base declarativa
# =========================================================================================
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    nombre = Column(String(50))
    apellido1 = Column(String(50))
    apellido2 = Column(String(50))
    # server_default: valor generado por la BD; alternativa: default=datetime.now
    creado = Column(DateTime, server_default=func.now())

    def __repr__(self) -> str:  # Representación útil para debug/logs
        return f"<Usuario id={self.id} username={self.username!r}>"


def seccion_2_modelo():
    encabezado("SECCIÓN 2 · Modelo declarativo")

    # * TEORÍA
    # -----------------------------------------------------------------
    # - El modelo 'Usuario' define la estructura de la tabla 'usuarios'.
    # - Columnas: id (PK), username (único y obligatorio), nombre y apellidos, creado.
    # - __repr__ ayuda a imprimir objetos de forma amigable.
    # -----------------------------------------------------------------

    # TODO: (Tema: OTRO MODELO)
    # Crea un segundo modelo 'Curso' con columnas: id (PK), nombre (String, NOT NULL), profesor (String).


# =========================================================================================
#  SECCIÓN 3 · Crear tablas y preparar la sesión
# =========================================================================================
def seccion_3_init_bd():
    encabezado("SECCIÓN 3 · Crear tablas y sesión")

    # * Crear tablas si no existen
    Base.metadata.create_all(engine)
    print("✅ Tablas creadas/verificadas en la BD.")

    # * Crear una sesión de trabajo
    session = SessionLocal()
    print("✅ Sesión abierta.")
    session.close()
    print("✅ Sesión cerrada.")

    # TODO: (Tema: PROBAR CONEXIÓN)
    # Abre una sesión, ejecuta una consulta simple (count de usuarios) y ciérrala.


# =========================================================================================
#  SECCIÓN 4 · CRUD con Session: crear, leer, filtrar, actualizar, eliminar
# =========================================================================================
def seccion_4_crud_basico():
    encabezado("SECCIÓN 4 · CRUD con ORM")

    # * Insertar registros ---------------------------------------------------------------
    try:
        with SessionLocal() as session:
            u1 = Usuario(username="jvazara", nombre="Jose", apellido1="Vázquez", apellido2="Arantegui")
            u2 = Usuario(username="ssanubi", nombre="Santiago", apellido1="Santolaria", apellido2="Ubieto")
            session.add_all([u1, u2])
            session.commit()
            print("✅ Insertados:", u1, u2)
    except SQLAlchemyError as e:
        print("⚠️ Error al insertar:", e)

    # * Leer todos los usuarios ----------------------------------------------------------
    try:
        with SessionLocal() as session:
            usuarios = session.query(Usuario).all()
            print("\n📋 Usuarios actuales:")
            for u in usuarios:
                print(u.username, u.nombre, u.apellido1, u.apellido2, u.creado)
    except SQLAlchemyError as e:
        print("⚠️ Error al consultar:", e)

    # * Filtrar por nombre ----------------------------------------------------------------
    try:
        with SessionLocal() as session:
            usuarios_jose = session.query(Usuario).filter(Usuario.nombre == "Jose").all()
            print("\n🔎 Usuarios con nombre 'Jose':")
            for u in usuarios_jose:
                print(u.username, u.nombre)
    except SQLAlchemyError as e:
        print("⚠️ Error en filtro:", e)

    # * Actualizar un registro -----------------------------------------------------------
    try:
        with SessionLocal() as session:
            u = session.query(Usuario).filter(Usuario.username == "jvazara").first()
            if u:
                u.nombre = "José Ignacio"
                session.commit()
                print("\n🔄 Usuario actualizado:", u.username, u.nombre)
            else:
                print("\n(Usuario 'jvazara' no encontrado para actualizar)")
    except SQLAlchemyError as e:
        print("⚠️ Error al actualizar:", e)

    # * Eliminar un registro -------------------------------------------------------------
    try:
        with SessionLocal() as session:
            u = session.query(Usuario).filter(Usuario.username == "ssanubi").first()
            if u:
                session.delete(u)
                session.commit()
                print("\n🗑 Usuario eliminado:", u.username)
            else:
                print("\n(Usuario 'ssanubi' no encontrado para eliminar)")
    except SQLAlchemyError as e:
        print("⚠️ Error al eliminar:", e)


# =========================================================================================
#  SECCIÓN 5 · Manejo de errores y transacciones (rollback)
# =========================================================================================
def seccion_5_errores():
    encabezado("SECCIÓN 5 · Errores y transacciones")

    # * TEORÍA
    # -----------------------------------------------------------------
    # - Envuelve commits en try/except SQLAlchemyError.
    # - Si algo falla: session.rollback() para deshacer la transacción.
    # - Cierra siempre la sesión (with SessionLocal(): ... lo hace por ti).
    # -----------------------------------------------------------------

    # TODO: (Tema: FORZAR ERROR)
    # Intenta insertar un usuario con username None (violará NOT NULL) y captura el error.


# =========================================================================================
#  SECCIÓN 6 · Autoevaluación: mini‑gestor con ORM (CLI simple)
# =========================================================================================
def seccion_6_autoevaluacion():
    encabezado("SECCIÓN 6 · Autoevaluación: mini‑gestor ORM")

    # * ENUNCIADO
    # -----------------------------------------------------------------
    # Implementa un mini‑menú (en esta misma función o en otra) con opciones:
    #   1) Insertar usuario (username, nombre, apellido1, apellido2)
    #   2) Listar usuarios
    #   3) Actualizar nombre por username
    #   4) Eliminar por username
    # Usa SessionLocal(), manejo de errores y commits/rollbacks.
    # -----------------------------------------------------------------

    # --- ZONA DEL ALUMNO ---------------------------------------------------------------
    # Escribe aquí el CLI minimalista. Mantén pocas líneas y mensajes claros.
    pass


# =========================================================================================
#  MENÚ PRINCIPAL
# =========================================================================================
def menu():
    while True:
        print("\nMENÚ · SQLAlchemy (ORM)")
        print("  1) Conceptos ORM")
        print("  2) Modelo declarativo")
        print("  3) Crear tablas y sesión")
        print("  4) CRUD básico")
        print("  5) Errores y transacciones")
        print("  6) Autoevaluación (mini‑gestor)")
        print("  0) Salir")

        try:
            op = int(input("Opción: ")) if RUN_INTERACTIVE else 7  # atajo para no interactivo
        except Exception:
            print("! Opción no válida.")
            continue

        if not RUN_INTERACTIVE:
            # Ejecuta todas las secciones una vez y termina (evita bucles infinitos)
            seccion_1_conceptos()
            seccion_2_modelo()
            seccion_3_init_bd()
            seccion_4_crud_basico()
            seccion_5_errores()
            seccion_6_autoevaluacion()
            break

        if op == 0:
            print("¡Hasta la próxima!")
            break
        elif op == 1:
            seccion_1_conceptos(); pause()
        elif op == 2:
            seccion_2_modelo(); pause()
        elif op == 3:
            seccion_3_init_bd(); pause()
        elif op == 4:
            seccion_4_crud_basico(); pause()
        elif op == 5:
            seccion_5_errores(); pause()
        elif op == 6:
            seccion_6_autoevaluacion(); pause()
        else:
            print("! Elige una opción del 0 al 6.")


# =========================================================================================
#  EJECUCIÓN
# =========================================================================================
if __name__ == "__main__":
    if not RUN_INTERACTIVE:
        # modo rápido: ejecuta todo y sale
        menu()
    else:
        menu()

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base=declarative_base() # se crea una clase base para las tablas de la base de datos
engine = create_engine('sqlite:///academia.db') # se crea un motor para la base de datos
class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usename = Column(String(50), nullable=False, unique=True)
    nombre = Column(String(50))
    apellido1 = Column(String(50))
    apellido2 = Column(String(50))
    creado = Column(DateTime, default=datetime.now())

    def __init__(self, usename, nombre, apellido1, apellido2): # se define el metodo 
        self.usename=usename
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
    def __str__(self): # se define el metodo __str__ para que al imprimir el objeto se muestre el mensaje
        return f'Añadido el usuario: {self.usename}'
    
Session = sessionmaker(engine) # se crea una clase para interactuar con la base de datos
session = Session() # se crea una sesion para interactuar con la base de datos

Base.metadata.drop_all(engine) # si existe, elimina la tabla de la base de datos
Base.metadata.create_all(engine) # crea la tabla en la base de datos

##################### AÑADIR UN REGISTRO A LA TABLA USUARIOS #############################
usuario1 = Usuarios('jvazara', 'Jose', 'Vázquez', 'Arantegui')
usuario2 = Usuarios('ssanubi', 'Santiago', 'Santolaria', 'Ubieto')
session.add(usuario1)
session.add(usuario2)
session.commit()
print(usuario1)
print(usuario2)
##################### CONSULTAR LOS REGISTROS DE UNA TABLA ################################
print('Todos los usuarios:')
usuarios = session.query(Usuarios).all() # se obtienen todos los registros de la tabla
for usuario in usuarios:
    print(usuario.usename, usuario.nombre, usuario.apellido1, usuario.apellido2, usuario.creado)
print('Usuarios con nombre Jose:')
usuarios = session.query(Usuarios).filter(Usuarios.nombre=='Jose') # solo el de nombre Jose
for usuario in usuarios:
    print(usuario.usename, usuario.nombre, usuario.apellido1, usuario.apellido2, usuario.creado) 

##################### ACTUALIZAR UN REGISTRO DE LA TABLA USUARIOS ##########################
usuario = session.query(Usuarios).filter(Usuarios.usename=='jvazara').first() # se obtiene el primer registro con usename=jvazara
usuario.nombre = 'José Ignacio' # se actualiza el nombre
session.commit() # se confirma la actualización
print('Usuario actualizado:')
print(usuario.usename, usuario.nombre, usuario.apellido1, usuario.apellido2, usuario.creado)

##################### ELIMINAR UN REGISTRO DE LA TABLA USUARIOS ##########################
usuario = session.query(Usuarios).filter(Usuarios.usename=='ssanubi').first() # se obtiene el primer registro con usename=ssanubi
session.delete(usuario) # se elimina el registro
session.commit() # se confirma la eliminación
print('Usuario eliminado:')
print(usuario.usename, usuario.nombre, usuario.apellido1, usuario.apellido2, usuario.creado)
