# Scope en Python

El **scope** o alcance en Python se refiere a la región del código donde una variable, función o clase es accesible. El alcance de un identificador depende del lugar donde fue creado y se gestiona según la **regla LEGB** (Local, Enclosing, Global, Built-in).

---

## Regla LEGB

Python organiza los alcances en cuatro niveles jerárquicos:

1. **Local (L)**: Variables definidas dentro de una función. Solo son accesibles dentro de esa función o sus funciones anidadas.
2. **Enclosing (E)**: Variables definidas en una función externa y accesibles en funciones anidadas internas.
3. **Global (G)**: Variables definidas a nivel de módulo. Son accesibles en todo el archivo, pero no dentro de funciones sin declaración explícita.
4. **Built-in (B)**: Funciones, variables y clases predefinidas en Python que están disponibles en cualquier parte del programa (por ejemplo, `len`, `print`, `list`, etc.).

> **Nota:** La palabra clave `global` permite modificar una variable definida en el scope global desde una función.

---

## Ejemplos de Scope

### 1. Scope Local

Las variables definidas dentro de una función son locales y no accesibles fuera de ella.

```python
def clear_string(string=''):
    clean_string = ''
    for letter in string:
        if letter == ' ' or letter.isalnum():
            clean_string += letter
    return clean_string

# ❌ Error: clean_string no está disponible fuera de la función
# print(clean_string)

random_string = 'Hol$a chic#os'
clean_string = clear_string(random_string)

# ✅ Imprime: Hola chicos
print(clean_string)
```

---

### 2. Scope Anidado (Enclosing)

Una función interna puede acceder a variables definidas en su función externa, pero no al revés.

```python
def outer_function():
    print('Outer Function')
    a = 10

    def inner_function():
        print('Inner Function')
        global b
        b = 20

        print('Variable de outer_function:', a)
        print('Variable global definida dentro de inner_function:', b)

    inner_function()

outer_function()

# ✅ Imprime: 20 (variable global creada en inner_function)
print(b)
```

---

### 3. Global Scope

Las variables definidas fuera de cualquier función tienen alcance global.

```python
a = 10
b = 20

def global_addition(custom_a=None, custom_b=None):
    global a, b
    a = custom_a if custom_a else a
    b = custom_b if custom_b else b
    return a + b

# ✅ Imprime: 50
print(global_addition(20, 30))
```

---

### 4. Built-in Scope

Las funciones y variables predefinidas en Python están disponibles globalmente en cualquier lugar del programa.

```python
print('Built-in scope:', len('Hola'))  # ✅ Imprime: 4
print('Built-in scope:', list(range(0, 10, 2)))  # ✅ Imprime: [0, 2, 4, 6, 8]
```

---

## ¿Qué son los Namespaces?

Los **namespaces** (espacios de nombres) son contenedores que mapean nombres a objetos (variables, funciones, clases). Funcionan como diccionarios y ayudan a organizar el código según los scopes.

- **Global Namespace**: Contiene nombres definidos a nivel de módulo.
- **Local Namespace**: Contiene nombres definidos dentro de una función.
- **Built-in Namespace**: Contiene nombres predefinidos por Python.

### Representación de Namespaces

![Tipos de Namespaces](https://github.com/itsronalds/python-course/assets/77751686/ded7d2e4-7153-4a79-af08-163ab08decf5)

> Los namespaces están directamente relacionados con el scope, ya que definen el contexto en el que los nombres son accesibles.

---
