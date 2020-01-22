# Encapsulación

class Prueba(object):
    def __init__(self):
        self.__privado = "Soy atributo privado"
        self.privado = "Soy atributo publico"

    def __metodoPrivado(self):
        return "Soy método privado"

    def metodoPublico(self):
        print("Soy método publico")

    def getPrivado(self):
        return self.__privado

    def setPrivado(self,valor):
        self.__privado = valor

obj = Prueba()
#print(obj.privado)
#print(obj.__privado)

#print(obj.metodoPublico())
#print(obj.__metodoPrivado())

obj.setPrivado("Nuevo Valor")
print(obj.getPrivado())
