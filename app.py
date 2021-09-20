from tkinter.constants import END
from typing import Text
from producto import Producto
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from linked_list import LinkedList, listaProductos, listaLineas
from linea_produccion import Linea_de_Produccion as LP
from producto import Producto
from maquina import Maquina
import time


import tkinter as tk
import tkinter.ttk as ttk
import Pmw
from tkinter import messagebox

nombreProducto = ""

def leerMaquina():
    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()
    
    no_lineas = root.find("CantidadLineasProduccion").text
    lineas = listaLineas()
    productos = listaProductos()
    
    
    row = 0
 
    frame_labels = tk.Frame(canvas1)
    
    label = tk.Label(frame_labels, text="Datos Maquina", font = "Arial 16 bold", anchor="w").grid(row=row,column=0, sticky="w")
    row += 1
    label = tk.Label(frame_labels, text=("Numero de lineas: " + str(no_lineas)), font = "Arial 12 bold").grid(row=row,column=0, sticky="w")
    row += 1
    
    label = tk.Label(frame_labels, text=" ").grid(row=row,column=0, sticky="w")
    row += 1
    
    for linea in root.findall("ListadoLineasProduccion"):
        for j in linea.findall("LineaProduccion"):
            lineas.insertar( LP(j.find("Numero").text, j.find("CantidadComponentes").text, j.find("TiempoEnsamblaje").text) )
            
            label = tk.Label(frame_labels, text=("Linea de Produccion " + str(j.find("Numero").text)), font = "Arial 12 bold").grid(row=row,column=0, sticky="w")
            row += 1
            label = tk.Label(frame_labels, text= ("-> Cantidad componentes: " + str(j.find("CantidadComponentes").text)), font = "Arial 12 bold").grid(row=row,column=0, sticky="w")
            row += 1
            label = tk.Label(frame_labels, text= ("-> Tiempo de Ensamblaje: " + str(j.find("TiempoEnsamblaje").text) + " s"), font = "Arial 12 bold").grid(row=row,column=0, sticky="w")
            row += 1
    
    label = tk.Label(frame_labels, text=" ").grid(row=row,column=0, sticky="w")
    row += 1
    
    for producto in root.findall("ListadoProductos"):   
        for j in producto.findall("Producto"):
            productos.insertar(Producto(j.find("nombre").text, j.find("elaboracion").text))
            label = tk.Label(frame_labels, text=("Nombre del Producto: " + str(j.find("nombre").text)), font = "Arial 12 bold").grid(row=row,column=0, sticky="w")
            row += 1
            label = tk.Label(frame_labels, text= ("-> Pasos: " + str(j.find("elaboracion").text)), font = "Arial 12 bold").grid(row=row,column=0, sticky="w")
            row += 1
            
    canvas1.create_window((0,0), window=frame_labels, anchor=tk.NW)
    frame_labels.update_idletasks()
    
    bbox1 = canvas1.bbox("all")
    canvas1.configure(scrollregion=bbox1, width=320, height=345)
    
    global Maquina_Actual   
    Maquina_Actual = Maquina(no_lineas,lineas,productos)
    
    
def elaborarProducto():
    
    nombre = cb_productos.get()
    
    for widget in canvas.winfo_children():
        widget.destroy()
        
    global Maquina_Actual
    pasos = Maquina_Actual.encender(nombre)
        
    largo = int(pasos.head.valor.largo) +1
    print(str(largo))
        
    frame_buttons = tk.Frame(canvas)
        
    lbl = tk.Label(frame_buttons, text=("Producto: " + nombre), font = "Arial 14 bold",  anchor="nw", justify="left")
    lbl.grid(row=0,column=0, columnspan=largo)
        
    lbl = tk.Label(frame_buttons, text=("Segundo"), font = "Arial 12 bold",  anchor="w")
    lbl.grid(row=1,column=0)
        
    noLinea = 1
    aux = pasos.head.valor.head
    aux = aux.siguiente
    while aux is not None:
        lbl = tk.Label(frame_buttons, text=("Linea " + str(noLinea)), font = "Arial 12 bold",  anchor="w")
        lbl.grid(row=1,column=noLinea)
        noLinea += 1
        aux = aux.siguiente

    fila = pasos.head
        
    noFila = 2
    noColumna = 0
        
    while fila is not None:
        columna = fila.valor.head
        while columna is not None:
            
            lbl = tk.Label(frame_buttons, text=(columna.valor), font = "Arial 12",  anchor="w")
            lbl.grid(row=noFila,column=noColumna, pady=10, padx=8)
            noColumna += 1
            columna = columna.siguiente
        noFila += 1
        noColumna = 0
        fila = fila.siguiente
        
    canvas.create_window((0,0), window=frame_buttons, anchor=tk.NW)
    frame_buttons.update_idletasks()
    
    bbox = canvas.bbox("all")
    canvas.configure(scrollregion=bbox, width=560, height=500)

    
