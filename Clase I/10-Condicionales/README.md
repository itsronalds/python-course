# Condicionales en Python

Los condicionales lógicos son una herramienta fundamental en todos los lenguajes de programación. En Python, se utilizan para tomar decisiones durante la ejecución del programa, evaluando si una condición es `True`.

## Tipos de condicionales en Python

Python cuenta con tres estructuras condicionales principales:

| **Condicional** |                                      **Explicación**                                      |                **Ejemplo** |
| :-------------- | :---------------------------------------------------------------------------------------: | -------------------------: |
| `if`            |          Evalúa si una expresión lógica es `True`. Si lo es, ejecuta el bloque.           |   `if 10 > 5: print(True)` |
| `elif`          |     Se utiliza después de un `if` para evaluar otra condición si el `if` es `False`.      | `elif 10 > 7: print(True)` |
| `else`          | Si todas las demás condiciones (`if` y `elif`) son `False`, ejecuta el bloque del `else`. |       `else: print(False)` |

> **Nota:** El uso de `elif` es necesario cuando se desea evaluar más de una condición adicional al `if`. Esto evita errores y asegura que solo un bloque se ejecute en la estructura condicional.

## Ejemplo práctico

```python
age = 18

if age < 18:
    print("Eres menor de edad.")
elif age == 18:
    print("¡Tienes exactamente 18 años!")
else:
    print("Eres mayor de edad.")
```

En este ejemplo:

1. Si `age` es menor que 18, se imprimirá "Eres menor de edad."
2. Si `age` es igual a 18, se imprimirá "¡Tienes exactamente 18 años!"
3. En cualquier otro caso (`age` mayor que 18), se imprimirá "Eres mayor de edad."

## ¿Por qué usar condicionales?

Los condicionales permiten controlar el flujo del programa dependiendo de las condiciones. Son útiles para manejar lógica compleja, validar datos, y tomar decisiones dinámicamente.

---

Si deseas aprender más sobre condicionales en Python, consulta la [documentación oficial de Python](https://docs.python.org/3/tutorial/controlflow.html).
