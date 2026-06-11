# =============================================================================
#  CURSO PYTHON CLASE 12 (AVANZADO) - BASES DE DATOS RELACIONALES PROFUNDAS
#  ----------------------------------------------------------------------------
#  En esta version ampliada trabajamos sobre SQLite pero con mentalidad de
#  proyecto profesional: normalizacion, relaciones, transacciones, exportacion
#  avanzada y prompts de IA para prototipar mas rapido.
#
#  Leyenda Better Comments:
#    # ! importante   |  # * definicion/foco   |  # ? idea/nota
#    # TODO: practica |  # NOTE: apunte util   |  # // deprecado
# =============================================================================

import sqlite3
import csv
import json
from pathlib import Path
from contextlib import contextmanager
from datetime import datetime
from typing import Iterable, Sequence, Any

DB_FILE = "campus_avanzado.db"
EXPORT_DIR = Path("export_bbdd_avanzado")
RUN_INTERACTIVE = True
PAUSE = False
IA_DEMO = True
SCHEMA_VERSION = 2

# * Firma ---------------------------------------------------------------------
def print_firma() -> None:
    print("\n" + "=" * 80)
    print("Autor: Joaquin | https://clasesonlinejoaquin.es | Clase 12 avanzada")
    print("=" * 80 + "\n")

# * Utilidades ----------------------------------------------------------------
def pause(msg: str = "Pulsa Enter para continuar...") -> None:
    if not PAUSE:
        return
    try:
        input(msg)
    except EOFError:
        pass

def encabezado(titulo: str) -> None:
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)

@contextmanager
def safe_session(db_path: str = DB_FILE, silence: bool = False):
    """Context manager que asegura foreign keys + rollback en errores."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        yield conn
        conn.commit()
    except sqlite3.Error as exc:
        conn.rollback()
        if not silence:
            print(f"[safe_session] Error SQLite: {exc}")
        raise
    finally:
        conn.close()

# * Bootstrap -----------------------------------------------------------------
def bootstrap_schema() -> None:
    """Crea tablas y datos base solo si hacen falta."""
    with safe_session() as conn:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS meta_schema (
                version INTEGER NOT NULL,
                applied_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                seniority INTEGER NOT NULL DEFAULT 1,
                creado_en TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                clave TEXT NOT NULL UNIQUE,
                horas INTEGER NOT NULL,
                nivel TEXT NOT NULL CHECK (nivel IN ('basico','intermedio','experto'))
            );

            CREATE TABLE IF NOT EXISTS inscripciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alumno_id INTEGER NOT NULL,
                curso_id INTEGER NOT NULL,
                estado TEXT NOT NULL DEFAULT 'pendiente',
                fecha_inscripcion TEXT NOT NULL DEFAULT (date('now')),
                UNIQUE(alumno_id, curso_id),
                FOREIGN KEY(alumno_id) REFERENCES alumnos(id) ON DELETE CASCADE,
                FOREIGN KEY(curso_id) REFERENCES cursos(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_inscripciones_estado ON inscripciones(estado);
            CREATE INDEX IF NOT EXISTS idx_cursos_nivel ON cursos(nivel);
            """
        )

        version_row = conn.execute("SELECT version FROM meta_schema ORDER BY applied_at DESC LIMIT 1").fetchone()
        if not version_row or version_row[0] < SCHEMA_VERSION:
            conn.execute(
                "INSERT INTO meta_schema(version, applied_at) VALUES(?, ?)",
                (SCHEMA_VERSION, datetime.now().isoformat(timespec="seconds")),
            )

        alumnos_count = conn.execute("SELECT COUNT(*) FROM alumnos").fetchone()[0]
        if alumnos_count == 0:
            conn.executemany(
                "INSERT INTO alumnos(nombre, email, seniority) VALUES(?,?,?)",
                [
                    ("Ada Lovelace", "ada@ejemplo.com", 5),
                    ("Linus Torvalds", "linus@ejemplo.com", 4),
                    ("Guido Rossum", "guido@ejemplo.com", 5),
                    ("Katia Vega", "katia@ejemplo.com", 3),
                ],
            )

        cursos_count = conn.execute("SELECT COUNT(*) FROM cursos").fetchone()[0]
        if cursos_count == 0:
            conn.executemany(
                "INSERT INTO cursos(nombre, clave, horas, nivel) VALUES(?,?,?,?)",
                [
                    ("SQL Moderno", "SQLPRO", 20, "intermedio"),
                    ("Modelado de Datos", "MODELO3N", 16, "experto"),
                    ("Automatizacion ETL", "ETL100", 24, "experto"),
                ],
            )

        insc_count = conn.execute("SELECT COUNT(*) FROM inscripciones").fetchone()[0]
        if insc_count == 0:
            conn.executemany(
                "INSERT INTO inscripciones(alumno_id, curso_id, estado) VALUES(?,?,?)",
                [
                    (1, 1, "completado"),
                    (1, 2, "completado"),
                    (2, 1, "en_progreso"),
                    (3, 3, "pendiente"),
                ],
            )

