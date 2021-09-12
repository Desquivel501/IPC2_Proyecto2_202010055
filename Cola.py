class Nodo:
    def __init__(self, valor = None):
        self.valor = valor
        self.siguiente = None
    
class Cola:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self,valor_nuevo):
        nuevo = Nodo(valor_nuevo)
        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo
        
    def dequeue(self):
        if self.head is not None:
            aux = self.head
            self.head = self.head.siguiente
            return aux
        else:
            return None
     
    def peek(self):
        return self.head
    
    def empty(self):
        if self.head is None:
            return True
        return False
    
class colaIntrucciones(Cola):
    def __init__(self, lineaProduccion, producto):
        Cola.__init__(self)
        self.lineaProduccion = lineaProduccion
        self.producto = producto
        self.componente_actual = 0
        self.parar = False
        self.ensamblando = False
        