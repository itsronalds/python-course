# Función map

Es una función de orden superior que acepta dos parámetros, el primer parámetro será una función que se ejecutará por cada elemento en el iterable, y el segundo parámetro será el iterable.

La función map tiene la capacidad de cambiar la estructura interna de un elemento iterable y devolver una lista.

# Iteración con función map

```$
# Creamos una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Función que suma cada elemento
def add(x):
    return x + 1

# Sumar un número a cada elemento
new_numbers = map(add, numbers)

# Retorna un objeto map
print(new_numbers)

# Podemos convertir a lista o tupla
new_numbers = list(new_numbers)

# Valores sumados
print(new_numbers)
```

# Iteración con función map y lambda

```$
# Creamos una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Sumar un número a cada elemento
new_numbers = map(lambda x: x + 1, numbers)

# Retorna un objeto map
print(new_numbers)

# Podemos convertir a lista o tupla
new_numbers = list(new_numbers)

# Valores sumados
print(new_numbers)
```

# Iterar dos iterables a la vez

```$
# Creamos dos listas paralelas
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]

# Sumamos un valor de una lista con el de la otra lista
numbers_3 = map(lambda x, y: x + y, numbers_1, numbers_2)

# Resultado
print(numbers_3)
```

> Si los iterables no son paralelos los datos que no pueden relacionarse no serán iterados
