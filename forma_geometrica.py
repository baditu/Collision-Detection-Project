import math


class FormaGeometrica(object):
    def __init__(self, idul, x, y):
        self.idul = idul
        self.x = x
        self.y = y

    def calculeaza_raza(self):
        raise NotImplementedError(f"Metoda calculeaza_raza nu este inca implementata.")

    def detectare_coliziune(self, figura):
        d = math.sqrt((self.x - figura.x) ** 2 + (self.y - figura.y) ** 2)
        r = self.calculeaza_raza() + figura.calculeaza_raza()

        if d <= r:
            return True
        else:
            return False

    def detectare_semi_incluziune(self, figura):
        coliziune = self.detectare_coliziune(figura)

        if coliziune and self.calculeaza_raza() > figura.calculeaza_raza():
            return True
        else:
            return False