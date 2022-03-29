from otro01 import nodo
class ListaEncabezado:
    def __init__(self,tipo) :  # METODO DE INICIO
        self.primero:nodo = None
        self.ultimo:nodo = None
        self.tipo = tipo
        self.size = 0
    def InsertarEncabezado(self,nuevo):
        self.size += 1 #Agranda la lista en uno
        if self.primero == None: #Verifica si la lista esta vacia
            self.primero = self.ultimo = nuevo #Inserta un nuevo elemento
        else:
            if nuevo.id < self.primero.id : #Revisa la posicion
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo #Inserta al principio
            elif nuevo.id > self.ultimo.id :
                self.ultimo.siguiente = nuevo #Inserta al final
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                temp:nodo = self.primero #Inserta en el medio recorriendo las filas
                while temp != None:
                    if nuevo.id < temp.id:
                        nuevo.siguiente = temp
                        nuevo.anterior = temp.anterior
                        temp.anterior.siguiente = nuevo
                        temp.anterior = nuevo
                        break
                    elif nuevo.id > temp.id:
                        temp = temp.siguiente
                    else:
                        break

    def MostrarEncabezados(self):
        temp = self.primero
        while temp != None:
            print ("Encabezado ",self.tipo, temp.id ) #Imprime los encabezados
            temp = temp.siguiente

    def getEncabezados (self,id) -> nodo: #Recorre hasta encontrar el deseado, busacndo por id
        temp = self.primero
        while temp != None:
            if id == temp.id:
                return (temp)
            else:
                temp = temp.siguiente
            
    
    
