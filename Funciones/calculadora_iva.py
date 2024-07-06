"""
Ejercicio: Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
"""
def calculadora_iva(cantidad, impuesto):
    tax = 1.00 + impuesto
    return cantidad * tax

print('Seleccione el porcentaje de impuesto que quiere aplicar: ')
print('[1]. Impuesto de un 4%')
print('[2]. Impuesto de un 10%')
print('[3]. Impuesto de un 21%')

num = int(input('Escriba su elección (1-3): '))
cantidad = float(input('Introduce la cantidad de dinero que quiere calcular: '))
print(f'Cantidad a calcular: {cantidad}€')

if num == 1:
    impuesto = 0.04
    print(f'La cantidad total para un impuesto del 4% es {calculadora_iva(cantidad, impuesto)}€')
elif num == 2:
    impuesto = 0.1
    print(f'La cantidad total para un impuesto del 10% es {calculadora_iva(cantidad, impuesto)}€')
elif num == 3:
    impuesto = 0.21
    print(f'La cantidad total para un impuesto del 21% es {calculadora_iva(cantidad, impuesto)}€')
else:
    print('Selecciona un valor correcto')