from __future__ import annotations
# ==============================================================================
# ARCHIVO: core/views.py (VISTAS DE LA APP)
# ==============================================================================
# ¿QUÉ ES UNA VISTA EN DJANGO?
#   - Una función (o clase) que recibe una petición HTTP y devuelve una respuesta.
#   - Es el "cerebro" de la aplicación: procesa datos, llama a modelos,
#     renderiza templates y devuelve HTML, JSON, archivos, etc.
#
# ANATOMÍA DE UNA VISTA:
#   def mi_vista(request: HttpRequest) -> HttpResponse:
#       # 1. Leer datos de la petición (GET, POST, headers, cookies...)
#       # 2. Procesar la lógica de negocio (consultas a BD, cálculos...)
#       # 3. Preparar el contexto (datos para el template)
#       # 4. Devolver una respuesta (HTML, JSON, redirect...)
#       return render(request, "template.html", contexto)
#
# TIPOS DE RESPUESTA COMUNES:
#   - HttpResponse("texto")         → Texto plano o HTML directo
#   - render(request, "t.html", {}) → Renderiza un template con contexto
#   - JsonResponse({"ok": True})    → Respuesta JSON (para APIs)
#   - redirect("/otra-url/")        → Redirige al navegador
#   - FileResponse(file)            → Descarga de archivos
#
# COMPARACIÓN CON FLASK:
#   │ Flask                      │ Django                          │
#   ├────────────────────────────┼─────────────────────────────────┤
#   │ @app.route("/")            │ path("", vista) en urls.py      │
#   │ return render_template()   │ return render(request, ...)     │
#   │ return jsonify()           │ return JsonResponse()           │
#   │ request.args.get()         │ request.GET.get()               │
#   │ request.form.get()         │ request.POST.get()              │
#   │ request.get_json()         │ json.loads(request.body)        │
# ==============================================================================

"""
Vistas de la app `core` (HTML + API JSON + errores).

Este archivo contiene todas las vistas del proyecto, organizadas por secciones:
  1) Vistas HTML (páginas web con templates)
  2) Parámetros en URL y query strings
  3) Mini API JSON (endpoints GET/POST)
  4) Manejadores de errores (404, 500)
"""

from typing import Any, Dict  # * Tipos para mejor autocompletado

# ==============================================================================
# IMPORTS DE DJANGO
# ==============================================================================
from django.http import (
    HttpRequest,   # * Objeto con toda la info de la petición
    HttpResponse,  # * Objeto de respuesta genérico
    JsonResponse,  # * Respuesta JSON automática
)
from django.shortcuts import (
    redirect,  # * Función para redirigir a otra URL
    render,    # * Función para renderizar templates
)
from django.urls import reverse  # * Obtiene la URL a partir del nombre de la ruta


# =========================================================================================
#  SECCIÓN 1 >> VISTAS HTML (home, about, formulario)
# =========================================================================================
# Estas vistas devuelven páginas HTML completas usando templates.
# Son las vistas "tradicionales" de una web.
# =========================================================================================


def inicio(request: HttpRequest) -> HttpResponse:
    """
    Página principal con formulario y enlaces de práctica.
    
    # ===========================================================================
    # URL: http://localhost:8000/
    # MÉTODO: GET
    # TEMPLATE: index.html
    # ===========================================================================
    #
    # ¿QUÉ HACE ESTA VISTA?
    #   - Muestra la página de inicio del proyecto
    #   - El template tiene un formulario que envía datos a /procesar/
    #   - También muestra enlaces a otras rutas de ejemplo
    #
    # FLUJO:
    #   1. Usuario visita http://localhost:8000/
    #   2. Django encuentra esta vista en urls.py
    #   3. Ejecutamos render() con el template y el contexto
    #   4. Django procesa el template y devuelve HTML
    #
    # ¿QUÉ ES EL CONTEXTO?
    #   - Un diccionario con datos que el template puede usar
    #   - En el template: {{ title }} → "Inicio"
    #   - Puedes pasar listas, objetos, funciones...
    """

    # * Preparamos el contexto (datos para el template)
    contexto = {
        "title": "Inicio",  # Se usa en <title>{{ title }}</title>
    }
    
    # * render() combina el template con el contexto y devuelve HTML
    # Argumentos:
    #   - request: siempre se pasa (necesario para CSRF, usuario, etc.)
    #   - "index.html": ruta del template (busca en TEMPLATES["DIRS"])
    #   - contexto: diccionario con variables para el template
    return render(request, "index.html", contexto)


