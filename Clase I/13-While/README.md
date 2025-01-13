# Ciclo while

Es un ciclo repetitivo que se ejecuta mientras una condición sea True:

```$
# Creamos un contador
counter = 0

while counter < 1000:
    counter += 1

# Da como resultado: 1000
print(counter)
```

# Operador break

Operador que detiene la ejecución del ciclo while, suele añadirse con una sentencia lógica:

```$
# Registrar solo los números del 1 al 5 y luego romper el ciclo
numbers = []
counter = 0

while counter < 10:
    counter += 1
    if counter > 5:
        break
    numbers.append(counter)

print(numbers)
```

# Operador continue

Operador que pasa la siguiente ejecución parecido a Next (siguiente). También suele añadirse con una sentencia lógica:

```$
# Registrar todos los números del 1 al 10 menos el 8
numbers = []
counter = 0

while counter < 10:
    counter += 1
    if counter == 8:
        continue
    numbers.append(counter)

print(numbers)
```

# Recorrer una lista

```$
# Creamos una lista de números
numbers = [1, 2, 3, 4, 5]
counter = 0

# Imprimir los números de la lista
while counter < len(numbers):
    print(numbers[counter])
    counter += 1
```
