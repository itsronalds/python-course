import operator
print('Iteración con función map\n')

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

print('\n Iterando con una función map y lambda\n')

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

print('\nIterando con map dos iterables a la vez\n')

# Creamos dos listas paralelas
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]

# Sumamos un valor de una lista con el de la otra lista
numbers_3 = map(lambda x, y: x + y, numbers_1, numbers_2)

# Resultado
print(tuple(numbers_3))