def leerSimulacion():
    global listadoProductos
    listadoProductos = LinkedList()
        
    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()
        
    for linea in root.findall("ListadoProductos"):
        for producto in linea.findall("Producto"):
                
            listadoProductos.insertar(producto.text)
                
    first = True
    aux = listadoProductos.head
    while aux is not None:
        if first:
            cb_productos['values'] = aux.valor
            first = False
        else:
            cb_productos['values'] = (cb_productos['values'], aux.valor)
        aux = aux.siguiente
    

def iniciarSimulacion():
    
    for widget in canvas.winfo_children():
        widget.destroy()
    
    global Maquina_Actual
    global listadoProductos
    pasos = Maquina_Actual.simulacion(listadoProductos)  
    
    productoActual = pasos.head
    noFila = 0
    noColumna = 0
    frame_buttons = tk.Frame(canvas)
    
    while productoActual is not None:
        
        largo = int(productoActual.valor.head.valor.largo) + 1
        
        lbl = tk.Label(frame_buttons, text=("Producto: " + productoActual.valor.x), font = "Arial 14 bold",  anchor="nw", justify="left")
        lbl.grid(row=noFila,column=0, columnspan=largo)
        noFila += 1
        
        lbl = tk.Label(frame_buttons, text=("Segundo"), font = "Arial 12 bold",  anchor="w")
        lbl.grid(row=noFila,column=0)
        
        aux = productoActual.valor.head.valor.head
        aux = aux.siguiente
        noLinea = 1
        while aux is not None:
            lbl = tk.Label(frame_buttons, text=("Linea " + str(noLinea)), font = "Arial 12 bold",  anchor="w")
            lbl.grid(row=noFila,column=noLinea)
            noLinea += 1
            aux = aux.siguiente
        noFila += 1
        
        fila = productoActual.valor.head
        
        while fila is not None:
            columna = fila.valor.head
            while columna is not None:
                lbl = tk.Label(frame_buttons, text=(columna.valor), font = "Arial 12",  anchor="w")
                lbl.grid(row=noFila,column=noColumna, pady=10, padx=8)
                noColumna += 1
                columna = columna.siguiente
            noFila += 1
            noColumna = 0
            fila = fila.siguiente
        noColumna = 0
        
        lbl = tk.Label(frame_buttons, text="", font = "Arial 12",  anchor="w")
        lbl.grid(row=noFila,column=noColumna, pady=10, padx=8)
        noFila += 1
        
        productoActual = productoActual.siguiente
        
    canvas.create_window((0,0), window=frame_buttons, anchor=tk.NW)
    frame_buttons.update_idletasks()
    
    bbox = canvas.bbox("all")
    canvas.configure(scrollregion=bbox, width=560, height=500)
    
           
def info():
    texto = '''Derek Esquivel Diaz
Carnet: 202010055
Introduccion a la programacion y computacion 2 "B"
Ingenieria en Ciencias y Sistemas
4to Semestre'''
    messagebox.showinfo(message=texto, title="Acerca de...")


