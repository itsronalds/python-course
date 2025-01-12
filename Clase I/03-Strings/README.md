# Strings

En Python, existen diferentes maneras de concatenar cadenas de texto, desde el uso del operador `+` hasta funciones como `format` y los f-strings.

---

## Concatenación de Strings

Podemos concatenar strings utilizando el símbolo `+`. Este método es común, pero no es muy eficiente cuando se necesitan concatenar muchos valores en un string.

> **Nota:** No es posible concatenar un string con valores de tipo `int` o `float` directamente utilizando `+`. Para ello, puedes convertirlos a `str` o usar la función `format`.

---

## Concatenación: Función `format`

La función `format` nos da mayor flexibilidad para incluir variables en cadenas de texto. Hay dos formas principales de usar esta función:

### Primera Forma: Uso Básico de `format`

Podemos utilizar `{}` como placeholders y pasar las variables en el orden correspondiente.

```python
name = 'Guido'
lastname = 'Van Rossum'
age = 67
language = 'Python'

presentation = 'Hola, mi nombre es {} {}, tengo {} años y soy creador del lenguaje de {}'.format(name, lastname, age, language)
print(presentation)
```

---

### Segunda Forma: F-Strings (Recomendado ✅)

Introducidos en Python 3.6, los f-strings simplifican el proceso de incluir variables en cadenas. Solo necesitas anteponer la letra `f` al string y usar placeholders `{}`.

```python
name = 'Guido'
lastname = 'Van Rossum'
age = 67
language = 'Python'

presentation = f'Hola, mi nombre es {name} {lastname}, tengo {age} años y soy creador del lenguaje de {language}'
print(presentation)
```

Este método es más conciso y legible.

---

## Tipos de Formatting

Podemos formatear valores en cadenas para ajustarlos según nuestras necesidades. Por ejemplo, podemos convertir un entero a un decimal con dos decimales utilizando el siguiente formato: `:.2f`.

### Ejemplo: Formateo de Números

```python
price = 14

# Forma 1: Usando format
print('La camisa cuesta {:.2f}'.format(price))

# Forma 2: Usando f-strings
print(f'La camisa cuesta {price:.2f}')
```

El resultado será el mismo en ambos casos:

```
La camisa cuesta 14.00
```

---

## Notas Importantes

- Los **f-strings** son más eficientes y legibles, por lo que se recomienda su uso.
- El string formatting es una herramienta poderosa para manejar y personalizar la salida de datos en Python.

Para más detalles, consulta la documentación de [w3schools](https://www.w3schools.com/python/ref_string_format.asp).
