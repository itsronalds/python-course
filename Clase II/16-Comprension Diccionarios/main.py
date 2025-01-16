# Creamos nuestro diccionario con nombres de algunos países
dict1 = {'a': 'usa', 'b': 'venezuela', 'c': 'chile'}

# Creamos un nuevo diccionario con los nombres formateados
dict2 = {key: value.capitalize() for (key, value) in dict1.items()}

# { 'a': 'Usa', 'b': 'Venezuela', 'c': 'Chile' }
print(dict2)

print('-------------------------------------------\n')

# Creamos nuestro diccionario con nombres de algunos países
dict1 = {'a': 1, 'b': 2, 'c': 3}

# Creamos un nuevo diccionario con los nombres en minúsculas
dict2 = {key*2: value for (key, value) in dict1.items()}

# { 'aa': 1, 'bb': 2, 'cc': 3 }
print(dict2)

print('-------------------------------------------\n')

# Creamos nuestro diccionario algunos números
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Creamos un nuevo diccionario con los números pares
dict2 = {key: value for (key, value) in dict1.items() if value % 2 == 0}

print('Números pares ===>', dict2)
