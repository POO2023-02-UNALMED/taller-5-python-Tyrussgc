from zooAnimales.animal import Animal


class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color, cantidad):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._colorEscamas = color
        self._cantidadAletas = cantidad
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        pass

    def crearSalmon(nombre, edad, genero):
        Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1

    def crearBacalao(nombre, edad, genero):
        Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad