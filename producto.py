from linked_list import LinkedList, listaInstrucciones
from Cola import colaIntrucciones
from analizador import Analizador
import re
from linea_produccion  import Linea_de_Produccion

class Producto:
    
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion
        
        
        scanner = Analizador(self.nombre)
        self.listaElaboracion = scanner.analizar(elaboracion)
        scanner.print()

    
    def algoritmo(self, lineas):
        self.getTiempo(lineas)
        
        ordenEnsambleje = self.getOrden()
        ensambleActual = ordenEnsambleje.head
        
        print('Produciendo... "' + self.nombre +'" ')
         
        terminado = False
        segundo = 1

        while terminado is False:
            print("Segundo: ", str(segundo))
            
            lineaActual = self.listaElaboracion.head
            done = False
            wait = False 
            
            temp = self.listaElaboracion.head
            while temp is not None:
                if temp.valor.parar:
                    wait = True
                temp = temp.siguiente
            
            while lineaActual is not None:
                if lineaActual.valor.empty():
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Operacion Concluida")
                        lineaActual = lineaActual.siguiente
                        continue
                
                elif lineaActual.valor.parar and lineaActual.valor.lineaProduccion != int(ensambleActual.valor):
                    print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Detenida")
                    lineaActual = lineaActual.siguiente
                    continue
                
                elif wait and lineaActual.valor.lineaProduccion != int(ensambleActual.valor):
                    print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Detenida")
                    lineaActual = lineaActual.siguiente
                    continue
                
                    
                elif lineaActual.valor.parar is False:
                    
                    objetivo = lineaActual.valor.peek()
                    objetivo_int = int(objetivo.valor.replace('C',""))
                    
                    
                    if lineaActual.valor.componente_actual < objetivo_int:
                        lineaActual.valor.componente_actual += 1
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Mover Brazo - Componente ", str(lineaActual.valor.componente_actual))
                            
                        if lineaActual.valor.componente_actual == objetivo_int:
                            lineaActual.valor.parar = True
                            lineaActual.valor.ensamblando = int(lineaActual.valor.costo)
                                                        
                    elif lineaActual.valor.componente_actual > objetivo_int:
                        lineaActual.valor.componente_actual -= 1
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Mover Brazo - Componente ", str(lineaActual.valor.componente_actual))
                            
                        if lineaActual.valor.componente_actual == objetivo_int:
                            lineaActual.valor.parar = True
                            lineaActual.valor.ensamblando = int(lineaActual.valor.costo)
                            
                    elif lineaActual.valor.componente_actual == objetivo_int:
                        lineaActual.valor.dequeue()
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Ensamblado - Componente ", str(lineaActual.valor.componente_actual))
                
                
                elif lineaActual.valor.parar and lineaActual.valor.lineaProduccion == int(ensambleActual.valor):
                    if lineaActual.valor.lineaProduccion == int(ensambleActual.valor):
                        
                        
                        lineaActual.valor.ensamblando -= 1
                        
                        if int(lineaActual.valor.ensamblando) == 0:
                            lineaActual.valor.dequeue()
                            print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Ensamblando - Componente ", str(lineaActual.valor.componente_actual))
                            lineaActual.valor.parar = False
                            done = True
                        
                        else:
                            print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Ensamblando - Componente ", str(lineaActual.valor.componente_actual))
                            
                    else:
                        print("Linea: ", str(lineaActual.valor.lineaProduccion) ," - Detenida")
                
                lineaActual = lineaActual.siguiente
                    
            segundo += 1
            print("")
            
            if done:
                ensambleActual = ensambleActual.siguiente
            
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
    
    
    def getTiempo(self, lineas):
        objetoLinea = lineas.head
        lineaActual = self.listaElaboracion.head
        
        while lineaActual is not None:
            while objetoLinea is not None:
                if int(objetoLinea.valor.numero) == int(lineaActual.valor.lineaProduccion):
                    lineaActual.valor.costo = objetoLinea.valor.tiempo
                objetoLinea = objetoLinea.siguiente
            lineaActual = lineaActual.siguiente

                      
            
    