# Decoradores
# Es una función que recibe una función y regresa una nueva función ya decorada

loggeado = False
usuario = "Codigo Facilito"

def admin(f):
    def comprobar(*args,**kwargs):
        if loggeado:
            f(*args,**kwargs)
        else:
            print("No tiene permisos de ejecutar:",f.__name__)
    return comprobar

def decorador(funcion):
    def funcionDecorada(*args,**kwargs):
        print("Función ejecutada:",funcion.__name__)
        funcion(*args,**kwargs)

    return funcionDecorada

@admin
@decorador
def resta(n,m):
    print(n-m)

resta(3,5)
