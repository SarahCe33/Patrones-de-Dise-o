'''                      Sarah Ramírez Cervantes
                        Patron de diseño Observer        '''
class Gato(object):
    def __init__(self, name):
        self.name = name
        
    def alimentar(self, mensaje):
        print('Llamar a {} "{}"'.format(self.name, mensaje))
        
    def mishi(self, mensaje):
        print('Llamar a {} "{}"'.format(self.name, mensaje))
        
class Rescatista(object):
    def __init__(self):
        self.gatos = set()
        
    def llamar(self, cual):
        self.gatos.add(cual)
        
    def regalar(self, cual):
        self.gatos.discard(cual)
        
    def alimentar(self, mensaje):
        for gato in self.gatos:
            gato.alimentar(mensaje)
    def alimentar(self, mensaje):
        for gato in self.gatos:
            gato.mishi(mensaje)        
rescatista = Rescatista()
            
salem = Gato('Salem')
darsy = Gato('Darsy')
zuzu = Gato('Zuzu')
anvorgueso = Gato('Anvorgueso')

rescatista.llamar(salem)
rescatista.llamar(darsy)
rescatista.llamar(zuzu)
rescatista.llamar(anvorgueso)

rescatista.alimentar("Hora de comer!")

rescatista.regalar(anvorgueso)

print("")

rescatista.alimentar("Mishi mishi!")

