# Programación orientada a objetos (POO)

La programación orientada a objetos es un paradigma que nos ayuda a dividir los componentes de un sistema en objetos.

# ¿Qué es un objeto?

Es un elemento que representa algo del mundo real, tiene propiedades y funciones que lo hacen únicos.

- Por ejemplo:

Un auto puede ser un objeto que contiene una marca, modelo, propietario que lo hacen único, el mismo también tiene acciones como arrancar, parar, etc.

# Beneficios de POO

- ✅ Código modularizado
- ✅ Código reutilizable (de una estructura de objeto podemos tener varios que sean diferentes según las propiedades que asignemos)
- ✅ La herencia hace que podamos utilizar propiedades y métodos en otros objetos que herean sus propiedades y métodos
- ✅ La abstracción ayuda a contener toda la lógica en funciones y poder tener una estructura más limpia

# Pilares de POO

- Encapsulación: nos permite tener propiedades privadas, protegidas y públicas que solo pueden ser modificables dentro del mismo objeto u otros objetos que heredan sus propiedades
- Herencia: es la forma en como pasamos atributos y métodos entre clases para tener un código más limpio y organizado
- Polimorfismo: es la capacidad que tienen las diferentes clases de una jerarquia de responder de forma diferente al llamado del mismo método
- Abstracción: nos permite diseñar todo lo que compone un objeto en cuanto a propiedades, métodos y abstraerlo todo en una clase

# Setter y Getter

Los setter y getter son métodos que nos ayudan a obtener y modificar valores privados de las clases:

```$
class Student:
    __name = None

    # setter
    def set_name(self, name):
        self.__name = name

    # getter
    def get_name(self):
        return self.__name


student = Student()

# add student name
student.set_name('Ronald Abu Saleh')

# get student name
student.get_name()
```
