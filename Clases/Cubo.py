class Cubo:
    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def volumen(self):
        return self.base * self.altura * self.profundidad


# Creación del objeto de la clase
base = int(input('Introduce la base del cubo: '))
altura = int(input('Introduce la altura del cubo: '))
profundidad = int(input('Introduce la profundidad del cubo: '))

cubo = Cubo(base, altura, profundidad)
print(f'El volumen del cubo es de {cubo.volumen()} m³')