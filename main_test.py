import sys

from cadran import Cadran
from cerc import Cerc
from dreptunghi import Dreptunghi
from forma_geometrica import FormaGeometrica
from patrat import Patrat
from spatiu_de_lucru import SpatiuDeLucru
from triunghi import Triunghi


if __name__ == '__main__':
    lista_figuri = []

    with open(sys.argv[1], "rt", encoding="utf-8") as f:
        for line in f.readlines():
            words = line.split()
            if words[0] == 'cerc':
                cerc = Cerc(words[1], int(words[2]), int(words[3]), int(words[4]))
                lista_figuri.append(cerc)
            elif words[0] == 'dreptunghi':
                dreptunghi = Dreptunghi(words[1], int(words[2]), int(words[3]), int(words[4]), int(words[5]))
                lista_figuri.append(dreptunghi)
            elif words[0] == 'triunghi':
                triunghi = Triunghi(words[1], int(words[2]), int(words[3]), int(words[4]), int(words[5]), int(words[6]))
                lista_figuri.append(triunghi)
            elif words[0] == 'patrat':
                patrat = Patrat(words[1], int(words[2]), int(words[3]), int(words[4]))
                lista_figuri.append(patrat)
            else:
                spatiu = SpatiuDeLucru(int(words[0]), int(words[1]), int(words[2]), int(words[3]))

    with open(sys.argv[2], "wt", encoding="utf-8") as g:
        for figura in lista_figuri:
            cadran = spatiu.verificare_cadran(figura)
            if cadran == -1:
                lista_figuri.remove(figura)

        for figura in lista_figuri:
            g.write(figura.idul + " | ")
            sir = ""
            for aux in lista_figuri:
                if figura != aux:
                    coliziune = figura.detectare_coliziune(aux)
                    if coliziune:
                        g.write(aux.idul + " ")
            g.write(" | ")
            for aux in lista_figuri:
                semi_incluziune = figura.detectare_semi_incluziune(aux)
                if semi_incluziune:
                    g.write(aux.idul + " ")
            g.write(" | ")
            g.write(str(spatiu.verificare_cadran(figura)))
            g.write("\n")
