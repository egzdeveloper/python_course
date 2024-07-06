class Aritmetica:
    """
    Clase aritmética para realizar las operaciones de sumas, restas, multiplicaciones y disvisiones.
    """
    def __init__(self, numA, numB):
        self.numA = numA
        self.numB = numB

    def sumar(self):
        return self.numB + self.numB

    def restar(self):
        return self.numA - self.numB

    def multiplicar(self):
        return self.numA * self.numB

    def dividir(self):
        return self.numA / self.numB


# Creamos los objetos
aritmetica1 = Aritmetica(6,2)
print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())