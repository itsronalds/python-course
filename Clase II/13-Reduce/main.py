# Importamos la función reduce
from functools import reduce

print('Obtener el menor número de una lista de números\n')

# Creamos una lista con valores aleatorios
numbers = [4, 2, 10, 1]

# Obtenemos el menor número de todos
smallest = reduce(lambda x, y: x if x < y else y, numbers)

# Hacemos print del valor
print(smallest)

print('\nObtener el total de números de una lista\n')

# Obtenemos el total de todos los números
total = reduce(lambda x, y: x + y, numbers)

# Hacemos print del valor
print(total)
