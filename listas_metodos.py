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

# Método extend: combina dos lista

print(lista)
iterable = "Cadena"
lista.extend(iterable)
print(lista)

print(lista)
iterable = (1,2,3,4)
lista.extend(iterable)
print(lista)

# Méotodo pop: Extrae un elemento y lo borra de la lista

print(lista)
print(lista.pop()) # Si no se coloca indice, borra el último
print(lista)

print(lista)
print(lista.pop(2))
print(lista)

# Método Remove

print(lista)
print(lista.remove(3))  # Elimina la primera ocurrencia
print(lista)

# Método Reverse

print(lista)
print(lista.reverse()) # Invierte la lista
print(lista)
