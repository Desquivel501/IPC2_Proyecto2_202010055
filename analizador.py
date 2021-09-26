
from linked_list import LinkedList
from Cola import colaIntrucciones

class Analizador:
    
    def __init__(self, producto):
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0
        self.IntruccionesPorLinea = LinkedList()
        self.producto = producto
        self.lineaActual = None
    
    def analizar(self, cadena):
        self.IntruccionesPorLinea = LinkedList()
        
        self.i = 0
        
        while self.i < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.i])
            elif self.estado == 1:
                self.estado1(cadena[self.i])
            elif self.estado == 2:
                self.estado2(cadena[self.i])
            self.i += 1
        
        self.lineaOrdenada = LinkedList()
        
        return self.IntruccionesPorLinea
                

    def estado0(self, caracter):
        if caracter.upper() == "L":
            self.columna += 1
            self.estado = 1
        
        elif caracter.upper() == "C":
            self.buffer += "C"
            self.columna += 1
            self.estado = 2
        
        else:
            self.columna += 1
            
    
    def estado1(self,caracter):
        linea = int(caracter)
        aux = self.IntruccionesPorLinea.head
        found = False
        while aux is not None:
            if aux.valor.lineaProduccion == linea:
                self.lineaActual = aux.valor
                found = True
            aux = aux.siguiente
        if found is False:
            self.lineaActual = colaIntrucciones(linea,self.producto)

        self.columna += 1
        self.estado = 0
    
    def estado2(self,caracter):
        if caracter.isdigit():
            self.buffer += str(caracter)
            self.lineaActual.enqueue(self.buffer)
            
            found = False
            
            aux = self.IntruccionesPorLinea.head
            while aux is not None:
                if aux.valor.lineaProduccion == self.lineaActual.lineaProduccion:
                    aux.valor = self.lineaActual
                    found = True
                aux = aux.siguiente
            if found is False:
                self.IntruccionesPorLinea.insertarEnOrden(self.lineaActual)
               
            self.buffer = ""
            self.columna +=1   
            self.estado = 0
                     

    def print(self):
        print("Producto: ",self.producto)
        aux = self.IntruccionesPorLinea.head         
        while aux is not None:
            print("Linea: ",aux.valor.lineaProduccion)
            temp = aux.valor.head
            while temp is not None:
                print(temp.valor, end=" ")
                temp = temp.siguiente
            print("")
            aux = aux.siguiente
        print("")
            