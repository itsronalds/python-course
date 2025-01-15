# Funciones Lambda en Python

Las **funciones lambda** son funciones **anónimas** y **de una sola línea** que se utilizan para tareas simples y específicas. Su sintaxis compacta las hace ideales para escribir funciones pequeñas que no necesitan ser reutilizadas en otras partes del programa.

---

## ¿Qué son las funciones Lambda?

Las funciones lambda en Python no tienen un nombre explícito y están limitadas a una sola expresión. Esto significa que todo el contenido debe evaluarse y devolverse en una línea.

### Ejemplo Básico

```python
# Declaramos una función lambda que suma dos números
suma = lambda x, y: x + y

# Usamos la función lambda
print(suma(10, 5))  # Resultado: 15
```

---

## ¿Por qué son importantes las funciones Lambda?

Las funciones lambda son útiles para:

- **Escribir funciones pequeñas** de manera concisa.
- **Usarlas como argumentos** en funciones de orden superior como `map`, `filter` o `reduce`.
- **Mejorar la legibilidad** en casos simples, manteniendo el código limpio y Pythonista.

### Ventajas

1. Reducen la necesidad de definir funciones largas y formales.
2. Facilitan la escritura de código más compacto y legible.

### Limitaciones

1. No pueden contener varias líneas de código.
2. Son menos legibles para operaciones complejas.

---

## Operador Ternario con Lambdas

Los **operadores ternarios** permiten escribir condiciones `if-else` en una sola línea, lo que los hace ideales para usarse en funciones lambda.

### Ejemplo con Lambda

```python
# Declaramos una función lambda que verifica si un número es par
es_par = lambda num: True if num % 2 == 0 else False

# Usamos la función lambda
print(es_par(10))  # Resultado: True
print(es_par(5))   # Resultado: False
```

---

## Aplicaciones de las Lambdas

Las funciones lambda se usan comúnmente en conjunto con funciones de orden superior como:

- **Map**: Aplica una función a cada elemento de un iterable.
- **Filter**: Filtra elementos de un iterable según una condición.
- **Reduce**: Reduce un iterable a un único valor (requiere importar `functools`).

Cada una de estas funciones será explicada más adelante en este curso.

---
