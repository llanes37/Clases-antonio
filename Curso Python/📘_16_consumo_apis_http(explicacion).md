# Clase 16 de Python - Consumo de APIs HTTP

**Autor:** Joaquín Rodríguez  
**Objetivo global:** Aprender a consumir APIs desde Python de forma **práctica y progresiva**: hacer peticiones **GET** y **POST**, trabajar con **JSON**, enviar **parámetros**, resumir respuestas útiles y manejar **errores de red** y **timeouts**.

---

## Cómo usar este material

1. **Lee primero este documento** para entender qué es una API y cómo se usa HTTP.
2. **Ejecuta** `16_consumo_apis_http.py` para ver ejemplos funcionales paso a paso.
3. **Completa** `16_consumo_apis_http(alumno).py` con tus propias peticiones y funciones auxiliares.
4. Usa esta unidad como puente entre:
   - Python general,
   - automatización,
   - y desarrollo web con Flask o Django.

> **Idea pedagógica:** este tema es muy valioso porque conecta Python con datos reales de internet. El alumno deja de trabajar solo con variables locales y empieza a interactuar con servicios externos.

---

## Qué aprenderás exactamente

- Qué es una API y qué significa hacer una petición HTTP.
- Cuándo usar **GET** y cuándo usar **POST**.
- Cómo enviar parámetros en una URL.
- Cómo leer respuestas en formato JSON.
- Cómo resumir información útil en lugar de imprimir todo.
- Cómo manejar errores de conexión o respuestas problemáticas.
- Cómo crear una función reutilizable para futuras APIs.

---

## ¿Qué es una API?

Una API es una interfaz que permite que un programa se comunique con otro programa. En lugar de que un humano haga clic en una web, nuestro script puede:

- pedir datos,
- enviar datos,
- filtrar resultados,
- y procesar respuestas automáticamente.

En esta unidad se usa un servicio de prueba muy conocido:

```txt
https://jsonplaceholder.typicode.com
```

Es ideal para aprender porque:

- responde rápido,
- devuelve JSON sencillo,
- y no requiere autenticación.

---

## SECCIÓN 1 · Primer GET

### Objetivos

- Entender qué hace una petición GET.
- Leer un JSON sencillo.
- Identificar sus campos principales.

### Teoría en claro

GET se usa para **consultar** información. No debería modificar datos del servidor.

Cuando haces:

```txt
GET /posts/1
```

la API responde con un objeto JSON similar a este:

```json
{
  "userId": 1,
  "id": 1,
  "title": "....",
  "body": "...."
}
```

### Demo guiada

El script del profesor:

- hace un GET a `/posts/1`,
- muestra el código HTTP,
- extrae `id`, `title` y `body`.

### Práctica (TODO)

1. Haz una petición a `/users/1`.
2. Muestra:
   - `name`
   - `email`
   - `company.name`
3. Usa `.get()` cuando sea posible para evitar errores.

### Error típico

Imprimir el JSON entero sin entender qué contiene. En esta unidad queremos aprender a **leer datos concretos**, no solo a descargar respuestas.

---

## SECCIÓN 2 · GET con parámetros

### Objetivos

- Entender qué son los query params.
- Filtrar resultados desde la propia URL.

### Ejemplo

```txt
/posts?userId=1
```

Aquí la ruta sigue siendo `/posts`, pero estamos pidiendo solo los posts del usuario 1.

### Teoría en claro

Los parámetros sirven para:

- filtrar,
- paginar,
- buscar,
- ordenar,
- o cambiar el comportamiento de una consulta.

### Demo guiada

El script:

- pide un `userId`,
- hace GET con parámetros,
- cuenta cuántos registros llegan,
- y muestra los primeros títulos.

### Práctica (TODO)

1. Pide una palabra al usuario.
2. Recorre los títulos recibidos.
3. Muestra solo los que contengan esa palabra.
4. Cuenta cuántos han coincidido.

### Idea importante

Aquí el alumno ya practica dos cosas a la vez:

- consumo de API,
- y procesamiento de listas con Python.

---

## SECCIÓN 3 · Leer JSON y resumir datos

### Objetivos

- Trabajar con listas de diccionarios.
- Seleccionar solo la información importante.

### Teoría en claro

Una respuesta JSON puede convertirse en:

- un `dict` si devuelve un único objeto,
- una `list` de `dict` si devuelve varios elementos.

En este tema interesa mucho enseñar a **resumir**. Por ejemplo, si la API devuelve usuarios con muchos datos, el alumno debe centrarse en:

- nombre,
- email,
- ciudad.

### Demo guiada

El script del profesor consulta `/users` y muestra, para varios usuarios:

- nombre,
- email,
- ciudad.

### Práctica (TODO)

1. Construye una lista de diccionarios con esta forma:

```python
{"nombre": ..., "email": ..., "ciudad": ...}
```

2. Recorre esa nueva lista y muéstrala.
3. Extra: ordénala por nombre.

### Error típico

