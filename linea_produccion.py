class Linea_de_Produccion:
    
    def __init__(self,numero, componentes, tiempo):
        self.numero = numero
        self.componentes = componentes
        self.tiempo = tiempo
        
    def get_numero(self):
        return self.numero