# Listas y sus métodos

lista = [1,"Dos",3]

# Método Buscar
buscar = 2
#print(buscar in lista)
#print(lista.index(buscar))

if buscar in lista:
    print(lista.index(buscar))
else:
    print("No está el elemento")

# Método Añadir al final
print(lista)
lista.append("Nuevo elemento")
print(lista)

# Método Contar
print(lista.count(3))

# Método Insertar
print(lista)
lista.insert(2,"Nuevo")
print(lista)
