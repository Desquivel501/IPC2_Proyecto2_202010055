class Nodo:
    def __init__(self, valor = None):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.head = None
    
    def push(self,valor_nuevo):
        nuevo = Nodo(valor_nuevo)
        if self.head is None:
            self.head = nuevo.siguiente

        else:
            nuevo.siguiente = self.head
            self.head = nuevo
    
    def pop(self):
        if self.head is not None:
            aux = self.head
            self.head = self.head.siguiente
            return aux
        else:
            return None
    
    def peek(self):
        return self.head