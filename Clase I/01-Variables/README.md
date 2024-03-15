# Variables

Las variables son un espacio que se reserva en memoria del sistema operativo para almacenar algún tipo de valor y poder ser recuperado y leido durante la ejecución del código.

A las variables se les asigna un nombre y posteriormente un valor:

```$
name = 'John Myers'
age = 25
height = 1.75
ocupation = 'Software Engineer'
```

# Tipos de datos primitivos

| Tipo de dato |                            Explicación                            |        Ejemplo |
| :----------- | :---------------------------------------------------------------: | -------------: |
| string       |                 Permite ingresar cadenas de texto                 | 'Hello Python' |
| integer      |            Permite utilizar valores númericos enteros             |             25 |
| float        |           Permite utilizar valores númericos decimales            |           1.75 |
| boolean      | Permite utilizar valores True o False haciendo referencia a 1 y 0 |           1.75 |

# Comentarios

Un comentario es una pieza de texto o código que el interprete ignora. Por lo tanto, no se ejecuta durante el proceso de compilación de nuestro código.

```$
# Comentario de una sola linea

'''
Mientras que utilizando esta expresión podemos
hacer comentarios que contengan
múltiples líneas
'''
```

# Indentación

La indentación trata de la capacidad del lenguaje para poder reconocer los diferentes bloques de código, como por ejemplo el código dentro de sentencias lógicas, bucles y funciones.

Cabe destacar que Python es un lenguaje extremadamente estricto con su indentación en su sintaxis por lo que una mala indentación puede causarnos errores.

> Además de poder reconocer los diferentes bloques de código, la indentación es importante no solo para Python, sino para todos los lenguajes de programación ya que nos ayuda a mantener una estructura más limpia y legible del código.

# Función print

Es una función build-in que nos permite pasarle como argumento una variable o dato y mostrar una salida en consola.

```$
name = 'John Myers'

# Nos devuelve en consola el valor de: John Myers
print(name)
```

# Función type

Función build-in que nos permite saber o mostrar en consola junto a print el tipo de variable, este puede ser string, int, float y boolean como algunos ejemplos.

```$
number = 10

# Esto nos devuelve una clase ya que todo es Python es un objeto, esta clase nos trae un atributo donde podemos saber el tipo de variable
print(type(number))
```

> Es importante recalcar que todo en Python es un objeto

# Función input

Función build-in que nos permite leer la entrada de un usuario, y a la vez podemos asignar dicho dato ingresado a una variable.

```$
# Solicitar al usuario su nombre
name = input('Ingresa tu nombre: ')

# Mostrar en consola el nombre
print(name)
```

> Todo lo ingresado mediante la función input será devuelto como valor string
