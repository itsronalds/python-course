# Métodos HTTP

Para comunicarse correctamente con las REST API's necesitamos utilizar el protocolo HTTP, y para ello necesitamos utilizar los métodos HTTP.

Estos métodos nos ayudan a comunicarnos con las REST API's señalando el tipo de acción que queremos ejecutar, entre los métodos se encuentran:

| Nombre |                        Explicación                        |
| :----- | :-------------------------------------------------------: |
| get    | Utilizado cuando queremos extraer datos desde un servidor |
| post   |        Utilizado cuando queremos crear un recurso         |
| put    |   Utilizado para actualizar recursos o crear uno nuevo    |
| delete |             Utilizado para eliminar recursos              |

> Estos son los métodos HTTP más utilizados y que nos permiten la acción de CRUD (create, read, update, delete) en nuestra REST API.
> 
![1656172124708](https://github.com/itsronalds/python-course-priv/assets/77751686/16cf3edf-8dfb-4f38-8ea1-d215efa38f7c)

# Códigos de status HTTP

Los códigos de status nos permite indicarle a la aplicación cliente que inició una solicitud si su solicitud fue procesada de manera exitosa, tuvo algún error, pasarle un mensaje informativo, etc.

Los códigos de status más populares son:

| Nombre                    |                                  Explicación                                   |
| :------------------------ | :----------------------------------------------------------------------------: |
| 200 OK                    |                Indica que la operación fue ejecutada con éxito                 |
| 400 BAD REQUEST           | Indica que la petición no posee la estructura correcta, como campos inválidos  |
| 401 UNAUTHORIZED          | Indica que el usuario no tiene acceso para acceder a los recursos que solicita |
| 404 NOT FOUND             |            Indica que el recurso al que se quiere acceder no existe            |
| 500 INTERNAL SERVER ERROR | Indica que la solicitud fue aceptada pero hubo un error interno en el servidor |

> Es muy importante el uso de try-except porque evitan que se produzca un **internal server error** indebido.

![wmkPPztB7KlAC7fPzO0-85NG8t0B9IEh4JEbt_ELP1pvJMhof9vt2pDSwrBZeXodoqaoV_Es1Rur-AWoeoOdV-RIde2vjqyMQuxrqch62uXZ1bsI0yaaMWx-f4cg4BlmOQrI2kFJ6CPXECCd69KeopE](https://github.com/itsronalds/python-course-priv/assets/77751686/987a8816-ebf7-47f4-9226-df4103a5e522)

