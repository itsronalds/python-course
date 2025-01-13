# Ciclo while

El ciclo `while` en Python es una estructura de control repetitiva que se ejecuta mientras una condición evaluada sea `True`.

## Ejemplo básico

```python
# Creamos un contador
counter = 0

while counter < 1000:
    counter += 1

# Da como resultado: 1000
print(counter)
```

## Operador break

El operador `break` se utiliza para detener la ejecución de un ciclo antes de que la condición del `while` sea falsa. Este operador suele combinarse con sentencias lógicas para controlar el flujo del programa.

### Ejemplo:

```python
# Registrar solo los números del 1 al 5 y luego romper el ciclo
numbers = []
counter = 0

while counter < 10:
    counter += 1
    if counter > 5:
        break
    numbers.append(counter)

print(numbers)  # Resultado: [1, 2, 3, 4, 5]
```

## Operador continue

El operador `continue` se utiliza para saltar la iteración actual y pasar directamente a la siguiente iteración del ciclo. Esto permite omitir ciertas ejecuciones dentro del ciclo.

### Ejemplo:

```python
# Registrar todos los números del 1 al 10 menos el 8
numbers = []
counter = 0

while counter < 10:
    counter += 1
    if counter == 8:
        continue
    numbers.append(counter)

print(numbers)  # Resultado: [1, 2, 3, 4, 5, 6, 7, 9, 10]
```

## Recorrer una lista con un ciclo while

Un ciclo `while` también puede utilizarse para iterar a través de los elementos de una lista utilizando un contador manual.

### Ejemplo:

```python
# Creamos una lista de números
numbers = [1, 2, 3, 4, 5]
counter = 0

# Imprimir los números de la lista
while counter < len(numbers):
    print(numbers[counter])
    counter += 1
```

Este enfoque es menos común en Python, ya que se suele preferir el uso de ciclos `for` para iterar sobre listas. Sin embargo, el `while` puede ser útil en casos donde el control del índice sea necesario.

---

## Notas importantes

- **Condición infinita:** Si la condición del `while` nunca llega a ser `False`, el ciclo se ejecutará indefinidamente. Es importante asegurarse de que la lógica del ciclo permita salir de él en algún momento.
- **Uso responsable:** Los operadores `break` y `continue` son herramientas poderosas, pero deben utilizarse de forma que no compliquen innecesariamente el flujo del programa.

Con estos conceptos básicos, puedes comenzar a utilizar el ciclo `while` en tus programas para manejar tareas repetitivas de manera eficiente.