# =============================================================================
#  SECCION 1 - Arquitectura relacional avanzada
# =============================================================================
def seccion_1() -> None:
    encabezado("SECCION 1 - Arquitectura relacional avanzada")

    # * Punto de partida ------------------------------------------------------
    # - Pensar tablas como "contratos"; cada columna requiere tipo, dominio y
    #   restricciones (NOT NULL, CHECK, DEFAULT).
    # - Normalizacion: 1NF (columnas atomicas), 2NF (sin dependencias parciales),
    #   3NF (atributos dependen solo de la clave). Menos redundancia => menos bugs.
    # - Claves candidatas vs primarias: elegir la que facilite joins y sea estable.
    # - Relaciones 1:N y N:M con tablas puente (inscripciones) y ON DELETE CASCADE.
    # - ACID: atomicidad (rollback), consistencia (constraints), aislamiento
    #   (WAL + transacciones) y durabilidad (commits + backups).
    # - Indices: aceleran filtros JOIN/WHERE pero ocupan disco; crea los que responden
    #   a tus consultas mas frecuentes (nivel, estado, fechas).

    print("Modelo creado en:", Path(DB_FILE).resolve())
    print("Meta version:", SCHEMA_VERSION)

    # TODO: (MAPEO FISICO)
    # Dibuja un diagrama rapido Alumno-Curso-Incripcion y marca donde usarias
    # claves naturales (email, codigo de curso) y donde una surrogate key (id entero).

# =============================================================================
#  SECCION 2 - Conexion robusta y migraciones rapidas
# =============================================================================
def seccion_2() -> None:
    encabezado("SECCION 2 - Conexion robusta y migraciones")
    bootstrap_schema()
    print("Base inicializada con WAL + indices avanzados.")

    with safe_session() as conn:
        conn.execute("PRAGMA journal_mode")
        stats = conn.execute(
            "SELECT COUNT(*), MIN(creado_en), MAX(creado_en) FROM alumnos"
        ).fetchone()
        print(f"Alumnos cargados: {stats[0]} | Rango fechas: {stats[1]} -> {stats[2]}")

    # TODO: (MIGRACION EXPRESS)
    # Agrega una tabla historial_cambios(id, tabla, descripcion, fecha) usando
    # conn.executescript. Inserta un registro cuando crees un nuevo indice.

# =============================================================================
#  SECCION 3 - CRUD profesional (bulk + transacciones)
# =============================================================================
def registrar_alumnos(nuevos: Iterable[Sequence[Any]]) -> None:
    with safe_session() as conn:
        for nombre, email, seniority in nuevos:
            conn.execute(
                """
                INSERT INTO alumnos(nombre, email, seniority)
                VALUES(?,?,?)
                ON CONFLICT(email) DO UPDATE SET
                    nombre=excluded.nombre,
                    seniority=excluded.seniority
                """,
                (nombre, email, seniority),
            )

def inscribir(alumno_email: str, curso_clave: str, estado: str = "pendiente") -> None:
    with safe_session() as conn:
        alumno_id = conn.execute(
            "SELECT id FROM alumnos WHERE email=?", (alumno_email,)
        ).fetchone()
        curso_id = conn.execute(
            "SELECT id FROM cursos WHERE clave=?", (curso_clave,)
        ).fetchone()
        if not alumno_id or not curso_id:
            raise ValueError("Alumno o curso inexistente para inscripcion avanzada")
        conn.execute(
            """
            INSERT INTO inscripciones(alumno_id, curso_id, estado)
            VALUES(?,?,?)
            ON CONFLICT(alumno_id, curso_id)
            DO UPDATE SET estado=excluded.estado
            """,
            (alumno_id[0], curso_id[0], estado),
        )

