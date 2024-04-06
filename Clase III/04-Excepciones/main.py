# assert
x = 10

# assert x == 9, "x no es 9"


def suma(x, y): return x + y


assert suma(2, 3) == 5, "La suma no es 5"

# print('\n----------------------------------------\n')

numbers = range(5)

developer = {
    'name': 'John',
    'age': 30,
    'position': 'Software Engineer'
}

# Exception
# Exception('this is an exception')

# SintaxError
# print('Welcome to Python'))

# Typerror
# print(10 / '2')

# NameError
# print(x)

# IndexError
# print(numbers[5])

# KeyError
# print(developer['salary'])

# ValueError
# print(int('l'))

# ZeroDivisionError
# print(2 / 0)

print('----------------------------------------')

# Try and Except in Python


def suma(x, y):
    try:
        return x + y
    except TypeError as te:
        return str(te)
    except Exception as e:
        return e


print(type(suma(2, 'l')))
print(suma(2, 'l'))


print('----------------------------------------')

# Finally in Python


try:
    print('Welcome to Python' + 2)
except:
    print('An error occurred')
finally:
    print('Finally block')

print('Exit.')

print('----------------------------------------')

# Raise: custom errors

# raise ('This is an exception')

try:
    name = 'Ronald'

    if name != 'John':
        raise Exception('This is not John')
except Exception as e:
    print(type(e))
    print(e)
    print(str(e))
    print(type(str(e)))
