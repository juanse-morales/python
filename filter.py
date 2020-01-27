# Función Filter

def filtro(elem):
    return (elem>0)

l = [1,-3,2,-7,-8,-9,10]

lr = filter(filtro,l)

print(l)
print(*lr)

def filtro2(elem):
    return (elem == "o")

s = "Hola mundo"

lr = filter(filtro2,s)

print(s)
print(*lr)
