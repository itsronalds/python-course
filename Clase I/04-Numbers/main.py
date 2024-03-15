'''
En esta sección exploraremos los diferentes tipos de números en Python y sus usos básicos.
'''

# Integers: números enteros positivos o negativos
lives = 3
print(type(lives))
print(lives)

# Disminuir el número de vidas
lives = lives - 1

# Forma Pythonica
lives -= 1

# Incrementar el número de vidas
lives += 2

print('----------------------------------------------------------------------------------------')

# Floats: números decimales
salary = 3500.00
print(type(salary))
print(salary)

print('----------------------------------------------------------------------------------------')

# Complex: números complejos
complex_number1 = complex(2, 3)
print(type(complex_number1))
print(complex_number1)

# Forma Pythonica
complex_number2 = 2 + 3j
print(type(complex_number2))
print(complex_number2)

# Suma de números complejos
complex_number3 = complex_number1 + complex_number2
print(type(complex_number3))
print(complex_number3)

print('----------------------------------------------------------------------------------------')

# Notación científica
number1 = 354547000000000000.000
print(number1)

number2 = 0.00000000000000000011
print(number2)

print('----------------------------------------------------------------------------------------')
