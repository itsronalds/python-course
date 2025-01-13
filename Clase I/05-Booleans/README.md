# Booleans

Los valores booleanos representan dos estados lógicos: `True` o `False`, los cuales corresponden a los valores binarios `1` y `0`.

```python
is_developer = True
print(is_developer)  # True

is_senior = False
print(is_senior)  # False
```

---

## Conversiones

Python permite convertir datos y estructuras de datos a valores booleanos (`True` o `False`), dependiendo de su contenido o estructura. A continuación, se detallan los casos más comunes:

### Valores que se Convierten en `False`

Los siguientes valores son evaluados como `False` al ser convertidos a booleanos:

| **Conversión** | **Resultado** |
| -------------- | ------------- |
| `bool('')`     | `False`       |
| `bool(0)`      | `False`       |
| `bool(0.0)`    | `False`       |
| `bool([])`     | `False`       |
| `bool({})`     | `False`       |
| `bool(())`     | `False`       |
| `bool(None)`   | `False`       |

### Valores que se Convierten en `True`

Cualquier valor no vacío o distinto de cero será evaluado como `True`:

| **Conversión**                                 | **Resultado** |
| ---------------------------------------------- | ------------- |
| `bool('Python')`                               | `True`        |
| `bool(1)`                                      | `True`        |
| `bool(1.0)`                                    | `True`        |
| `bool(['Python', 'Go', 'JavaScript', 'Rust'])` | `True`        |
| `bool({'a': 'b', 'b': 'a'})`                   | `True`        |
| `bool(('a', 10, True, False))`                 | `True`        |

---

## Operador `not`

El operador `not`, también conocido como operador de negación, se utiliza para invertir el valor booleano de una expresión.

```python
is_developer = True
is_professor = False

# Resultado: False
print(not is_developer)

# Resultado: True
print(not is_professor)
```

---

## Notas Importantes

- Los valores **vacíos** (cadenas, listas, diccionarios, tuplas, etc.) y el valor `None` siempre serán evaluados como `False`.
- Valores **no vacíos** o números diferentes de `0` serán evaluados como `True`.
- Este comportamiento facilita la evaluación de condiciones en estructuras de control como `if`, proporcionando flexibilidad al trabajar con diferentes tipos de datos.
