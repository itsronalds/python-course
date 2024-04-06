# Args en funciones

La palabra clave \*args en funciones, es la forma en como pasamos un número indefinido de valores como parámetros de una función.

> Tienen el nombre como non-keyworded porque los valores los obtenemos a través de una tupla donde solo encontramos los valores sin palabras claves.

# ¿Cómo utilizamos \*args en funciones?

```$
# Definimos una función que tome un número de parámetros indefinidos
def print_numbers(*argv):
    for num in argv:
        print(num)


# Llamamos a la función imprimir números y le pasamos una serie de números
print_numbers(1, 10, 20, 40, 0, 10)
```

# Utilizar \*args en funciones con paráemtros por aparte

Cuando utilizamos \*args en funciones podemos utilizarlo con otros parámetros de la siguiente manera:

```$
# Definimos nuestra función con *args y algún parámetro por aparte
def plus_random_number(plus_number, *argv):
    new_numbers = []

    for number in argv:
        new_numbers.append(number + plus_number)

    return new_numbers


# Ejecutamos la función pasando un número de sumatoria y un número indefinido de valores
new_numbers = plus_random_number(5, 10, 15, 20, 25, 30)

# Imprimimos nueva lista de números
print(new_numbers)
```
