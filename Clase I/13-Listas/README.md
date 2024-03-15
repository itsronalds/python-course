# Listas

Son estructuras de datos que almacenan valores de todo tipo, son desordenadas, esto significa que son mutables y no tienen un orden en específico ya que cambiar durante la ejecución del código.

```$
# Declaramos una lista con algunos valores
numbers = [1, 2, 3, 4, 5]

# Imprimos el tipo de dato
print(type(numbers))

# Imprimimos los valores que hay dentro
print(numbers)
```

> Las listas son muy importantes en las aplicaciones del mundo real porque pueden contener una gran cantidad de datos almacenados.

# Indexación

Al igual que en los strings, podemos obtener valores específicos de nuestra lista a través de un índice.

```$
# Declaramos una lista
numbers = [1, 2, 3, 4, 5]

# Obtenemos un valor
index = 4
value = numbers[4]

# Resultado: 5
print(value)
```

> Los indices en las listas empiezan desde la posición 0

# Indexación: última posición

Podemos utilizar la función len para obtener la última posición:

```$
# Declaramos una lista
numbers = [1, 2, 3, 4, 5]

# Obtenemos la última posición
index = len(numbers) - 1
value = numbers[index]

# Resultado: 5
print(numbers)
```

# Actualizando valores

Una vez más, las listas son estructuras de datos mutables, por lo que podemos actualizar algún dato dentro de ellas:

```$
# Declaramos una lista de lenguajes de programación
programming_languages = ['Python', 'JavaScript', 'Java', 'Golang']

# Pedimos al usuario cuál es su tercer lenguaje favorito
favorite_language = input('¿Cuál es tu tercer lenguaje favorito? ')

# Actualizamos el tercer lenguaje de la lista
programming_languages[2] = favorite_language

# Imprimimos la lista actualizada
print(programming_languages)
```

# Slicing

Al igual que en los strings, podemos cortar listas para obtener una más específica:

```$
# Declaramos una lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtenemos una nueva lista desde el número 5 al 10
print(numbers[4:])
```

# Operador in

Podemos utilizar el operador in en listas para determinar si posee un determinado valor:

```$
# Declaramos una lista
courses_for = ['Python', 'JavaScript', 'Rust']

# Queremos saber si hay cursos para Python
has_python = 'Python' in courses_for

# Resultado: True
print(has_python)

# Queremos saber si hay cursos para Golang
has_golang = 'Golang' in courses_for

# Resultado: False
print(has_golang)
```
