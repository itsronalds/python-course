'''

Aquí se muestran los tipos de datos básicos en Python

'''

# ---------------------------------------------- Variables y lectura ----------------------------------------------

# string
name = 'John Myers'

# Conocer el tipo de dato de una variable
print(type(name))

# Imprimir el valor de una variable
print(name)

# int
age = 30
print(type(age))
print(age)


# float
height = 1.83
print(type(height))
print(height)

# bool
is_developer = True
print(type(is_developer))
print(is_developer)

is_student = False
print(is_student)

# ---------------------------------------------- Sobreescribir variables ----------------------------------------------

name = 'Ronald Abu Saleh'
print(name)

age = 25
print(age)

is_developer = False
print(is_developer)

# ---------------------------------------------- Función de input -----------------------------------------------------

# Solicitar el nombre al usuario
name = input('What is your name? ')

# Imprimir el tipo de dato (la función input siempre devuelve un string)
print(type(name))

# Imprimir el valor de la variable en consola
print(name)
