# Listas y Métodos de Listas en Python

Las listas son estructuras de datos fundamentales en Python que permiten almacenar múltiples valores de cualquier tipo. Son **mutables** y desordenadas, lo que significa que sus elementos pueden cambiar de posición o valor durante la ejecución del programa.

> Las listas son especialmente útiles en aplicaciones del mundo real, ya que permiten manejar grandes cantidades de datos de forma eficiente.

## Creación de una Lista

Podemos crear listas utilizando corchetes (`[]`) y separando los elementos con comas:

```python
# Declaramos una lista con algunos valores
numbers = [1, 2, 3, 4, 5]

# Imprimimos el tipo de dato
print(type(numbers))  # Resultado: <class 'list'>

# Imprimimos los valores dentro de la lista
print(numbers)  # Resultado: [1, 2, 3, 4, 5]
```

---

## Indexación

La indexación permite acceder a elementos específicos de una lista utilizando su posición. En Python, los índices comienzan desde `0`.

```python
# Declaramos una lista
numbers = [1, 2, 3, 4, 5]

# Obtenemos un valor en el índice 4
value = numbers[4]

# Resultado: 5
print(value)
```

### Última posición

Podemos obtener el último elemento utilizando la función `len`:

```python
# Declaramos una lista
numbers = [1, 2, 3, 4, 5]

# Obtenemos la última posición
index = len(numbers) - 1
value = numbers[index]

# Resultado: 5
print(value)
```

---

## Slicing

El slicing permite obtener sublistas definiendo un rango de índices.

```python
# Declaramos una lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtenemos una sublista desde el número 5 al 10
sublist = numbers[4:]

# Resultado: [5, 6, 7, 8, 9, 10]
print(sublist)
```

---

## Actualización de Valores

Dado que las listas son mutables, podemos actualizar cualquier elemento accediendo a su índice:

```python
# Declaramos una lista de lenguajes de programación
programming_languages = ['Python', 'JavaScript', 'Java', 'Golang']

# Actualizamos el tercer lenguaje
programming_languages[2] = 'C++'

# Resultado: ['Python', 'JavaScript', 'C++', 'Golang']
print(programming_languages)
```

---

## Operador `in`

El operador `in` se utiliza para verificar si un valor específico está presente en una lista:

```python
# Declaramos una lista
courses = ['Python', 'JavaScript', 'Rust']

# Verificamos si hay un curso de Python
print('Python' in courses)  # Resultado: True

# Verificamos si hay un curso de Golang
print('Golang' in courses)  # Resultado: False
```

---

# Métodos de Listas

Python proporciona métodos muy útiles para manipular listas. A continuación, explicamos los más importantes:

| Método       | Descripción                                                                        | Ejemplo                                   |
| ------------ | ---------------------------------------------------------------------------------- | ----------------------------------------- |
| `append()`   | Añade un elemento al final de la lista.                                            | `list.append('value')`                    |
| `insert()`   | Inserta un elemento en una posición específica.                                    | `list.insert(5, 'value')`                 |
| `remove()`   | Elimina la primera coincidencia de un valor en la lista.                           | `list.remove('value')`                    |
| `pop()`      | Elimina y retorna el último elemento de la lista.                                  | `list.pop()`                              |
| `pop(index)` | Elimina y retorna el elemento en el índice especificado.                           | `list.pop(2)`                             |
| `reverse()`  | Invierte el orden de los elementos en la lista.                                    | `list.reverse()`                          |
| `sort()`     | Ordena los elementos de la lista en orden ascendente (o descendente si se indica). | `list.sort()` / `list.sort(reverse=True)` |

---

## Ejemplos de Uso de Métodos

### Añadir Elementos

- **Al final de la lista**:

```python
numbers = [1, 2, 3, 4]
numbers.append(5)

# Resultado: [1, 2, 3, 4, 5]
print(numbers)
```

- **En una posición específica**:

```python
numbers = [1, 2, 3, 4]
numbers.insert(2, 10)

# Resultado: [1, 2, 10, 3, 4]
print(numbers)
```

### Remover Elementos

- **Por valor**:

```python
numbers = [1, 2, 3, 4]
numbers.remove(2)

# Resultado: [1, 3, 4]
print(numbers)
```

- **Último elemento**:

```python
numbers = [1, 2, 3, 4]
numbers.pop()

# Resultado: [1, 2, 3]
print(numbers)
```

- **Por índice**:

```python
numbers = [1, 2, 3, 4]
numbers.pop(1)

# Resultado: [1, 3, 4]
print(numbers)
```

- **Usando `del`**:

```python
numbers = [1, 2, 3, 4]
del numbers[0]

# Resultado: [2, 3, 4]
print(numbers)
```

### Revertir una Lista

```python
numbers = [1, 2, 3, 4]
numbers.reverse()

# Resultado: [4, 3, 2, 1]
print(numbers)
```

### Ordenar una Lista

- **De menor a mayor (números)**:

```python
numbers = [4, 2, 1, 3]
numbers.sort()

# Resultado: [1, 2, 3, 4]
print(numbers)
```

- **En orden alfabético (cadenas)**:

```python
developers = ['Ronald A.', 'Andrés M.']
developers.sort()

# Resultado: ['Andrés M.', 'Ronald A.']
print(developers)
```

- **De mayor a menor usando `reverse` en `sort`**:

```python
numbers = [4, 1, 2, 3]
numbers.sort(reverse=True)

# Resultado: [4, 3, 2, 1]
print(numbers)
```
