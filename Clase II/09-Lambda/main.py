# Declaramos nuestra función lambda que suma dos parámetros
addition = (lambda x, y: x + y)

# Imprimimos el resultado: 15
print('SUMA ==>', addition(10, 5))

# Múltiplicar parámetros
multiply = (lambda x, y: x * y)

print('MULTIPLICACIÓN ==>', multiply(2, 10))

# Lambda con expresión lógica
is_pair = (lambda num: True if num % 2 == 0 else False)

# True
print('Is 10 pair:', is_pair(10))

# False
print('Is 5 pair:', is_pair(5))
