# Mutabilidad e Inmutabilidad en Python

En Python, las estructuras de datos se clasifican en **mutables** e **inmutables**. La **mutabilidad** se refiere a la capacidad de una estructura de datos para modificar su contenido después de ser creada.

## Estructuras de Datos Inmutables

Las estructuras inmutables no permiten cambios en su contenido una vez creadas. Cualquier operación que busque modificar una estructura inmutable generará una nueva estructura en memoria. Estas estructuras suelen ofrecer ventajas en términos de velocidad de lectura, ya que el intérprete no necesita verificar cambios en su estado.

Algunas estructuras de datos inmutables en Python son:

| Tipo de Dato            | Descripción                               |
|-------------------------|-------------------------------------------|
| **Cadenas de caracteres** (`str`) | Secuencias de texto. |
| **Números** (`int`, `float`, `complex`) | Valores numéricos de diversos tipos. |
| **Tuplas** (`tuple`)    | Secuencias ordenadas de elementos.        |

## Estructuras de Datos Mutables

Las estructuras mutables permiten modificar su contenido después de ser creadas, lo que significa que se pueden agregar, eliminar o cambiar elementos en ellas.

Algunas estructuras de datos mutables en Python son:

| Tipo de Dato            | Descripción                               |
|-------------------------|-------------------------------------------|
| **Listas** (`list`)     | Secuencias ordenadas de elementos.        |
| **Diccionarios** (`dict`) | Colecciones de pares clave-valor.        |
| **Conjuntos** (`set`)   | Colecciones de elementos únicos no ordenados. |

## Consideraciones Importantes

- Al concatenar cadenas de texto o utilizar operadores aritméticos con valores numéricos, se crean nuevos objetos en lugar de modificar los existentes.

- Las estructuras inmutables son generalmente más eficientes en términos de rendimiento para operaciones de lectura, debido a que su estado no cambia.

- Las estructuras mutables ofrecen flexibilidad para modificar datos en su lugar, lo cual es útil en diversas situaciones de programación.

## Referencias

- [Understanding Mutable and Immutable Data Types in Python](https://www.linkedin.com/pulse/understanding-mutable-immutable-data-types-python-rasmi-ranjan-swain/)

---

Este documento proporciona una visión general de la mutabilidad e inmutabilidad en Python, destacando las diferencias clave entre las estructuras de datos mutables e inmutables y sus implicaciones en el desarrollo de software.
