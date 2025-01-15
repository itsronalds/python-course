# Tuplas en Python

Las **tuplas** son estructuras de datos **inmutables** en Python. Esto significa que, una vez creadas, **no se pueden modificar**. Aunque comparten algunas similitudes con las listas, su inmutabilidad las hace ideales para datos que no deben cambiar.

## Creación de una Tupla

Podemos crear una tupla utilizando paréntesis `()` o la función `tuple()`:

```python
# Declaración de una tupla
numbers = (1, 2, 3, 4)

# Verificar el tipo de dato
print(type(numbers))  # Resultado: <class 'tuple'>

# Mostrar la tupla
print(numbers)  # Resultado: (1, 2, 3, 4)
```

## Métodos de las Tuplas

Aunque las tuplas son inmutables, cuentan con algunos métodos útiles que nos permiten realizar consultas específicas:

| **Método**      | **Descripción**                                                        | **Ejemplo**             |
|------------------|------------------------------------------------------------------------|--------------------------|
| `index(value)`   | Retorna la posición de la **primera ocurrencia** del valor especificado. | `tuple.index('value')`   |
| `count(value)`   | Retorna la cantidad de veces que el valor aparece en la tupla.         | `tuple.count('value')`   |

## Uso de los Métodos

### Obtener el Índice de un Valor

El método `index()` devuelve la posición de un elemento dentro de la tupla:

```python
# Declaramos una tupla
data = (1, 2, 3, 4, 'request 1', 'request 2')

# Buscar el índice del valor 'request 1'
index = data.index('request 1')

# Imprimir el valor utilizando su índice
print(data[index])  # Resultado: request 1
```

### Contar Ocurrencias de un Valor

El método `count()` nos permite contar cuántas veces aparece un valor en una tupla:

```python
# Declaramos una tupla con valores repetidos
data = (1, 2, 'a data', 4, 4, 4, 5, 6, '...n data')

# Contar cuántas veces aparece el número 4
time_4 = data.count(4)

# Imprimir el resultado
print(f'El número 4 aparece {time_4} veces')  # Resultado: El número 4 aparece 3 veces
```

## Convertir una Tupla a Lista (y viceversa)

En Python, podemos convertir fácilmente una tupla a una lista (y viceversa) para realizar modificaciones cuando sea necesario:

```python
# Declaramos una tupla
server_data = ('data 1', 'data 2', 'data 3', '10', 1, True, False)

# Mostrar la tupla original
print(server_data)  # Resultado: ('data 1', 'data 2', 'data 3', '10', 1, True, False)

# Convertimos la tupla en una lista para modificarla
server_data_list = list(server_data)

# Eliminamos los valores booleanos
server_data_list.remove(True)
server_data_list.remove(False)

# Mostrar la lista modificada
print(server_data_list)  # Resultado: ['data 1', 'data 2', 'data 3', '10', 1]

# Convertimos de nuevo la lista a una tupla
server_data_tuple = tuple(server_data_list)

# Mostrar la nueva tupla
print(server_data_tuple)  # Resultado: ('data 1', 'data 2', 'data 3', '10', 1)
