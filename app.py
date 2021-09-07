from producto import Producto
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from linked_list import LinkedList 
from linea_produccion import Linea_de_Produccion as LP
from producto import Producto
from maquina import Maquina

if __name__ == '__main__':
    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()
    maquinas = LinkedList()
    
    no_lineas = root.find("CantidadLineasProduccion").text
    lineas = LinkedList()
    productos = LinkedList()
    
    
    for linea in root.findall("ListadoLineasProduccion"):
        for j in linea.findall("LineaProduccion"):
            lineas.insertar( LP(j.find("Numero").text, j.find("CantidadComponentes").text, j.find("TiempoEnsamblaje").text) )
    
    for producto in root.findall("ListadoProductos"):   
        for j in producto.findall("Producto"):
            productos.insertar( Producto(j.find("nombre").text, j.find("elaboracion").text))
            
    Maquina_Actual = Maquina(no_lineas,lineas,productos)

    Maquina_Actual.printMaquina()