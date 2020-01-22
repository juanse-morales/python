# Bucles

# While
edad = 0
while edad<=20:

    if edad == 15:
        edad = edad + 1
        continue

    print('Tienes: ' + str(edad) + ' de edad.')
    edad = edad + 1

edad = 0
while edad<=20:

    if edad == 15:
        break

    print('Tienes: ' + str(edad) + ' de edad.')
    edad = edad + 1


# For

lista = ['Elemento 1','Elemento 2', 'Elemento 3']

for elem in lista:
    print(elem)

for letra in 'Cadena':
    print(letra)
