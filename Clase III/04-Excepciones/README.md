# Excepciones y manejo de errores

El manejo de errores en sumamente importante para que nuestro programa o aplicación no se detenga, pues de no manejar correctamente cada error nuestro programa puede necesitar un reinicio y esto es indeseable para usuarios que interactuan con el mismo.

Python es un lenguaje que nos ayuda a manejar errores fácilmente mediante excepciones.

# Primero, exploremos los assert

Trata de una palabra clave encargada de revisar el resultado de pequeños fragmentos de código, nos ayuda a realizar un test simplificado de manera puntual.

```$
# assert
x = 10

# Nos arroja un assertionError ya que x == 10
assert x == 9, "x no es 9"


def suma(x, y): return x + y

# Nos nos arroja un error ya que 2 + 3 es 5
assert suma(2, 3) == 5, "La suma no es 5"
```

# Excepciones

Son clases de Python que nos ayudan a darnos información valiosa de errores mediante propiedades que estas poseen. A continuación se puede observar una tabla.

| Nombre            |                        Explicación                        |
| :---------------- | :-------------------------------------------------------: |
| Exception         |              Error general y personalizable               |
| SyntaxError       |                   Error en la sintáxis                    |
| TypeError         |       Operaciones con tipos de datos incompatibles        |
| NameError         |               Cuando una variable no existe               |
| IndexError        |          Cuando un índice de una lista no existe          |
| KeyError          |       Cuando una llave de un diccionario no existe        |
| ValueError        |    Cuando le pasamos a una función el valor incorrecto    |
| AttributeError    | Cuando un atributo o método no es encontrado en un objeto |
| IOError           |    Errores durante la lectura y escritura de archivos     |
| ZeroDivisionError |             Intentar dividir un valor entre 0             |
| ImportError       |             Importar un módulo que no existe              |

# Manejo de errores (try-except)

El try-except nos ayuda a poder manejar errores en Python sin que nuestro programa principal se termine, esto es sumamente importante para proyectos en producción, una plataforma no debería de caer cada cuanto suceda cualquier error.

Utilizando try-except podemos gestionar errores específicos a través de las clases de excepciones o errores generales con la clase Except.

```$
def suma(x, y):
    try:
        return x + y
    except TypeError as te:
        return str(te)
    except Exception as e:
        return e


print(type(suma(2, 'l')))
print(suma(2, 'l'))
```

# Finally

Palabra reservada que ejecuta código al terminal el try o si se produce una excepción.

```$
try:
    print('Try this code')
except:
    print('An error')
finally:
    print('execute anyway')
```

# Raise

Palabra reservada que nos ayuda a lanzar algún error personalizado dentro de un try-except.

```$
try:
    name = 'Ronald'

    if name != 'John':
        raise Exception('This is not John')

except Exception as e:
    print(type(e))
    print(e)
    print(str(e))
    print(type(str(e)))
```
