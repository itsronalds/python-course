# Si sumamos dos números flotantes, el resultado puede ser exacto si uno de los valores tienen solo decimales en 0.
from math import isclose
x = 1.1 + 2.0
print(x)

# Si sumamos dos números flotantes, el resultado puede ser inexacto si uno de los valores no contienen solo decimales en 0.
x = 2.2 + 1.1
print(x)

# Comparación de números flotantes inexáctos.
x = 3.3
y = 2.2 + 1.1
print(x == y)

# Solución 1: Convertir el número flotante a una cadena y comparar.
x = 3.3
y = 2.2 + 1.1

y_str = format(y, '.1f')

print(y_str == str(x))

# Solución 2: Redondear el número flotante y comparar.
x = 3.3
y = 2.2 + 1.1

# Obtenemos el número flotante redondeado a un decimal.
y_round = round(y, 1)

print(y_round == x)

# Solución 3: Utilizar la función isclose del módulo math.

x = 3.3
y = 2.2 + 1.1

print(isclose(x, y))

# Solución 4: Utilizar la función isclose del módulo math con un margen de tolerancia.

x = 3.3
y = 2.2 + 1.1

tolerance = 0.00001

# Sin función isclose.
print(abs(x - y) < tolerance)

# Con función isclose y margen de tolerancia.
print(isclose(x, y, abs_tol=tolerance))
