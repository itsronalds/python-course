# Funciones

Son bloques de código donde abstraemos cierta lógica encargada de resolver algún problema y las modularizamos a través de funciones.

En toda la programación en general las funciones son necesarias, nos aportan muchos beneficios como:

- ✅ Modularizar código
- ✅ Descomponer un gran problema en diferentes funciones para ser más legible
- ✅ Cada función tiene una responsabilidad única

Algunas malas prácticas 🤔:

- ❌ Nombres ambiguos para nuestras funciones
- ❌ Una función que tiene más de una responsabilidad

# ¿Cómo declaramos una función?

La palabra clave es def, seguido del nombre y parámetros:

```$
# Declaramos una función de suma
def addition(a, b):
    return a + b

# Declaramos una función de resta
def subtract(a, b):
    return a - b

a = 10
b = 5

# Sumamos dos números: 15
total1 = addition(a, b)

# Restamos dos números: 5
total2 = subtract(a, b)
```

# ¿Qué son los parámetros específicamente?

Son referencias de las variables que le pasamos a la función, de esta forma podemos manipular dichos valores y utilizarlos.

# Parámetros por defecto

Al crear una función los parámetros pueden tener valores por defecto en caso de que no le pasemos valores a dicha función al llamarla:

- La función **randint** nos otorga un valor entero según el rango que le pasemos por parámetro:

```$
from random import randint

# Declaramos una función con valores por defecto
def get_random_num(a=0, b=10):
    return randint(a, b)


# Al llamar a la función sin pasarle parámetros esta se ejecuta con los que tiene por default
print(get_random_num())

# Luego, podemos incluso solo pasarle un valor diferente
print(get_random_num(5))

# O, pasarle los dos valores en si
print(get_random_num(5, 25))
```

# Funciones de múltiples return

Son funciones que retornan más de un valor o estructura de datos, la salida de una función con múltiples return vienen a través de una tupla.

A los resultados de la función puedes ingresar colocando la posición a la que te gustaría acceder.

- Por ejemplo:

```$
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
```

# ¿Qué quiere decir "pass"?

Es una palabra clave en el lenguaje que le indica al interprete que una sentencia no tiene código aún establecido por lo que evita mostrarnos un error.

```$
# Declaración de funciones sin código implementado
def addition(a, b):
    pass


def subtract(a, b):
    pass
```

> Es importante tener en cuenta que deben haber tres saltos de linea entre las funciones, esto es opcional pero está recomendado en el coding style de Python.
