# Diccionarios

Los diccionarios en Python son estructuras de datos mutables que nos permiten almacenar datos mediante pares **clave-valor**.

---

## Creación de un Diccionario

```python
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}
print(type(person))

# Diccionario completo
print(person)
```

---

## Añadiendo Valores

Podemos agregar nuevas claves y valores al diccionario:

```python
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}

# Añadimos un nuevo par clave-valor
person['experience'] = 'semi-senior'

# Imprimimos el nuevo valor
print(person['experience'])
```

---

## Accediendo a Valores

```python
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer'
}

# Accedemos a un valor usando su clave
print(person['name'])  # Resultado: Ryan Jenkins

# Ejemplo práctico
print(f"Hola, mi nombre es {person['name']}, tengo {person['age']} años y soy {person['position']}.")
```

---

## Actualizando un Valor

```python
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer',
    'experience': 'semi-senior'
}

# Actualizamos un valor existente
person['experience'] = 'senior'

# Imprimimos el nuevo valor
print(person['experience'])
```

---

## Eliminando Valores

Usamos el operador `del` para eliminar una clave:

```python
# Creamos un diccionario
person = {
    'name': 'Ryan Jenkins',
    'age': 45,
    'position': 'Software Engineer',
    'experience': 'semi-senior'
}

# Eliminamos la clave 'age'
del person['age']

# Imprimimos el diccionario actualizado
print(person)
```

---

## Métodos de Diccionarios

Los diccionarios incluyen métodos útiles para manipular su contenido.

| Método      | Descripción                                   | Ejemplo                       |
| ----------- | --------------------------------------------- | ----------------------------- |
| `get()`     | Obtiene un valor mediante una clave           | `dict.get('key')`             |
| `update()`  | Añade o actualiza un par clave-valor          | `dict.update({'key': value})` |
| `pop()`     | Elimina un elemento especificado por su clave | `dict.pop('key')`             |
| `popitem()` | Elimina el último par clave-valor             | `dict.popitem()`              |
| `clear()`   | Elimina todos los elementos del diccionario   | `dict.clear()`                |
| `copy()`    | Crea una copia superficial del diccionario    | `dict.copy()`                 |

---

## Ejemplos de Métodos

### Método `get()`

```python
# Creamos un diccionario
car = {
    'model': 'Honda Civic',
    'owner': 'Ryan Jenkins',
    'year': 2010
}

# Obtenemos el año del auto
print(car.get('year'))
```

---

### Método `update()`

Añadir o actualizar valores:

```python
# Creamos un diccionario
car = {
    'model': 'Honda Civic',
    'owner': 'Ryan Jenkins',
    'year': 2010
}

# Añadimos un nuevo par clave-valor
car.update({'price': 4500})

# Actualizamos un valor existente
car.update({'year': 2018})

# Imprimimos el diccionario actualizado
print(car)
```

---

### Métodos `pop()`, `popitem()` y `clear()`

#### `pop()`

```python
# Creamos un diccionario
course = {
    'name': 'Python y Desarrollo Back-End',
    'tutor': 'Ronald A.',
    'levels': ['basic', 'intermediate', 'advanced'],
    'year': 2024
}

# Eliminamos un elemento especificado
course.pop('levels')

# Imprimimos el diccionario actualizado
print(course)
```

#### `popitem()`

```python
# Creamos un diccionario
course = {
    'name': 'Python y Desarrollo Back-End',
    'tutor': 'Ronald A.',
    'levels': ['basic', 'intermediate', 'advanced'],
    'year': 2024
}

# Eliminamos el último par clave-valor
course.popitem()

# Imprimimos el diccionario actualizado
print(course)
```

#### `clear()`

```python
# Creamos un diccionario
course = {
    'name': 'Python y Desarrollo Back-End',
    'tutor': 'Ronald A.',
    'levels': ['basic', 'intermediate', 'advanced'],
    'year': 2024
}

# Eliminamos todos los elementos
dict.clear()

# Imprimimos el diccionario vacío
print(course)
```

---

## Método `copy()`

Evita referencias compartidas entre variables:

```python
# Creamos un diccionario
laptop = {
    'model': 'XYExample-1',
    'brand': 'HP',
    'price': 599
}

# Copiamos el diccionario
new_laptop = laptop.copy()

# Alteramos el original
laptop['model'] = 'Lenovo'

# La copia permanece intacta
print(new_laptop['model'])  # Resultado: XYExample-1
```
