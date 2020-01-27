# Función Reduce
# Esta función permite reducir una lista o una secuencia a un solo elemento

s = ('H','o','l','a','_','M','u','n','d','o')

def concatenar(a,b):
    return a+b

from functools import reduce
sr = reduce(concatenar,s)

print(type(sr))
print(sr)

s = (1,2,3)

def suma(a,b):
    return a+b

from functools import reduce
sr = reduce(suma,s)

print(type(sr))
print(sr)
