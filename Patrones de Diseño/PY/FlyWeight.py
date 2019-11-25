class Felinos(object):
   def __init__(self):
      pass
   
   def especie(self, gene_code):
      return "Felino [%s]:" % (gene_code)
class Tipo(object):
   tipo = {}
   
   def __new__(cls, nombre, tipo_id):
      try:
         id = cls.tipo[tipo_id]
      except KeyError:
         id = object.__new__(cls)
         cls.tipo[tipo_id] = id
      return id
   
   def set_felino_info(self, felino_info):
      fl = Felinos()
      self.felino_info = fl.especie(felino_info)
   
   def get_felino_info(self):
      return (self.felino_info)

def lista():
   data = (('b', 1, 'Jaguar'), ('o', 2, 'Oselote'),('a', 1, 'Puma'))
   felinos_tip = []
   for i in data:
      obj = Tipo(i[0], i[1])
      obj.set_felino_info(i[2])
      felinos_tip.append(obj)
   
   for i in felinos_tip:
      print ("id = " + str(id(i)))
      print (i.get_felino_info())

if __name__ == '__main__':
   lista()
