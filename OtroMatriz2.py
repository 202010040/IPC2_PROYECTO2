from otro01 import nodo
from otroList import ListaEncabezado
import os
import webbrowser

class Nodo_Interno():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = x  
        self.y = y  
        self.arriba = None
        self.abajo = None
        self.derecha = None 
        self.izquierda = None  
        self.recorrida = 0
        self.atorada = False

class MatrizDispersa():
    def __init__(self, capa):
        self.capa = capa
        self.filas = ListaEncabezado('fila')
        self.columnas = ListaEncabezado('columna')


    def insert(self, pos_x, pos_y, caracter):
        nuevo = Nodo_Interno(pos_x, pos_y, caracter) 
       
        nodo_X = self.filas.getEncabezados(pos_x)
        nodo_Y = self.columnas.getEncabezados(pos_y)

        if nodo_X == None:
            nodo_X = nodo(pos_x)
            self.filas.InsertarEncabezado(nodo_X)

        if nodo_Y == None: 
            nodo_Y = nodo(pos_y)
            self.columnas.InsertarEncabezado(nodo_Y)

        if nodo_X.acceso == None: 
            nodo_X.acceso = nuevo
        else: 
            if nuevo.y < nodo_X.acceso.y: 
                nuevo.derecha = nodo_X.acceso              
                nodo_X.acceso.izquierda = nuevo
                nodo_X.acceso = nuevo
            else:
                temp : Nodo_Interno = nodo_X.acceso    
                while temp != None:                      
                    if nuevo.y < temp.y:
                        nuevo.derecha = temp
                        nuevo.izquierda = temp.izquierda
                        temp.izquierda.derecha = nuevo
                        temp.izquierda = nuevo
                        break;
                    elif nuevo.x == temp.x and nuevo.y == temp.y: 
                        break;
                    else:
                        if temp.derecha == None:
                            temp.derecha = nuevo
                            nuevo.izquierda = temp
                            break;
                        else:
                            temp = temp.derecha 
    
        if nodo_Y.acceso == None: 
            nodo_Y.acceso = nuevo
        else: 
            if nuevo.x < nodo_Y.acceso.x:
                nuevo.abajo = nodo_Y.acceso
                nodo_Y.acceso.arriba = nuevo
                nodo_Y.acceso = nuevo
            else:
                temp2 : Nodo_Interno = nodo_Y.acceso
                while temp2 != None:
                    if nuevo.x < temp2.x:
                        nuevo.abajo = temp2
                        nuevo.arriba = temp2.arriba
                        temp2.arriba.abajo = nuevo
                        temp2.arriba = nuevo
                        break;
                    elif nuevo.x == temp2.x and nuevo.y == temp2.y: 
                        break;
                    else:
                        if temp2.abajo == None:
                            temp2.abajo = nuevo
                            nuevo.arriba = temp2
                            break
                        else:
                            temp2 = temp2.abajo

    def graficarDibujo(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')

        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.y: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
#--------------------------------------VALIDA LOS COLORES ------------------------------------
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format(posy_celda, posx, pivote_celda.x, pivote_celda.y)
                elif pivote_celda.caracter == " ":
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(posy_celda, posx, pivote_celda.x, pivote_celda.y) 
                elif pivote_celda.caracter == "E":
                    contenido += '\n\tnode[label=" " fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format(posy_celda, posx, pivote_celda.x, pivote_celda.y)
                elif pivote_celda.caracter == "R":
                    contenido += '\n\tnode[label=" " fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format(posy_celda, posx, pivote_celda.x, pivote_celda.y)
                elif pivote_celda.caracter == "C":
                    contenido += '\n\tnode[label=" " fillcolor="blue" pos="{},-{}!" shape=box]i{}_{};'.format(posy_celda, posx, pivote_celda.x, pivote_celda.y)
                elif pivote_celda.caracter == "Y":
                    contenido += '\n\tnode[label=" " fillcolor="yellow" pos="{},-{}!" shape=box]i{}_{};'.format(posy_celda, posx, pivote_celda.x, pivote_celda.y)

                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.derecha.x, pivote_celda.derecha.y)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.derecha.x, pivote_celda.derecha.y)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.x, pivote.acceso.y)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.x, pivote.acceso.y)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.abajo.x, pivote_celda.abajo.y)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.abajo.x, pivote_celda.abajo.y) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.x, pivote.acceso.y)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.x, pivote.acceso.y)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        print("Listo")
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)

 #------------------------------ BUSCAR Y RECORRER----------------------------------

    def busqueda (self,x,y):
        temp:Nodo_Interno = self.filas.primero.acceso #Guarda un temporal
        if temp == None: # Ver si esta vacia
            print ("vacia")
        else:
            while temp.derecha != None: #MIENTRAS HAYA OTRA COLUMNA
                temp2 = temp #Guardo el encabezado de fila
                while temp.abajo != None:# MIENTRAS HAYA OTRA FILA
                    if temp.x == x and temp.y == y: #VALIDA LAS COORDENADAS X Y Y
                        return (temp)
                        break
                    else:
                        temp = temp.abajo #avanza en fila 
                temp = temp2.derecha#Avanza en columna
            return None # Si no se haya nada, se retorna vacio


    def Pasable (self,dron):
        if dron == None: # Ver si esta vacia
            print("Vacia")
            return False
        else: #Si no esta vacia se verifica si es pasable
            c1 = dron.caracter== "*" or dron.caracter == "M" or dron.caracter == "R" or dron.recorrida >= 2#Valida si es pasable o no
            if c1 == True:
                print("no pasable" ,dron.x,dron.y)
                return False
            else:
                return True


    def buscarCivil (self,x,y, entradax, entraday):
        civil = self.busqueda(x,y)
        entrada = self.busqueda(entradax,entraday)
        if civil == None or entrada == None: # Existe algun Civil?
            print("no existe")

        elif entrada != None:

            dron = entrada

            while (dron.x == civil.x and dron.y == civil.y) == False: #CUANDO EL DRON NO HAYA LLEGADO A LAS COORDENADAS DE CIVIL
                
                dron1 = dron.arriba #Obtiene las posiciones de los nodos aledaños
                dron2 = dron.abajo
                dron3 = dron.izquierda
                dron4 = dron.derecha

                #ESTA ATORADA SI YA NO HAY SALIDA
                atorada = self.Pasable(dron1) ==self.Pasable(dron2) == self.Pasable(dron3)==self.Pasable(dron4)== False
                if atorada == True:
                    dron.atorada = True
                    dron.caracter = " "
                    print ("atorada")
                    return None

                if dron.atorada == False: # solo puede avanzar si no se atora
                    if self.Pasable(dron1) == True:  #Revisa si se puede pasar
                        dron1.recorrida += 1
                        dron1.caracter = "Y" #Marcar como recorrido den el grafico
                        self.buscarCivil(x,y,dron1.x,dron1.y) #Avanzar

                    elif self.Pasable(dron2) == True:  #Revisa si se puede pasar
                        dron2.recorrida += 1
                        dron2.caracter = "Y" #Marcar como recorrido den el grafico
                        self.buscarCivil(x,y,dron2.x,dron2.y) #Avanzar

                    elif self.Pasable(dron3) == True:  #Revisa si se puede pasar
                        dron3.recorrida += 1
                        dron3.caracter = "Y" #Marcar como recorrido den el grafico
                        self.buscarCivil(x,y,dron3.x,dron3.y) #Avanzar

                    elif self.Pasable(dron4) == True:  #Revisa si se puede pasar
                        dron4.recorrida += 1
                        dron4.caracter = "Y" #Marcar como recorrido den el grafico
                        self.buscarCivil(x,y,dron4.x,dron4.y) #Avanzar    
                    else:
                        print ("No pasable")
                        return

            self.graficarDibujo("Prueba")
                