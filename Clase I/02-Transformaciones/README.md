# Conversiones de datos

Trata de convertir un tipo de dato a otro utilizando funciones de Python.

# Funciones de conversión

| Función |                           Explicación                           |             Ejemplo |
| :------ | :-------------------------------------------------------------: | ------------------: |
| str     |             Permite convertir un valor a un string              |   str(1500) => 1500 |
| int     |     Permite convertir un valor string o decimal a un entero     | int('1000') => 1000 |
| float   |     Permite convertir un valor string o entero a un decimal     |   float(15) => 15.0 |
| bool    | Permite convertir valores o estructuras de datos a True o False |     bool(1) => True |

# Funciones de conversión: bool

La conversión de datos con la función bool funciona diferente a los demás casos, si bien al intentar convertir una letra a un número entero nos da un error de Exception, esto no ocurre cuando intentamos convertir un valor o estructura de datos a un boolean.

Para poder ilustrar esto, se analizará la siguiente tabla:

## Valores False

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

## Valores True

| Coversión                                    | Resultado |
| :------------------------------------------- | :-------: |
| bool('Python')                               |   True    |
| bool(1)                                      |   True    |
| bool(1.0)                                    |   True    |
| bool(['Python', 'Go', 'JavaScript', 'Rust']) |   True    |
| bool({ 'a': 'b', b: 'a' })                   |   True    |
| bool(('a', 10, True, False))                 |   True    |
