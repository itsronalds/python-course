print("Sin comprensión de listas:")

numbers = [1, 2, 3, 4, 5]
pair_numbers = []

for x in numbers:
    if x % 2 == 0:
        pair_numbers.append(x)

print(pair_numbers)

print('\n-----------------------------------\n')

print("Comprensión de listas:")

numbers = [1, 2, 3, 4, 5]

# Extraer solo los números pares
pair_numbers = [x for x in numbers if x % 2 == 0]

# Resultado: [2, 4]
print(pair_numbers)

print('\n-----------------------------------\n')

print("Comprensión de listas con modificaciones:")

places = ['venezuelA', 'argentinA', 'chilE', 'uruguaY', 'paraguAy', 'boliVia']
places_capitalize = [place.capitalize() for place in places]

print(places_capitalize)
