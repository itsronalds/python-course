# Métodos de listas

Las listas son estructuras de datos mutables que nos permiten almacenar datos de todo tipo, por lo que existen métodos muy útiles para modificar a nuestro objetivo una lista.

Durante esta clase veremos los diversos métodos de listas y como aplicarlos.

- Métodos de listas:

| Métodos    |                                     Explicación                                      |                 Ejemplo |
| :--------- | :----------------------------------------------------------------------------------: | ----------------------: |
| append()   |                            Añadir un elemento a la lista                             |    list.append('value') |
| insert()   |                  Añadir un elemento a la lista junto a la posición                   | list.insert(5, 'value') |
| remove()   | Elimina la primera coincidencia de la lista según el valor que pasemos por parámetro |    list.remove('value') |
| pop()      |                        Elimina el último elemento de la lista                        |              list.pop() |
| pop(index) |                       Elimina el valor de un índice específico                       |             list.pop(2) |
| reverse()  |                   Coloca en reverso los elementos de nuestra lista                   |          list.reverse() |
| sort()     |                                 Ordena nuestra lista                                 |             list.sort() |

# Crear una list

```$
numbers = [1, 2, 3, 4, 5, '...n']
```

# Leer un elemento

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Obtenemos un elemento según su posición (la posición debe existir, sino recibiremos un error de Exception)

# 2
print(numbers[1])
```

# Añadir un elemento

- Añadir elemento a última posición

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Añadir elemento a última posición
numbers.append(5)

# [1, 2, 3, 4, 5]
print(numbers)
```

- Añadir elemento a una posición en específico

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Añadir elemento a última posición
numbers.insert(3, 10)

# [1, 2, 3, 10, 4]
print(numbers)
```

# Actualizar un elemento

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Actualizamos un elemento según su posición (la posición debe existir, sino recibiremos un error de Exception)
numbers[3] = 5

# [1, 2, 3, 5]
print(numbers)
```

# Remover un elemento

- Método remove:

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Removemos un elemento según la primera coincidencia que se encuentre
numbers.remove(1)

# [2, 3, 4]
print(numbers)
```

- Método pop:

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Removemos el último elemento de la lista
numbers.pop()

# [1, 2, 3]
print(numbers)
```

- Método pop con índice:

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Removemos el elemento de la lista según índice pasemos como parámetro a pop
numbers.pop(0)

# [2, 3, 4]
print(numbers)
```

- Delete según su índice:

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Removemos un elemento según su posición
del numbers[1]

# [1, 3, 4]
print(numbers)
```

# Reverse

```$
# Declaramos una lista
numbers = [1, 2, 3, 4]

# Revertimos la lista
numbers.reverse()

# [4, 3, 2, 1]
print(numbers)
```

# Sort

El método sort puede ordenar:

- Una lista númerica del más bajo al más alto

```$
# Declaramos una lista
numbers = [4, 2, 1, 3]

# Revertimos la lista
numbers.sort()

# [1, 2, 3, 4]
print(numbers)
```

- Una lista de strings en el orden alfabético:

```$
# Declaramos una lista
developers = ['Ronald A.', 'Andrés M.']

# Ordenamos la lista según el alfabeto
developers.sort()

# ['Andrés M.', 'Ronald A.']
print(developers)
```

- Método reverse de sort:

```$
# Declaramos una lista
numbers = [4, 1, 2, 3]

# Ordenamos la lista de mayor a menor
numbers.sort(reverse=True)

# [4, 3, 2, 1]
print(numbers)
```

> Solo podemos utilizar sort si la lista posee elementos del mismo tipo de datos sea: solo numbers o strings.
