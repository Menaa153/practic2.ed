
from Acciones import Actions
from DoubleList import DoubleList
from ListSimple import ListSimple
from QueueQueue import Queue
from StackList import StackList
import datetime

def main():
    
    
    print("Bienvenido a la Practica 2 de ED\n")
    
    while True:
        cedula = input("Digite su numero de Cedula: ")
        password = input("Digite su contraseña: ")
        
        validar = Actions.verificar_credenciales(cedula, password)
        if validar:
            print(f"Acceso concedido como {validar}.")
            BD, BA, ML =  Actions.leerdatosoptimo2(cedula)
            break
        else:
            print("Acceso denegado. Credenciales incorrectas. Intente nuevamente")
    
    if validar == "empleado":
        print("sos un esclavo")
    while True:
        
        print("\nMenú:")
        print("1. Revisar bandeja de entrada")
        print("2. Ver mensajes leidos")
        print("3. Redactar nuevo MSM")
        print("4. Borradores")
        print("5. Guardar datos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            
            Actions.mostrar_mensajes(BA, ML)
            
            
        elif opcion == "2":
            if ML.isEmpty():
                print("No tienes mensajes leidos")
            else: ML.display()
        
        elif opcion == "3":
            
            
            ccuserdest = input("Ingrese CC del destinatario: ")
            asuntomsm = input("Asunto de mensaje: ")
            mensaje = input("Mensaje a enviar: ")
            fechaENV = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            
            msmenviar = [fechaENV, cedula, asuntomsm, mensaje]
            
            while True:
            
                print("\nMenú:")
                print("1. Guardar como borrador")
                print("2. Descartar")
                print("3. Enviar")
                print("4. Salir")
                
                opcion = input("¿Que deseas hacer?: ")
                
                if opcion == "1":
                    BD.push(msmenviar)
                    BD.display()
                    print("Mensaje guardado como borrador.")
                    break
                
                elif opcion == "2":
                    break
                
                elif opcion == "3":
                    
                    BADest = Actions.leerBADestinatario(ccuserdest)
                    BADest.addFirst(msmenviar)
                    BADest.display()
                    print("Mensaje enviado con exito")
                    break
                
                
                else:
                    print("Opción no válida. Intente de nuevo.")
            
            
        elif opcion == "4":
            if BD.isEmpty():
                print("No tienes borradores :)")
            else:
                
                while True:
                    
                    bdexistentes = BD.top()
                    if bdexistentes == None:
                        print("No tines mas borradores")
                        break
                    
                    else:
                        print(BD.top())
                    
                        print("\n")
                        print("1. Descartar")
                        print("2. Enviar")
                        print("3. Salir")
                        
                        opcion = input("¿Que deseas hacer?: ")
                        
                        if opcion == "1":
                            
                            BD.pop()
                            print("El mensaje ha sido descartado")
                        
                        elif opcion == "2":
                            
                            ccdes = input("Confirme CC del destinatario: ")
                            BADest = Actions.leerBADestinatario(ccdes)
                            BADest.addFirst(BD.top())
                            BADest.display()
                            BD.pop()
                            
                            print("Mensaje enviado con exito.")
                            
                        elif opcion == "3":
                            break
                    
                else:
                    print("Opción no válida. Intente de nuevo.")
        
        elif opcion == "5":
            pass
        
        elif opcion=="6":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main = main()