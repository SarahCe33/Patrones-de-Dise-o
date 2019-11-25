'''                      Sarah Ramírez Cervantes
                        Patron de diseño Proxy        '''
class Inventario(object):
    items = None

    def __init__(self):
        self.items = []

    def __call__(self):
        return ' '.join(self.items) if self.items is not None else ''

    def Clave(self):
        self.items.append('1234')
        return self
    def Seccion(self):
        self.items.append('A1')
        return self
import operator

class Proxy(object):
    def __init__(self, some_object):
        self.some_object = some_object

    def __getattr__(self, name):
        self.method = operator.methodcaller(name)
        return self

    def __call__(self, *args, **kw):
        self.some_object = self.method(self.some_object, *args, **kw)
        return self

    def perform(self):
        return self.some_object()
    
vestidos = Inventario()
pro= Proxy(vestidos)
print (pro.Clave().Seccion().perform())
