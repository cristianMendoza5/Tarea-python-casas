class casas:
    def __init__(self,ventanas,puertas,techos):
        self.__ventanas = ventanas 
        self.__puertas = puertas
        self.__techos = techos

    @property
    def _ventanas(self):
        return self.__ventanas

    @_ventanas.setter
    def _ventanas(self, value):
        self.__ventanas = value

    @property
    def _puertas(self):
        return self.__puertas

    @_puertas.setter
    def _puertas(self, value):
        self.__puertas = value

    @property
    def _techos(self):
        return self.__techos

    @_techos.setter
    def _techos(self, value):
        self.__techos = value

    class Vivienda_Familiar:
        def __init__(self,ventanas,puertas,techos,piscina):
            super().__init__(self,ventanas,puertas,techos,piscina)
            self._piscina = piscina
    @property
    def piscina(self):
        return self._piscina

    @piscina.setter
    def piscina(self, value):
        self._piscina = value

    class Apartamento:
        def __init__(self,ventanas,puertas,techos,Balcones):
            super().__init__(self,ventanas,puertas,techos,Balcones)
            self._Balcones = Balcones

    @property
    def Balcones(self):
        return self._Balcones

    @Balcones.setter
    def Balcones(self, value):
        self._Balcones = value

    class bungalos:
        def __init__(self,ventanas,puertas,techos,Jardin):
            super().__init__(self,ventanas,puertas,techos,Jardin)
            self._Jardin = Jardin

    @property
    def Jardin(self):
        return self._Jardin

    @Jardin.setter
    def Jardin(self, value):
        self._Jardin = value
