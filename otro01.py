class nodo:
    def __init__(self,id):
         self.id:int = id     #Instanciar las coordenadas
         self.siguiente = None #Lo de las listas de siiempre
         self.anterior = None
         self.acceso = None
class arbol: #Arbol de posibles recorridos
   def __init__(self,caracter):
       self.derecha = None
       self.izquierda = None
       self.arriba = None
       self.abajo = None
       self.caracter = caracter