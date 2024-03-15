# Métodos de string

text1 = 'Soy desarrollador de REST APIs con Python'

# Pasar string a mayúsculas
print('upper =>', text1.upper())

# Pasar string a minúculas
print('lower =>', text1.lower())

# Contar cuantas veces se repite 'o'
print('count =>', text1.count('o'))

# Mayúsculas a minúsculas y minúsculas a mayúsculas
print('swapcase =>', text1.swapcase())

# Verifica si una cadena empieza con determinado valor
print('startswith =>', text1.startswith('Soy desarrollador'))

# False ya que la cadena a verificar debe ser exactamente igual
print('startswith =>', text1.startswith('soy desarrollador'))

# ¿Cómo solucionamos este problema? Utilizando lower en la cadena a verificar
print('startswith-lower =>', text1.lower().startswith('soy desarrollador'))

# Verifica si una cadena termina con determinado valor
print('endswith =>', text1.lower().endswith('python'))

# Pasa una cadena de texto a formato título
print('title =>', 'python course'.title())

# Verifica si una cadena es un número
print('isdigit =>', '6851'.isdigit())

# Solo nos retorna True si es un valor entero
print('isdigit-negativo =>', '6851.10'.isdigit())

print('--------------------------------------------------------------')

# Operadores generales en string: len, in

text2 = 'Estoy viendo el curso de Python'

print('len =>', len(text2))

# in es un operador que si encuentra coincidencias devuelve True de lo contario devuelve False

# Nota: este operador también en sensible a mayúsculas y minúsculas
key_word = 'Python'

print('in =>', key_word in text2)
