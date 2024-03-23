# Creamos un conjunto de números
numbers = {1, 2, 3, 4, 1}

# Resultado: { 1, 2, 3, 4 } ya que elimina valores duplicados
print(numbers)

print('-------------------------------------------------------------')

print('Método add')

# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Agregamos un nuevo valor
numbers.add(20)

# Resultado: 1, 2, 5, 10, 20
print(numbers)

print('-------------------------------------------------------------')

print('Método update')

# Creamos conjunto A
numbers_a = {1, 10, 5, 2}

# Creamos conjunto B
numbers_b = {1, 11, 5, 3}

# Actualizamos conjunto a
numbers_a.update(numbers_b)

# Resultado: 1, 2, 3, 5, 10, 11
print(numbers_a)

print('-------------------------------------------------------------')

print('Método discard')

# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Removemos el valor 10
numbers.discard(10)

# Resultado: 1, 2, 5
print(numbers)

print('-------------------------------------------------------------')

print('Método remove')

# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Removemos el valor 5
numbers.remove(5)

# Resultado: 1, 2, 10
print(numbers)

print('-------------------------------------------------------------')

print('Método pop')

# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Removemos un valor random
print('Removed item =>', numbers.pop())

# Mostramos el resultado
print(numbers)

print('-------------------------------------------------------------')

print('Método union')

# Creamos un conjunto a
numbers_a = {1, 10, 5, 2}

# Creamos un conjunto b
numbers_b = {6, 7, 11, 12}

# Creamos un nuevo conjunto a partir de la unión
numbers_c = numbers_a.union(numbers_b)

# Mostramos el resultado
print(numbers_c)
