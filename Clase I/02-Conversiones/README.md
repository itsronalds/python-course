# Conversiones de Datos

En Python, las conversiones de datos permiten transformar un valor de un tipo de dato a otro utilizando funciones específicas.

---

## Funciones de Conversión

| **Función** | **Descripción**                                                 | **Ejemplo**            |
| ----------- | --------------------------------------------------------------- | ---------------------- |
| `str`       | Convierte un valor a un string.                                 | `str(1500)` → `'1500'` |
| `int`       | Convierte un valor string o decimal a un número entero.         | `int('1000')` → `1000` |
| `float`     | Convierte un valor string o entero a un número decimal (float). | `float(15)` → `15.0`   |
| `bool`      | Convierte valores o estructuras de datos a `True` o `False`.    | `bool(1)` → `True`     |

---

## Funciones de Conversión: `bool`

La conversión de datos con la función `bool` tiene un comportamiento único en comparación con otras funciones de conversión. Mientras que intentar convertir valores no compatibles (como una letra a un entero) puede generar errores, con `bool` no ocurre lo mismo.

La función `bool` convierte los valores y estructuras de datos a `True` o `False`, dependiendo de su contenido. A continuación, se detalla cómo funciona esta conversión:

---

### Valores que se Convierten en `False`

| **Conversión** | **Resultado** |
| -------------- | ------------- |
| `bool('')`     | `False`       |
| `bool(0)`      | `False`       |
| `bool(0.0)`    | `False`       |
| `bool([])`     | `False`       |
| `bool({})`     | `False`       |
| `bool(())`     | `False`       |
| `bool(None)`   | `False`       |

---

### Valores que se Convierten en `True`

| **Conversión**                                 | **Resultado** |
| ---------------------------------------------- | ------------- |
| `bool('Python')`                               | `True`        |
| `bool(1)`                                      | `True`        |
| `bool(1.0)`                                    | `True`        |
| `bool(['Python', 'Go', 'JavaScript', 'Rust'])` | `True`        |
| `bool({'a': 'b', 'b': 'a'})`                   | `True`        |
| `bool(('a', 10, True, False))`                 | `True`        |

---

## Notas Importantes

- **Valores Vacíos o Nulos:** En Python, estructuras vacías (como listas, diccionarios, o tuplas) y valores nulos (como `None`) siempre serán convertidos a `False`.
- **Valores No Vacíos:** Cualquier estructura de datos no vacía, cadena de texto, o número diferente de cero será evaluado como `True`.
- Este comportamiento es útil al evaluar condiciones en estructuras de control como `if`, ya que facilita trabajar con diversos tipos de datos.
