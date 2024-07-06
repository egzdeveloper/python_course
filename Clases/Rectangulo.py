class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2

    def area(self):
        return self.base * self.altura


# Creación de objetos de la clase
base = int(input('Introduce la base del rectángulo: '))
altura = int(input('Introduce la altura del rectángulo: '))

rectangulo = Rectangulo(base, altura)
print(f'El perímetro del rectángulo es de {rectangulo.perimetro()}')
print(f'El área del rectángulo es de {rectangulo.area()}')