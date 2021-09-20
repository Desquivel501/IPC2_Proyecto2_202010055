import copy
from linked_list import LinkedList

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
    
    def encender(self, producto):
        aux = self.productos.head
        estadoInicial = copy.deepcopy(self.productos)
        proceso = None
        while aux is not None:
            if aux.valor.nombre == producto:
                proceso = aux.valor.algoritmo(self.lineas)
            aux = aux.siguiente
        
        self.productos = estadoInicial
        
        return proceso
        
    def simulacion(self, listaProductos):
        estadoInicial = copy.deepcopy(self.productos)
        producto = listaProductos.head
        proceso = LinkedList()
        
        while producto is not None:
            aux = self.productos.head
            while aux is not None:
                if aux.valor.nombre == producto.valor:
                    proceso.insertar(aux.valor.algoritmo(self.lineas))
                aux = aux.siguiente
            producto = producto.siguiente
        
        self.productos = estadoInicial
        return proceso
        
        
        
    