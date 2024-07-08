from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        super().__init__(marca, tipo_entrada)
        self._id_raton = Raton.contador_ratones

    def __str__(self):
        return f'[Ratón] Id: {self._id_raton}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'
