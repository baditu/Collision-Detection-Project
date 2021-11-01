from forma_geometrica import FormaGeometrica


class Cerc(FormaGeometrica):
    def __init__(self, idul, x, y, raza):
        super().__init__(idul, x, y)
        self.raza = raza

    def calculeaza_raza(self):
        return self.raza