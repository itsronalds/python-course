# Módulos en Python

Todos los archivos en Python son módulos, y se utilizan para modularizar el código en diferentes archivos para mantener la estructura de un proyecto más organizada y legible, además de mantenible durante el tiempo.

# ¿Por qué los módulos son tan importantes en Python?

Esto se debe a que en Python se utiliza una palabra clave **name**, está se encarga de comunicarnos cuál es el programa principal y cuales son los secundarios durante la importanción de módulos.

¿Pero, esto que significa? 🤔

> Dado que todo archivo es un módulo, podemos importar módulos externos correspondientes a una librería u otro programa escrito en Python y utilizar las funciones, clases o variables existentes en dichos módulos o programa sin ejecutar el código hasta que lo requiramos.

# Pero primero, ¿Qué es **name**?

Trata de una palabra clave reservada por el lenguaje que nos indica si el módulo que estamos ejecutando es el módulo principal de ejecución o no, de esta forma podemos llevar mayor control del código ejecutaremos.

# ¿Cómo utilizamos **name**?

Se utiliza principalmente con una sentencia if en nuestro módulo principal:

```$
# main.py

# Definimos nuestra función principal que ejecutará toda la aplicación
def app():
    pass


# app() solo será ejecutado si ejecutamos main.py como módulo principal
if __name__ == '__main__':
    app()
```

# Evitar que se ejecute no deseado

Imaginemos que tenemos dos archivos, **main.py** y **users.py**:

- main.py

```$
import users

if __name__ == '__main__':
    print('Si ejecutamos main.py como script principal se ejecutará este print')

    # get users from db
    user_list = users.get_users()

    # create user
    user_created = users.create_user('Ronald', 'Abu Saleh')
```

- users.py

```$
def get_users():
    '''Obtiene usuarios desde la base de datos'''
    pass


def create_user(name, lastname):
    '''Inserta un usuario en base de datos'''
    pass


if __name__ == '__main__':
    print('Si ejecutamos users.py como script principal se ejecutará este print')
```
