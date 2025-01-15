# Métodos String

Funciones build-in que podemos aplicar en los strings para poder manipularlos a nuestra conveniencia.

- Los métodos string más comunes son los siguientes:

| Métodos    |                          Explicación                          |                                     Ejemplo |
| :--------- | :-----------------------------------------------------------: | ------------------------------------------: |
| upper      |               Convierte la cadena a mayusculas                |                   'hello'.upper() = 'HELLO' |
| lower      |               Convierte la cadena a minusculas                |                   'HELlo'.lower() = 'hello' |
| count      | Cuenta las veces que aparece una letra o palabra en la cadena |                     'colors'.count('0') = 2 |
| swapcase   |  Convierte minusculas a mayusculas y mayusculas a minusculas  |  'Hello Python'.swapcase() = 'hELLO pYTHON' |
| startswith |    Analiza si una cadena empieza con alguna letra/palabra     | 'Is my favorite'.startswith('Is my') = True |
| endswith   |    Analiza si una cadena termina con alguna letra/palabra     |      'It's my house'.endswith('use') = True |
| title      |                 Convierte una cadena a título                 |  'python course'.title() => 'Python Course' |
| isdigit    |               Evalua si un string es un dígito                |                      '658'.isdigit() = True |

# Operadores generales

Pueden ser utilizados en diferentes tipos de datos como: string, list, dict, etc.

- Dos operadores muy comunmente utilizado en strings son los siguientes:

| Métodos |                       Explicación                        |                                        Ejemplo |
| :------ | :------------------------------------------------------: | ---------------------------------------------: |
| len     |             Evalua la longitud de una cadena             |                             len('welcome') = 7 |
| in      | Evalua si un determinado valor se encuentra en la cadena | 'programmer' in "I'm programmer" a programmer' |
