text = 'Today I wake up at 9:00 am.'

# Acceder a una posición del string
value = text[4]
print(value)

# Obtener solo el horario
schedule = text[19:26]

# Resultado: 9:00 am
print('Schedule =>', schedule)

text = 'Today I played soccer'

first_words = text[:14]

# Resultado: Today I played
print('First words =>', first_words)

# Extraer carácteres de dos en dos
text = 'Welcome to the island'

# Resultado:
print(text[::2])
