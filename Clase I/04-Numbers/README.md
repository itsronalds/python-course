# Numbers

En Python tenemos tres tipos de valores númericos que son: enteros, flotantes y complejos, los cuales serán explorados a más detalle a continuación

# Enteros

Los enteros son números que no poseen decimales en su estructura:

```$
lives = 3

# Añadir vidas
lives = lives + 1
print(lives) # 4

# Eliminar vidas
lives = lives - 1
print(lives) # 3
```

# Flotantes

Los flotantes son números que poseen decimales en su estructura:

```$
pant_price = 15.99
print(pant_price)

# Descuento 20%
pant_price = pant_price * 0.20
print(pant_price) # 12.792
```

# Complejos

Los complejos son aquellos que poseen una combinación de números reales e imaginarios.

La parte de números reales puede ser manejada por número enteros o decimales mientras que la parte imaginaria es aquella cuyo cuadrado es negativo.

> Python es un lenguaje de progamación que se adapta muy bien a la ciencia de datos y las matemáticas, por lo que es bueno para el manejo de números complejos

```$
# Podemos utilizar la función de complex para crear un número complejo
example1 = complex(10, 20)

## 10 + 20j
print(example1)

# O podemos ingresar el número imaginario directamente
example2 = 20 + 10j

## 20 + 10j
print(example2)
```

> Los valores complex admiten operadores aritméticos menos el floor division o los operadores de comparación

# Notación científica

Para expresar valores significativamente grandes o pequeños, se utiliza la notación científica que es una forma de escribir dichos valores de una manera abriviada:

```$
number_a = 4500000000000000000.1
print(number_a)

number_b = 0.0000000000000000011
print(number_b)
```

> El interprete de Python pasa automáticamente valores flotantes que son muy grandes o muy pequeños a notación científica para ser más fácil de leer, no quiere decir que el valor haya cambiado, solo su representación cambió.

# Recursos

- [Notación científica](https://www.todamateria.com/notacion-cientifica/)
- [Números complejos en Python](https://www.python-engineer.com/posts/complex-numbers-python/)
