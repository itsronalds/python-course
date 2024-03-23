# Scope en Python

El scope o alcance trata de la región donde una variable, clase o función puede ser utilizada según el lugar donde se creo en primera instancia.

# Regla LEGB (Local, Enclosing, Global, Build-in)

Python utiliza la regla de LEGB para sus scopes, cada uno maneja diferentes alcances y lo veremos a continuación:

- Local (o alcance de función): Todas las variables o funciones que se definan dentro de un bloque de código o cuerpo de una función solo podrán ser utilizadas dentro de la misma función o dentro de funciones anidadas

- Anidado (o no local): Todas las variables y funciones que son definidas dentro de una función anidada no podrán ser utilizadas en una función de orden superior y tampoco en el global scope

- Global (o módulo): Variables, funciones y clases que pueden ser ejecutadas dentro de cualquier scope en el módulo o archivo.

- Build-in: Funciones, variables o clases que pueden ser llamadas en cualquier lugar de nuestro programa Python, tienen un scope super global.

> Podemos usar la palabra clave **global** para poder cambiarle el scope a una variable dentro de una función por ejemplo y de esta forma poder hacer uso de la misma en un scope global o de módulo.

# Scope local

```$
def clear_string(string=''):
    clean_string = ''
    for letter in string:
        if letter == ' ' or letter.isalnum():
            clean_string += letter
    return clean_string


# ❌ Nos da error porque la variable se encuentra definida en un scope local o de función
# print(clean_string)

random_string = 'Hol$a chic#os'

clean_string = clear_string(random_string)

# ✅ String limpio sin caracteres especiales
print(clean_string)
```

# Scope anidado

```$
def outer_function():
    print('Outer Function')

    a = 10

    # No podemos utilizar la variable b porque está definida dentro de un scope anidado
    # print(b)

    def inner_function():
        print('Inner Function')

        # global scope
        global b
        b = 20

        print('Outer function variable:', a)
        print('Inner function variable:', b)

    inner_function()


outer_function()

# Global scope
print(b)
```

# Global scope

```$
a = 10
b = 20


def global_addition(custom_a, custom_b):
    a = custom_a if custom_a else a
    b = custom_b if custom_b else b

    return a + b


# Resultado: 50
print(global_addition(20, 30))
```

# Build-in scope

- Algunos ejemplos:

```$
print('Built-in scope:', len('Hola'))
print('Built-in scope:', list(range(0, 10, 2)))
```
