# asignar funciones a variables
def sum(a, b):
    return a + b


# instanciamos función sum a addition
addition = sum

# ejecutamos addition
print(addition(10, 20))

print('-----------------------------' * 2)


def plus_one(number):

    def add_one(number):
        return number + 1

    result = add_one(number)

    return result


print('-----------------------------' * 2)

# funciones como parámetro de otra función


def sum(x, y):
    return x + y


def calculator(function, x, y):
    result = function(x, y)
    return result


print(calculator(sum, 10, 20))

print('-----------------------------' * 2)


# funciones que tienen acceso a los parámetros de su función padre

def print_message(message):

    def send():
        print(message)

    send()


print_message('The best Python')

print('-----------------------------' * 2)

# Funciones que devuelven funciones


def upper_split(text):
    text = text.upper()

    def split():
        return text.split()

    return split


a = upper_split('Hello World')
b = a()

print(b)

print('-----------------------------' * 2)

# decoradores: primera forma


def uppercase_decorator(function):

    def wrapper():
        func = function()

        return func.upper()

    return wrapper


def greeting():
    return 'hello to everyone'


decorator = uppercase_decorator(greeting)

print(decorator())

print('-----------------------------' * 2)

# decoradores: segunda forma


def uppercase_decorator(function):

    def wrapper():
        func = function()

        return func.upper()

    return wrapper


@uppercase_decorator
def greeting():
    return 'hello to everyone'


print(greeting())

print('-----------------------------' * 2)

# múltiples decoradores


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

print('-----------------------------' * 2)

# decoradores con argumentos


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

main(req, res={})
