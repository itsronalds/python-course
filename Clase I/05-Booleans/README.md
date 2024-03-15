# Booleans

Son valores True o False que corresponde a los binarios 1 y 0.

```$
is_developer = True
print(is_developer)

is_senior = False
print(is_senior)
```

# Transformaciones

Datos y estructura de datos pueden transformarse a booleanos True o False dependiendo de su estructura. A continuación se puede apreciar la manera en como valores puede traducirse a valores booleanos:

- Datos y estructuras de datos que pasan a False

| Coversión  | Resultado |
| :--------- | :-------: |
| bool('')   |   False   |
| bool(0)    |   False   |
| bool(0.0)  |   False   |
| bool([])   |   False   |
| bool({})   |   False   |
| bool(())   |   False   |
| bool(None) |   False   |
| bool([])   |   False   |

- Datos y estructuras de datos que pasan a True

| Coversión                                    | Resultado |
| :------------------------------------------- | :-------: |
| bool('Python')                               |   True    |
| bool(1)                                      |   True    |
| bool(1.0)                                    |   True    |
| bool(['Python', 'Go', 'JavaScript', 'Rust']) |   True    |
| bool({ 'a': 'b', b: 'a' })                   |   True    |
| bool(('a', 10, True, False))                 |   True    |

# Operador not

También conocido como operador de negación, es utilizado para revertir valores booleanos:

```$
is_developer = True
is_professor = False

# Resultado: False
print(not is_developer)

# Resultado: True
print(not is_professor)
```
