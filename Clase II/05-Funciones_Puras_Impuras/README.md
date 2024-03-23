# Funciones puras e impuras

En Python hay dos tipos de funciones, puras e impuras cada una se diferencia de la otra según el proceso que realiza y como lo realiza.

# Funciones puras

Son funciones que retornan un valor preciso según los parámetros que le pasemos, generalmente son fáciles de leer y pueden interactuar con variables o valores globales pero sin mutarlos.

- Funciones puras que solo interactuan con parámetros y devuelven un resultado preciso:

```$
def addition(x, y):
    return x + y


def to_lower(str=''):
    return str.lower()


# Resultado: 590
print(addition(40, 50))

# Resultado: hello
print(to_lower('HellO'))
```

- Funciones que interactuan con valores externos a la función pero que siempre devuelve un output preciso ya que no muta el valor externo:

```$
customers = ['Ronald A.', 'Jesús M.', 'Andrés M.']


def add_customer(name):
    new_customers = [*customers, name]
    return new_customers


customer_1 = add_customer('Benito M.')

# Resultado: ['Ronald A.', 'Jesús M.', 'Andrés M.', 'Benito M.']
print(customer_1)
```

# Funciones impuras

Son funciones que normalmente dependen de variables o estructuras externas para funciones, pero que además alteran dichas estructuras por lo que en cada llamada a la función el output será diferente:

```$
numbers = [1, 2, 3]


def add_number(number):
    numbers.append(number)
    return numbers


result1 = add_number(10)
print('Result 1', result1)

result2 = add_number(10)
print('Result 2', result2)
```
