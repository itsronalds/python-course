# Operadores Aritméticos

Se utilizan en las operaciones matemáticas para llegar a un determinado resultado.

| **Operador** | **Explicación**                                                                                        | **Ejemplo**    |
| ------------ | ------------------------------------------------------------------------------------------------------ | -------------- |
| `+`          | El operador de suma permite sumar dos números                                                          | `10 + 5 = 15`  |
| `-`          | El operador de resta permite restar dos números                                                        | `10 - 5 = 5`   |
| `*`          | El operador de multiplicación permite multiplicar dos números                                          | `2 * 10 = 20`  |
| `/`          | Permite dividir dos números y siempre nos dará un valor decimal                                        | `10 / 2 = 5.0` |
| `%`          | El operador módulo permite obtener el sobrante de una división                                         | `9 % 2 = 1`    |
| `//`         | Permite dividir dos números y si el resultado tiene sobrante nos redondea el resultado al menor entero | `3 // 2 = 1`   |

---

## Precedencia de los Operadores Aritméticos

En Python se sigue el mismo orden de precedencia que en matemáticas:

| **Prioridad** | **Operador** | **Explicación** |
| ------------- | ------------ | --------------- |
| `1`           | `()`         | Paréntesis      |
| `2`           | `**`         | Exponencial     |
| `3`           | `*`          | Multiplicación  |
| `4`           | `/`          | División        |
| `5`           | `+`          | Suma            |
| `6`           | `-`          | Resta           |

---

## Operadores Aritméticos en Strings

Es posible utilizar operadores aritméticos como el `+` y el `*` en strings:

- **`+`**: Concatena dos strings.
- **`*`**: Multiplica strings y los repite.

**Ejemplos:**

```python
# Concatenación con '+'
greeting = "Hola, " + "mundo!"
print(greeting)  # Hola, mundo!

# Repetición con '*'
repeated = "Python! " * 3
print(repeated)  # Python! Python! Python!
```
