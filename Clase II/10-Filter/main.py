print('Filtrar números pares con la función filter\n')

# Creamos una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Función para filtrar números pares


def pairs(num):
    if num % 2 == 0:
        return True
    else:
        return False


# Filtrar números pares
pair_numbers = list(filter(pairs, numbers))

# Números pares
print(pair_numbers)

print('\nFiltrar números impares con la función filter utilizando lambda\n')

numbers = range(0, 10)

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)
