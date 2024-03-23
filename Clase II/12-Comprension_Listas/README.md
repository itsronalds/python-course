# Comprensión de listas

Es una manera corta de poder crear una nueva lista a partir de otra lista pero con los valores que necesitamos según la lógica proporcionada.

- Sintáxis:

> newlist = [expression for item in iterable if condition == True]

La compresión de listas en una forma Pythonista de extraer datos de una lista a partir de una iteración en vez de usar el for loop.

Cabe destacar que la condicional es opcional según lo que requiramos.

# A todas estas, ¿Qué beneficios tiene?

Cuando necesitamos crear una nueva lista a partir de otra y extraer los datos que requerimos la compresión de listas puede ser muy util:

- ✅ Tu código será más profesional (Pythonista)
- ✅ Será un código más corto y compresible
- ✅ Es muy flexible para extraer datos o alterarlos si así lo necesitas

# ¿Cómo lo utilizamos?

Te enseño:

- ✅ Manera correcta:

```$
numbers = [1, 2, 3, 4, 5]

# Quiero extraer solo los números pares
pair_numbers = [x for x in numbers if x % 2 == 0]

# [2, 4]
print(pair_numbers)
```

- ❌ Manera no Pythonista:

```$
numbers = [1, 2, 3, 4, 5]
pair_numbers = []

for x in numbers:
    if x % 2 == 0:
        pair_numbers.append(x)

print(pair_numbers)
```

# Modificaciones de datos con comprensión de listas

Además de filtrar, podemos modificar datos y generar una lista con los datos ajustados a como lo necesitamos, por ejemplo:

```$
places = ['venezuelA', 'argentinA', 'chilE', 'uruguaY', 'paraguAy', 'boliVia']
places_capitalize = [place.capitalize() for place in places]

# ['Venezuela', 'Argentina', 'Chile', 'Uruguay', 'Paraguay', 'Bolivia']
print(places_capitalize)
```
