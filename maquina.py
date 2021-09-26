import copy
import re
import os
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
        
    
    def reporteGraphviz(self, producto):
        aux = self.productos.head
        estadoInicial = copy.deepcopy(self.productos)
        while aux is not None:
            if aux.valor.nombre == producto:
                break
            aux = aux.siguiente
        
        pasos = LinkedList()
        
        lista_re = re.findall(r"L\w+", aux.valor.elaboracion)
        i = 0
        while i < len(lista_re):
            pasos.insertar(lista_re[i].replace("p",""))  
            i += 1
            
        temp = pasos.head
        cont = 0
        
        graphviz = '''
        digraph L{
            node[shape=box]

            subgraph cluster_p{
                label= "Pasos: ''' + producto +  ''' "

                '''
        ancla = "nodo0"
        while temp is not None:
            graphviz += '''nodo'''+str(cont)+'''[label = "'''+temp.valor+'''"]\n  '''
            if cont != 0:
                graphviz += "nodo"+str(cont-1)+"->"+"nodo"+str(cont) + '[label="        "]\n'
                graphviz += "{rank=same; "+ancla+"; nodo"+str(cont) + "}\n"
            cont +=1
            temp = temp.siguiente
        
        graphviz += '''        
            }
        }
        '''
        archivo = open('Reportes\\grafico.dot',"w+")
        archivo.write(graphviz)
        print("Archivo generado en: ", os.getcwd() +"\\Reportes\\grafico.png")
        archivo.close()

        os.system('dot -Tpng Reportes\\grafico.dot -o Reportes\\grafico.png')