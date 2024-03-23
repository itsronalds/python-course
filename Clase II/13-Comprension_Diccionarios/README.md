# Comprensión de diccionarios

Al igual que la comprensión de listas, la comprensión de diccionarios nos permite crear un nuevo diccionario con valores que necesitamos según la lógica proporcionada.

- Sintáxis

> {key:value for (key, value) in dict1.items() if condition == True}

La comprensión de diccionarios es una forma Pythonista de crear un nuevo diccionario estructurado a lo que necesitemos y así evitar el for loop.

Cabe destacar que la condicional es opcional según lo que requiramos.

# ¿Beneficios?

Al igual que la comprensión de listas, tiene los mismos beneficios:

- ✅ Tu código será más profesional (Pythonista)
- ✅ Será un código más corto y compresible
- ✅ Es muy flexible para extraer datos o alterarlos si así lo necesitas

# ¿Cómo lo utilizamos?

La sintaxis puede parecer un poco diferente pero en esencia es lo mismo que en las listas:

- Extraer un nuevo diccionario con valores en lower:

```$
# Creamos nuestro diccionario con nombres de algunos países
dict1 = { 'a': 'USA', 'b': 'VENEZUELA', 'c': 'CHILE' }

# Creamos un nuevo diccionario con los nombres en minúsculas
dict2 = { key:value.lower() for (key, value) in dict1.items() }

# { 'a': 'usa', 'b': 'venezuela', 'c': 'chile' }
print(dict2)
```

- Podemos incluso cambiar los nombres de nuestras keys:

```$
# Creamos nuestro diccionario con nombres de algunos países
dict1 = { 'a': 1, 'b': 2, 'c': 3 }

# Creamos un nuevo diccionario con los nombres en minúsculas
dict2 = { key*2:value for (key, value) in dict1.items() }

# { 'a': 'usa', 'b': 'venezuela', 'c': 'chile' }
print(dict2)
```

- Crear un nuevo diccionario solo con números pares:

```$
# Creamos nuestro diccionario algunos números
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Creamos un nuevo diccionario con los números pares
dict2 = {key: value for (key, value) in dict1.items() if value % 2 == 0}

# { 'b':2, 'd':4, 'f':6 }
print(dict2)
```
