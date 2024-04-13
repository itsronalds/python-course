# API

API hace referencia a **Application Programming Interface** y se trata de un conjunto de herramientas o funciones que nos ayudan a interactuar con otras aplicaciones, es por decir la pieza intermedia que conecta dos sistemas.

Por ejemplo:

- La API de React: nos permite integrar funciones, hooks y las funcionalidades de React (proyecto) en nuestra app
- La API de Python: nos otorga la oportunidad de interactuar con todas las funciones nativas de Python por lo que conectamos nuestra app de Python con las funciones nativas de Python que forman parte del proyecto

![What-is-an-API](https://github.com/itsronalds/python-course-priv/assets/77751686/cd18e1bf-1ad6-42b1-9f41-ab0a5379c513)

# REST API's

REST API es el termino que se refiere a una aplicación que funciona del lado del servidor y utiliza el protocolo HTTP para el intercambio de información con aplicaciones clientes que pueden ser:

- Una app móvil
- Una app web
- Una app de escritorio
- Otras REST API's

REST tiene el significado de **Representational State Transfer** también denominado servicios REST.

> Normalmente estas aplicaciones además de atender solicitudes de aplicaciones clientes, también se conectan con bases de datos para el almacenamiento y obtención de información.

![1622931040032](https://github.com/itsronalds/python-course-priv/assets/77751686/16f99336-2fa4-4b2f-b175-edaf47daf783)

# Arquitectura cliente-servidor

Es la arquitectura en la que se basan las REST API's para el intercambio de información entre aplicaciones, consiste en:

- **1er paso**: hacer una petición desde una aplicación cliente al servidor
- **2do paso**: obtener una respuesta del servidor

> Diferencia de la arquitectura **bidireccional** donde el servidor y el cliente pueden intercambiarse mensajes en imfroación en tiempo real sin esperar que el cliente envié una petición para ser respondida.

# Arquitectura bidireccional | Tiempo real

Esta es una de las últimas arquitecturas empleadas en el protocolo de las REST API's para el intercambio de datos en tiempo real entre cliente y servidor, donde también se utilizan técnicas de broadcast donde enviamos mensajes o datos a una cantidad indefinida de clientes.

![63fe488452cc63cf1cb0ae45_148 2](https://github.com/itsronalds/python-course-priv/assets/77751686/08762211-a52e-4484-8c94-ab1db75118b6)
