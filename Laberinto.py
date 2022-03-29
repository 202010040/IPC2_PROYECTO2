creador = {
    3,2,2,2,9,
    1,2,2,2,9,
    1,1,2,1,9,
    1,1,2,4
}
# 3 representa el inicio del laberinto
# 4 representa el final
# 2 es un espacio en blanco
# 1 es pared
# 5 es piso trampa
# 6 es pared trampa
# 7 es etrada de tunel
# 8 es la salida del tunel
# 9 es una nueva linea
camino = ""
laberinto = []
linea = 0
laberinto.append([]) #Agrega una lista nueva para distinguir los niveles
respuestas = [] #Arreglo de respuestas
maxver = 0 #Maximos verticales
maxhor = 0 #Maximos Horizontales
piso = []

for imprimir in creador:
    if imprimir == 9:
        laberinto.append([]) #Cada vez que haya un 9 se crea una nueva linea
        linea += 1
    else:
        laberinto[linea].append(imprimir) #La fila añade un nuevo nodo 

for a in laberinto:
    maxver+=1 #Va iterando la cantidad de filas y columnas
    maxhor = 0#Por cada nueva fila, regresa a la columna 0
    for b in a:
        maxhor+=1# POr cada fila va iternado las columnas

def confirmar( vertical, horizontal, camino, salida, trampap, trampa,entrada):
    if (vertical == -1 or horizontal == -1 or vertical == maxver or horizontal == maxhor)


def dibujar():#Imprime el texto en consola
    impri = "\t\t\t\t\t\t\t"
    for imprimir in creador:
        if imprimir == 9:
            print (impri)
            impri = "\t\t\t\t\t\t\t"
        else:
            impri = str(str(impri)+str(imprimir))
    print(impri)

def caminos():
    num = 0
    for a in laberinto:
        piso.append([])
        for b in a:
            piso[num].append(False)
        num +=1

def setup ():
    vertical = 0
    horizontal = 0
    pos = False
    pos2 = False
    pos3 = False
    pos4 = False

    for a in laberinto:
        horizontal = 0 #Restea la horizontal
        for buscar in a:
            if buscar== 3:
                inicio = [vertical, horizontal] #Busca coordenadas verticales y horizontales
            if buscar== 4:
                final = [vertical, horizontal]
            if buscar== 7 and pos == False: #Busca tuneles
                entrada = [vertical, horizontal]
                pos = True
            elif pos == False:
                entrada = [-1,-1]
            if buscar == 8 and pos2 == False: # Busca tuneles 
                salida = [vertical, horizontal]
                pos2 == True
            elif pos2 == False:
                salida = [-1,-1]
            if buscar == 5 and pos3 == False: # Busca trampas de piso  
                trampap = [vertical, horizontal]
                pos3 == True
            elif pos3 == False:
                trampap = [-1,-1]
            if buscar == 6 and pos4 == False: # Busca trampas de pared 
                trampa = [vertical, horizontal]
                pos4 == True
            elif pos4 == False:
                trampa = [-1,-1]
            horizontal += 1 #Avanza horiznotalmente
        vertical += 1 # avanza verticalmente
    buscador = [inicio[0],inicio[1]]
    confirmar(inicio[0],inicio[1],camino,salida,trampa,trampap,entrada)
dibujar()