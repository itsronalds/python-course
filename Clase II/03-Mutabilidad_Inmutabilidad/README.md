# Mutabilidad e Inmutabilidad

Python posee estructuras de datos mutables e inmutables, la mutabilidad en programación se refiere a la capacidad de una estructura de datos en cambiar su estructura interna en cuanto a los datos que almacena.

> Las estructuras de datos inmutables siempre tendrán ventaja en cuanto a velocidad de lectura sobre las estructuras mutables, esto ocurre porque el interprete no tiene que analizar el estado inicial y final de una estructura de datos.

• Estructuras de datos inmutables:

| #   | Estructura de datos |                        Descripción                         |
| :-- | :-----------------: | :--------------------------------------------------------: |
| 1   |       Strings       |                    Cadena de caracteres                    |
| 2   | Int, Float, Complex |                Todo tipo de valor númerico                 |
| 3   |       Tuplas        | Guarda valores a través de posiciones similar a las tuplas |

• Estructuras de datos mutables:

| #   | Estructura de datos |                       Descripción                        |
| :-- | :-----------------: | :------------------------------------------------------: |
| 1   |       Listas        | Guarda valores a través de posiciones de manera ordenada |
| 2   |    Diccionarios     |       Guarda valores a través de pares llave-valor       |
| 3   |      Conjuntos      |           Guarda valores de manera no ordenada           |

> Cuando concatenamos strings o usamos operadores aritméticos con valores númericos estamos creando un nuevo valor, no estamos mutando el valor anterior

# Referencia

> - [Mutable & Immutable Data Types](https://www.linkedin.com/pulse/understanding-mutable-immutable-data-types-python-rasmi-ranjan-swain/)
