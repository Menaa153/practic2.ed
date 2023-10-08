from Node import Node
from ListSimple import ListSimple
from DoubleNode import DoubleNode
from DoubleList import DoubleList


# Función para verificar las credenciales del usuario
def verificar_credenciales(identificacion, contraseña):
    with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Archivos proyecto/Password.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split()  # Dividir la línea por espacios
            if len(partes) == 3:
                cedula, clave, rol = partes
                if identificacion == cedula and contraseña == clave:
                    return rol
    return None

# Función principal para el acceso al sistema
def acceder_sistema():
    print("Bienvenido al sistema de autenticación.")
    identificacion = input("Ingrese su número de identificación: ")
    contraseña = input("Ingrese su contraseña: ")
    
    rol = verificar_credenciales(identificacion, contraseña)
    if rol:
        print(f"Acceso concedido como {rol}.")
        # Aquí puedes realizar las acciones específicas del usuario (empleado o administrador)
    else:
        print("Acceso denegado. Credenciales incorrectas.")



def main():
    
    while True:
        acceder_sistema()
        
        
        print("/nMenú:")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Guardar Usuario(s) en CSV")
        print("5. Mostrar Usuarios")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            usuarios = registro_usuarios.agregar_usuario()
            
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