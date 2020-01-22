# Listas: Son un tipo de colección ordenada, son el equivalente a arreglos y vectores
# Las listas pueden contener enteros, booleanos, cadenas y listas.

l = [2,"Tres",True,["uno",10]]

l2 = l[1]

print(l)
print(l2)

l3 = l[3][0]
print(l3)

l[1] = 4
print(l[1])
print(l)

l4 = l[0:3] #Extrae tres elementos de l empezando desde 0
print(l4)

l5 = l[0:3:2] #Extrae tres elementos de l empezando desde 0 saltando de uno en uno
print(l5)

l6 = l[1::2]
print(l6)

l[0:2] = [4,3]
print(l)

l[0:2] = [4]
print(l)

l7 = l[-1]
print(l7)
