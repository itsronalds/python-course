# Ciclo for

Uno de los ciclos más utilizados en Python para poder iterar estructuras de datos como: strings, listas, sets, diccionarios y tuplas.

En esta sección veremos cómo recorrer cada una de las estructuras de datos mencionadas y algunos operadores que podemos utilizar.

## Recorrer estructuras de datos

### Recorrer un string

```python
quote = 'Welcome'
new_quote = ''

for letter in quote:
    new_quote += letter

print(new_quote)
```

### Recorrer una lista

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

### Recorrer un diccionario

```python
laptop = {
    'model': 'Example-x10',
    'brand': 'Apple',
}

for key in laptop:
    print(f'{key}: {laptop[key]}')
```

### Recorrer un set

```python
data = { 'data 1', 10, 'data 2' }

for value in data:
    print(value)
```

### Recorrer una tupla

```python
numbers = (1, 10, 6, 5, 8)

for value in numbers:
    print(value)
```

## Operador break

Detiene la ejecución del ciclo for como en el ciclo while.

```python
fruits = ['Fresa', 'Banana', 'Melón', 'Patilla']

for fruit in fruits:
    if fruit == 'Melón':
        break
    print('Fruta =>', fruit)
```

## Operador continue

Continúa a la siguiente iteración.

```python
fruits = ['Fresa', 'Banana', 'Melón', 'Patilla']

for fruit in fruits:
    if fruit == 'Fresa':
        continue
    print('Fruta =>', fruit)
```

## Función range

Función que nos ayuda a iterar una estructura de datos a través de posiciones numéricas:

```python
for x in range(6):
    print(x)
```

> Por default la función range comienza desde el número 0.

```python
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    print(numbers[i])
```

## Función enumerate

Función que nos permite obtener el índice por cada iteración.

```python
numbers = [1, 2, 3, 4]

for index, value in enumerate(numbers):
    print(f'Posición: {index} => Valor: {value}')
```

## Sentencia else en ciclo for

La sentencia else la podemos utilizar cuando un ciclo for finaliza su ejecución.

```python
numbers = [1, 2, 3, 4]

for value in numbers:
    print(value)
else:
    print('Ciclo finalizado')
```
