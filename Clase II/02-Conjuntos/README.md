# Conjuntos

Estructura de datos mutables que guarda valores únicos y de una manera no ordenada.

```python
# Creamos un conjunto de números
numbers = { 1, 2, 3, 4, 1 }

# Resultado: { 1, 2, 3, 4 }
print(numbers)
```

> ✅ Los conjuntos eliminan valores duplicados

> ✅ Podemos eliminar valores duplicados de listas y tuplas a través de conjuntos

> ❌ No acepta valores de tipo lista o diccionario

# Métodos de conjuntos

Al ser una estructura mutable posee métodos para manipular sus datos, los más útiles son:

| Métodos   |                                      Explicación                                       |                                 Ejemplo |
| :-------- | :------------------------------------------------------------------------------------: | --------------------------------------: |
| add()     |                               Añade un valor al conjunto                               |                 values.add('New value') |
| update()  |                        Actualiza un conjunto añadiendo valores                         | values.update({ 'value 1', 'value 2' }) |
| discard() |                     Elimina el valor que le pasemos por parámetro                      |       values.discart('Value to remove') |
| remove()  |                     Elimina el valor que le pasemos por parámetro                      |        values.remove('Value to remove') |
| pop()     |                                Elimina un valor random                                 |                            values.pop() |
| union()   | Como update pero puede agregar varios conjuntos a la vez y debemos instanciar la union |          values.union(set1, set2, n...) |

> - La diferencia entre **discard** y **remove** es que **discard** no nos devuelve un error si no encuentra el valor que buscamos, mientras que **remove** nos da una excepción.

# Método add

Añade un nuevo valor al conjunto:

```python
# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Agregamos un nuevo valor
numbers.add(20)

# Resultado: {1, 2, 5, 10, 20}
print(numbers)
```

# Método update

Actualiza un conjunto agregando nuevos valores de otro conjunto:

```python
# Creamos conjunto A
numbers_a = {1, 10, 5, 2}

# Creamos conjunto B
numbers_b = {1, 11, 5, 3}

# Actualizamos conjunto a
numbers_a.update(numbers_b)

# Resultado: {1, 2, 3, 5, 10, 11}
print(numbers_a)
```

# Método discard

Elimina un valor que le pasemos por parámetro:

```python
# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Removemos el valor 10
numbers.discard(10)

# Resultado: {1, 2, 5}
print(numbers)
```

# Método remove

Elimina un valor que le pasemos por parámetro pero si el elemento no existe arroja una excepción:

```python
# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Removemos el valor 5
numbers.remove(5)

# Resultado: {1, 2, 10}
print(numbers)
```

# Método pop

Elimina un valor random:

```python
# Creamos un conjunto
numbers = {1, 10, 5, 2}

# Removemos un valor random
numbers.pop()

# Mostramos el resultado
print(numbers)
```

# Método union

Une uno o más conjuntos al conjunto principal y genera uno nuevo:

```python
# Creamos un conjunto a
numbers_a = {1, 10, 5, 2}

# Creamos un conjunto b
numbers_b = {6, 7, 11, 12}

# Creamos un nuevo conjunto a partir de la unión
numbers_c = numbers_a.union(numbers_b)

# Mostramos el resultado
print(numbers_c)
```
