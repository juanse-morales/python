#enconding: utf-8
# Sentencias condicionales
# Nos permite ejecutar un bloque de código siempre que se cumpla una condición, solamente se va a ejecutar una vez cada que hagamos la evaluación.

edad = 15
m_edad = 18

if edad >= m_edad:
    print('Eres mayor de edad')
    if False:
        print('Se sigue ejecutando')
    else:
        print('Asd')
else:
    print('No eres mayor de edad')
print('Esto se ejecuta siempre')

edad = 12
if edad >= 0 and edad < 18:
    print('Eres un niño')
elif edad >= 18 and edad < 27:
    print('Eres un joven')
elif edad >= 27 and edad < 60:
    print('Eres un adulto')
else:
    print('Eres de la tercera edad')
