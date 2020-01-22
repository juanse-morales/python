# Cadenas y métodos

s = "Hola Mundo"
print(len(s)) # Dimensión de caracteres y longitud de la cadena

# CADENA.count(valor,inicio,fin)

print(s.count("o",0,3))
print(s.count("o",5)) # Cuenta hasta el final de la cadena

print(s.lower())
print(s.upper())

# CADENA.replace(valor,nuevo,repeticiones)

print(s.replace('o','x'))
print(s.replace('o','x',1))

# CADENA.split(separador,maxsplit)

print(s.split("a"))
print(s.split("o",1))
print(s.split())

# CADENA.find(valor,inicio,fin)
print(s.find('a'))
print(s.rfind('o'))

# CADENA.join(secuencia)

t = ("H","o","l","a")
s = ";"
r = ""

print(s.join(t))
print(r.join(t))
