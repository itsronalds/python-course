print('LOCAL SCOPE')

# ✅ Forma Pythonica de limpiar un string


def clear_string(string=''):
    return ''.join(letter for letter in string if letter == ' ' or letter.isalnum())


# ❌ Forma no Pythonica de limpiar un string
# def clear_string(string=''):
#     clean_string = ''
#     for letter in string:
#         if letter == ' ' or letter.isalnum():
#             clean_string += letter
#     return clean_string


# ❌ Nos da error porque la variable se encuentra definida en un scope local o de función
# print(clean_string)

random_string = 'Hol$a chic#os'

clean_string = clear_string(random_string)

# ✅ String limpio sin caracteres especiales
print(clean_string)

print('--------------------------------------------------')

print('NESTED SCOPE')


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

print('--------------------------------------------------')

print('GLOBAL SCOPE')

a = 10
b = 20


def global_addition(custom_a, custom_b):
    a = custom_a if custom_a else a
    b = custom_b if custom_b else b

    return a + b


# Resultado: 50
print(global_addition(20, 30))

print('--------------------------------------------------')

print('BUILT-IN SCOPE')

print('Built-in scope:', len('Hola'))
print('Built-in scope:', list(range(0, 10, 2)))
