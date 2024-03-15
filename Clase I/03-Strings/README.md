# Strings

Se explora las diferentes formas de concatenar strings mediante el uso de + o la función format y sus múltiples tipos.

# Concatenación de strings

Podemos concatenar strings utilizando el simbolo de +, esta es la manera más común pero no es muy óptimo cuando queremos concatenar varios datos en un string.

> No podemos utilizar este método como forma de concatenar un string con un valor de tipo number ya sea int o float, para eso usamos la función format.

# Concatenación: Función format

En Python podemos dar uso de la función format para tener más flexibilidad a la hora de concatenar valores que provienen de variables en una cadena string.

- Primera forma de hacer uso de format:

```$
name = 'Guido'
lastname = 'Van Rossum'
age = 67
language = 'Python'

presentation = 'Hola, mi nombre es {} {}, tengo {} años y soy creador del lenguaje de {}'.format(name, lastname, age, language)
```

Debemos de colocar las variables dentro de la función format acorde al orden que queremos que se muestren en nuestro string, donde cada apartado se utilizan placeholders.

Podemos utilizar valores de tipo number ya sean int o float en nuestros strings y no ocurrirán problemas.

- Segunda y mejor forma de hacer uso de format ✅:

```$
name = 'Guido'
lastname = 'Van Rossum'
age = 67
language = 'Python'

presentation = f'Hola, mi nombre es {name} {lastname}, tengo {age} años y soy creador del lenguaje de {language}'
```

Utilizando la letra clave f antes del string, podemos pasar directamente las variables a los placeholders reduciendo el código y la complejidad.

# Tipos de Formatting

Podemos utilizar los formatting types para manipular nuestros valores a como nosotros los necesitamos utilizando algunos parámetros claves.

En el ejemplo a continuación pasaremos un valor de tipo int a float utilizando la función format:

```$
price = 14

# Forma 1
print('La camisa cuesta {:.2f}').format(price)

# Forma 2
print(f'La camisa cuesta {price:.2f}')
```

- Podemos aprender más acerca del formatting string en [w3schools](https://www.w3schools.com/python/ref_string_format.asp)
