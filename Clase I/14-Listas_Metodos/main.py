# Crear una lista
numbers = [1, 2, 3, 4]

# Leer un elemento
value = numbers[1]
print(value)

# Actualizar un elemento
numbers[3] = 5

# 1ra solución: Eliminar un elemento
del numbers[3]
print(numbers)

numbers.append(4)
numbers.append(5)

# 2da solución: remove
numbers.remove(4)
print(numbers)

# 3ra solución: pop (eliminar el último elemento)
numbers.pop()
print(numbers)

# 4ta solución: pop (elemento específico según índice)
numbers.pop(0)
print(numbers)

# Método reverse: revierte los elementos de la lista
numbers.reverse()
print(numbers)

numbers.append(1)
numbers.append(4)

# Método sort: ordena los elementos de una lista
print('Unordered =>', numbers)

# sort asc
numbers.sort()

print('Unordered ASC =>', numbers)

# sort desc
numbers.sort(reverse=True)

print('Unordered DESC =>', numbers)

# Método sort en strings
developers = ['Ronald A.', 'Andrés M.']

# Ordenamos la lista según el alfabeto
developers.sort()

print(developers)
