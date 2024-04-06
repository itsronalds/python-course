from random import randint

# Crear una clase


class Person:
    # Atributo protegido
    _bank_code = None

    def __init__(self, name, lastname, bank_code):
        print('Person was created')

        # add attr
        self.name = name
        self.lastname = lastname
        self._bank_code = bank_code

    def talk(self):
        return 'Talk...'

    def walk(self):
        return 'Walk...'

    def _protected_method(self):
        return 'Protected method'


class Student(Person):
    # Atributo privado
    __student_code = randint(0, 1000000)

    def __init__(self, name, lastname, bank_code, student_code):
        super().__init__(name, lastname, bank_code)
        self.__student_code = student_code

        print(self._protected_method())
        print(self.__private_method())

    def get_bank_code(self):
        return self._bank_code

    def __private_method(self):
        return 'Private method'

    # setter
    def set_student_code(self, code):
        print('code', code)
        self.__student_code = code

    # getter
    def get_student_code(self):
        return self.__student_code
    
    # argv y kwargs
    def get_notes(*argv, **kwargs):
        print(argv)
        print(kwargs)


student1 = Student('Ronald', 'Abu Saleh', '01256547510', '26275576')

print('Student Bank Code', student1.get_bank_code())

student1.set_student_code('26258888')
print('Student Code', student1.get_student_code())


# setter & getter
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
print(student.get_name())