# Kwargs en funciones

La palabra clave \*\*kwargs permite pasarle a una función a través de parámetros un diccionario (pares clave-valor) con una cantidad de valores indefinidos.

> Se maneja a través del llaves clave-valor y se obtienen mediante un diccionario en una función.

# ¿Cómo utilizamos \*\*kwargs en funciones?

```$
# Definimos una función que obtenga un diccionario mediante un **kwargs
def print_values(**kwargs):
    for (key, value) in kwargs.items():
        print(key, '=>', value)

# Pasamos a la función parámetros mediante clave-valor
print_values(name='Ronald', lastname='Abu Saleh', age=30)
```

# Utilizar \*\*kwargs con parámetros por aparte

```$
# Definimos una función que obtenga un diccionario mediante un **kwargs
def greetings(welcome, **kwargs):
    quote = f'{welcome} {kwargs['name']} {kwargs['lastname']} de {kwargs['age']} años'
    print(quote)

# Pasamos a la función parámetros mediante clave-valor
greetings(name='Ronald', lastname='Abu Saleh', age=30)
```
