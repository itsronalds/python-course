# Numbers

En Python, existen tres tipos principales de valores numéricos: `int`, `float` y `complex`. A continuación, se explica cada uno de estos tipos en detalle con ejemplos prácticos.

---

## Enteros (`int`)

Los valores `int` representan números enteros que no poseen decimales.

### Ejemplo:

```python
lives = 3

# Incrementar vidas
lives = lives + 1
print(lives)  # Salida: 4

# Reducir vidas
lives = lives - 1
print(lives)  # Salida: 3
```

---

## Flotantes (`float`)

Los valores `float` representan números con decimales.

### Ejemplo:

```python
pant_price = 15.99
print(pant_price)  # Salida: 15.99

# Aplicar descuento del 20%
pant_price = pant_price * 0.80
print(pant_price)  # Salida: 12.792
```

---

## Complejos (`complex`)

Los números `complex` son aquellos que combinan una parte real y una parte imaginaria. La parte real puede ser un entero o flotante, mientras que la parte imaginaria siempre incluye la unidad imaginaria `j`, cuyo cuadrado es negativo.

Python facilita el manejo de números complejos, lo que lo convierte en una herramienta ideal para cálculos matemáticos avanzados.

### Ejemplo:

```python
# Crear un número complejo usando la función complex
example1 = complex(10, 20)
print(example1)  # Salida: (10+20j)

# Crear un número complejo directamente
def example2 = 20 + 10j
print(example2)  # Salida: (20+10j)
```

### Notas:

- Los números `complex` admiten operadores aritméticos como suma, resta y multiplicación.
- No admiten divisiones de piso (`//`) ni operadores de comparación como `<` o `>`.

---

## Notación científica

Para representar valores extremadamente grandes o pequeños, Python utiliza la notación científica, que es una forma abreviada y más legible de escribir dichos números.

### Ejemplo:

```python
number_a = 4500000000000000000.1
print(number_a)  # Salida: 4.5e+18

number_b = 0.0000000000000000011
print(number_b)  # Salida: 1.1e-18
```

Python convierte automáticamente los valores flotantes muy grandes o pequeños a notación científica para mejorar la legibilidad, sin alterar su valor subyacente.

---

## Recursos adicionales

- [Notación científica](https://www.todamateria.com/notacion-cientifica/)
- [Números complejos en Python](https://www.python-engineer.com/posts/complex-numbers-python/)