def about(request: HttpRequest) -> HttpResponse:
    """
    Página informativa que explica la estructura del proyecto.
    
    # ===========================================================================
    # URL: http://localhost:8000/about/
    # MÉTODO: GET
    # TEMPLATE: about.html
    # ===========================================================================
    """

    contexto = {"title": "Acerca de"}
    return render(request, "about.html", contexto)


def procesar(request: HttpRequest) -> HttpResponse:
    """
    Procesa el formulario enviado por POST.
    
    # ===========================================================================
    # URL: http://localhost:8000/procesar/
    # MÉTODO: POST (si llega GET, redirige al inicio)
    # TEMPLATE: resultado.html
    # ===========================================================================
    #
    # ¿CÓMO FUNCIONA UN FORMULARIO POST?
    #   1. El usuario rellena el formulario en index.html
    #   2. Al hacer click en "Enviar", el navegador hace POST a /procesar/
    #   3. Django ejecuta esta vista
    #   4. Leemos los datos con request.POST.get("campo")
    #   5. Procesamos y devolvemos una respuesta
    #
    # ¿POR QUÉ POST Y NO GET?
    #   - GET: datos en la URL (?nombre=Pepe) → visible, limitado, cacheable
    #   - POST: datos en el body → oculto, sin límite, para modificaciones
    #
    # CSRF (Cross-Site Request Forgery):
    #   - Django requiere un token CSRF en formularios POST
    #   - En el template: {% csrf_token %}
    #   - Protege contra ataques donde otra web envía forms a tu servidor
    """

    # ! PASO 1: Verificar que el método es POST
    # Si alguien accede directamente a /procesar/ por GET, lo mandamos al inicio
    if request.method != "POST":
        # reverse() obtiene la URL a partir del nombre de la ruta
        # "core:inicio" → "/" (namespace:nombre)
        return redirect(reverse("core:inicio"))

    # ! PASO 2: Leer los datos del formulario
    # request.POST es un diccionario con los campos del form
    # .get("nombre") devuelve None si no existe (no lanza error)
    # or "" → si es None, usamos string vacío
    # .strip() → quitamos espacios al inicio y final
    nombre = (request.POST.get("nombre") or "").strip()

    # ! PASO 3: Validar los datos
    # Si el nombre está vacío, volvemos al inicio sin procesar
    if not nombre:
        # TODO: Sería mejor mostrar un mensaje de error al usuario
        # Puedes usar django.contrib.messages para mensajes flash
        return redirect(reverse("core:inicio"))

    # ! PASO 4: Renderizar la respuesta
    contexto = {
        "title": "Resultado",
        "nombre": nombre,  # El template mostrará: "Hola, {{ nombre }}!"
    }
    return render(request, "resultado.html", contexto)


# =========================================================================================
#  SECCIÓN 2 >> PARÁMETROS DE RUTA Y QUERY STRINGS
# =========================================================================================
# Django permite capturar valores de la URL de dos formas:
#   1) Parámetros en la ruta: /saluda/Joaquin/ → nombre = "Joaquin"
#   2) Query strings: /buscar/?q=django → request.GET.get("q") = "django"
# =========================================================================================


def saluda(request: HttpRequest, nombre: str) -> HttpResponse:
    """
    Saluda usando un parámetro capturado en la URL.
    
    # ===========================================================================
    # URL: http://localhost:8000/saluda/<nombre>/
    # EJEMPLOS:
    #   /saluda/Ada/      → nombre = "Ada"
    #   /saluda/Joaquin/  → nombre = "Joaquin"
    # ===========================================================================
    #
    # ¿CÓMO SE DEFINE EN urls.py?
    #   path("saluda/<str:nombre>/", views.saluda, name="saluda")
    #
    # ¿QUÉ SIGNIFICA <str:nombre>?
    #   - <str:...> indica que es un string (cualquier texto sin /)
    #   - nombre es el nombre del parámetro
    #   - Django lo pasa automáticamente como argumento a la vista
    #
    # OTROS TIPOS DE PARÁMETROS:
    #   - <int:id>    → número entero
    #   - <slug:titulo> → texto-con-guiones
    #   - <uuid:token> → identificador único
    """
    
    # Devolvemos HTML directamente (sin template)
    # Para respuestas simples está bien, pero para páginas complejas usa templates
    return HttpResponse(f"<h1>¡Hola, {nombre}! 👋</h1>")


