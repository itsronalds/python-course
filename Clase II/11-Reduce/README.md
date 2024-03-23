# Función reduce

Es una función de orden superior que acepta dos parámetros, el primer parámetro será una función que se ejecutará por cada elemento en el iterable, y el segundo parámetro será el iterable.

La función reduce nos otorga dos valores, el previo y el posterior para poder hacer nuestros calculos correspondientes dependiendo de lo que queramos lograr.

# Obtener el menor número

```$
# Importamos la función reduce
from functools import reduce

# Creamos una lista con valores aleatorios
numbers = [4, 2, 10, 1]

# Obtenemos el menor número de todos
smallest = reduce(lambda x, y: x if x < y else y, numbers)

# Hacemos print del valor
print(smallest)
```

# Obtener la suma de todos los números

```$
# Importamos la función reduce
from functools import reduce

# Creamos una lista con valores aleatorios
numbers = [4, 2, 10, 1]

# Sumatoria de todos los números
total = reduce(lambda x, y: x + y, numbers)

# Hacemos print del valor
print(total)
```
