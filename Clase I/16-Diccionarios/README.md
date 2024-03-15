# Diccionarios

Estructuras de datos mutable que nos permiten almacenar datos mediante pares key-value.

- Creamos una diccionario:

```$
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}
print(type(person))

# Diccionario con todas sus llaves y valores
print(person)
```

- Añadiendo valores:

```$
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}

# Añadir un nuevo par key-value
person['experience'] = 'semi-senior'

# Imprimiendo el nuevo valor
print(person['experience'])
```

- Accediendo a valores:

```$
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}

# Imprimir nombre: Ryan Jenkins
print(person['name'])

# Imprimir una presentación
print(f'Hola, mi nombre es {person['name]}, tengo {person['age']} de edad y actualmente soy {person['position']}')
```

- Actualizando un valor

```$
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer',
    'experience': 'semi-senior'
}

# Actualizando la experiencia
person['experience'] = 'senior'

# Imprimiendo el nuevo valor
print(person['experience'])
```

- Eliminando un valor con el operador del:

```$
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer',
    'experience': 'semi-senior'
}

# Eliminamos la edad
del person['age']

# Imprimimos el diccionario actualizado
print(person)
```

# Métodos de diccionarios

Los diccionarios son estructuras de datos mutables, por lo que a través de algunos métodos podemos alterar su estructura.

| Métodos   |                           Explicación                           |                       Ejemplo |
| :-------- | :-------------------------------------------------------------: | ----------------------------: |
| get()     |         Obtiene un valor pasando el nombre de la llave          |               dict.get('key') |
| update()  |   Nos permite añadir o actualizar un elemento del diccionario   | dict.update({ 'key': value }) |
| pop()     |          Elimina la llave que le pasemos por parámetro          |               dict.pop('key') |
| popitem() |            Elimina el último valor de un diccionario            |                dict.popitem() |
| clear()   |           Elimina todas las llaves de un diccionario            |                  dict.clear() |
| copy()    | Instancia un diccionario creando una nueva refrencia en memoria |                   dict.copy() |

# Método get

Obtenemos un valor de un diccionario:

```$
# Creamos un diccionario
car = {
    model: 'Honda Civic',
    owner: 'Ryan Jenkins',
    year: 2010
}

# Obtenemos el años del auto
print(car.get('year'))
```

# Método update

- Añadimos un nuevo valor:

```$
# Creamos un diccionario
car = {
    model: 'Honda Civic',
    owner: 'Ryan Jenkins',
    year: 2010,
}

# Añadimos un nuevo valor
car.update({ 'price': 4500 })

# Imprimimos el nuevo valor
print(f'El carro modelo {car['model']} tiene de propietario a {car['owner']} y cuesta al rededor de {car['price']} USD')
```

- Actualizar un valor:

```$
# Creamos un diccionario
car = {
    model: 'Honda Civic',
    owner: 'Ryan Jenkins',
    year: 2010,
}

# Actualizamos el año
car.update({ 'year': 2018 })

# Imprimimos el nuevo valor
print(f'El carro modelo {car['model']} del año {car[year]}')
```

# Métodos pop, popitem y clear

- Método pop elimina una llave que le pasemos por parámetro:

```$
# Creamos un diccionario
course = {
    name: 'Python y Desarrollo Back-End'
    tutor: 'Ronald A.',
    levels: ['basic', 'intermediate', 'advanced'],
    year: 2024
}

# Eliminamos los niveles
course.pop('levels')

# Imprimimos el diccionario actualizado
print(course)
```

- Método popitem elimina la última llave:

```$
# Creamos un diccionario
course = {
    name: 'Python y Desarrollo Back-End'
    tutor: 'Ronald A.',
    levels: ['basic', 'intermediate', 'advanced'],
    year: 2024
}

# Eliminamos la última llave
course.popitem()

# Imprimimos el diccionario actualizado
print(course)
```

- Método clear elimina todas las llaves:

```$
# Creamos un diccionario
course = {
    name: 'Python y Desarrollo Back-End'
    tutor: 'Ronald A.',
    levels: ['basic', 'intermediate', 'advanced'],
    year: 2024
}

# Eliminamos todas las llaves
course.clear()

# Imprimimos el diccionario vacío
print(course)
```

# Método copy

- Cuando intentamos instanciar un diccionario en una variable pueden ocurrir comportamientos inesperados:

```$
# Creamos un diccionario
laptop = {
    model: 'XYExample-1',
    brand: 'HP',
    price: 599
}

# Creamos una nueva variable e instanciamos laptop
new_laptop = laptop

'''
Si alteramos los valores de "laptop" también se alterarán en "new_laptop"

¿Por qué sucede esto?

Porque Python automáticamente les colocará la misma referencia o dirección de memoria a "new_laptop" de "laptop", por motivos de rendimiento.

Python automáticamente controla los procesos de referencia en memoria
'''

# Cambiamos el modelo de "laptop"
laptop['model'] = 'Lenovo'

# Ahora, revisamos el modelo de "new_laptop", dará como resultado: Lenovo en vez de HP
print(new_laptop['model'])
```

- Para solucionar este problema utilizamos el método copy:

```$
# Creamos un diccionario
laptop = {
    model: 'XYExample-1',
    brand: 'HP',
    price: 599
}

# Creamos una nueva variable e instanciando "laptop" con el método copy (creando una nueva instancia en memoria)
new_laptop = laptop.copy()

# Alteramos el modelo de "laptop"
laptop['model'] = 'Lenovo'

# Verificamos el modelo de new_laptop, como resultado obtendremos: HP
print(new_laptop['model'])
```
