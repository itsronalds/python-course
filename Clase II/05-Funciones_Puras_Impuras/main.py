print('Funciones puras')

# Ejemplo #1: Función que depende solo de sus parámetros


def addition(x, y):
    return x + y


def to_lower(str=''):
    return str.lower()


print(addition(40, 50))
print(to_lower('HellO'))


# Ejemplo 2: Funciones que interactuan con valores externos pero sin mutarlos

customers = ['Ronald A.', 'Jesús M.', 'Andrés M.']


def add_customer(name):
    new_customers = [*customers, name]
    return new_customers


customer_1 = add_customer('Benito M.')
print(customer_1)

print('----------------------------------------------------------------')

numbers = [1, 2, 3]


def add_number(number):
    numbers.append(number)
    return numbers


result1 = add_number(10)
print('Result 1', result1)

result2 = add_number(10)
# print('Result 1', result1)
print('Result 2', result2)

# print(result1)
# print(result2)

# if result1 == result2:
#     print('Same')
# else:
#     print('Not same')
