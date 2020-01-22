# Funciones: una función es un fragmento de código en el cual se realiza algunas tareas.

def mi_funcion(num1=0,num2=0):
    print(num1+num2)

mi_funcion(3)

def mi_funcion2(cad,v=2,*algomas):  #Tupla
    print(cad * v)
    for cadena in algomas:
        print(cadena * v)

mi_funcion2('Python ',5,'Hola ','Adios ','N ','Cadenas ')

def mi_funcion3(cad,v=2,**algomas):    #Diccionario
    print(cad * v)
    print(algomas['ce'])
    print(algomas['am'])

mi_funcion3('Python ',5,ce='Hola',am='Adios')

def mi_funcion4(num1,num2):
    return num1+num2

r = mi_funcion4(3,4)
print(r)
