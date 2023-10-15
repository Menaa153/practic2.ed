from Node import Node
from ListSimple import ListSimple
from DoubleNode import DoubleNode
from DoubleList import DoubleList

def leerdatosoptimo():
    ccempleados=[]
    ext = ["B", "BA", "ML"]
    with open("Practica2\Archivos proyecto\Empleados.txt", "r") as archivo:
        for linea in archivo:
            info = linea.strip().split(',')
            ccempleados.append(info[1])
    
    for usuario in ccempleados:
        for extension in ext:
            archivo_path = f"C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/{usuario}{extension}.txt"
            try:
                with open(archivo_path, "r") as archivo:
                    lineas = archivo.readlines()
                    # Procesa las líneas del archivo como desees
                    for linea in lineas:
                        pass
                        # Haz algo con las líneas, por ejemplo, almacénalas en una estructura de datos
                    print(f"ARCHIVO {usuario}{extension} LEIDO")
            except FileNotFoundError:
                # Maneja el caso en el que el archivo no existe
                print(f"El archivo {usuario}{extension} no existe.")

