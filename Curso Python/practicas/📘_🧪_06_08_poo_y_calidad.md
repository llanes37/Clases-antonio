# 📘 Práctica Integrada 06_08 · POO y Calidad

## Qué bloque se consolida aquí

Esta práctica sirve para comprobar si el alumno ya ha superado la fase de resolver todo con listas y funciones y empieza a pensar en estructura:

- clases
- objetos
- responsabilidades
- reglas del negocio
- excepciones

## Qué debería demostrar el alumno

Al terminar este bloque, el alumno debería poder:

- distinguir datos de comportamiento
- decidir qué lógica debe vivir en una clase
- mantener estado coherente entre varias entidades
- usar excepciones cuando el problema es de negocio
- justificar por qué su diseño tiene sentido

## Por qué una mini biblioteca es un buen escenario

La biblioteca obliga a trabajar con reglas reales:

- un libro puede estar disponible o prestado
- un usuario puede pedir un libro o devolverlo
- prestar y devolver cambian estado
- hay errores que no son técnicos, sino de negocio

## Relación con el temario

- Tema 06: clases, objetos, atributos, métodos y estado
- Tema 07: control de errores con excepciones
- Tema 08: organización sensata del código

## Estrategia recomendada de resolución

Secuencia aconsejable:

1. definir las entidades base
2. construir la clase coordinadora
3. registrar libros y usuarios
4. implementar préstamos
5. implementar devoluciones
6. añadir historial o resumen

## Qué debería mirar el profesor al corregir

- si cada clase tiene una responsabilidad reconocible
- si el estado cambia de forma coherente
- si el préstamo y la devolución modifican lo que deben
- si la excepción está bien situada
- si el código se entiende sin explicación constante

## Errores frecuentes

- crear clases sin justificar su papel
- dejar la lógica importante fuera de la clase central
- no sincronizar el estado del libro y del usuario
- lanzar excepciones sin criterio
- capturar demasiado pronto y esconder el problema

## Buenas preguntas de repaso

- ¿Qué aporta aquí una clase que no aportaba una lista de diccionarios?
- ¿Qué responsabilidad debe asumir la clase principal?
- ¿Qué diferencia hay entre un error técnico y una excepción de negocio?
- ¿Qué parte del estado cambia cuando se presta un libro?

## Señal de que el bloque está maduro

El bloque ya está bien asentado cuando el alumno:

- no crea clases por decorar
- entiende mejor el reparto de responsabilidades
- usa excepciones con sentido
- y empieza a escribir código más estable y menos improvisado

## Buen uso del laboratorio IA

Buenas ampliaciones:

- límite de préstamos por usuario
- búsqueda por autor
- estado reservado
- separación en módulos

Malas ampliaciones:

- interfaz web
- autenticación
- base de datos completa antes de tiempo
