import xml.etree.ElementTree as ET
from clases import *
from mosaicoList import ciudades_list

def descifrar_arbol():
    ciudades = ciudades_list()

    file = 0
    arbol = ET.parse("prueba.xml")
    raiz = arbol.getroot()

    for listaCiudad in raiz.findall("listaCiudades"):
        Nombre = ""      # VARIABLE PARA GUARDAR EL NOMBRES DE LA CIUDAD
        filas = 0        #VARIABLE PARA GUARDAR LAS FILAS DE LA CIUDAD
        columnas = 0     #VARIABLE PARA GUARDAR LAS COLUMNAS DE LA CIUDAD
        cadena = ""      #UNA CADENA QUE IRÁ CONCATENANDO PARA MANDAR UNA CADENA DE TEXTO A LA CIUDAD
        for ciudad in listaCiudad.findall("ciudad"):
            for nombre0 in ciudad.findall("nombre"):
                filas = (nombre0.get("filas"))
                columnas =  (nombre0.get("columnas"))
                Nombre = str(nombre0.text)
            for fila in ciudad.findall("fila"):
                textFila =  ((str(fila.text)).replace('"','')) #Elimina las comillas
                cadena += (textFila) # CONCATENA EL TEXTO DE CADA FILA
                print(cadena, Nombre)
        ciudades.añadir (Nombre, filas, columnas, cadena,)
    ciudades.recorrer()

descifrar_arbol()