if __name__ == '__main__':
    
    window = tk.Tk()
    window.geometry("1000x585")
    window.title("Digital Intelligence, S. A.")
    window.resizable(width=False, height=False)
    
    menubar = tk.Menu(window)
    window.config(menu=menubar)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Cargar Maquina", command=leerMaquina)
    filemenu.add_command(label="Cargar Simulacion", command= leerSimulacion)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=window.quit)
    
    reportmenu = tk.Menu(menubar, tearoff=0)
    reportmenu.add_command(label="Reporte HTML")
    reportmenu.add_command(label="Reporte Graphviz")

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...", command = info)

    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Reporte", menu=reportmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
        
        
    fr_main = tk.Frame(window, width=980, height=560, relief=tk.GROOVE, bd=2)
    fr_main.place(x = 10, y = 10)
    
    
    label = tk.Label(fr_main, text="Producto:", font = "Arial 16 bold"). place(x = 45, y = 30)
        
    cb_productos = ttk.Combobox(fr_main, values=[], width=20, font = "Arial 16 bold")
    cb_productos.place(x = 45, y = 60)
    cb_productos.bind("<<ComboboxSelected>>")
    
    btn_elaborar = tk.Button(fr_main, text="Elaborar", width=21, font = "Arial 14 bold", bg='#ff9999', command=elaborarProducto)
    btn_elaborar.place(x = 45, y = 100)
    

    
    
    fr_maquina = tk.Frame(fr_main, width=320, height=345, relief=tk.GROOVE, bd=2)
    fr_maquina.place(x = 10, y = 165)

    frame_maquina = tk.Frame(fr_maquina,  width=320, height=345)
    frame_maquina.grid(row=2, column=0, pady=(5, 0), sticky='nw')

    # Add a canvas in that frame
    canvas1 = tk.Canvas(frame_maquina, width=320, height=345)
    canvas1.grid(row=0, column=0, sticky="news")

    # Link a scrollbar to the canvas
    vsb1 = tk.Scrollbar(frame_maquina, orient="vertical", command=canvas1.yview)
    vsb1.grid(row=0, column=1, sticky='ns')
    canvas1.configure(yscrollcommand=vsb1.set)
    
    hsbar2 = tk.Scrollbar(frame_maquina, orient="horizontal", command=canvas1.xview)
    hsbar2.grid(row=1, column=0, sticky=tk.EW)
    canvas1.configure(xscrollcommand=hsbar2.set)

    
    
  
  
  
    fr_pasos = tk.Frame(fr_main, width=560, height=500, relief=tk.GROOVE, bd=2)
    fr_pasos.place(x = 360, y = 10)
    
    frame_canvas = tk.Frame(fr_pasos, width=560, height=500,)
    frame_canvas.grid(row=3, column=0, pady=(5, 0), sticky='nw')

    
    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, width=560, height=500,)
    canvas.grid(row=0, column=0, sticky="news")

    # Link a scrollbar to the canvas
    vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    
    hsbar = tk.Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=tk.EW)
    canvas.configure(xscrollcommand=hsbar.set)


    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    # tv = ttk.Treeview(fr_pasos)
    # tv['columns']=('Rank', 'Name', 'Badge')
    # tv.column('#0', width=0, stretch="no")
    # tv.column('Rank', width=80)
    # tv.column('Name',  width=80)
    # tv.column('Badge',  width=80)

    # tv.heading('#0', text='' )
    # tv.heading('Rank', text='Id', )
    # tv.heading('Name', text='rank')
    # tv.heading('Badge', text='Badge')

    # tv.pack()
    
    # tv = ttk.Treeview(fr_pasos)
    # tv['columns']=('Rank', 'Name', 'Badge')
    # tv.column('#0', width=0, stretch="no")
    # tv.column('Rank', width=80)
    # tv.column('Name',  width=80)
    # tv.column('Badge',  width=80)

    # tv.heading('#0', text='' )
    # tv.heading('Rank', text='Id', )
    # tv.heading('Name', text='rank')
    # tv.heading('Badge', text='Badge')

    # tv.pack()
    
    # tv = ttk.Treeview(fr_pasos)
    # tv['columns']=('Rank', 'Name', 'Badge')
    # tv.column('#0', width=0, stretch="no")
    # tv.column('Rank', width=80)
    # tv.column('Name',  width=80)
    # tv.column('Badge',  width=80)

    # tv.heading('#0', text='' )
    # tv.heading('Rank', text='Id', )
    # tv.heading('Name', text='rank')
    # tv.heading('Badge', text='Badge')

    # tv.pack()
    
    
    
    # # t = tk.Table(fr_pasos)
    
    # # scrollbar = tk.Scrollbar(fr_pasos)
    # # scrollbar.pack(side="right", fill="y")
    

    # # scrollbar.config(command=listbox.yview)
    


    
    # fr_velocidad = tk.Frame(fr_main, width=320, height=40, relief=tk.GROOVE, bd=2)
    # fr_velocidad.place(x = 10, y = 480)
    
    # Pmw.initialise()

    # horiz = Pmw.RadioSelect(fr_velocidad,
    # labelpos = 'w',
    # label_text = 'Horizontal',
    # frame_borderwidth = 2,
    # frame_relief = 'ridge'
    # )
    # horiz.pack(fill = 'x', padx = 10, pady = 10)
    
    # for text in ('Fruit', 'Vegetables', 'Cereals', 'Legumes'):
    #     horiz.add(text)
    # horiz.invoke('Cereals')
    
    window.mainloop()



    
    