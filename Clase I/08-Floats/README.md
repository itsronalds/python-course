# Floats

En Python cuando intentamos sumar valores flotantes podemos obtener resultados inesperados:

```$
x = 1.1 + 2.2

# Resultado: 3.3000000000000003
print(x)

y = 1.1 + 2.0

# Resultado: 3.1
print(y)
```

Si no tenemos cuidado podríamos tener errores al realizar comparaciones:

```
x = 3.3
y = 2.2 + 1.1

# Resultado: False
print(x == y)

# Resultado: 3.3000000000000003
print(y)
```

# Comparación correcta

Teniendo en cuenta los posibles errores que podemos presentar cuando intentamos comparar valores flotantes, existen algunas técnicas que podemos aplicar:

## Solución 1: Función formatd

Al utilizar la función format podemos formatear el flotante que posee una alta precisión y extraer las decimales que necesitamos:

```$
x = 3.3
y = 2.2 + 1.1

y_str = format(y, '.1f')

# Resultado: '3.3'
print(y_str)

# Resultado: True
print(str(x) == y_str)
```

## Solución 2: Función round

La función round nos permite obtener una cantidad de decimales según el número que queremos extraer:

```$
x = 3.3
y = 2.2 + 1.1

rounded_y = round(y, 1)

# Resultado: True
print(x == rounded_y)
```

## Solución 3: Función isclose de la librería math

La función isclose nos permite saber si dos números están relativamente cerca, suele usarse para comparar flotantes:

```$
from math import isclose

x = 3.3
y = 2.2 + 1.1

# Resultado: True
print(isclose(x, y))
```

## Solución 4: Margen de tolerancia

El margen de tolerancia es utilizado para determinar si dos valores con decimales son cercanos o no:

```$
x = 3.3
y = 2.2 + 1.1

tolerance = 0.00001

# Resultado: True
print(abs(x - y) < tolerance)
```

# Recursos

> - [Python floats](https://www.pythontutorial.net/advanced-python/python-float/)
