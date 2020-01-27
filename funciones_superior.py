# Funciones de orden superior
# Paradigma de la programación funcional
# Los programas se basen principalmente por funciones

def prueba(f):
    return f()

def porEnviar():
    return 2+2

print(prueba(porEnviar))

def seleccion(operacion):
    def suma(n,m):
        return n+m

    def multiplicacion(n,m):
        return n*m

    if operacion == "suma":
        return suma
    elif operacion == "multi":
        return multiplicacion

fGuardada = seleccion("suma")

print(fGuardada)
print(fGuardada(3,4))

def seleccion2(operacion,n,m):
    def suma(n,m):
        return n+m

    def multiplicacion(n,m):
        return n*m

    if operacion == "suma":
        return suma(n,m)
    elif operacion == "multi":
        return multiplicacion(n,m)

print(seleccion2("suma",2,2))