Confundirse entre:

- una lista de resultados,
- y un solo objeto JSON.

Por eso conviene imprimir primero el tipo o inspeccionar un elemento antes de trabajar más en serio.

---

## SECCIÓN 4 · POST JSON

### Objetivos

- Aprender a enviar datos a una API.
- Construir y enviar un payload JSON.

### Teoría en claro

POST se usa normalmente para:

- crear recursos,
- enviar formularios,
- o mandar información al servidor.

En Python, un payload se suele construir como un diccionario:

```python
payload = {
    "title": "Curso Python APIs",
    "body": "Probando POST",
    "userId": 99
}
```

### Demo guiada

El script:

- crea un payload,
- lo envía a `/posts`,
- recibe una respuesta JSON,
- y la muestra formateada con `json.dumps(..., indent=2)`.

### Práctica (TODO)

1. Construye tu propio payload.
2. Envíalo al endpoint `/posts`.
3. Muestra:
   - código HTTP,
   - y JSON devuelto.

### Nota importante

En `jsonplaceholder` el POST es simulado, pero didácticamente sirve perfectamente para practicar el flujo.

---

## SECCIÓN 5 · Errores, timeouts y cliente sencillo

### Objetivos

- Introducir manejo de errores de red.
- Evitar bloqueos por peticiones lentas.
- Construir una función reutilizable.

### Teoría en claro

Al consumir APIs pueden fallar varias cosas:

- la conexión,
- el DNS,
- el servidor,
- la ruta,
- el tiempo de respuesta,
- o incluso el formato JSON.

Por eso conviene:

- usar `try/except`,
- establecer un `timeout`,
- y encapsular peticiones en funciones.

### Demo guiada

El script muestra:

- buenas prácticas,
- una petición con timeout,
- y varios `except` (`HTTPError`, `URLError`, etc.).

### Práctica (TODO)

Crea una función:

```python
def obtener_json(url, params=None):
    ...
```

que:

1. haga GET,
2. use timeout,
3. devuelva `[]` o `{}` si falla,
4. imprima un error claro.

### Idea potente del tema

Aquí el alumno pasa de “hacer una petición” a “diseñar un cliente sencillo”. Ese salto es muy importante porque ya se parece más a código real.

---

## Autoevaluación final · Mini cliente de API

### Objetivos

- Integrar GET, POST, JSON y manejo de errores.

### Tareas

1. Haz un GET a `/users` y muestra nombre + email de 3 usuarios.
2. Haz un GET a `/posts?userId=1` y cuenta cuántos posts llegan.
3. Haz un POST a `/posts` con un payload propio.
4. Crea una función `cliente_get(url, params=None)`.
5. Maneja errores con `try/except` y timeout.
6. Extra: guarda en un archivo JSON alguno de los resultados.

### Rúbrica rápida

- **Correcto**: el alumno realiza GET, POST y procesa JSON.
- **Bien**: además encapsula lógica en funciones.
- **Excelente**: maneja errores, usa timeout y deja el código reutilizable.

---

## `requests` o `urllib`

### `requests`

- Más legible.
- Muy usado en proyectos reales.
- Ideal para enseñar de forma cómoda.

### `urllib`

- Viene con Python.
- No requiere instalar librerías extra.
- Útil para explicar la base sin dependencias externas.

### En este curso

El tema queda preparado para ambas opciones:

- `requests` si está disponible,
- `urllib` como respaldo.

Esto evita que el alumno dependa obligatoriamente de una sola librería para practicar.

---

## Apéndice A · Códigos HTTP más comunes

- `200 OK` → petición correcta.
- `201 Created` → recurso creado correctamente.
- `400 Bad Request` → petición mal construida.
- `401 Unauthorized` → falta autenticación.
- `404 Not Found` → recurso no encontrado.
- `500 Internal Server Error` → error del servidor.

**Idea práctica:** no hace falta memorizar todos, pero sí reconocer los más frecuentes.

---

## Apéndice B · Checklist del alumno

- [ ] Entiendo qué es una API.
- [ ] Sé hacer un GET.
- [ ] Sé enviar parámetros.
- [ ] Sé leer JSON.
- [ ] Sé hacer un POST con JSON.
- [ ] Sé manejar errores básicos de red.
- [ ] Sé crear una función auxiliar para reutilizar peticiones.

---

## Retos extra

1. Guarda en un archivo local los usuarios recibidos.
2. Crea una función que filtre usuarios por ciudad.
3. Crea una función que haga GET y POST según un parámetro.
4. Mide cuánto tarda una petición con `time.perf_counter()`.
5. Compara cómo sería la misma petición con `requests` y con `urllib`.

---

## Qué has aprendido

- Cómo consultar datos de una API.
- Cómo enviar parámetros en una URL.
- Cómo trabajar con respuestas JSON.
- Cómo hacer peticiones POST con payloads.
- Cómo manejar errores y timeouts.
- Cómo empezar a construir un pequeño cliente HTTP reutilizable en Python.