def listar_inscripciones() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        for row in conn.execute(
            """
            SELECT a.nombre AS alumno, c.nombre AS curso, i.estado
            FROM inscripciones i
            JOIN alumnos a ON a.id = i.alumno_id
            JOIN cursos c ON c.id = i.curso_id
            ORDER BY a.nombre, c.nivel DESC
            """
        ):
            print(f"- {row['alumno']} -> {row['curso']} ({row['estado']})")

def seccion_3() -> None:
    encabezado("SECCION 3 - CRUD profesional")
    registrar_alumnos(
        [
            ("Maria SQL", "maria@ejemplo.com", 2),
            ("Rafa Warehousing", "rafa@ejemplo.com", 4),
        ]
    )
    inscribir("maria@ejemplo.com", "SQLPRO", "en_progreso")
    inscribir("rafa@ejemplo.com", "ETL100", "pendiente")
    listar_inscripciones()

    # TODO: (TRANSACCION PERSONALIZADA)
    # Crea una funcion que abra safe_session y ejecute varias inserciones usando
    # SAVEPOINT. Provoca un error intencional para verificar que se hace rollback.

# =============================================================================
#  SECCION 4 - Consultas SELECT avanzadas
# =============================================================================
def seccion_4() -> None:
    encabezado("SECCION 4 - SELECT + joins + analitica")
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row

        print("Top seniority y cursos que cursa:")
        for row in conn.execute(
            """
            SELECT a.nombre, a.seniority, GROUP_CONCAT(c.nombre, ', ') AS cursos
            FROM alumnos a
            LEFT JOIN inscripciones i ON i.alumno_id = a.id
            LEFT JOIN cursos c ON c.id = i.curso_id
            GROUP BY a.id
            HAVING a.seniority >= 4
            ORDER BY a.seniority DESC
            """
        ):
            print(f"  {row['nombre']} ({row['seniority']}): {row['cursos']}")

        print("\nRanking por horas totales inscritas (window function):")
        for row in conn.execute(
            """
            SELECT a.nombre,
                   SUM(c.horas) AS horas_total,
                   RANK() OVER (ORDER BY SUM(c.horas) DESC) AS posicion
            FROM inscripciones i
            JOIN alumnos a ON a.id = i.alumno_id
            JOIN cursos c ON c.id = i.curso_id
            GROUP BY a.id
            """
        ):
            print(f"  #{row['posicion']} {row['nombre']} -> {row['horas_total']}h")

        print("\nCursos expertos con pocas inscripciones:")
        for row in conn.execute(
            """
            SELECT c.nombre, COUNT(i.id) AS inscritos
            FROM cursos c
            LEFT JOIN inscripciones i ON i.curso_id = c.id
            WHERE c.nivel = 'experto'
            GROUP BY c.id
            HAVING inscritos < 2
            """
        ):
            print(f"  {row['nombre']} => {row['inscritos']} alumnos")

    # TODO: (SUBCONSULTA)
    # Escribe una consulta que muestre alumnos cuyo promedio de horas por curso
    # sea mayor a 18h usando una CTE (WITH ...).

# =============================================================================
#  SECCION 5 - Manejo de errores, logging y diagnostico
# =============================================================================
def seccion_5() -> None:
    encabezado("SECCION 5 - Manejo de errores avanzado")

    try:
        inscribir("no_existe@correo.com", "SQLPRO")
    except ValueError as exc:
        print("Validacion previa:", exc)

    try:
        with safe_session() as conn:
            conn.execute(
                "INSERT INTO inscripciones(alumno_id, curso_id) VALUES(999, 999)"
            )
    except sqlite3.IntegrityError as exc:
        print("Integridad protegida:", exc)

    # TODO: (LOGGER PERSONAL)
    # Integra el modulo logging para enviar errores a un fichero errors.log con
    # timestamp y la consulta que fallo.

