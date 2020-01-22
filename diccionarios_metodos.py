# Diccionarios y sus métodos

diccionario = {
    "redes_sociales": ['Twitter','Facebook','LinkedIn'],
    3: 'Tres',
    'Hola':"Mundo"
}

print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())

# DICCIONARIO.pop(valor,d)
print(diccionario)
print(diccionario.pop(3))
print(diccionario)

print(diccionario.pop(4,-1))
print(diccionario)

del diccionario['Hola']
print(diccionario)

diccionario.clear()
print(diccionario)

diccionario["clave_nueva"] = 'Valor'
print(diccionario)

# Método copy

diccionario_2 = diccionario.copy()
print(diccionario_2)
