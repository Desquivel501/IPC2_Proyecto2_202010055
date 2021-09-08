from linked_list import LinkedList

class Producto:
    
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        
        self.elaboracion = LinkedList()
        aux = elaboracion.split(" ")
        for i in aux:
            self.elaboracion.insertar(i.replace("p",""))
        
        
    