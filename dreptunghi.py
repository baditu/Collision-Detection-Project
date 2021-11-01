from forma_geometrica import FormaGeometrica


class Dreptunghi(FormaGeometrica):
    def __init__(self, idul, x, y, lungime, latime):
        super().__init__(idul, x, y)
        self.lungime = lungime
        self.latime = latime

    def calculeaza_raza(self):
        return max(self.lungime, self.latime) / 2