# =============================================================================
#  SECCION 6 - Exportacion avanzada
# =============================================================================
def export_table(nombre_tabla: str, campos: Sequence[str]) -> None:
    EXPORT_DIR.mkdir(exist_ok=True)
    destino_csv = EXPORT_DIR / f"{nombre_tabla}.csv"
    destino_json = EXPORT_DIR / f"{nombre_tabla}.json"

    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        filas = [dict(row) for row in conn.execute(f"SELECT {', '.join(campos)} FROM {nombre_tabla}")]

    with destino_csv.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(filas)

    destino_json.write_text(
        json.dumps(filas, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Exportado {nombre_tabla} -> {destino_csv.name}, {destino_json.name}")

def seccion_6() -> None:
    encabezado("SECCION 6 - Exportar datasets listos para BI")
    export_table("alumnos", ["id", "nombre", "email", "seniority", "creado_en"])
    export_table("cursos", ["id", "nombre", "clave", "nivel", "horas"])
    export_table("inscripciones", ["id", "alumno_id", "curso_id", "estado", "fecha_inscripcion"])

    # TODO: (PIPELINE)
    # Implementa una funcion que exporte directamente a parquet usando pandas y
    # compara tamanos entre CSV y parquet.

# =============================================================================
#  SECCION 7 - Laboratorio IA avanzado
# =============================================================================
def seccion_7_ia() -> None:
    encabezado("SECCION 7 - Laboratorio IA (prompts de nivel senior)")

    print("Ideas de prompts para usar con ChatGPT o Claude:")
    prompts = [
        "Genera un script SQLite con validaciones y triggers que mantengan la tabla \"inscripciones\" sincronizada con cupos disponibles por curso.",
        "Refactoriza el CRUD para exponerlo como CLI con argparse incluyendo banderas --export y --interactive.",
        "Crea un pipeline ETL que lea alumnos desde un CSV externo, normalice correos repetidos y sincronice la BD usando UPSERT.",
    ]
    for idx, prompt in enumerate(prompts, start=1):
        print(f"  {idx}) {prompt}")

    if IA_DEMO:
        print("\nDemo rapida: idea de consulta propuesta por IA ->")
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                """
                WITH resumen AS (
                    SELECT c.nivel, COUNT(*) AS total
                    FROM cursos c
                    JOIN inscripciones i ON i.curso_id = c.id
                    GROUP BY c.nivel
                )
                SELECT nivel, total FROM resumen ORDER BY total DESC LIMIT 1
                """
            ).fetchone()
            if row:
                print(f"  Nivel con mas demanda: {row['nivel']} ({row['total']} inscripciones)")

    # TODO: (ZONA DEL ALUMNO)
    # 1. Pide a la IA que cree la funcion mi_script_ia() con alguna mejora real.
    # 2. Pega el codigo aqui, ejecuta la funcion y documenta resultados.

    # def mi_script_ia():
    #     pass
    # mi_script_ia()

# =============================================================================
#  Autoevaluacion
# =============================================================================
def autoevaluacion() -> None:
    encabezado("AUTOEVALUACION - Mini proyecto de matriculas")
    print("Objetivo: consolidar todo lo anterior con un caso completo.")
    print(
        "1) Crea tabla auditoria (id, tabla, accion, payload_json, fecha).\n"
        "2) Implementa triggers AFTER INSERT/UPDATE/DELETE sobre inscripciones\n"
        "   que registren los cambios en auditoria.\n"
        "3) Escribe una consulta que muestre cuantas acciones por tipo ocurren\n"
        "   por dia.\n"
        "4) Exporta auditoria a un CSV y envia captura en el campus."
    )

    # TODO: (EVIDENCIA)
    # Agrega capturas o registros en tu README del curso mostrando comandos usados
    # y reflexiona sobre ventajas de usar prompts para documentar migraciones.

# =============================================================================
#  Menu principal
# =============================================================================
def menu() -> None:
    while True:
        print_firma()
        print("MENU - Bases de Datos (avanzado)")
        print("  1) Arquitectura relacional")
        print("  2) Conexion + migraciones")
        print("  3) CRUD profesional")
        print("  4) Consultas avanzadas")
        print("  5) Manejo de errores")
        print("  6) Exportacion avanzada")
        print("  7) Laboratorio IA")
        print("  8) Autoevaluacion")
        print("  0) Salir")

        try:
            opcion = int(input("Opcion: "))
        except Exception:
            print("Opcion invalida. Usa numeros del 0 al 8.")
            continue

        if opcion == 0:
            print("Hasta la proxima!")
            break
        elif opcion == 1:
            seccion_1(); pause()
        elif opcion == 2:
            seccion_2(); pause()
        elif opcion == 3:
            seccion_3(); pause()
        elif opcion == 4:
            seccion_4(); pause()
        elif opcion == 5:
            seccion_5(); pause()
        elif opcion == 6:
            seccion_6(); pause()
        elif opcion == 7:
            seccion_7_ia(); pause()
        elif opcion == 8:
            autoevaluacion(); pause()
        else:
            print("Selecciona una opcion valida.")

# =============================================================================
#  Ejecucion directa
# =============================================================================
if __name__ == "__main__":
    menu()
