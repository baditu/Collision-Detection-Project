from cadran import Cadran


class SpatiuDeLucru(object):
    def __init__(self, x1, y1, x2, y2):
        self.cadran1 = Cadran(((x1 + x2) / 2), ((y1 + y2) / 2), x2, y2)
        self.cadran2 = Cadran(x1, ((y1 + y2) / 2), ((x1 + x2) / 2), y2)
        self.cadran3 = Cadran(x1, y1, ((x1 + x2) / 2), ((y1 + y2) / 2))
        self.cadran4 = Cadran(((x1 + x2) / 2), y1, x2, ((y1 + y2) / 2))

    def verificare_cadran(self, figura):
        if self.cadran1.x1 < figura.x < self.cadran1.x2 and self.cadran1.y1 < figura.y < self.cadran1.y2:
            return 1
        elif self.cadran2.x1 < figura.x < self.cadran2.x2 and self.cadran2.y1 < figura.y < self.cadran2.y2:
            return 2
        elif self.cadran3.x1 < figura.x < self.cadran3.x2 and self.cadran3.y1 < figura.y < self.cadran3.y2:
            return 3
        elif self.cadran4.x1 < figura.x < self.cadran4.x2 and self.cadran4.y1 < figura.y < self.cadran4.y2:
            return 4
        else:
            return -1
