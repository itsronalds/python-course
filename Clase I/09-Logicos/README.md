# Operadores lógicos

Son operadores que nos ayudan a determinar decisiones durante la ejecución del código, entre ellos tenemos: and, or y not.

# and

Nos permite determinar si una u otra/s condiciones son todas True, en caso contrario obtendremos un False.

- Podemos utilizar booleanos:

```$
# True
print(True and True)

# False
print(True and False)

# False
print(False and True)

# False
print(False and False)
```

- O números:

```$
# True
print(5 < 10 and 1 < 5)

# False
print(5 < 10 and 1 > 5)
```

# or

Nos permite determinar si al menos una de las condiciones es True, de lo contario recibiremos un False:

```$
# True
print(True or True)

# True
print(True or False)

# False
print(False or False)
```

# not

Ver sección [05-Booleans](https://github.com/itsronalds/python-course/tree/main/05-Booleans)
