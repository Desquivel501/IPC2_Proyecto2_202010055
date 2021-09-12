

class Maquina:
    
    def __init__(self, no_lineas, lineas, productos):
        self.no_lineas = no_lineas
        self.lineas = lineas
        self.productos = productos
        
    def get_no_lineas(self):
        return self.no_lineas
    
    def get_lineas(self):
        return self.lineas
    
    def get_productos(self):
        return self.productos
    
    def printMaquina(self):
        i = 1
        print("Maquina ", str(i))
        print("CantidadLineasProduccion: ", str(self.no_lineas))
        print("")
        print("ListadoLineasProduccion: ")
        self.lineas.printLinea()
        print("ListadoProductos: ")
        self.productos.printProducto()
    
    def encender(self):
        aux = self.productos.head
        while aux is not None:
            aux.valor.algoritmo()
            aux = aux.siguiente
        
    