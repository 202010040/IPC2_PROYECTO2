from OtroMatriz2 import MatrizDispersa

matriz =MatrizDispersa(0)

def insertaTodo():
    with open('Figura.txt') as archivo:
        l=0
        c=0
        lineas=archivo.readlines()
        for linea in lineas:
            columnas=linea
            l+=1
            for col in columnas:
                if col != '\n':
                    c+=1
                    matriz.insert(l,c,col)
            c=0 #arreglar con una lista de listas de letras
        matriz.buscarCivil(3,16,3,10,3,10)
insertaTodo()
#insertaSeleccion()s