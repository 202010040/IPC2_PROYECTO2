class mosaico: #CADA UNO DE LOS MOSAICOS ES UN CUADRITO, LA LISTA ES LA MATRIZ
    def __init__(self, tipo, posx, posy,pasar,puntos ):
        self.tipo = tipo 
        self.posx = posx
        self.posy = posy
        self.pasar = pasar
        self.puntos = puntos
        self.siguiente = None
        self.anterior = None
class ciudad:
    def __init__(self, nombre, filas, columnas, cadena): #LA CIUDAD TENDRA UNA SOLA CADENA SEPARADA DE COLUMNAS
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.cadema = cadena