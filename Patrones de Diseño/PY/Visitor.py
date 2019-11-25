'''                      Sarah Ramírez Cervantes
                        Patron de diseño Visitor        '''
from __future__ import generators
import random


class Coral(object):
    def aceptar(self, visitor):
        visitor.visit(self)
    def habitar(self, pez):
        print(self, "Habitante: ", pez)
    def comer(self, depredador):
        print(self, "Comido por: ", depredador)
    def __str__(self):
        return self.__class__.__name__
# ---------------  Corales   ---------------------

class AcroporaPalmata(Coral):
    pass
class ColpophylliaNatans(Coral):
    pass
class StylasterRoseus(Coral):
    pass


# ---------------  Visitor  ---------------------
class Visitor:
    def __str__(self):
        return self.__class__.__name__

# -----------------------------------------------
class CriaturaMarina(Visitor): pass
class Pez(CriaturaMarina): pass
class Depredador(CriaturaMarina): pass

class Mandarin(Pez):
    def visit(self, coral):
        coral.habitar(self)

class Payaso(Pez):
    def visit(self, coral):
        coral.habitar(self)


class EstrellaMar(Depredador):
    def visit(self, coral):
        coral.comer(self)

def CoralH(n):
    corales = Coral.__subclasses__()
    for i in range(n):
        yield random.choice(corales)()


payaso = Payaso()
mandarin = Mandarin()
estrella = EstrellaMar()
for coral in CoralH(4):
    coral.aceptar(payaso)
    coral.aceptar(mandarin)
    coral.aceptar(estrella)
