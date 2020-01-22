# Herencia

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
    def estudiarCaso(self,de):
        print('Debo estudiar el caso de',de)

pedro = IngSistemas()
raul = LicDerecho(21)

pedro.hablar('Hola')
raul.hablar('Hola, pedro!')

pedro.programar('Python')
raul.estudiarCaso('Pedro')

# print('Edad de pedro:', pedro.edad)
# print('Edad de raul:', raul.edad)
