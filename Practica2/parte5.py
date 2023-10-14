from DoubleNode import DoubleNode
from DoubleList import DoubleList
from ListSimple import ListSimple
from QueueQueue import Queue
from Node import Node

# Crear una instancia de la lista doble
bandeja_de_entrada = DoubleList()
mensajes_leidos = Queue()

# Abrir el archivo para lectura
with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/1007748337BA.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        bandeja_de_entrada.addFirst(linea.strip().split(','))
        
# Abrir el archivo para lectura
with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/1007748337ML.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        mensajes_leidos.enqueue(linea.strip().split(','))

def guardarDatoss():
    # Abrir el archivo para escritura
    with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/1007748337-BA.txt", "w") as archivo:
        current_node = bandeja_de_entrada.first()
        while current_node:
            data = current_node.getData()  # Asumiendo que cada nodo almacena datos en un atributo "data"
            archivo.write(','.join(data) + '\n')
            current_node = current_node.getNext()
    
    # Abrir el archivo para escritura
    with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/1007748337-ML.txt", "w") as archivo:
        while not mensajes_leidos.isEmpty():
            data = mensajes_leidos.dequeue()
            
            # Obtener los datos del nodo doble
            datos = data.getData()
            
            
            # Escribir los datos en el archivo
            archivo.write(','.join(datos) + '\n')


def mostrar_mensajes(bandeja_de_entrada, mensajes_leidos):
    current = bandeja_de_entrada.first()
    
    # Verificar si la bandeja de entrada está vacía
    if current is None:
        print("La bandeja de entrada está vacía.")
        return
    
    mensajes = []  # Almacenar los mensajes en una lista
    
    # Crear una lista de mensajes numerados
    mensaje_numero = 1
    while current is not None:
        fecha, correo, remitente, mensaje = current.getData()
        mensajes.append([fecha, correo, remitente, mensaje])
        print(f"{mensaje_numero}. Correo: {correo}, Remitente: {remitente}, Fecha: {fecha}")
        current = current.getNext()
        mensaje_numero += 1
    
    # Solicitar al usuario que seleccione un mensaje
    while True:
        try:
            seleccion = int(input("Ingrese el número del mensaje que desea ver (0 para salir): "))

            if seleccion == 0:
                break  # El usuario quiere salir
            elif 1 <= seleccion <= len(mensajes):
                # El usuario seleccionó un mensaje válido, mostrar el mensaje completo
                fecha, asunto, remitente, mensaje = mensajes[seleccion - 1]
                print(f"Fecha: {fecha}\nAsunto: {asunto}\nRemitente: {remitente}\nMensaje: {mensaje}\n")
                
                creardat= mensajes[seleccion-1]
                #print(creardat)
                msmremo = bandeja_de_entrada.search_node(creardat)
                
                
                bandeja_de_entrada.remove(msmremo)
                
                msmnode = Node(msmremo.getData())
                
                mensajes_leidos.enqueue(msmnode)
                mensajes_leidos.display()
            

                print("Mensaje marcado como leído y movido a mensajes leídos.")
                break
            else:
                print("Número de mensaje no válido. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
        # Actualizar current para el siguiente ciclo del bucle
        current = bandeja_de_entrada.first()

def ejecutar():
    
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
            #bandeja_de_entrada.display()
            bandeent= mostrar_mensajes(bandeja_de_entrada, mensajes_leidos)
            
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
            guardarDatoss()
        
        elif opcion=="6":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


ejecutar()



# Llamar a la función para mostrar los mensajes
#mostrar_mensajes(bandeja_de_entrada)
