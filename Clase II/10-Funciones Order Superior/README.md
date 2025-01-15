# Funciones de Orden Superior en Python

Las **funciones de orden superior** son aquellas que:

1. **Aceptan otras funciones como parámetros.**
2. **Pueden retornar una función como resultado.**

Estas funciones son muy útiles para escribir código más flexible, modular y reutilizable. A continuación, exploramos ambos casos con ejemplos prácticos.

---

## 1. Función de Orden Superior que Acepta una Función como Parámetro

Un ejemplo común es un **calculador** que acepta diferentes operaciones matemáticas como parámetros:

```python
# Función para sumar
def addition(a, b):
    return a + b

# Función para restar
def subtract(a, b):
    return a - b

# Función calculadora que acepta una operación como parámetro
def calculator(operation, a, b):
    # Validamos que los parámetros sean números
    if not isinstance(a, (int, float)):
        return 'Error: El primer valor no es válido'

    if not isinstance(b, (int, float)):
        return 'Error: El segundo valor no es válido'

    # Ejecutamos la operación
    return operation(a, b)

# Uso de la calculadora con funciones
result1 = calculator(addition, 10, 10)
result2 = calculator(subtract, 20, 10)

print('Suma:', result1)       # Resultado: 20
print('Resta:', result2)      # Resultado: 10
```

---

## 2. Función de Orden Superior que Retorna Otra Función

Una función puede devolver otra función, lo que permite crear funciones dinámicas y personalizadas.

```python
# Función externa que retorna funciones internas
def outer(x):
    # Función para sumar
    def add(y):
        return x + y

    # Función para restar
    def subtract(y):
        return x - y

    # Retornamos ambas funciones como una tupla
    return add, subtract

# Creamos un conjunto de funciones basado en un valor inicial
functions = outer(10)

# Usamos la primera función (add)
result1 = functions[0](5)
print('Suma:', result1)  # Resultado: 15

# Usamos la segunda función (subtract)
result2 = functions[1](5)
print('Resta:', result2)  # Resultado: 5
```

---

## Ventajas de las Funciones de Orden Superior

1. **Reutilización del código:** Facilitan la escritura de funciones genéricas que se pueden personalizar con otras funciones.
2. **Flexibilidad:** Permiten pasar lógica específica como parámetros.
3. **Composición funcional:** Se pueden combinar funciones para construir pipelines de procesamiento.

> Estas características hacen que las funciones de orden superior sean fundamentales en paradigmas como la **programación funcional**.

---
