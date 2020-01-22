# Clases y objetos

class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print(mensaje)

pedro = Humano(26)
raul = Humano(21)

pedro.hablar('Hola')
raul.hablar('Hola, pedro!')

print('Edad de pedro:', pedro.edad)
print('Edad de raul:', raul.edad)
