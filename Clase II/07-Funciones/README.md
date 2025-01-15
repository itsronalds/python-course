# Funciones en Python

Las **funciones** son bloques de código reutilizables diseñados para resolver un problema específico. Su propósito es modularizar la lógica del programa, facilitando la lectura, el mantenimiento y la reutilización del código.

## Beneficios de las Funciones

- ✅ Modularizar código para mantenerlo organizado.
- ✅ Descomponer problemas grandes en partes más pequeñas y manejables.
- ✅ Asignar una única responsabilidad a cada función, mejorando la legibilidad y el mantenimiento.

### Malas Prácticas

- ❌ Usar nombres ambiguos o poco descriptivos para las funciones.
- ❌ Crear funciones con más de una responsabilidad.

---

## Declaración de una Función

En Python, las funciones se definen utilizando la palabra clave `def`, seguida del nombre de la función, sus parámetros (si los hay) y el bloque de código.

```python
# Declaramos una función de suma
def addition(a, b):
    return a + b

# Declaramos una función de resta
def subtract(a, b):
    return a - b

# Uso de las funciones
a = 10
b = 5

# Sumamos dos números
total1 = addition(a, b)  # Resultado: 15

# Restamos dos números
total2 = subtract(a, b)  # Resultado: 5
```

---

## Parámetros en las Funciones

Los **parámetros** son variables que se definen en la función para recibir datos y manipularlos.

### Parámetros por Defecto

En Python, los parámetros pueden tener valores predeterminados. Si no se pasa un valor al llamar a la función, se usará el valor por defecto.

```python
from random import randint

# Declaramos una función con valores por defecto
def get_random_num(a=0, b=10):
    return randint(a, b)

# Llamadas a la función
print(get_random_num())      # Usa los valores por defecto: a=0, b=10
print(get_random_num(5))     # Usa a=5 y b=10
print(get_random_num(5, 25)) # Usa a=5 y b=25
```

---

## Funciones con Múltiples Retornos

Una función puede devolver más de un valor al mismo tiempo. Estos valores se empaquetan en una **tupla**, y puedes acceder a cada elemento por su posición.

```python
# Diccionario de usuario
user = {
    'fullname': 'Ronald Abu Saleh',
    'username': 'itsronalds',
    'birthday': '01-07-98'
}

# Función que retorna múltiples valores
def get_user_data(user):
    fullname = user['fullname']
    username = user['username']
    birthday = user['birthday']

    if not fullname or not username or not birthday:
        return 'Required fields'

    return fullname, username, birthday

# Llamada a la función
user_data = get_user_data(user)
print(user_data)  # Resultado: ('Ronald Abu Saleh', 'itsronalds', '01-07-98')
```

---

## Uso de la Palabra Clave `pass`

La palabra clave `pass` se utiliza cuando se necesita declarar una función sin implementar su lógica. Esto evita que el intérprete arroje errores.

```python
# Declaración de funciones sin implementar
def addition(a, b):
    pass

def subtract(a, b):
    pass
```

> **Nota:** Según el estilo de codificación recomendado por Python (PEP 8), deben incluirse tres líneas en blanco entre las funciones para mejorar la legibilidad.

---
