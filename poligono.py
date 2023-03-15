from shapely import Polygon


class Poligono:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcularAreaPoligono(self):
        pgon = Polygon(zip(self.x, self.y))
        return pgon.area