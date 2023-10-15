from ListSimple import ListSimple
from DoubleList import *
from Acciones import Actions

"""Empleados = DoubleList()

Empleados.addFirst(10)
Empleados.addFirst(11)
Empleados.addFirst(12)
Empleados.addFirst(13)

Empleados.display()"""




def cambiar_contra():
    print("1. CAMBIAR CONTRASEÑA DE USUARIO")
    a = input()
    
    if a=="1":
        passwordd = Actions.leerDatos()
        cc=input("ingrese la cedula: ")
        # Modificar la contraseña de un empleado (suponiendo que eres administrador)
        #empleado_a_modificar = "1007748337"
        nueva_password = input("Ingrese nueva contraseña: ")
        if passwordd.cambiar_contraseña(cc, nueva_password):
            print("\nContraseña modificada con éxito.\n")
        else:
            print("El empleado no fue encontrado o no eres administrador.")

        # Imprimir la lista
        passwordd.display()


cambiar_contra()

