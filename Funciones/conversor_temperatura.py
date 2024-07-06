"""
Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
"""

def to_celsius(temp):
    return temp * 9/5 + 32

def to_fahrenheit(temp):
    return (temp - 32) * 5/9

temperatura = float(input('Proporciona un valor en grados fahrenheit para convertir a celsius: '))
print(f'La temperatura en grados celsius es: {to_celsius(temperatura):.2f}ºC')

temperatura = float(input('Proporciona un valor en grados celsius para convertir a fahrenheit: '))
print(f'La temperatura en grados fahrenheit es: {to_fahrenheit(temperatura):0.2f}ºF')

