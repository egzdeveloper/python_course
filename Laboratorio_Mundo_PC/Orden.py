class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        text = ''

        for comp in self._computadoras:
            text += comp.__str__()

        return f'''
[Orden] Id: {self._id_orden}
Computadoras: {text}
'''
