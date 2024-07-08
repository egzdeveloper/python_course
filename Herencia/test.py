from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto cuadrado'.center(50, '-'))
cuadrado = Cuadrado(lado=5, color='Rojo')
print(f'Cálculo área cuadrado: {cuadrado.area()}')
print(f'{cuadrado}\n')

print('Creación Objeto rectangulo'.center(50, '-'))
rectangulo = Rectangulo(alto=5, ancho=4, color='Verde')
print(f'Cálculo área rectángulo: {rectangulo.area()}')
print(rectangulo)