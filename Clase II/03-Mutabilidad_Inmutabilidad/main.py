# Strings
print('Strings')

place = 'Los Angeles'
print(place)

# ❌ Obtenemos una excepción
# place[0] = 'l'

place = place.replace('L', 'l')

# ✅ El método replace crea un nuevo objeto string - Resultado: los Angeles
print(place)

print('---------------------------------------------')

# Valores númericos
print('INTEGER')

a = 10
b = 5

# ✅ Al usar un operador aritmético se crea un nuevo objeto numérico
c = a + b
print(c)

print('---------------------------------------------')

print('FLOATS')

x = 10.5
y = 1.11

c = x + y
print(c)

print('---------------------------------------------')

print('COMPLEX')

a = 2 + 3j
b = 1 + 2j

c = a + b
print(c)

print('---------------------------------------------')

print('TUPLES')

t = (1, 'a', 2, '3')
print(t)

# ❌ No podemos mutar un objeto tuple
# t[0] = 'b'

# Solo podemos usar métodos de read como index o count
print(t.index('a'))
print(t.count(2))

print('---------------------------------------------')

# Listas

print('LISTS')

l = [1, {'a': 'a', 'b': 'b'}, 2, 3, 'a']

# ✅ Podemos mutar un objeto lista
index = l.index('a')
l[index] = 4

print(l)

print('---------------------------------------------')

print('DICTIONARIES')

d = {'a': 1, 'b': 2, 'c': 3}

# ✅ Podemos mutar un objeto diccionario
d['d'] = 4
print(d)

print('---------------------------------------------')

print('SETS')

s = {1, 2, 3, 4, 5}

# ✅ Podemos mutar un objeto set
s.update({6, 7, 8, 9, 10})

print(s)
