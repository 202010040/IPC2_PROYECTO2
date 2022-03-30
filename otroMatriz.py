
import os
import webbrowser
from otro01 import nodo
from otroList import ListaEncabezado 

class nodoInterno():
    def __init__(self,x,y,letra) : #Inicializar los nodos ortogonales
        self.letra = letra
        self.x = x
        self.y = y
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

class MatrizDispersa():
    def __init__(self,capa) : #Inicializar la matriz
        self.capa = capa
        self.filas = ListaEncabezado("fila") #Listas de encabezados x y y
        self.columnas = ListaEncabezado("columna")

    def insertar (self,x,y,letra):
        new = nodoInterno(x,y,letra)
        nodox = self.filas.getEncabezados(x)
        nodoy = self.filas.getEncabezados(y)

        if nodox == None: #Verifica si existe encabezado en la fila
            nodox = nodo(x)
            self.filas.InsertarEncabezado(nodox)

        if nodoy == None: #Verifica si existe encabezado en la fila
            nodoy = nodo(y)
            self.columnas.InsertarEncabezado(nodoy)
        
        if nodox.acceso == None: # -- comprobamos que el nodox no esta apuntando hacia ningun nodoInterno
            nodox.acceso = new
        else: # -- si esta apuntando, validamos si la posicion de la columna del new nodoInterno es menor a la posicion de la columna del acceso 
            if new.y < nodox.acceso.y: # F1 --->  NI 1,1     NI 1,3
                new.derecha = nodox.acceso              
                nodox.acceso.izquierda = new
                nodox.acceso = new
            else:
                #de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el new nodoInterno
                tmp : nodoInterno = nodox.acceso     # nodox:F1 --->      NI 1,2; NI 1,3; NI 1,5;
                while tmp != None:                      #NI 1,6
                    if new.y < tmp.y:
                        new.derecha = tmp
                        new.izquierda = tmp.izquierda
                        tmp.izquierda.derecha = new
                        tmp.izquierda = new
                        break;
                    elif new.x == tmp.x and new.y == tmp.y: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp.derecha == None:
                            tmp.derecha = new
                            new.izquierda = tmp
                            break;
                        else:
                            tmp = tmp.derecha 
                             #         nodoy:        C1    C3      C5      C6
                             # nodox:F1 --->      NI 1,2; NI 1,3; NI 1,5; NI 1,6;
                             # nodox:F2 --->      NI 2,2; NI 2,3; NI 2,5; NI 2,6;

        # ----- INSERTAR new EN COLUMNA
        if nodoy.acceso == None:  # -- comprobamos que el nodoy no esta apuntando hacia ningun nodoCelda
            nodoy.acceso = new
        else: # -- si esta apuntando, validamos si la posicion de la fila del new nodoCelda es menor a la posicion de la fila del acceso 
            if new.x < nodoy.acceso.x:
                new.abajo = nodoy.acceso
                nodoy.acceso.arriba = new
                nodoy.acceso = new
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el new
                tmp2 : nodoInterno = nodoy.acceso
                while tmp2 != None:
                    if new.x < tmp2.x:
                        new.abajo = tmp2
                        new.arriba = tmp2.arriba
                        tmp2.arriba.abajo = new
                        tmp2.arriba = new
                        break;
                    elif new.x == tmp2.x and new.y == tmp2.y: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = new
                            new.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo

        # TERMINA LA ISERCION DE NODOS
    
    def dibujar (self,nombre):
        texto = '''digraph G{
        node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
        edge[style = "bold"]
        node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        texto += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')
        
        #GRAFICAR LOS ENCABEZADOS DE LA FILA

        pivot = self.filas.primero #PRIMER BUCLE (ENCABEZADOS)
        i = 0
        while pivot != None:
            texto += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivot.id,i, pivot.id)
            pivot = pivot.siguiente
            i += 1

        pivot = self.filas.primero # SEGUNDO BUCLE
        while pivot.siguiente != None:
            print("bucle1")
            texto += '\n\tx{}->x{};'.format(pivot.id, pivot.siguiente.id)
            texto += '\n\tx{}->x{}[dir=back];'.format(pivot.id, pivot.siguiente.id)
            pivot = pivot.siguiente
        texto += '\n\traiz->x{};'.format(self.filas.primero.id)

        #GRAFICAR LOS ENCABEZADOS DE COLUMNA
        pivoty = self.columnas.primero
        j = 0
        while pivoty != None:
            print("bucle2")
            texto += '\n\ty{}->y{};'.format(pivoty.id, j, pivoty.id)
            pivoty = pivoty.siguiente
            j +=1
        pivoty = self.columnas.primero
        while pivoty.siguiente != None:
            texto += '\n\ty{}->y{};'.format(pivoty.id, pivoty.siguiente.id)
            texto += '\n\ty{}->y{}[dir=back];'.format(pivoty.id, pivoty.siguiente.id)
            pivoty = pivoty.siguiente
        texto += '\n\traiz->y{};'.format(self.columnas.primero.id)

        #GRAFICARLOS NODOS INTERNOS
        pivot = self.filas.primero
        k = 0
        while pivot != None:
            print("bucle3")
            inter : nodoInterno = pivot.acceso
            while inter != None:#"BUSCA UNA POSICION EN Y"
                pivoty = self.columnas.primero
                posyCelda = 0
                while pivoty != None :
                    print("bucle")
                    if pivoty.id == inter.y: break### CUIDADO CON ESTO
                    posyCelda+=1
                    pivoty = pivoty.siguiente
                
                #VALIDACIONES DE FIGURA

                if inter.letra == "*":
                    texto += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format(  posyCelda, k, inter.x, inter.y)
                else:
                    texto += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format(posyCelda, k, inter.x, inter.y) 
                
                inter =inter.derecha

            inter = pivot.acceso
            while inter != None:
                if inter.derecha != None:
                    texto += '\n\ti{}_{}->i{}_{};'.format(inter.x, inter.y,inter.derecha.x, inter.derecha.y)
                    texto += '\n\ti{}_{}->i{}_{}[dir=back];'.format(inter.x, inter.y, inter.derecha.x, inter.derecha.y)
                inter = inter.derecha #RECORRE LAS CELDAS

            texto += '\n\tx{}->i{}_{};'.format(pivot.id, pivot.acceso.x, pivot.acceso.y)
            texto += '\n\tx{}->i{}_{}[dir=back];'.format(pivot.id, pivot.acceso.x, pivot.acceso.y)
            pivot = pivot.siguiente
            k+=1
        
        pivot = self.columnas.primero #RECORRER NODOS DE LA MATRIZ EN COLUMNAS
        while pivot != None:
            inter: nodoInterno = pivot.acceso
            while inter != None:
                if inter.abajo != None:
                    texto += '\n\ti{}_{}->i{}_{};'.format(inter.x, inter.y, inter.abajo.x, inter.abajo.y)
                    texto +='\n\ti{}_{}->i{}_{}[dir=back];'.format(inter.x, inter.y,inter.abajo.x, inter.abajo.y) 
                inter = inter.abajo
            texto += '\n\ty{}->i{}_{};'.format(pivot.id, pivot.acceso.x, pivot.acceso.y)
            texto += '\n\ty{}->i{}_{}[dir=back];'.format(pivot.id, pivot.acceso.x, pivot.acceso.y)
            pivot = pivot.siguiente

        texto += '\n}' 
        #GENERAR EL DOT
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(texto)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)

    def graficarDibujo(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')

        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
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

        # --graficar nodos columna
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

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : nodoInterno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.y: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.letra == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.x, pivote_celda.y
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.x, pivote_celda.y
                    ) 
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
            pivote_celda : nodo = pivote.acceso
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
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)