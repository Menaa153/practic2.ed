

def main():
    registro_usuarios = RegistroUsuarios(capacidad_maxima=8)
    registro_usuarios.leerDatos()
    
    while True:
        
        print("\nMenú:")
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