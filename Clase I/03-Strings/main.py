name = 'Guido'
lastname = 'Van Rossum'

print(name, lastname)

# Concatenación de strings
fullname = name + lastname
print(fullname)

# Colocar un espacio entre strings
fullname = name + ' ' + lastname
print(fullname)

# Uso de apostrofes
quote = "I'm a programmer"
print(quote)

quote = 'I\'m a programmer'
print(quote)

quote2 = 'My favorite language is "Python"'
print(quote2)

# Concatenación de string

# No es posible concatenar un valor string con un valor de tipo número, por ejemplo:
# print('Mi nombre es ' + name + ' y tengo: ' + 25)

# Forma 1
template1 = 'Hi, my name is ' + name + ' and my lastname is ' + lastname
print(template1)

# Forma 2
template2 = 'Hi, my fullname is {} and I\'m {} years old'.format(fullname, 25)
print(template2)

# Forma 3
template3 = f'Hi, my fullname is {fullname} and I\'m {25} years old'
print(template3)

# Utilizar función format para pasar valores enteros a decimal en string
template4 = f'The result is: {3:.2f}'
print(template4)

shirt_price = 49

template5 = f'The shirt price is: ${shirt_price:.2f}'
print(template5)
