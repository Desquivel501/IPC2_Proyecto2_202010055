class Nodo:
    def __init__(self, valor = None ):
        self.valor = valor
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.largo = 0
        self.x = None
    
    def insertar(self, valor_nuevo):
        nuevo = Nodo(valor_nuevo)
        if self.head == None:
            self.head = nuevo
            return
        aux = self.head
        while(aux.siguiente != None):
            aux = aux.siguiente
        aux.siguiente = nuevo
        self.largo += 1


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
        self.largo -= 1
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
    
    
class listaProductos(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        
    def printProducto(self):
        aux = self.head
        while aux is not None:
            print("Nombre Producto: ", str(aux.valor.nombre))
            print("-> Elaboracion: ", str(aux.valor.elaboracion))
            print("")
            aux = aux.siguiente
            
    
      

class listaLineas(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
    
    def printLinea(self):
        aux = self.head
        while aux is not None:
            print("Linea Numero: ", str(aux.valor.numero))
            print("-> Numero Componentes: ", str(aux.valor.componentes))
            print("-> Tiempo: ", str(aux.valor.tiempo))
            print("")
            aux = aux.siguiente           
                

class listaInstrucciones(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
    
    def printElaboracion(self):
        aux = self.head
        pasos = ""
        while  aux is not None:
            pasos += aux.valor
            pasos += " "
            aux = aux.siguiente
        return pasos
    
