# Función filter

Es una función de orden superior que acepta dos parámetros, el primer parámetro será una función que se ejecutará por cada elemento en el iterable, y el segundo parámetro será el iterable.

La función filter se encarga de filtrar elementos a partir de una condicional.

# Iteración con función filter

```$
# Creamos una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Función para filtrar números pares
def pairs(num):
    if num % 2 == 0:
        return True
    else:
        return False


# Filtrar números pares
pair_numbers = list(filter(pairs, numbers))

# Números pares
print(pair_numbers)
```

# Iterar con función filter y lambda

```$
# Creamos un iterable de 0 a 10
numbers = range(0, 10)

# Filtramos los números impares
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Mostrar impares
print(odd_numbers)
```
