# Función `filter` en Python

La función **`filter`** es una función de orden superior que permite filtrar elementos de un iterable (como listas o tuplas) según una condición definida por una función. Devuelve únicamente los elementos que cumplen con la condición especificada.

---

## ¿Cómo Funciona `filter`?

La función **`filter`** acepta dos parámetros:

1. **Una función** que retorna `True` o `False` para cada elemento del iterable.
2. **Un iterable** como una lista, tupla o rango.

El resultado es un objeto `filter` que contiene solo los elementos para los cuales la función devolvió `True`.

---

## Ejemplo: Filtrar Elementos con una Función Normal

A continuación, filtramos los números pares de una lista:

```python
# Lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Función para filtrar números pares
def is_even(num):
    return num % 2 == 0

# Aplicamos filter para obtener los números pares
pair_numbers = list(filter(is_even, numbers))

# Imprimimos los números pares
print(pair_numbers)  # Resultado: [2, 4, 6]
```

---

## Ejemplo: Filtrar con `lambda`

Las **funciones lambda** simplifican aún más el uso de `filter`, ya que permiten definir la lógica de la función directamente en el lugar donde se aplica:

```python
# Rango de números de 0 a 10
numbers = range(0, 10)

# Filtramos los números impares con una lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Imprimimos los números impares
print(odd_numbers)  # Resultado: [1, 3, 5, 7, 9]
```

---

## Características de `filter`

- **Condicional basada en funciones**: Requiere una función que devuelva un valor booleano (`True` o `False`) para cada elemento.
- **Iteración eficiente**: Devuelve un objeto `filter`, que es un iterable eficiente, en lugar de generar inmediatamente una lista o tupla.
- **Compatible con funciones lambda**: Ideal para operaciones rápidas y concisas.

---

## Ventajas de Usar `filter`

1. **Simplicidad**: Elimina la necesidad de escribir bucles manuales para filtrar elementos.
2. **Legibilidad**: Hace que el código sea más limpio y fácil de entender.
3. **Eficiencia**: Evalúa los elementos a medida que se iteran, sin crear estructuras de datos innecesarias.

---

## Consideraciones

- El resultado de `filter` debe convertirse a una lista o tupla si se necesita un acceso directo a los datos filtrados.
- La función pasada como parámetro debe manejar correctamente los datos del iterable para evitar errores.

---
