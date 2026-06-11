from __future__ import annotations
# ==============================================================================
# ARCHIVO: core/middleware.py (MIDDLEWARE PERSONALIZADO)
# ==============================================================================
# ¿QUÉ ES UN MIDDLEWARE?
#   - Código que se ejecuta ANTES y DESPUÉS de cada petición HTTP.
#   - Es como una "cebolla": cada middleware envuelve la petición.
#   - Útil para tareas transversales: logs, autenticación, métricas, CORS...
#
# FLUJO DE UNA PETICIÓN CON MIDDLEWARE:
#   
#   Petición HTTP →
#       → Middleware 1 (process_request) →
#           → Middleware 2 (process_request) →
#               → VISTA (genera respuesta) →
#           ← Middleware 2 (process_response) ←
#       ← Middleware 1 (process_response) ←
#   ← Respuesta HTTP
#
# COMPARACIÓN CON FLASK:
#   │ Flask                  │ Django Middleware              │
#   ├────────────────────────┼────────────────────────────────┤
#   │ @app.before_request    │ process_request()              │
#   │ @app.after_request     │ process_response()             │
#   │ @app.errorhandler      │ process_exception()            │
#
# ¿CÓMO ACTIVAR UN MIDDLEWARE?
#   En settings.py → MIDDLEWARE = [..., "core.middleware.RequestLogMiddleware"]
#   El ORDEN importa: se ejecutan de arriba a abajo en request,
#   y de abajo a arriba en response.
# ==============================================================================

"""Middleware didáctico que imita before_request / after_request de Flask."""

import time  # * Para medir tiempos de respuesta

from django.conf import settings  # * Para acceder a DEBUG y otras configuraciones
from django.http import HttpRequest, HttpResponse  # * Tipos de petición/respuesta
from django.utils.deprecation import MiddlewareMixin  # * Clase base para middleware


class RequestLogMiddleware(MiddlewareMixin):
    """
    Middleware de logging y métricas.
    
    # ===========================================================================
    # ¿QUÉ HACE ESTE MIDDLEWARE?
    # ===========================================================================
    # 1. Imprime cada petición en consola (cuando DEBUG=True)
    # 2. Mide el tiempo que tarda en procesarse cada petición
    # 3. Añade cabeceras personalizadas (X-Response-Time-ms, X-Author, etc.)
    #
    # ¿PARA QUÉ SIRVE EN LA VIDA REAL?
    # - Debugging: ver qué peticiones llegan al servidor
    # - Métricas: medir rendimiento, detectar endpoints lentos
    # - Auditoría: registrar quién accede a qué
    # - Seguridad: validar tokens, bloquear IPs, etc.
    # ===========================================================================
    """

    def process_request(self, request: HttpRequest) -> None:
        """
        Se ejecuta ANTES de que Django llame a la vista.
        
        # =====================================================================
        # ¿CUÁNDO USAR process_request?
        # =====================================================================
        # - Validar autenticación (tokens, API keys)
        # - Bloquear peticiones por IP o rate limiting
        # - Leer y procesar cabeceras personalizadas
        # - Iniciar mediciones de tiempo
        # - Logging de peticiones entrantes
        #
        # RETURN VALUES:
        # - None → continúa al siguiente middleware/vista
        # - HttpResponse → corta la cadena y devuelve esa respuesta
        # =====================================================================
        """
        
        # ! LOG EN CONSOLA (solo si DEBUG=True)
        # En producción no queremos llenar los logs con cada petición
        if getattr(settings, "DEBUG", False):
            print(f"📥 [MIDDLEWARE] {request.method} {request.path}")

        # * GUARDAR TIEMPO DE INICIO
        # Usamos un atributo personalizado en el objeto request
        # Esto nos permite acceder al tiempo en process_response
        # type: ignore → ignoramos el error de tipado (atributo dinámico)
        request._start_time = time.perf_counter()

    def process_response(
        self,
        request: HttpRequest,
        response: HttpResponse,
    ) -> HttpResponse:
        """
        Se ejecuta DESPUÉS de la vista, justo antes de enviar la respuesta.
        
        # =====================================================================
        # ¿CUÁNDO USAR process_response?
        # =====================================================================
        # - Añadir cabeceras a todas las respuestas (CORS, seguridad, etc.)
        # - Logging del tiempo de respuesta
        # - Modificar el contenido de la respuesta (con cuidado)
        # - Comprimir respuestas (gzip)
        # - Añadir cookies
        #
        # ! IMPORTANTE: SIEMPRE debe devolver un HttpResponse
        # =====================================================================
        """

        # * CALCULAR TIEMPO DE RESPUESTA
        # Recuperamos el tiempo de inicio que guardamos en process_request
        start = getattr(request, "_start_time", None)
        
        if start is not None:
            # Calculamos el tiempo transcurrido en milisegundos
            elapsed_ms = (time.perf_counter() - start) * 1000
            
            # Añadimos una cabecera con el tiempo de respuesta
            # El cliente puede leerla en DevTools → Network → Headers
            response.headers.setdefault("X-Response-Time-ms", f"{elapsed_ms:.2f}")
            
            # Log en consola (solo DEBUG)
            if getattr(settings, "DEBUG", False):
                print(f"📤 [MIDDLEWARE] {request.path} → {elapsed_ms:.2f}ms")

        # * CABECERAS PERSONALIZADAS DE EJEMPLO
        # Estas cabeceras son solo para que el alumno las vea en DevTools
        # En producción pondrías cosas útiles como:
        # - X-Request-ID: identificador único de la petición
        # - X-Cache: si la respuesta viene de caché
        # - Content-Security-Policy: políticas de seguridad
        response.headers.setdefault("X-Powered-By", "Django-Proyecto-Facil")
        response.headers.setdefault("X-Author", "Joaquin")
        
        # ! SIEMPRE devolver la respuesta (modificada o no)
        return response

    # =========================================================================
    # OTROS MÉTODOS DE MIDDLEWARE (opcionales)
    # =========================================================================
    # 
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     """Se ejecuta DESPUÉS de process_request pero ANTES de la vista."""
    #     # Útil para: logging del nombre de la vista, permisos por vista, etc.
    #     pass
    #
    # def process_exception(self, request, exception):
    #     """Se ejecuta si la vista lanza una excepción no capturada."""
    #     # Útil para: logging de errores, notificar a Sentry, etc.
    #     pass
    #
    # def process_template_response(self, request, response):
    #     """Se ejecuta si la respuesta tiene render() pendiente."""
    #     # Útil para: modificar el contexto antes del render
    #     pass

