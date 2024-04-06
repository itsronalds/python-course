# Definimos una función que obtenga un diccionario mediante un **kwargs
def print_values(**kwargs):
    for (key, value) in kwargs.items():
        print(key, '=>', value)


# Pasamos a la función parámetros mediante clave-valor
print_values(name='Ronald', lastname='Abu Saleh', age=30)

print('\n-------------------------------------------------\n')


# Definimos una función que obtenga un diccionario mediante un **kwargs
def greetings(welcome, **kwargs):
    quote = f'{welcome} {kwargs['name']} {
        kwargs['lastname']} de {kwargs['age']} años'
    print(quote)


# Pasamos a la función parámetros mediante clave-valor
greetings('Bienvenido/a', name='Ronald', lastname='Abu Saleh', age=30)
