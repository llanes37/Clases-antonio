# 📘 Clase 17 de Python — Gradle desde cero (wrapper, `build.gradle.kts`, tareas y validación con Python)

## 🧭 Cómo usar este material

Esta unidad es **opcional** dentro del curso. No es troncal para aprender Python, pero sí útil si quieres enseñar:

- tooling de proyectos,
- automatización de builds,
- y cómo Python puede ayudar a validar o generar configuración de otros ecosistemas.

Es especialmente buena para alumnos que también tocan:

- Java,
- Kotlin,
- Android,
- o proyectos donde aparece `gradlew`.

---

## 🎯 Qué aprenderás exactamente

Al terminar esta unidad deberías poder:

- entender qué es Gradle sin entrar en exceso de teoría,
- distinguir `gradlew` de una instalación global,
- reconocer las partes básicas de un `build.gradle.kts`,
- identificar tareas frecuentes como `build`, `test`, `clean` y `run`,
- y usar Python para leer, validar o generar bloques de configuración simples.

---

## 🧩 Mapa del temario

1. Fundamentos de Gradle y wrapper
2. Anatomía de `build.gradle.kts`
3. Tareas habituales
4. Tareas custom generadas con Python
5. Validación de configuración
6. Laboratorio IA
7. Autoevaluación final

---

## SECCIÓN 1 · Fundamentos de Gradle y wrapper

### 🎯 Objetivos

- Entender para qué sirve Gradle.
- Saber por qué `gradlew` es importante.

### 🧠 Teoría en claro

Gradle es un sistema de build. En vez de ejecutar pasos manuales uno por uno, define tareas como:

- compilar,
- testear,
- limpiar,
- ejecutar,
- empaquetar.

El **wrapper** (`gradlew`, `gradlew.bat`) sirve para que el proyecto use una versión concreta de Gradle sin depender de lo que tenga instalado cada persona.

### Idea docente importante

Aquí no hace falta enseñar Gradle “a nivel experto”. Basta con que el alumno entienda:

- qué archivos suele haber,
- qué comando ejecuta,
- y qué ventaja tiene sobre una instalación global.

### 🛠️ ZONA DEL ALUMNO · TODO

- Busca si existe `gradle/wrapper/gradle-wrapper.properties`.
- Si existe, intenta leer su versión.

---

## SECCIÓN 2 · Anatomía de `build.gradle.kts`

### 🎯 Objetivos

- Reconocer las secciones esenciales de un build script.

### 🧠 Teoría en claro

Las partes más comunes son:

- `plugins { }`
- `repositories { }`
- `dependencies { }`
- configuración de la aplicación o del módulo

Ejemplo mínimo:

```kotlin
plugins {
    id("application")
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
}
```

### Regla práctica

Si un alumno no entiende todo el archivo, no pasa nada. Primero debe ser capaz de responder:

- qué plugin hay,
- dónde descarga dependencias,
- y qué dependencia de test aparece.

### 🛠️ ZONA DEL ALUMNO · TODO

- Haz un checklist con Python:
  - plugin,
  - repositorio,
  - bloque de dependencias,
  - `mavenCentral`.

---

## SECCIÓN 3 · Tareas habituales

### 🎯 Objetivos

- Recordar pocas tareas, pero útiles.

### 🧠 Teoría en claro

Las más importantes para empezar son:

- `./gradlew build`
- `./gradlew test`
- `./gradlew clean`
- `./gradlew run`
- `./gradlew tasks`

### Idea potente del tema

No necesitas memorizar decenas de tareas. Necesitas reconocer las que aparecen una y otra vez en proyectos reales.

### 🛠️ ZONA DEL ALUMNO · TODO

- Explica con tus palabras qué hace cada una.
- Añade una tarea más si vienes de Android o Java.

---

## SECCIÓN 4 · Tareas custom generadas con Python

### 🎯 Objetivos

- Ver que Python puede ayudar fuera de su propio ecosistema.

### 🧠 Teoría en claro

Python no sustituye a Gradle aquí. Lo usamos como herramienta auxiliar para:

- generar plantillas,
- automatizar texto,
- validar configuración,
- o preparar scripts docentes.

Ejemplo conceptual:

```python
def generar_tarea_custom(nombre):
    return f'''
tasks.register("{nombre}") {{
    doLast {{
        println("Hola desde {nombre}")
    }}
}}
'''.strip()
```

### 🛠️ ZONA DEL ALUMNO · TODO

- Genera una tarea `saludo`.
- Genera otra llamada `verificarTodo`.

---

## SECCIÓN 5 · Validar configuración con Python

### 🎯 Objetivos

- Usar comprobaciones pequeñas sobre un build script.

### 🧠 Teoría en claro

Igual que en otros temas del curso, aquí Python se usa para responder preguntas claras:

- ¿está `mavenCentral()`?
- ¿hay plugin `application`?
- ¿existe bloque de `dependencies`?
- ¿hay dependencia de test?

Esto es útil como ejercicio de parsing sencillo y automatización ligera.

### 🛠️ ZONA DEL ALUMNO · TODO

- Convierte 3 comprobaciones en `assert`.
- Piensa qué fallaría si faltara `repositories`.

---

## SECCIÓN 6 · Laboratorio IA

### 🎯 Objetivos

- Usar IA para aclarar tooling sin perder criterio técnico.

### 🧰 Prompt Kit recomendado

```text
Actua como profesor de Gradle para principiantes.
Quiero:
1. Explicacion simple de plugins, repositories y dependencies
2. Un ejemplo minimo de build.gradle.kts
3. Una tarea custom sencilla
4. Explicacion corta de cuando usar build, test, clean y run
No uses jerga innecesaria.
```

### Regla importante

Si la IA te da un bloque que no entiendes, no lo pegues sin revisar.

---

## AUTOEVALUACIÓN FINAL · Mini verificador de proyecto Gradle

### 🎯 Objetivos

- Combinar lectura de archivos, strings, validación y generación de texto.

### 🛠️ Enunciado

Crea un mini script que:

- detecte si existe wrapper,
- lea la versión si puede,
- compruebe si hay plugin y dependencias,
- y genere una tarea custom lista para pegar.

### 📏 Rúbrica rápida

- Correctitud: 50%
- Claridad del código: 20%
- Validaciones útiles: 20%
- Presentación de resultados: 10%

---

## APÉNDICE A · Dónde encaja esta unidad

Esta unidad encaja mejor:

- al final del curso,
- como bloque extra,
- o dentro de un itinerario más técnico de tooling y automatización.

No sustituye temas troncales de Python. Los complementa.

---

## ✅ Qué has aprendido

- Qué es Gradle a nivel práctico.
- Qué aporta el wrapper.
- Cómo leer un `build.gradle.kts`.
- Qué tareas básicas reconocer.
- Cómo usar Python para automatizar o validar un build script.
