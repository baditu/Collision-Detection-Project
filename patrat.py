from forma_geometrica import FormaGeometrica


class Patrat(FormaGeometrica):
    def __init__(self, idul, x, y, latura):
        super().__init__(idul, x, y)
        self.latura = latura

    def calculeaza_raza(self):
        return self.latura / 2