# Recorre un string

print('Recorre un string')

quote = 'Welcome'

for letter in quote:
    print(letter)

print('-' * 80)

print('Recorrer una lista')

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

print('-' * 80)

print('Recorrer un diccionario')

laptop = {
    'model': 'Example-x10',
    'brand': 'Apple',
}

for key in laptop:
    print(f'{key}:{laptop[key]}')

print('-' * 80)

print('Recorrer un set')

data = {'data 1', 10, 'data 2'}

for value in data:
    print(value)

print('-' * 80)

print('Recorrer una tupla')

numbers = (1, 10, 6, 5, 8)

for value in numbers:
    print(value)

print('-' * 80)

print('Operador break')

fruits = ['Fresa', 'Banana', 'Melón', 'Patilla']

for fruit in fruits:
    if fruit == 'Melón':
        break
    print('Fruta =>', fruit)

print('-' * 80)

print('Operador continue')

fruits = ['Fresa', 'Banana', 'Melón', 'Patilla']

for fruit in fruits:
    if fruit == 'Fresa':
        continue
    print('Fruta =>', fruit)

print('-' * 80)

print('Función range')

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    print(numbers[i])

print('-' * 80)

print('Función enumerate')

numbers = [1, 2, 3, 4]

for index, value in enumerate(numbers):
    print(f'Posición: {index} => Valor: {value}')

print('-' * 80)

print('Sentencia lógica else en for')

numbers = [1, 2, 3, 4]

for value in numbers:
    print(value)
else:
    print('Ciclo finalizado')
