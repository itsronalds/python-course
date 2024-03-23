# Funciones Lambda

Funciones anónimas (no poseen un nombre) de una sola línea.

¿Qué significa esto? 🤔

No puedes escribir más de una linea en una función lambda, por lo que el valor de retorno debe tener una lógica de una sola línea.

- Ejemplo:

```$
# Declaramos nuestra función lambda que suma dos parámetros
x = lambda x, y: x + y

# Imprimimos el resultado: 15
print(x(10, 5))
```

# ¿Por qué las funciones lambda son importantes?

Son funciones que pueden ser utilizadas en casos de usos específicos y poseen una estructura muy corta, por lo que es más entendible y Pythonista.

Las lambdas las podemos utilizar en:

- Funciones de orden superior
- Map function
- Filter function
- Reduce function

> Cada una de ellas explicadas más adelante

# Operador ternario (if-else) en lambdas

Los operadores ternarios son la forma corta de ejecutar una sentencia lógica en una sola línea, reduciendo drásticamente el código:

```$
is_pair = (lambda num: True if num % == 0 else False)

# True
print(is_pair(10))

# False
print(is_pair(5))
```
