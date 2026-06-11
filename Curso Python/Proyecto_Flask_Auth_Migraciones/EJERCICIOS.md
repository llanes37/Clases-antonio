# Ejercicios - Proyecto Flask Auth + Migraciones

Estos ejercicios están pensados para reforzar el proyecto por capas.  
El orden recomendado no es aleatorio: empieza por validaciones, sigue por auth, continúa por permisos y termina con migraciones y testing.

---

## Cómo usar esta hoja de ejercicios

1. Haz primero los ejercicios **básicos**.
2. Cuando el flujo de registro y login esté claro, pasa a los de **sesión y permisos**.
3. Deja los de **migraciones** y **testing** para el final.
4. Si das clase, puedes repartirlos como mini bloques:
   - auth
   - perfil
   - admin
   - migraciones
   - tests

---

## Nivel 1 · Básico

## 1. Validaciones de registro

### Objetivo

Mejorar la calidad del alta de usuario.

### Tareas

- Obliga a que la password tenga mínimo 6 caracteres.
- Obliga a que el email contenga `@`.
- Muestra mensajes flash distintos según el error.
- Evita espacios vacíos al principio o al final en nombre y email.

### Criterio de éxito

- no se crean usuarios inválidos,
- el formulario informa bien del problema,
- y el usuario entiende qué debe corregir.

---

## 2. Perfil editable

### Objetivo

Permitir que el usuario modifique sus propios datos.

### Tareas

- Añade ruta GET/POST `/perfil/editar`.
- Permite cambiar:
  - nombre
  - email
- Si el nuevo email ya existe en otro usuario, bloquea el cambio.

### Criterio de éxito

- el usuario autenticado puede editar su perfil,
- pero no puede duplicar emails de otros usuarios.

---

## 3. Cambio de password

### Objetivo

Practicar una de las operaciones más típicas de auth.

### Tareas

- Crea un formulario con:
  - password actual
  - nueva password
- Verifica la password actual antes de guardar.
- Obliga a longitud mínima.
- Guarda siempre con `set_password(...)`.

### Criterio de éxito

- la password anterior deja de funcionar,
- la nueva sí funciona,
- y nunca se guarda texto plano.

---

## Nivel 2 · Sesión y permisos

## 4. Notas privadas

### Objetivo

Completar el mini dominio del proyecto.

### Tareas

- Añade edición de notas.
- Añade borrado de notas.
- Evita que un usuario edite o borre notas de otro.

### Criterio de éxito

- cada usuario solo ve y gestiona sus propias notas,
- y el backend impide accesos no permitidos.

### Pregunta didáctica

> ¿Dónde debe comprobarse la propiedad de una nota: en la plantilla o en la vista?

---

## 5. Panel admin

### Objetivo

Hacer el panel un poco más útil sin perder simplicidad.

### Tareas

- Añade filtro por rol (`student` / `admin`).
- Añade búsqueda por email.
- Añade contador total de usuarios activos e inactivos.

### Criterio de éxito

- el panel permite localizar usuarios más rápido,
- y sigue protegido por `admin_required`.

---

## 6. Ruta “mi sesión”

### Objetivo

Entender mejor qué significa estar autenticado.

### Tareas

- Crea una ruta `/me` o `/sesion`.
- Si hay sesión, muestra:
  - id
  - nombre
  - email
  - role
- Si no hay sesión, redirige al login.

### Criterio de éxito

- el alumno puede inspeccionar visualmente qué usuario está activo.

---

## Nivel 3 · Migraciones

## 7. Añadir un campo nuevo al modelo

### Objetivo

Practicar el motivo real por el que existen las migraciones.

### Tareas

- Añade un campo `ultimo_login` al modelo `User`.
- Genera una migración.
- Aplícala.
- Comprueba que la base de datos cambia sin recrearla desde cero.

### Criterio de éxito

- se genera una migración nueva,
- `flask db upgrade` se ejecuta correctamente,
- y el proyecto sigue funcionando.

---

## 8. Estado de borrado lógico

### Objetivo

Practicar evolución de esquema y reglas de negocio.

### Tareas

- Añade un campo `deleted` o `archivada` a `NotaPrivada`.
- Haz que borrar una nota no la elimine realmente, sino que la marque.
- Oculta las archivadas en la portada.

### Criterio de éxito

- la tabla cambia con migración,
- la lógica de la app respeta ese cambio,
- y el alumno entiende la diferencia entre borrar físicamente y borrar lógicamente.

---

## Nivel 4 · Testing

## 9. Registro inválido

### Objetivo

Mejorar la cobertura del flujo de autenticación.

### Tareas

- Añade un test donde falte:
  - nombre
  - o email
  - o password
- Comprueba que el usuario no se crea.

### Criterio de éxito

- el test falla si el backend permite registros inválidos.

---

## 10. Login inválido

### Objetivo

Verificar que la seguridad mínima funciona.

### Tareas

- Añade test con password incorrecta.
- Añade test con usuario inexistente.
- Verifica que no se abre sesión.

### Criterio de éxito

- el sistema rechaza credenciales inválidas con comportamiento consistente.

---

## 11. Cambio de rol

### Objetivo

Validar el panel admin con tests.

### Tareas

- Añade test para cambiar un usuario de `student` a `admin`.
- Comprueba después en BD que el rol cambió.

### Criterio de éxito

- la acción del panel no solo responde bien, sino que realmente persiste el cambio.

---

## Nivel 5 · Bonus

## 12. Integrar `Flask-Login`

### Objetivo

Comparar solución manual vs librería especializada.

### Tareas

- Sustituye la gestión manual de sesión por `Flask-Login`.
- Compara:
  - qué simplifica,
  - qué añade,
  - qué sigue siendo responsabilidad tuya.

### Criterio de éxito

- el alumno entiende que una librería puede abstraer trabajo, pero no sustituye los conceptos.

---

## 13. API mínima autenticada

### Objetivo

Preparar el siguiente salto del bloque Flask.

### Tareas

- Crea una pequeña API `/api/me`.
- Si el usuario tiene sesión, devuelve JSON con:
  - id
  - nombre
  - email
  - role
- Si no hay sesión, devuelve 401 o redirección según el enfoque que decidas enseñar.

### Criterio de éxito

- el proyecto empieza a unir auth web y consumo de API.

---

## 14. Auditoría simple

### Objetivo

Introducir trazabilidad mínima.

### Tareas

- Guarda cuándo se hace login correcto.
- Actualiza `ultimo_login`.
- Muéstralo en perfil o admin.

### Criterio de éxito

- el alumno ve un ejemplo real de “dato técnico útil” que no es solo visual.

---

## Propuesta de orden mínimo si vas justo de tiempo

Si solo quieres hacer 5 ejercicios, yo haría estos:

1. Validaciones de registro
2. Cambio de password
3. Notas privadas: editar/borrar
4. Añadir `ultimo_login` con migración
5. Test de login inválido

---

## Rúbrica rápida

- **Correcto**: el ejercicio funciona y no rompe lo anterior.
- **Bien**: el código está ordenado y reutiliza funciones/decoradores.
- **Muy bien**: además añade validaciones y tests.
- **Excelente**: conecta auth, permisos, migraciones y testing con criterio.

---

## Idea final

Estos ejercicios no son “extras sueltos”.  
Están pensados para que el alumno recorra exactamente los problemas reales que aparecen al pasar de una app Flask sencilla a una app con usuarios, seguridad y evolución del esquema.