def suma(request: HttpRequest, a: int, b: int) -> HttpResponse:
    """
    Suma dos números enteros recibidos por la URL.
    
    # ===========================================================================
    # URL: http://localhost:8000/suma/<a>/<b>/
    # EJEMPLOS:
    #   /suma/3/5/    → a = 3, b = 5, resultado = 8
    #   /suma/10/20/  → a = 10, b = 20, resultado = 30
    # ===========================================================================
    #
    # ¿CÓMO SE DEFINE EN urls.py?
    #   path("suma/<int:a>/<int:b>/", views.suma, name="suma")
    #
    # ¿POR QUÉ <int:...>?
    #   - Django convierte automáticamente el string de la URL a entero
    #   - Si pones /suma/tres/cinco/ → Error 404 (no coincide con int)
    #   - Esto es VALIDACIÓN AUTOMÁTICA por tipo
    """

    resultado = a + b
    return HttpResponse(f"<h2>{a} + {b} = <strong>{resultado}</strong></h2>")


def buscar(request: HttpRequest) -> JsonResponse:
    """
    Lee parámetros en la query string (?q=valor&page=2) y devuelve JSON.
    
    # ===========================================================================
    # URL: http://localhost:8000/buscar/?q=django&page=2
    # RESPUESTA: {"ok": true, "q": "django", "page": 2, "total_results": 42}
    # ===========================================================================
    #
    # ¿QUÉ ES UNA QUERY STRING?
    #   - Los parámetros que van después del ? en la URL
    #   - Formato: ?clave1=valor1&clave2=valor2
    #   - Se accede con request.GET (un diccionario)
    #
    # ¿CUÁNDO USAR QUERY STRINGS VS PARÁMETROS EN RUTA?
    #   - Ruta (/users/123/): para identificar RECURSOS (obligatorios)
    #   - Query (?page=2&sort=name): para FILTROS y OPCIONES (opcionales)
    #
    # DIFERENCIA CON request.POST:
    #   - request.GET: parámetros de la URL (visible, cualquier método HTTP)
    #   - request.POST: datos del body (oculto, solo método POST)
    """

    # * Leer parámetro 'q' (término de búsqueda)
    # .get("q", "") → si no existe, devuelve ""
    q = request.GET.get("q", "")

    # * Leer parámetro 'page' (número de página)
    # Como viene como string, hay que convertirlo a int
    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        # Si alguien pone ?page=abc, usamos página 1
        page = 1

    # * Preparar respuesta JSON
    data: Dict[str, Any] = {
        "ok": True,
        "q": q,
        "page": page,
        "total_results": 42,  # Valor de ejemplo
    }
    
    # JsonResponse convierte el diccionario a JSON automáticamente
    return JsonResponse(data)


# =========================================================================================
#  SECCIÓN 3 >> MINI API JSON (GET/POST)
# =========================================================================================
# Las APIs REST devuelven datos en formato JSON en lugar de HTML.
# Son ideales para:
#   - Aplicaciones móviles (el móvil consume la API)
#   - Single Page Applications (React, Vue, Angular)
#   - Integraciones entre sistemas
#   - Servicios que otros desarrolladores pueden usar
# =========================================================================================


def api_echo(request: HttpRequest) -> JsonResponse:
    """
    Echo API → repite lo que mandas en la query string.
    
    # ===========================================================================
    # URL: http://localhost:8000/api/echo/?q=hola
    # MÉTODO: GET
    # RESPUESTA: {"ok": true, "echo": "hola"}
    # ===========================================================================
    #
    # ¿PARA QUÉ SIRVE?
    #   - Probar que la API funciona
    #   - Entender cómo leer parámetros GET
    #   - Ver cómo devolver JSON
    #
    # PRUÉBALO CON CURL:
    #   curl "http://localhost:8000/api/echo/?q=hola"
    """

    q = request.GET.get("q", "")
    return JsonResponse({"ok": True, "echo": q})


