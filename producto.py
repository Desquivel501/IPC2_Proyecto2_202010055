from linked_list import LinkedList, listaInstrucciones
from Cola import colaIntrucciones
from analizador import Analizador
import re

class Producto:
    
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion
        
        
        scanner = Analizador(self.nombre)
        self.listaElaboracion = scanner.analizar(elaboracion)
        scanner.print()

    
    def algoritmo(self):
        
        ordenEnsambleje = self.getOrden()
        ensambleActual = ordenEnsambleje.head
        
        print('Produciendo... "' + self.nombre +'" ')
        
        
        terminado = False
        parar = False
        segundo = 1
        lineaEnsamblando = 0

        
        while terminado is False:
            print("Segundo: ", str(segundo))
            lineaActual = self.listaElaboracion.head
            
            detener_next = False
            if parar is True:
                detener_next = True
            
            
            while lineaActual is not None:
                if lineaActual.valor.empty():
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Operacion Concluida")
                        lineaActual = lineaActual.siguiente
                        continue
                
                # if lineaActual.valor.parar == True is True and lineaActual.valor.listaElaboracion != ensambleActual:
                #     print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Detenida")
                #     lineaActual = lineaActual.siguiente
                #     continue
                    
                
                if detener_next is False:
                    
                    objetivo = lineaActual.valor.peek()
                    objetivo_int = int(objetivo.valor.replace('C',""))
                    
                    
                    if lineaActual.valor.empty() is False:
                        if lineaActual.valor.componente_actual < objetivo_int:
                            lineaActual.valor.componente_actual += 1
                            print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Mover Brazo - Componente ", str(lineaActual.valor.componente_actual))
                            
                            if lineaActual.valor.componente_actual == objetivo_int:
                                lineaEnsamblando = lineaActual.valor.lineaProduccion
                                lineaActual.valor.parar = True
                                parar = True
                                                        
                        elif lineaActual.valor.componente_actual > objetivo_int:
                            lineaActual.valor.componente_actual -= 1
                            print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Mover Brazo - Componente ", str(lineaActual.valor.componente_actual))
                            
                            if lineaActual.valor.componente_actual == objetivo_int:
                                lineaEnsamblando = lineaActual.valor.lineaProduccion
                                lineaActual.valor.parar = True
                                parar = True
                            
                        elif lineaActual.valor.componente_actual == objetivo_int:
                            lineaActual.valor.dequeue()
                            print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Ensamblado - Componente ", str(lineaActual.valor.componente_actual))
                
                
                else:
                    if lineaActual.valor.lineaProduccion == lineaEnsamblando:
                        lineaActual.valor.dequeue()
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Ensamblando - Componente ", str(lineaActual.valor.componente_actual))
                        parar=False
                        lineaActual.valor.parar == False
                    else:
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Detenida")
                
                lineaActual = lineaActual.siguiente
                    
                    
                
            
            segundo += 1
            print("")
            
            
            stop = True
            comprobacion = self.listaElaboracion.head
            while comprobacion is not None:
                if comprobacion.valor.empty() is False:
                    stop = False
                comprobacion = comprobacion.siguiente
            if stop:
                terminado = True
        print("")
            
    
    def getOrden(self):
        lista = LinkedList()                    
        lista_re = re.findall(r"L[0-9]", self.elaboracion)
        
        i = 0
        while i < len(lista_re):
            lista.insertar(lista_re[i].replace("L","0"))  
            i += 1
            
        return lista
                      
            
    