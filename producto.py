from linked_list import LinkedList

class Producto:
    
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion
        
    def parse_elaboracion(self):
        lista = LinkedList()
        