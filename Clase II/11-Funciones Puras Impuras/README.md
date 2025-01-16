# Funciones Puras e Impuras en Python

En Python, las funciones se clasifican en **puras** e **impuras** dependiendo de cómo interactúan con los datos y el entorno. Comprender estas diferencias es fundamental para escribir código más predecible y mantenible.

---

## ¿Qué son las Funciones Puras?

Las funciones puras son aquellas que:

1. Retornan un valor predecible según los parámetros que reciben.
2. No alteran el estado externo (no mutan variables globales u objetos).
3. Siempre producen el mismo resultado para los mismos argumentos.

### Ejemplo: Funciones Puras

#### Solo interactúan con parámetros y devuelven resultados precisos

```python
def addition(x, y):
    return x + y


def to_lower(text=''):
    return text.lower()

# Resultado: 90
print(addition(40, 50))

# Resultado: 'hello'
print(to_lower('HellO'))
```

#### Interactúan con valores externos pero no los mutan

```python
customers = ['Ronald A.', 'Jesús M.', 'Andrés M.']

def add_customer(name):
    # Generamos una nueva lista sin alterar la original
    new_customers = [*customers, name]
    return new_customers

# Resultado: ['Ronald A.', 'Jesús M.', 'Andrés M.', 'Benito M.']
customer_1 = add_customer('Benito M.')
print(customer_1)

# La lista original no se altera
print(customers)  # Resultado: ['Ronald A.', 'Jesús M.', 'Andrés M.']
```

---

## ¿Qué son las Funciones Impuras?

Las funciones impuras son aquellas que:

1. Dependan de variables o estructuras externas.
2. Alteran el estado externo (mutan variables globales, listas, diccionarios, etc.).
3. Pueden producir resultados diferentes incluso si reciben los mismos argumentos.

### Ejemplo: Funciones Impuras

```python
numbers = [1, 2, 3]

def add_number(number):
    # Modifica la lista global
    numbers.append(number)
    return numbers

# Primera ejecución
result1 = add_number(10)
print('Result 1:', result1)  # Resultado: [1, 2, 3, 10]

# Segunda ejecución
result2 = add_number(10)
print('Result 2:', result2)  # Resultado: [1, 2, 3, 10, 10]
```

---

## Diferencias Clave entre Funciones Puras e Impuras

| **Aspecto**             | **Funciones Puras**                                             | **Funciones Impuras**                                               |
| ----------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Predictibilidad**     | Siempre producen el mismo resultado para los mismos argumentos. | Los resultados pueden variar según el estado externo.               |
| **Efectos Secundarios** | No tienen efectos secundarios (no alteran el estado externo).   | Pueden alterar variables globales o estructuras externas.           |
| **Pruebas Unitarias**   | Fáciles de probar debido a su consistencia.                     | Más difíciles de probar debido a su dependencia del estado externo. |

---

## Ventajas de Usar Funciones Puras

1. **Predecibilidad**: El resultado es consistente y fácil de razonar.
2. **Fácil de Testear**: No dependen de estados externos, lo que simplifica las pruebas unitarias.
3. **Reutilizabilidad**: Pueden integrarse fácilmente en diferentes partes del programa sin efectos secundarios.

---

## Conclusión

- **Usa funciones puras** siempre que sea posible para mantener un código limpio, predecible y fácil de mantener.
- **Utiliza funciones impuras con precaución**, solo cuando realmente necesites alterar el estado externo o trabajar con datos dinámicos.

Escribir código funcional y estructurado no solo mejora la calidad del software, sino también la experiencia del desarrollador. 🚀
