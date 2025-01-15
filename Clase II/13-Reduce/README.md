# Función `reduce` en Python

La función **`reduce`** es una poderosa herramienta en Python que pertenece al módulo `functools`. Es una función de orden superior que permite aplicar una operación acumulativa sobre un iterable, reduciéndolo a un único valor.

---

## ¿Cómo Funciona?

La función **`reduce`** acepta dos parámetros:

1. **Una función**:

   - Esta función debe aceptar dos argumentos:
     - El **acumulador**, que guarda el resultado parcial de la operación.
     - El **elemento actual** del iterable.

2. **Un iterable**:
   - Una colección de datos como una lista o tupla, sobre la cual se aplicará la operación.

Durante cada iteración, `reduce` utiliza el acumulador y el elemento actual para realizar la operación especificada, y el resultado se almacena como nuevo acumulador para la siguiente iteración. Al final, devuelve un único valor.

> **Nota:** Es necesario importar `reduce` desde el módulo `functools` antes de usarla.

---

## Ejemplo 1: Obtener el Menor Número

En este ejemplo, utilizamos `reduce` para encontrar el menor número dentro de una lista:

```python
# Importamos la función reduce
from functools import reduce

# Creamos una lista con valores aleatorios
numbers = [4, 2, 10, 1]

# Obtenemos el menor número de todos
smallest = reduce(lambda x, y: x if x < y else y, numbers)

# Hacemos print del valor
print(smallest)  # Resultado: 1
```

---

## Ejemplo 2: Obtener la Suma de Todos los Números

Con `reduce`, también podemos calcular la suma total de los elementos de un iterable:

```python
# Importamos la función reduce
from functools import reduce

# Creamos una lista con valores aleatorios
numbers = [4, 2, 10, 1]

# Sumatoria de todos los números
total = reduce(lambda x, y: x + y, numbers)

# Hacemos print del valor
print(total)  # Resultado: 17
```

---

## Ventajas de Usar `reduce`

1. **Simplicidad:** Permite realizar operaciones acumulativas complejas con una sola función.
2. **Versatilidad:** Útil para cálculos como sumas, multiplicaciones, mínimos, máximos, etc.
3. **Compatibilidad:** Se combina perfectamente con funciones lambda para escribir código más compacto.

---

## Consideraciones

- `reduce` está diseñado para operaciones acumulativas; si necesitas iterar sobre los elementos sin acumular resultados, considera usar otras funciones como `map` o `filter`.
- Asegúrate de que la función que pases como primer parámetro maneje correctamente los tipos de datos en el iterable para evitar errores.

---
