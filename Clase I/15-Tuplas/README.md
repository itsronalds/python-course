# Tuplas

Las tuplas en Python son estructuras de datos inmutables, esto significa que una vez creado no puede alterarse su estructura de datos, son parecidos a las list en algunos métodos.

Creamos una tupla de la siguiente manera:

```$
numbers = (1, 2, 3, 4)

# Tuple
print(type(numbers))

# (1, 2, 3, 4)
print(numbers)

```

# Métodos de tuplas

Las tuplas posee métodos que podemos utilizar en determinadas ocasiones dependiendo de nuestro objetivo.

- Métodos de tuplas:

| Métodos      |                           Explicación                            |              Ejemplo |
| :----------- | :--------------------------------------------------------------: | -------------------: |
| index(value) |           Retorna la posición de la primera ocurrencia           | tuple.index('value') |
| count(value) | Retorna la cantidad de veces que encuentra el valor que deseamos | tuple.count('value') |

# Indice de un valor

```$
# Declaramos una tupla
data = (1, 2, 3, 4, 'request 1', 'request 2')

# 4
index = data.index('request 1')

# request 1
print(data[index])
```

# Contar ocurrencias

```$
# Declaramos una tupla con ocurrencias
data = (1, 2, 'a data', 4, 4, 4, 5, 6, '...n data')

# Obtener ocurrencias para "4"
occurrence = data.count(4)

# El número 4 aparece 3 veces
print(f'El número 4 aparece {occurrence} veces')
```

# Convertir tupla a lista (y viceversa)

Al igual como vimos en la sección de transformaciones, en Python podemos usar esta técnica con listas y tuplas:

```$
# Declaramos una tupla
server_data = ('data 1', 'data 2', 'data 3', '10', 1, True, False)

# ('data 1', 'data 2', 'data 3', '10', 1, True, False)
print(server_data)

# Queremos modificar la tupla, pasamosla a lista
server_data_list = list(server_data)

# Eliminamos los valores booleanos
server_data_list.removeU(True)
server_data_list.removeU(False)

# ['data 1', 'data 2', 'data 3', '10', 1]
print(server_data_list)

# Pasamos de lista a tupla
server_data_tuple = tuple(server_data_list)
```
