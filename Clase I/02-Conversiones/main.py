# Tema: Conversiones de Datos

# string
name = 'John Myers'

# int
age = 30

# float
salary = 1000.0

# bool
is_junior = True

# ❌ No se pueden concatenar una variable y un string
# print(name + ' is ' + age + ' years old')

# ✅ Usando la función str() para convertir el int a string
print('Hola, mi nombre es ' + name + ' y tengo ' + str(age) + ' años')

# ✅ Pasamos la variable salary que es un float a string
print('Soy Junior Python Developer y gano ' +
      str(salary) + ' dólares mensuales')

print('-----------------------------')

repository_stars = '1000'

# ❌ No se pueden sumar un int y un string
# repository_stars = repository_stars + 1

# ✅ Usando la función int() para convertir el string a int
repository_stars = int(repository_stars) + 1
print('repository_stars =>', type(repository_stars))

# 💡 Manera corta de hacerlo
# repository_stars = str(int(repository_stars) + 1)

# Transformamos el int a string para poder concatenarlo
repository_stars = str(repository_stars)
print('repository_stars =>', type(repository_stars))

# Resultado
print('Mi repositorio tiene ' + repository_stars + ' estrellas')

print('-----------------------------')

budget = 1000
print(budget)

budget = float(budget)
print(budget)

print('Mi presupuesto es de ' + str(budget) + ' dólares')

print('-----------------------------')

'''
En Python, los valores que se evalúan como False son:
    - False
    - None
    - 0
    - 0.0
    - ''
    - []
    - ()
    - {}
'''

programming_language = ''
print(bool(programming_language))

errors = 0
print(bool(errors))

programming_languages = []
print(bool(programming_languages))

work_days = ()
print(bool(work_days))

company_info = {}
print(bool(company_info))

print('-----------------------------')

programming_language = 'Python'
print(bool(programming_language))

errors = 1
print(bool(errors))

programming_languages = ['Python', 'JavaScript', 'Java']
print(bool(programming_languages))

work_days = ('Monday', 'Tuesday', 'Wednesday')
print(bool(work_days))

company_info = {'name': 'URBE', 'employees': 100}
print(bool(company_info))
