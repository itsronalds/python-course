from random import randint


def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


a = 10
b = 5

print('SUMA ==>', addition(a, b))
print('RESTA ==>', subtract(a, b))

print('-------------------------------')

print('DEFAULT PARAMETERS')


def get_random_num(a=0, b=10):
    return randint(a, b)


print(get_random_num(5, 25))

a = 10, 20, 30
a = a[0], a[1], 40
print(a)

print('-------------------------------')

user = {
    'fullname': 'Ronald Abu Saleh',
    'username': 'itsronalds',
    'birthday': '01-07-98'
}


def get_user_data(user):
    fullname = user['fullname']
    username = user['username']
    birthday = user['birthday']

    if fullname == '' or username == '' or birthday == '':
        return 'Required fields'

    return fullname, username, birthday


user_data = get_user_data(user)

# tuple: ('Ronald Abu Saleh', 'itsronalds', '01-07-98')
print(user_data)

# Presentación
print(f'Hola, mi nombre es {user_data[0]}, mi username en GitHub es {
      user_data[1]} y nací en {user_data[2]}')

print('-------------------------------')


def addition_pass(a, b):
    pass


def subtract_pass(a, b):
    pass