def api_saludo(request: HttpRequest) -> JsonResponse:
    """
    Recibe JSON en el body y devuelve un saludo personalizado.
    
    # ===========================================================================
    # URL: http://localhost:8000/api/saludo/
    # MÉTODO: POST
    # BODY: {"nombre": "Ada"}
    # RESPUESTA: {"ok": true, "mensaje": "Hola, Ada!", "status": "success"}
    # ===========================================================================
    #
    # ¿CÓMO ENVIAR JSON AL SERVIDOR?
    #   - El cliente (JavaScript, Postman, curl) hace POST con body JSON
    #   - Cabecera: Content-Type: application/json
    #   - Django lo recibe en request.body (bytes)
    #   - Lo parseamos con json.loads()
    #
    # PRUÉBALO CON CURL:
    #   curl -X POST http://localhost:8000/api/saludo/ \
    #        -H "Content-Type: application/json" \
    #        -d '{"nombre": "Ada"}'
    #
    # CÓDIGOS HTTP DE RESPUESTA:
    #   - 200 OK: todo bien
    #   - 400 Bad Request: datos inválidos
    #   - 405 Method Not Allowed: método HTTP incorrecto
    """

    import json  # * Para parsear JSON

    # ! PASO 1: Verificar que el método es POST
    if request.method != "POST":
        return JsonResponse(
            {"ok": False, "error": "Método no permitido; usa POST"},
            status=405,  # 405 = Method Not Allowed
        )

    # ! PASO 2: Parsear el JSON del body
    try:
        # request.body son bytes, hay que decodificar a string
        raw_body = request.body.decode("utf-8") or "{}"
        # json.loads() convierte el string JSON a diccionario Python
        data = json.loads(raw_body)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return JsonResponse(
            {"ok": False, "error": "Body JSON no válido"},
            status=400,  # 400 = Bad Request
        )

    # ! PASO 3: Validar que sea un diccionario
    if not isinstance(data, dict):
        return JsonResponse(
            {"ok": False, "error": "Se esperaba un objeto JSON {}"},
            status=400,
        )

    # ! PASO 4: Extraer y validar el campo "nombre"
    nombre = str(data.get("nombre", "")).strip()
    if not nombre:
        return JsonResponse(
            {"ok": False, "error": "Campo 'nombre' requerido"},
            status=400,
        )

    # ! PASO 5: Devolver respuesta exitosa
    return JsonResponse(
        {
            "ok": True,
            "mensaje": f"¡Hola, {nombre}!",
            "status": "success"
        },
        status=200,
    )


def api_health(request: HttpRequest) -> JsonResponse:
    """
    Health check → comprueba que la app responde.
    
    # ===========================================================================
    # URL: http://localhost:8000/api/health/
    # MÉTODO: GET
    # RESPUESTA: {"status": "ok"}
    # ===========================================================================
    #
    # ¿PARA QUÉ SIRVE?
    #   - Monitoreo: herramientas como Kubernetes comprueban si la app vive
    #   - Load balancers: para saber a qué servidores enviar tráfico
    #   - Debugging: verificar rápidamente que el servidor funciona
    #
    # EN PRODUCCIÓN PODRÍAS AÑADIR:
    #   - Conexión a la base de datos
    #   - Estado de servicios externos
    #   - Versión de la aplicación
    """

    return JsonResponse({"status": "ok"})


