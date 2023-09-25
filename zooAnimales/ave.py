from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._colorPlumas = color
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        pass

    def crearHalcon(nombre, edad, genero):
        Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1

    def crearAguila(nombre, edad, genero):
        Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color):
        self._colorPlumas = color