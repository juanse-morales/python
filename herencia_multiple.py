# Herencia Multiple

class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print(mensaje)

class IngSistemas(Humano):
    def __init__(self):   # Sobrescribe el constructor padre
        print('Hola soy ing')

    def programar(self,lenguaje):
        print('Voy a programar en',lenguaje)

class LicDerecho(Humano):
    def __init__(self,escuela):
        print('Licenciado en derecho egresado de:',escuela)

    def estudiarCaso(self,de):
        print('Debo estudiar el caso de',de)

class Estudioso(LicDerecho,IngSistemas):
    pass # Significa vete, no hay nada que ver aquí

pepe = Estudioso('UdC')

pepe.hablar('Hola soy de herencia multiple')
pepe.programar('C++')
pepe.estudiarCaso('Juan')
