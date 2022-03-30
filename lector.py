import xml.etree.ElementTree as ET
from clases import *
from mosaicoList import ciudades_list

def descifrar_arbol():
    ciudades = ciudades_list()

    fila = 0
    arbol = ET.parse("prueba.xml")
    raiz = arbol.getroot()

    for listaCiudad in raiz.findall("listaCiudades"):
        for ciudad in listaCiudad.findall("ciudad"):
            cadena = ""
            for fila in ciudad.findall("fila"):
                textFila =  ((str(fila.text)).replace('\"','')) #Elimina las comillas
                cadena += (textFila.strip()) # CONCATENA EL TEXTO DE CADA FILA
                cadena += '\n'
            return(cadena)

descifrar_arbol()