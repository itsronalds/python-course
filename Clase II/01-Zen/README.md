# Zen de Python

Escrito por Tim Peters, se basa en una serie de reglas o también denominadas filosofía Pythonista que nos ayuda a mantener un código más profesional y mejor estructurado, a la vez más sencillo de leer.

Es importante tener en cuenta que estas reglas no son indispensables seguirlas y solo están como sabiduría a tener en cuenta al escribir código en Python.

> Tim escribió estás reglas como algo divertido y se lo envío a Guido Van Rossum (creador de Python), nunca pensó que Guido tomaría estas reglas en serio, pero para su sorpresa estás fueron incluidas al lenguaje mediante un módulo llamado this

# Módulo this

Python posee un módulo llamado this, trata de un módulo especial que nos muestra en consola el Zen de Python a través de 19 consejos.

- Ejecutamos el módulo de la siguiente manera:

```$
import this

# Print en consola del Zen de Python
print(this)
```

# Traducción

| #   |                                                Regla                                                |
| :-- | :-------------------------------------------------------------------------------------------------: |
| 1   |                                       Bello es mejor que feo                                        |
| 2   |                                  Explícito es mejor que implícito                                   |
| 3   |                                    Simple es mejor que complejo                                     |
| 4   |                                  Complejo es mejor que complicado                                   |
| 5   |                                     Plano es mejor que anidado                                      |
| 6   |                                     Disperso es mejor que denso                                     |
| 7   |                                        La legibilidad cuenta                                        |
| 8   |             Los casos especiales no son tan especiales como para quebrantar las reglas              |
| 9   |                                 Aunque lo práctico gana a la pureza                                 |
| 10  |                      Los errores nunca deberían dejarse pasar silenciosamente                       |
| 11  |                          A menos que hayan sido silenciados explícitamente                          |
| 12  |                      Frente a la ambigüedad, rechaza la tentación de adivinar                       |
| 13  |               Debería haber una —y preferiblemente sólo una— manera obvia de hacerlo                |
| 14  | Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés (Guido van Rossum) |
| 15  |                                      Ahora es mejor que nunca                                       |
| 16  |                             Aunque nunca es a menudo mejor que ya mismo                             |
| 17  |                   Si la implementación es difícil de explicar, es una mala idea.                    |
| 18  |               Si la implementación es fácil de explicar, puede que sea una buena idea               |
| 19  |                   Los "namespaces" son una gran idea ¡Hagamos más de esas cosas!                    |

# A todas estas, ¿Qué son los namespaces?

Son contenedores que contienen identificadores de nombres a objetos correspondientes (variables, funciones, clases), dichos namespaces se encuentran en forma de diccionarios.

En otras palabras, los espacios de nombres nos ayudan a utilizar variables, funciones y clases a través de sus alcances o scopes y estos son guardados en objetos enlanzados a identificadores.

> Los namespaces tienen mucho que ver con scoper lo cual veremos más adelante.
