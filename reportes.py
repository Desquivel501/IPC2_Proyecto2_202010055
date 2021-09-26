import os
from lxml import etree

class ReporteHtml:
   
    def __init__(self,nombre,pasos):
        self.nombre = nombre
        self.pasos = pasos
       
    def generarHtml(self):
        largo = self.pasos.largo
        html = '''
        <!doctype html>
        <html lang="en">
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">

                <title>Producto: ''' + self.nombre +'''</title>
            </head>
            <body>
                <p>&nbsp;</p>
                <h1 style="text-align: center;">Producto: ''' + self.nombre +'''</h1>
                <p>&nbsp;</p>
                
                 <table style="height: 108px; width: 80%; border-collapse: collapse; margin-left: auto; margin-right: auto;" class="table table-hover table-striped">
                    <thead class="thead-dark">
                        <tr style="height: 18px;">
                            <th><strong>Segundo</strong></th>'''               
        
        noLinea = 1
        aux = self.pasos.head.valor.head
        aux = aux.siguiente
        while aux is not None:
            html += f"<th><strong>Linea {aux.linea}</strong></th>"
            noLinea += 1
            aux = aux.siguiente  
            
        html += '''
                        </tr> 
                    </thead>
                    <tbody>
                    
        '''                
        
        fila = self.pasos.head
        while fila is not None:
            html += '<tr style="height: 18px;">'
            columna = fila.valor.head
            while columna is not None:
                html += '<td>' + columna.valor +'</span></td>'
                columna = columna.siguiente  
            html += '</tr>'
            fila = fila.siguiente                    
                            
        html += '''     
                </tbody>    

                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns" crossorigin="anonymous"></script>
            
            </body>
        </html>
        
        ''' 
        
        cwd = os.getcwd()
        archivo = open('Reportes\\Reporte.html',"w+")
        archivo.write(html)
        print("Se ha generado el reporte en: " + cwd + "\\Reportes\\Reporte.html")
        archivo.close()
    
class reporteXml:
    
    def __init__(self, nombre, pasos, NombreSimulacion):
        self.nombre = nombre
        self.pasos = pasos
        self.NombreSimulacion = NombreSimulacion
    
    def generarXml(self):
        root = etree.Element('SalidaSimulacion')
        tree = etree.ElementTree(root)
        
        nombreSimulacion = etree.Element('Nombre')
        nombreSimulacion.text = str(self.NombreSimulacion)
        root.append(nombreSimulacion)
        
        listadoProductos = etree.Element('ListadoProductos')
        root.append(listadoProductos)
        
        producto = etree.Element('Producto')
        listadoProductos.append(producto)
        
        nombreProducto = etree.Element('Nombre')
        nombreProducto.text = str(self.nombre)
        producto.append(nombreProducto)

        tiempo = self.pasos.largo + 1
        tiempoTotal = etree.Element('TiempoTotal')
        tiempoTotal.text = str(tiempo)
        producto.append(tiempoTotal)
        
        ElaboracionOptima = etree.Element('ElaboracionOptima')
        producto.append(ElaboracionOptima)
        
    
        fila = self.pasos.head
        while fila is not None:
            cont = 1
            columna = fila.valor.head
            tiempo = etree.Element('Tiempo')
            tiempo.set('NoSegundo', columna.valor)
            ElaboracionOptima.append(tiempo)
            columna = columna.siguiente
            
            while columna is not None:
                lineaEnsamblaje = etree.Element('lineaEnsamblaje')
                lineaEnsamblaje.set('NoLinea', str(columna.linea))
                lineaEnsamblaje.text = str(columna.valor).replace(">", "")
                tiempo.append(lineaEnsamblaje)
                cont += 1
                columna = columna.siguiente
                
            fila = fila.siguiente

        
        
        try:
            cwd = os.getcwd()
            filename = cwd + '\\Reportes\\Reporte.xml'
            tree.write(filename, pretty_print=True)
            print("El archivo se ha generado exitosamente")
        except Exception as e:
            print("ERROR: ",e)
            