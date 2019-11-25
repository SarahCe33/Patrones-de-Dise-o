'''          Sarah Ramirez Cervantes GITI11071-E
               Patron de diseño Medieator              '''

print("     /---------------------------")
print("    /        /\_/\              /|")
print("   /        (>’.’<)   /\_/\    / |")
print("  /------------------(>’.’<)--/  |")
print("  |     Cats in the Box       |  /")
print("  |                           | /")
print("  |---------------------------|/")
print("")
print("")

class Caja(object):
    
    def entrar(self, mascota,  message):
        print("[{}]: {}".format( mascota, message))
        
        
'''A class whose instances want to interact with each other.'''

class Mascota (object):
    def __init__(self, name):
        self.name = name
        self.caja= Caja()
 
    def dormir(self, message):
        self.caja.entrar(self, message)
        
    def __str__(self):
        return self.name

        
class Gato (Mascota):
    def mauyar(self):
        pass


class Perro(Mascota):
    def ladrar(self):
        pass
 
salem = Gato('Salem')
darsy = Gato('Darsy')
zuzu = Gato('Zuzu')
rocko = Perro('Rocko')


salem.dormir("Entro a la caja")
darsy.dormir("Entro a la caja")
rocko.dormir("Entro a la caja")
salem.dormir("Salio  a la caja")
darsy.dormir("Salio de la caja")
zuzu.dormir("Entro a la caja")
