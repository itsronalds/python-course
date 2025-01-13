# Operadores Lógicos en Python

Los operadores lógicos en Python nos permiten realizar evaluaciones condicionales y tomar decisiones basadas en múltiples criterios. Los principales operadores son `and`, `or` y `not`.

---

## Operador `and`

El operador `and` evalúa si **todas** las condiciones son `True`. Si alguna es `False`, el resultado será `False`.

### Ejemplo con valores booleanos:

```python
# True
print(True and True)

# False
print(True and False)

# False
print(False and True)

# False
print(False and False)
```

### Ejemplo con comparaciones numéricas:

```python
# True (ambas condiciones son verdaderas)
print(5 < 10 and 1 < 5)

# False (la segunda condición es falsa)
print(5 < 10 and 1 > 5)
```

---

## Operador `or`

El operador `or` evalúa si **al menos una** de las condiciones es `True`. Si todas las condiciones son `False`, el resultado será `False`.

### Ejemplo con valores booleanos:

```python
# True
print(True or True)

# True
print(True or False)

# False
print(False or False)
```

---

## Operador `not`

El operador `not` invierte el valor booleano de una expresión. Es decir, si la expresión es `True`, devolverá `False`, y viceversa.

Consulta más detalles sobre el operador `not` en la sección [05-Booleans](https://github.com/itsronalds/python-course/tree/main/05-Booleans).

---

### Recursos Adicionales

- [Documentación oficial de Python sobre operadores lógicos](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Explicación de operadores en Python](https://realpython.com/python-operators/#logical-operators)
