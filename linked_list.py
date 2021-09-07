class Nodo:
    def __init__(self, valor = None ):
        self.valor = valor
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertar(self, valor_nuevo):
        nuevo = Nodo(valor_nuevo)
        if self.head == None:
            self.head = nuevo
            return
        aux = self.head
        while(aux.siguiente != None):
            aux = aux.siguiente
        aux.siguiente = nuevo


    def remover(self, indice):
        pre = self.head
        k = 0
        while (k < int(indice)-1):
            pre = pre.sig
            k += 1
            
            if pre is None:
                print("Error: Index not found")
                return None
            
        borrar = pre.siguiente
        aft = borrar.siguiente
        pre.siguiente = aft
        return borrar
    
    
    def buscar(self, indice):
        aux = self.head
        k = 0
        while (k < int(indice)):
            aux = aux.sig
            k += 1
            
            if aux is None:
                print("Error: Index not found")
                return None
        return aux
    
    
    def printLinea(self):
        aux = self.head
        while aux is not None:
            print("Linea Numero: ", str(aux.valor.numero))
            print("-> Numero Componentes: ", str(aux.valor.componentes))
            print("-> Tiempo: ", str(aux.valor.tiempo))
            print("")
            aux = aux.siguiente
    
    
    def printProducto(self):
        aux = self.head
        while aux is not None:
            print("Nombre Producto: ", str(aux.valor.nombre))
            print("-> Elaboracion: ", str(aux.valor.elaboracion))
            print("")
            aux = aux.siguiente
    
    

            
                
        