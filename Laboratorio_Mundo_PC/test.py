from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Benq', 24)
teclado1 = Teclado('NewSkill', 'Bluetooth')
computadora1 = Computadora('Msi Modern', monitor1, teclado1, raton1)

raton2 = Raton('Asus', 'Bluetooth')
monitor2 = Monitor('Philips', 32)
teclado2 = Teclado('Logitech', 'USB')
computadora2 = Computadora('Asus Vivobook', monitor2, teclado2, raton2)

computadoras = [computadora1]

orden = Orden(computadoras)
print(orden)
orden.agregar(computadora2)
print(orden)