# Operadores de Comparación

Los **operadores de comparación** en Python son herramientas esenciales para evaluar relaciones entre dos valores, ya sean números o cadenas de texto. Estos operadores siempre devuelven un valor booleano: `True` o `False`.

## Tabla de Operadores de Comparación

| **Operador** | **Descripción**                                          | **Ejemplo** | **Resultado** |
| ------------ | -------------------------------------------------------- | ----------- | ------------- |
| `==`         | Verifica si dos valores son iguales.                     | `5 == 5`    | `True`        |
| `!=`         | Verifica si dos valores son diferentes.                  | `5 != 3`    | `True`        |
| `>`          | Verifica si el primer valor es mayor que el segundo.     | `6 > 5`     | `True`        |
| `<`          | Verifica si el primer valor es menor que el segundo.     | `5 < 6`     | `True`        |
| `>=`         | Verifica si el primer valor es mayor o igual al segundo. | `10 >= 11`  | `False`       |
| `<=`         | Verifica si el primer valor es menor o igual al segundo. | `9 <= 9`    | `True`        |

## Ejemplos de Uso

### Comparación de Números

```python
x = 10
y = 20

# Igualdad
print(x == y)  # False

# Mayor que
print(y > x)  # True

# Menor o igual que
print(x <= 10)  # True
```

### Comparación de Strings

Python también permite comparar cadenas de texto basándose en el orden lexicográfico (similar al orden alfabético):

```python
name_a = "Alice"
name_b = "Bob"

# Comparar igualdad
print(name_a == name_b)  # False

# Comparar menor que (orden alfabético)
print(name_a < name_b)  # True
```

## Notas Importantes

- **Sensibilidad a mayúsculas y minúsculas:** Las comparaciones entre cadenas de texto distinguen entre mayúsculas y minúsculas. Por ejemplo, `"Python" != "python"`.
- **Operadores en estructuras lógicas:** Estos operadores son fundamentales para las estructuras de control como `if`, `while`, y otras.
- **Tipos compatibles:** Aunque puedes comparar diferentes tipos de datos, hacerlo puede llevar a resultados inesperados. Por ejemplo, `"5" == 5` devuelve `False` porque uno es string y el otro es entero.

## Uso Combinado con Operadores Lógicos

Los operadores de comparación pueden combinarse con operadores lógicos (`and`, `or`, `not`) para evaluar condiciones complejas:

```python
age = 25

# Verificar si la edad está entre 18 y 30
is_young_adult = age >= 18 and age <= 30
print(is_young_adult)  # True
```

> **Nota:** Estos operadores se utilizan frecuentemente en sentencias lógicas como `if`, las cuales se exploran más a fondo en secciones posteriores.
