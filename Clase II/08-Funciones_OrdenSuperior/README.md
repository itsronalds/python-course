# Funciones de orden superior

Son funciones que aceptan otras funciones como parámetros y pueden retornar un valor o una función para ser instanciada en una variable y posteriormente ejecutada.

- Función de orden superior que acepta una función como parámetro:

```$
def addition(a, b):
    return a + b


def substract(a, b):
    return a - b


def calculator(operation, a, b):

    if not isinstance(a, (int, float)):
        return 'Wrong first value'

    if not isinstance(b, (int, float)):
        return 'Wrong second value'

    return operation(a, b)


a = calculator(addition, 10, 10)
b = calculator(substract, 20, 10)
print('Addition', a)
print('Substract', b)
```

- Función de orden superior que me retorna una función:

```$
def outer(x):

    def add(y):
        return x + y

    def substract(y):
        return x - y

    return add, substract


c = outer(10)
d = c[0](20)
print(d)

e = c[1](5)
print(e)
```
