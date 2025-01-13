numbers = [1, 2, 3, 4, 5]
print(type(numbers))
print(numbers)

# Obtenemos un valor
index = 4
value = numbers[4]

print(value)

print('---------------------------------------------')

# Obtenemos la última posición
index = len(numbers) - 1
value = numbers[index]

# Resultado: 5
print(numbers)

print('---------------------------------------------')

programming_languages = ['Python', 'JavaScript', 'Java', 'Golang']

# Pedimos al usuario cuál es su tercer lenguaje favorito
favorite_language = input('¿Cuál es tu tercer lenguaje favorito? ')

# Actualizamos el tercer lenguaje de la lista
programming_languages[2] = favorite_language

# Imprimimos la lista actualizada
print(programming_languages)

print('---------------------------------------------')

# Slicing
print(numbers[4:])

print('---------------------------------------------')

courses_for = ['Python', 'JavaScript', 'Rust']

# ¿Hay cursos para Python?
has_python = 'Python' in courses_for
print(has_python)

# ¿Hay cursos para Golang?
has_golang = 'Golang' in courses_for
print(has_golang)
