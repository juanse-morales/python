# Funciones lambda
# Son funciones anónimas que por ende se ejecuta únicamente en el momento en el que se está creando

# Función a utlizar con map() y reduce()
#def suma(n,m):
#    return n+m

# Función a utilizar con filter()
#def filtrar(n):
#    return (n == 'o')

li = [1,-2,1,-4]
lo = [5,3,6,7]
s = "Hoola Mundo"

suma = lambda n,m: n+m

from functools import reduce
print(*map(suma,li,lo))
print(*filter(lambda n: n=='o',s))
print(reduce(suma,lo))
print(suma(3,4))
