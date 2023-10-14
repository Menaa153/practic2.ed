
from Acciones import Actions
from DoubleList import DoubleList
from ListSimple import ListSimple
from QueueQueue import Queue
from StackList import StackList

def main():
    
    
    print("Bienvenido a la Practica 2 de ED\n")
    
    while True:
        cedula = input("Digite su numero de Cedula: ")
        password = input("Digite su contraseña: ")
        
        validar = Actions.verificar_credenciales(cedula, password)
        if validar:
            print(f"Acceso concedido como {validar}.")
            
            break
        else:
            print("Acceso denegado. Credenciales incorrectas. Intente nuevamente")
    
    
    while True:
        
        print("\nMenú:")
        print("1. Revisar bandeja de entrada")
        print("2. Ver mensajes leidos")
        print("3. Mensaje de borradores")
        print("4. Enviar mensaje")
        print("5. Guardar datos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            Actions.leerdatosoptimo2(cedula)
            #Actions.mostrar_mensajes()
            
        elif opcion == "2":
            id = int(input('Ingrese el ID del Usuario a buscar: '))
            usuarios = registro_usuarios.buscar_usuario(id)
            if usuarios==None:
                print('El Usuario no existe')
            else:
                print(usuarios)
        
        elif opcion == "3":
            id = int(input('Ingrese el ID del usuario a eliminar: '))
            usuarios = registro_usuarios.eliminar_usuario(id)
        
        elif opcion == "4":
            guardarDatos= registro_usuarios.guardarDatos()
        
        elif opcion == "5":
            usuarios = registro_usuarios.getUsuarios()
            for usuario in usuarios:
                print(f"{usuario}")
        
        elif opcion=="6":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main = main()