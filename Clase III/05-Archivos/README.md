# Archivos

Python nos otorga formas de interactuar con archivos, pudiendo ser estos .txt o .csv. Para leer o escribir un archivo debemos utilizar la función open

# Métodos de archivos

| Método     |                           Explicación                           |
| :--------- | :-------------------------------------------------------------: |
| open()     |                 Se encarga de abrir un archivo                  |
| read()     |               Se encarga de leer todo el archivo                |
| readline() | Se encarga de leer un archivo línea a línea según lo ejecutemos |
| writable() |       Nos permite saber si en un archivo puede escribirse       |
| readable() |         Nos permite saber si un archivo puede ser leido         |

# ¿Cómo utilizamos open?

La función open recibe varios parámetros que son:

- Dirección del archivo
- Tipo de acción
- Formato del archivo (enconding)

Para el tipo de acción tenemos la siguiente tabla:

| Acción |                                                       Explicación                                                       |
| :----- | :---------------------------------------------------------------------------------------------------------------------: |
| r      |                        Nos permite leer un archivo, si este no existe nos arroja un error de I/O                        |
| r+     |                  Nos permite leer y escribir un archivo, si este no existe nos arroja un error de I/O                   |
| w      |    Nos permite escribir un archivo sobreescribiendo todo lo que había en el, si el archivo no existe crea uno nuevo     |
| w+     | Nos permite escribir y leer un archivo sobreescribiendo todo lo que había en el, si el archivo no existe crea uno nuevo |
| a      |        Nos permite escribir un archivo añadiendo el nuevo texto al final, si el archivo no existe crea uno nuevo        |
| a+     |                     Nos permite escribir y leer un archivo, si el archivo no existe crea uno nuevo                      |

```$
# Abrimos un archivo
file = open('./text.txt', 'r+')

# Leemos el archivo
print(file.read())

# Lo cerramos
file.close()
```