def api_calculadora(
    request: HttpRequest,
    operacion: str,
    a: int,
    b: int,
) -> JsonResponse:
    """
    Calculadora simple como API JSON.
    
    # ===========================================================================
    # URL: http://localhost:8000/api/calculadora/<operacion>/<a>/<b>/
    # EJEMPLOS:
    #   /api/calculadora/suma/3/5/     → {"resultado": 8}
    #   /api/calculadora/resta/10/4/   → {"resultado": 6}
    #   /api/calculadora/multiply/3/4/ → {"resultado": 12}
    #   /api/calculadora/divide/10/2/  → {"resultado": 5.0}
    # ===========================================================================
    #
    # OPERACIONES SOPORTADAS:
    #   - suma      → a + b
    #   - resta     → a - b
    #   - multiply  → a * b
    #   - divide    → a / b (error si b = 0)
    #
    # MANEJO DE ERRORES:
    #   - Operación no válida → 400 Bad Request
    #   - División por cero → 400 Bad Request
    """

    # Normalizamos la operación a minúsculas para comparar
    operacion = operacion.lower()

    # ! Usamos if/elif para seleccionar la operación
    # En Python 3.10+ podrías usar match/case (pattern matching)
    if operacion == "suma":
        resultado: float | int = a + b
    elif operacion == "resta":
        resultado = a - b
    elif operacion == "multiply":
        resultado = a * b
    elif operacion == "divide":
        # ! Validación: no se puede dividir por cero
        if b == 0:
            return JsonResponse(
                {"ok": False, "error": "División por cero no permitida"},
                status=400,
            )
        resultado = a / b
    else:
        # Operación no reconocida
        return JsonResponse(
            {"ok": False, "error": f"Operación '{operacion}' no válida. Usa: suma, resta, multiply, divide"},
            status=400,
        )

    # Respuesta exitosa con todos los datos
    return JsonResponse({
        "ok": True,
        "operacion": operacion,
        "a": a,
        "b": b,
        "resultado": resultado,
    })


# =========================================================================================
#  SECCIÓN 4 >> MANEJADORES DE ERRORES
# =========================================================================================
# Django permite personalizar las páginas de error (404, 500, etc.)
# Se registran en urls.py: handler404 = "core.views.error_404"
#
# ! IMPORTANTE: Solo funcionan cuando DEBUG=False en settings.py
# ! En desarrollo, Django muestra su página de debug con el traceback completo
# =========================================================================================


def error_404(request: HttpRequest, exception: Exception) -> JsonResponse:
    """
    Respuesta JSON para rutas no encontradas (404).
    
    # ===========================================================================
    # SE ACTIVA CUANDO: el usuario visita una URL que no existe
    # EJEMPLO: http://localhost:8000/esta-ruta-no-existe/
    # ===========================================================================
    #
    # ¿POR QUÉ JSON Y NO HTML?
    #   - Este proyecto es didáctico y muestra cómo hacer APIs
    #   - En una web real probablemente mostrarías una página HTML bonita
    #   - Para una API pura, JSON es lo correcto
    #
    # PARÁMETROS:
    #   - request: la petición HTTP
    #   - exception: la excepción que causó el 404 (normalmente Http404)
    """

    return JsonResponse(
        {
            "error": "Ruta no encontrada",
            "status": 404,
            "path": request.path,  # Mostramos qué ruta intentó acceder
            "mensaje": "La página que buscas no existe. Revisa la URL.",
        },
        status=404,
    )


def error_500(request: HttpRequest) -> JsonResponse:
    """
    Respuesta JSON para errores internos del servidor (500).
    
    # ===========================================================================
    # SE ACTIVA CUANDO: hay un error no capturado en el código
    # EJEMPLO: una vista lanza una excepción que no se maneja
    # ===========================================================================
    #
    # ¿POR QUÉ NO MOSTRAR EL ERROR REAL?
    #   - Por seguridad: los detalles del error podrían revelar info sensible
    #   - Los errores detallados van a los logs, no al usuario
    #   - En desarrollo (DEBUG=True) sí se muestran los detalles
    """

    return JsonResponse(
        {
            "error": "Error interno del servidor",
            "status": 500,
            "mensaje": "Algo salió mal. El equipo técnico ha sido notificado.",
        },
        status=500,
    )


def error_intencional(request: HttpRequest) -> HttpResponse:
    """
    Genera un error para probar el manejador 500.
    
    # ===========================================================================
    # URL: http://localhost:8000/error-intencional/
    # ===========================================================================
    #
    # ¿PARA QUÉ SIRVE?
    #   - Probar que el handler500 funciona correctamente
    #   - Ver cómo Django maneja excepciones no capturadas
    #   - Demostrar la diferencia entre DEBUG=True y DEBUG=False
    #
    # ! OJO: Con DEBUG=True verás el traceback completo
    # ! Con DEBUG=False verás la respuesta de error_500()
    """

    # Lanzamos una excepción a propósito
    raise RuntimeError("💥 ¡Error simulado para demostración didáctica!")



