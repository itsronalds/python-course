# Fundamentos de Python: Variables y Funciones Básicas

Este documento proporciona una introducción a algunos conceptos fundamentales de Python, incluyendo el uso de variables, tipos de datos primitivos, comentarios, indentación y funciones esenciales.

---

## **¿Qué son las Variables?**

En Python, las variables son espacios reservados en la memoria del sistema operativo que se utilizan para almacenar valores. Estos valores pueden ser recuperados y utilizados en la ejecución del programa.

A cada variable se le asigna un nombre único y, opcionalmente, un valor inicial. Ejemplo:

```python
name = 'John Myers'
age = 25
height = 1.75
occupation = 'Software Engineer'
```

---

## **Tipos de Datos Primitivos**

En Python, los tipos de datos primitivos son los más básicos y esenciales para trabajar con valores. A continuación, se describen los principales:

| **Tipo de Dato** | **Descripción**                                              | **Ejemplo**       |
|-------------------|--------------------------------------------------------------|-------------------:|
| `string`          | Permite almacenar cadenas de texto.                         | `'Hello Python'`  |
| `int`             | Permite almacenar números enteros.                          | `25`              |
| `float`           | Permite almacenar números decimales.                        | `1.75`            |
| `bool`            | Representa valores lógicos: `True` o `False` (1 y 0).       | `True`            |

---

## **Comentarios**

Los comentarios son fragmentos de texto dentro del código que no son ejecutados por el intérprete. Se utilizan para explicar o documentar partes del código.

### Ejemplos:

```python
# Comentario de una sola línea

'''
Comentario de
múltiples líneas
'''
```

---

## **Indentación**

La indentación es fundamental en Python, ya que define los bloques de código. Se utiliza especialmente en estructuras como sentencias condicionales, bucles y funciones.

### **Características clave:**
- Python es estrictamente sensible a la indentación. Una mala indentación generará errores.
- Además de su importancia funcional, una buena indentación mejora la legibilidad del código.

```python
if True:
    print("Este bloque está correctamente indentado")
```

---

## **Funciones Esenciales en Python**

### **1. Función `print()`**
La función `print()` permite mostrar en consola el valor de una variable o cualquier otro dato.

```python
name = 'John Myers'

# Muestra "John Myers" en la consola
print(name)
```

---

### **2. Función `type()`**
La función `type()` devuelve el tipo de dato de una variable o valor. Esto puede ser útil para depurar o entender el comportamiento del programa.

```python
number = 10

# Devuelve <class 'int'>, ya que todo en Python es un objeto
print(type(number))
```

> **Nota:** En Python, todo es un objeto.

---

### **3. Función `input()`**
La función `input()` permite recibir datos desde el usuario a través de la consola. Lo ingresado por el usuario siempre será tratado como una cadena (`string`).

```python
# Solicitar al usuario su nombre
name = input('Ingresa tu nombre: ')

# Mostrar el nombre ingresado en consola
print(name)
```

> **Nota:** Si se necesita otro tipo de dato, se debe realizar una conversión explícita.

---

## **Conclusión**

Este documento cubre conceptos básicos de Python que son esenciales para principiantes. Dominar estos fundamentos te permitirá sentar una base sólida para desarrollar aplicaciones más avanzadas en Python. Recuerda que la práctica constante y la escritura de código limpio son claves para convertirte en un mejor programador.

---
