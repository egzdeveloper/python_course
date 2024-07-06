"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores.
"""

def sumar(*numeros) -> int:
    total = 0
    for numero in numeros:
        total += numero

    return total

print(sumar(1,5,8))

"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores.
"""

def multiplicar(*numeros) -> int:
    total = 1
    for numero in numeros:
        total *= numero

    return total

print(multiplicar(1,5,8))