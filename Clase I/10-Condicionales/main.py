if True:
    print('Este bloque de código será ejecutado.')

if False:
    print('Este bloque de código no será ejecutado.')

print('---------------------------------------------------------')

# Evaluar nombres de mascotas

pet = input('¿Cuál es tu mascota favorita? ')

if pet == 'perro':
    print('Tu mascota favorita es: perro')
else:
    print('Tu mascota favorita es:', pet)

print('---------------------------------------------------------')

# Evaluar dos condiciones

programming_language = input('¿Cuál es tu lenguaje de programación favorito? ')

if programming_language == 'python':
    print('Mi lenguaje favorito número 1 es:', programming_language)
if programming_language == 'golang':
    print('Mi lenguaje favorito número 2 es:', programming_language)
else:
    print('Mi lenguaje favorito es:', programming_language)

'''
En el caso anterior el asume que los ultimos bloques if-else son los últimos, por lo que se ejecuta:

- primer if separado del segundo if
- segundo if junto al else

Cuando en realidad tratamos de evaluar 3 condiciones en una misma condición lógica
'''

print('---------------------------------------------------------')

# Para solucionar este problema, siempre debemos usar elif en condiciones que lleven más de un if

programming_language = input('¿Cuál es tu lenguaje de programación favorito? ')

if programming_language == 'python':
    print('Mi lenguaje favorito número 1 es:', programming_language)
elif programming_language == 'golang':
    print('Mi lenguaje favorito número 2 es:', programming_language)
else:
    print('Mi lenguaje favorito es:', programming_language)
