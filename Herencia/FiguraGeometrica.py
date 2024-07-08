class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if self._validar(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print('Valor erróneo del ancho')
        if self._validar(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('Valor erróneo del alto')

    def __str__(self):
        return f'<FiguraGeometrica> Alto: {self.alto}, Ancho: {self.ancho}'

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print('Valor erróneo del ancho')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('Valor erróneo del alto')

    def _validar(self, valor) -> bool:
        return True if 0 < valor < 10 else False
