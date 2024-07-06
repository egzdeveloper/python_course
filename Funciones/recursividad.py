"Ejercicio 1. Obtener el resultado del factorial introducido como argumento"
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


"""
Ejercicio 2. Introducir un número como parámetro e imprimir la sucesión descendente hasta 1
usando funciones recursivas. Si el número es negativo o 0, salir de la ejecución
"""
def recursion_descendente(numero):
    if numero >= 0:
        print(numero)
        recursion_descendente(numero - 1)

recursion_descendente(10)