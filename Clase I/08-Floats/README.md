# Números flotantes (Floats)

En Python, cuando intentamos sumar valores flotantes, podríamos obtener resultados inesperados debido a la manera en que estos números se representan internamente:

```python
x = 1.1 + 2.2

# Resultado: 3.3000000000000003
print(x)

y = 1.1 + 2.0

# Resultado: 3.1
print(y)
```

Estos resultados pueden generar errores al realizar comparaciones entre valores flotantes:

```python
x = 3.3
y = 2.2 + 1.1

# Resultado: False
print(x == y)

# Resultado: 3.3000000000000003
print(y)
```

## Comparación correcta

Para evitar errores al comparar valores flotantes, existen varias técnicas que podemos aplicar:

### Solución 1: Utilizar la función `format`

Al emplear la función `format`, podemos formatear el valor flotante con una precisión específica y trabajar con las decimales necesarias:

```python
x = 3.3
y = 2.2 + 1.1

y_str = format(y, '.1f')

# Resultado: '3.3'
print(y_str)

# Resultado: True
print(str(x) == y_str)
```

### Solución 2: Utilizar la función `round`

La función `round` nos permite redondear un valor flotante a un número específico de decimales:

```python
x = 3.3
y = 2.2 + 1.1

rounded_y = round(y, 1)

# Resultado: True
print(x == rounded_y)
```

### Solución 3: Usar un margen de tolerancia

El margen de tolerancia permite determinar si dos valores flotantes son suficientemente cercanos, considerando una diferencia mínima aceptable:

```python
x = 3.3
y = 2.2 + 1.1

tolerance = 0.00001

# Resultado: True
print(abs(x - y) < tolerance)
```

## Recursos adicionales

- [Python floats](https://www.pythontutorial.net/advanced-python/python-float/)
