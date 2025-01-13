# Creamos un contador del 1 al 1000
counter = 0

while counter < 1000:
    counter += 1

print('Del 1-1000 =>', counter)

print('-------------------------------------------------------------')

# Operador break en while
numbers = []
counter = 0

while counter < 10:
    counter += 1
    if counter > 5:
        break
    numbers.append(counter)

print('Números del 1-5 =>', numbers)

print('-------------------------------------------------------------')

# Operador continue en while
numbers = []
counter = 0

while counter < 10:
    counter += 1
    if counter == 8:
        continue
    numbers.append(counter)

print('Del 1-10 al menos el 8 =>', numbers)

print('-------------------------------------------------------------')

# Recorrer una lista con while
numbers = [1, 2, 3, 4, 5]
counter = 0

# Imprimir los números de la lista
while counter < len(numbers):
    print(numbers[counter])
    counter += 1
