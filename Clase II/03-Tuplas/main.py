# Creamos una tupla de datos
data = (1, 2, 5, 'data x', 1, 'data y')
print(type(data))
print(data)

# Leemos un valor de la tupla
print(data[3])

# Indice de "data y"
index = data.index('data y')

# Obtenemos ese valor
print(data[index])

# Contamos las ocurrencias de el valor entero "1"
count = data.count(1)
print(count)

print(f'El valor 1 aparece {count} veces.')

# Pasamos de tupla a lista
data_list = list(data)
print(type(data_list))
print('List =>', data_list)

# Modificamos la lista
data_list.append('data z')
print('Modified list =>', data_list)

# Eliminamos los valores enteros
data_list.remove(1)
data_list.remove(2)
data_list.remove(5)
data_list.remove(1)

# Pasamos de lista a tupla
data_tuple = tuple(data_list)
print(type(data_tuple))
print('Tupla de datos modificado =>', data_tuple)
