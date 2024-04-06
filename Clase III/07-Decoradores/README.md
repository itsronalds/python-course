# Decoradores

Son funciones que envuelven otra función y objeto para añadir funcionalidades sin alterar la estructura de dicha función u objeto.

Antes de comprender los decoradores debemos tener en cuenta varios conceptos:

# Asignar funciones a variables

Las funciones no solo pueden ser llamadas desde su nombre, sino que pueden asignarse a variables para posteriormente ser ejecutadas:

```$
def sum(a, b):
    return a + b


# instanciamos función sum a addition
addition = sum

# ejecutamos addition
print(addition(10, 20))
```

# Declarar función dentro de otra función

Podemos crear funciones anidadas que tengan acceso a las variables y parámetros de la función de orden superior:

```$
def plus_one(number):

    def add_one(number):
        return number + 1

    result = add_one(number)

    return result
```

# Pasar función como parámetro de otra función

Las funciones de orden superior son aquellas que reciben una función como parámetro o devuelven una función:

```$
def sum(x, y):
    return x + y


def calculator(function, x, y):
    result = function(x, y)
    return result


print(calculator(sum, x, y))
```

# Funciones que tienen acceso a paámetros o variables de su función padre

```$
def print_message(message):

    def send():
        print(message)

    send()


print_message('The best Python')
```

# Funciones que devuelven funciones

Las funciones que devuelven otras funciones son denominadas funciones de orden superior:

```$
def upper_split(text):
    text = text.upper()

    def split():
        return text.split()

    return split


a = upper_split('Hello World')
b = a()

print(b)
```

# Decorador

Función que envuelve otra función para añadir nuevas funcionalidades sin alterar la estructura de la función envolvida:

- Primera forma:

```$
def uppercase_decorator(function):

    def wrapper():
        func = function()

        return func.upper()

    return wrapper


def greeting():
    return 'hello to everyone'


decorator = uppercase_decorator(greeting)

print(decorator())
```

- Segunda forma:

```$
def uppercase_decorator(function):

    def wrapper():
        func = function()

        return func.upper()

    return wrapper


@uppercase_decorator
def greeting():
    return 'hello to everyone'


print(greeting())
```

# Múltiples decoradores

```$
def split_decorator(function):

    def wrapper():
        func = function()

        return func.split()

    return wrapper

def uppercase_decorator(function):

    def wrapper():
        func = function()

        return func.upper()

    return wrapper


@split_decorator
@uppercase_decorator
def greeting():
    return 'hello to everyone'


print(greeting())
```

# Decoradores con argumentos

```$
def decorator(function):

    def wrapper(req, res):
        # print(req)

        req['body']['username'] = 'max'

        return function(req, res)

    return wrapper


@decorator
def main(req, res):
    print('Hello', req, res)
    return req, res

req = {
    'body': {
        'username': 'ronald',
        'password': '123456'
    }
}

main(req, res = {})
```
