from zooAnimales.animal import Animal


class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color, largo):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._colorEscamas = color
        self._largoCola = largo
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        pass

    def crearIguana(nombre, edad, genero):
        Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1

    def crearSerpiente(nombre, edad, genero):
        Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo):
        self._largoCola = largo