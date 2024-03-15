# Indexación de Strings

Trata de obtener un valor de una determinada posición del string:

```$
text = 'Welcome to USA'

# Obtenemos la 'U' de USA
print(text[11])
```

> Las posiciones de los strings siempre comienzan desde 0 a ...n, por esa razón la posición que queremos extraer es 11.

# Extracción

Para poder manipular una cadena y extraer los valores deseados, podemos jugar un poco con la indexación:

- Para obtener el último carácter:

```$
text = 'Welcome to Japón'

# Primera manera
print(text[len(text - 1)])

# Segunda manera (más sencilla)
print(text[-1])
```

> len nos devuelve la longitud de carácteres, pero como los strings comienzan desde la posición 0, debemos restarle 1 a la longitud.

# Slicing

Podemos cortar una cadena dentro de otra cadena para obtener solo el valor deseado:

```$
text = 'Today I wake up at 9:00 am.'

# Obtener solo el horario
schedule = text[19:26]

# Resultado: 9:00 am.
print(schedule)
```

# Slicing: Primeras palabras

```$
text = 'Today I played soccer'

first_words = text[:14]

# Resultado: Today I played
print(first_words)
```

# Extración: dos en dos (depende del valor que pasemos por parámetro)

```$
text = 'Welcome to the island'

# Resultado: Wloet h sad
print(text[::2])
```

> El primer carácter siempre será extraido
