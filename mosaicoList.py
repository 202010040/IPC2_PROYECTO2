from clases import ciudad, mosaico
class mosaico_list:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False
    def unir (self):
        if self.vacia() == False:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    def añadir (self, tipo, posx, posy,pasar,puntos):
        new = mosaico(tipo,posx, posy,pasar,puntos)
        if self.vacia():
            self.primero == self.ultimo == new
        else:
            temp = self.ultimo 
            self.ultimo = temp.siguiente = new
            self.ultimo.anterior = temp
    def recorrer(self):
        if self.vacia():
            print("Está vacia")
        else:
            temp = self.primero
            while temp != None:
                print(temp.tipo + " "+temp.posx + " "+temp.posy + " ")                          #Bucle a ejecutar
                temp = temp.siguiente
class ciudades_list:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False
    def unir (self):
        if self.vacia() == False:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    def añadir (self, nombre, filas, columnas, cadena):
        new = ciudad(nombre, filas, columnas, cadena)
        if self.vacia():
            self.primero == self.ultimo == new
            print (new)
        else:
            temp = self.ultimo 
            self.ultimo = temp.siguiente = new
            self.ultimo.anterior = temp
    def recorrer(self):
        if self.vacia() == True:
            print("Está vacia")
        else:
            temp = self.primero
            while temp != None:
                print(temp.nombre)   #Bucle a ejecutar
                temp = temp.siguiente