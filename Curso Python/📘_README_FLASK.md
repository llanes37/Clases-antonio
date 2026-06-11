# ðŸŒ Flask Tutorial â€” Inicio RÃ¡pido

**VersiÃ³n didÃ¡ctica y comentada paso a paso**

Autor: JoaquÃ­n | Web: https://clasesonlinejoaquin.es/

---

## ðŸš€ Inicio en 5 minutos

### 1ï¸âƒ£ Crear entorno virtual

```bash
python -m venv env
```

### 2ï¸âƒ£ Activar (Windows)

```bash
.\env\Scripts\activate
```

### 3ï¸âƒ£ Instalar Flask

```bash
pip install flask
```

### 4ï¸âƒ£ Ejecutar el tutorial

```bash
python "cursos/Curso Python/14_flask_tutorial.py"
```

### 5ï¸âƒ£ Abrir en navegador

```
http://127.0.0.1:5000/
```

---

## ðŸ“‹ QuÃ© encontrarÃ¡s

En la pÃ¡gina principal verÃ¡s 6 secciones de aprendizaje:

### 1ï¸âƒ£ Formulario (POST)
- EnvÃ­a tu nombre con `<form method="post">`
- Flask procesa datos con `request.form`
- Redirige a pÃ¡gina de resultado

### 2ï¸âƒ£ Rutas con parÃ¡metros (/ruta/valor)
- URLs dinÃ¡micas: `/saluda/Juan`
- Tipado automÃ¡tico: `/suma/3/5`
- Ejemplos: int, float, string

### 3ï¸âƒ£ Query Strings (?param=valor)
- ParÃ¡metros en URL: `/buscar?q=flask&page=2`
- Opcionales con defaults
- Lectura con `request.args.get()`

### 4ï¸âƒ£ API JSON (GET/POST)
- Endpoints sin HTML
- GET: `/api/echo?q=hola`
- POST: envÃ­a JSON, recibe JSON

### 5ï¸âƒ£ Manejo de errores (404, 500)
- Ruta no encontrada: 404
- Error del servidor: 500
- Manejadores personalizados

### ðŸ“š Recursos y referencias

---

## ðŸ“‚ Archivos

- **14_flask_tutorial.py** â€” CÃ³digo principal (â†‘ aquÃ­)
- **📘_PRACTICAS_FLASK.md** â€” Ejercicios guiados con soluciones
- **📘_README_FLASK.md** â€” Este archivo

---

## ðŸŽ“ Conceptos aprendidos

âœ… Crear aplicaciÃ³n Flask  
âœ… Rutas (@app.route)  
âœ… ParÃ¡metros dinÃ¡micos  
âœ… MÃ©todos HTTP (GET, POST)  
âœ… Formularios HTML  
âœ… Plantillas Jinja2  
âœ… API JSON y cÃ³digos de estado  
âœ… Manejo de errores  
âœ… Hooks (before_request, after_request)  

---

## ðŸ”¥ CaracterÃ­sticas destacadas

### CÃ³digo comentado paso a paso
- Better Comments: `# * # ! # ? # TODO`
- ExplicaciÃ³n de cada concepto
- Ejemplos funcionales

### Plantillas Jinja2 inline
- Todo en un archivo (sin carpetas)
- Herencia de plantillas (`extends`)
- Bloques reemplazables

### API REST
- GET y POST
- JSON request/response
- CÃ³digos de estado HTTP

### DiseÃ±o con Bootstrap 5
- UI moderna y responsiva
- Cards, alertas, formularios
- DevTools integration

---

## ðŸ› ï¸ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask
```

### Error: "Address already in use"
- Puerto 5000 ocupado
- Cambia en `app.run(port=5001)`

### Los cambios no se ven
- Guarda el archivo (Ctrl+S)
- Recarga el navegador (Ctrl+R)
- Debug mode estÃ¡ activo âœ…

### Â¿CÃ³mo paro el servidor?
```
Ctrl+C en terminal
```

---

## ðŸ“– PrÃ³ximos pasos

1. **Leer el cÃ³digo comentado**
   - Lee el archivo `14_flask_tutorial.py`
   - Cada secciÃ³n explica su propÃ³sito

2. **Realizar prÃ¡cticas**
   - Abre `📘_PRACTICAS_FLASK.md`
   - 6 prÃ¡cticas guiadas
   - Retos avanzados

3. **Modificar y experimentar**
   - Cambia plantillas
   - AÃ±ade nuevas rutas
   - Crea tu propia API

4. **Avanzar a nivel intermedio**
   - Base de datos (SQLite, PostgreSQL)
   - AutenticaciÃ³n y sesiones
   - ValidaciÃ³n de datos
   - Testing unitario
   - Despliegue en servidor

---

## ðŸ§ª Pruebas rÃ¡pidas

### Probar formulario
1. Llena el formulario en inicio
2. EnvÃ­a
3. Ves pÃ¡gina de resultado

### Probar ruta con parÃ¡metros
```
http://127.0.0.1:5000/saluda/TuNombre
http://127.0.0.1:5000/suma/10/5
```

### Probar API JSON (DevTools Console)
```javascript
fetch('/api/echo?q=hola')
  .then(r => r.json())
  .then(d => console.log(d))
```

---

## ðŸ“ž Contacto

- **Email**: hola@clasesonlinejoaquin.es
- **Web**: https://clasesonlinejoaquin.es/
- **Horario**: Consulta web para clases online

---

## ðŸ“œ Licencia

Contenido educativo. Libre para usar en clase.

---

**AÃºn no sabes Flask? Â¡Hoy es el dÃ­a! ðŸš€**

Sigue estos pasos y en 5 minutos tendrÃ¡s tu primer servidor web funcionando.

