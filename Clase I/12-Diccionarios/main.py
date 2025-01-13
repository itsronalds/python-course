# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}

# Imprimimos el tipo
print(type(person))

# Imprimimos el resultado
print(person)

# Accediendo a valores
print(person['name'])
print(person['age'])
print(person['position'])

# Añadiendo valores
person['experience'] = 'semi-senior'
print(person['experience'])

# Modificando valores
person['experience'] = 'senior'
print(person['experience'])

# Eliminando valores
del person['age']
print(person)

print('----------------------------------------------------------------------------------')

car = {
    'model': 'Honda Civic',
    'owner': 'Ryan Jenkins',
    'year': 2010
}

# Accediendo a valores: método get
print(f'El auto {car.get('model')} es del año {car.get('year')}')

# Añadiendo nuevos valores: método update
car.update({'price': 4500})
print(f'''El auto {car['model']} del año {car['year']} propietario {
      car['owner']} cuesta al rededor de {car['price']} USD''')

# Actualizando valores: método update
car.update({'year': 2018})
print(f'El año del auto {car["model"]} es {car['year']}')

# Eliminando valores: método pop
car.pop('price')
print(car)

# Eliminando valores: método popitem
car.popitem()
print(car)

# Eliminamos todas las llaves del diccionario: método clear
car.clear()
print(car)
