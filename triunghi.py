from forma_geometrica import FormaGeometrica


class Triunghi(FormaGeometrica):
    def __init__(self, idul, x, y, l1, l2, l3):
        super().__init__(idul, x, y)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def calculeaza_raza(self):
        return max(self.l1, self.l2, self.l3) / 2
