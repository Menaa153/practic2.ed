
from DoubleList import DoubleList
from ListSimple import ListSimple
from QueueQueue import Queue
from StackList import StackList
import datetime
class Actions:
    
    def leerDatos():
        
        Empleados = DoubleList()
        Password = DoubleList()
        
        with open("Practica2\Archivos proyecto\Password.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                Password.addFirst(linea.strip())
        
        return Password
    
    def agregar_usuario(self):
        # Se verifica que haya espacio para agregar un usuario
        if len(self._usuarios) < self._capacidad_maxima:
            
            # Solicita id para verificar si el usuario existe o no, si no existe se procedera a pedir los datos de el usuario para registrarlo
            id = int(input("Ingrese el ID del Usuario: "))
            if self.buscar_usuario(id)==None:
                # Solicita los datos del usuario al usuario
                nombre = input("Ingrese el nombre del Usuario: ")
                ciudad_nac = input('Ingrese la ciudad donde nació: ')
                
                # Solicita datos de la fecha de nacimiento del usuario
                dd = input("Ingrese el día de nacimiento (dd): ")
                mm = input("Ingrese el mes de nacimiento (mm): ")
                aaaa = input("Ingrese el año de nacimiento (aaaa): ")
                
                # Crea una instancia de la clase Fecha con los datos ingresados por el usuario anteriormente
                fecha_usuario = Fecha(dd=dd, mm=mm, aaaa=aaaa)
                
                # Solicita datos de dirección del usuario
                calle = input("Ingrese la calle: ")
                noCalle = input("Ingrese el número de la calle: ")
                nomenclatura = input("Ingrese la nomenclatura: ")
                barrio = input("Ingrese el barrio: ")
                ciudad = input("Ingrese la ciudad: ")
                
                # Crea una instancia de la clase Direccion con los datos ingresados por el usuario anteriormente
                direccion_usuario = Direccion(calle=calle, noCalle=noCalle, nomenclatura=nomenclatura, barrio=barrio, ciudad=ciudad)
                
                # Solicita los otros datos del usuario
                telefono = input("Ingrese el teléfono del usuario: ")
                email = input("Ingrese el Email del usuario: ")
                
                # Crea una instancia de la clase Usuario utilizando los objetos ya obtenidos
                usuario = Usuario(id=id, nombre=nombre, fecha_nac=fecha_usuario, ciudad_nac=ciudad_nac, direccion=direccion_usuario, telefono=telefono, email=email)
                
                self._usuarios.append(usuario) #se agrega el usuario a la lista de usuarios
                self._usuarios.sort(key=lambda u: u._id) #se ordena los usuarios de forma ascendente segun su ID
                print("¡Usuario registrado correctamente!")
            else:
                print("Ya existe un usuario con ese ID.")
        else:
            print("El registro está lleno, no se puede agregar más usuarios.")
    
    def buscar_usuario(self, id):
        for i in self._usuarios:
            if i._id==id:
                return i # Devuelve el usuario si se encuentra
        return None # Devuelve None solo si no se encuentra 
    
    
    def eliminar_usuario(self, id):
        usuario = self.buscar_usuario(id)
        if usuario:
            self._usuarios.remove(usuario)
            print("¡Usuario eliminado con exito!")
        
        else:
            print("No se encontró un usuario con esa identificación.")
    
    
    
    def verificar_credenciales(identificacion, contraseña):
        with open("Practica2\Archivos proyecto\Password.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split()  # Dividir la línea por espacios
                if len(partes) == 3:
                    cedula, clave, rol = partes
                    if identificacion == cedula and contraseña == clave:
                        return rol
        return None

    def lecturadatos():
        
        # Crear una instancia de la lista doble
        bandeja_de_entrada = DoubleList()
        mensajes_leidos = Queue()

        # Abrir el archivo para lectura
        with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/1007748337-BA.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                bandeja_de_entrada.addFirst(linea.strip().split(','))
                
        # Abrir el archivo para lectura
        with open("C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/1007748337-ML.txt", "r") as archivo:
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
                # Convierte data a una lista si no lo es
                dataa = list(data)
                archivo.write(','.join(dataa) + '\n')
                


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
                    
                    msmremo = bandeja_de_entrada.search_node(creardat)
                    
                    
                    bandeja_de_entrada.remove(msmremo)
                    mensajes_leidos.enqueue(msmremo)
                    mensajes_leidos.display()

                    print("Mensaje marcado como leído y movido a mensajes leídos.")
                    break
                else:
                    print("Número de mensaje no válido. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")
            
            # Actualizar current para el siguiente ciclo del bucle
            current = bandeja_de_entrada.first()
    
    def leerdatosoptimo2(cedula):
        ccempleado = cedula
        ext = ["B", "BA", "ML"]
        BD = StackList()
        BA = DoubleList()
        ML = Queue()
        
        #for usuario in ccempleado:
        for extension in ext:
            archivo_path = f"C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/{ccempleado}{extension}.txt"
            try:
                with open(archivo_path, "r") as archivo:
                    lineas = archivo.readlines()
                    # Procesa las líneas del archivo como desees
                    for linea in lineas:
                        if extension == ext[0]:
                            BD.push(linea)
                        if extension == ext[1]:
                            BA.addFirst(linea.strip().split(','))
                        if extension == ext[2]:
                            ML.enqueue(linea.strip().split(','))
                    print(f"ARCHIVO {ccempleado}{extension} LEIDO")
            except FileNotFoundError:
                # Maneja el caso en el que el archivo no existe
                print(f"El archivo {ccempleado}{extension} no existe.")
        
        return BD, BA, ML
    
    def leerBADestinatario(cedula):
        BAA = DoubleList()
        archivo_path = f"C:/Users/SEGATOP/Documents/Estructura de datos/Practica2/Empleados/{cedula}BA.txt"
        with open(archivo_path, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                BAA.addLast(linea.strip().split(','))
            print(f"ARCHIVO {cedula}BA LEIDO")
        return BAA
    
    
    
    def RedactarMSM():
        ccuserdest = input("Ingrese CC del destinatario: ")
        asuntomsm = input("Asunto de mensaje: ")
        mensaje = input("Mensaje a enviar: ")
        while True:
        
            print("\nMenú:")
            print("1. Guardar como borrador")
            print("2. Descartar")
            print("3. Enviar")
            print("4. Salir")
            
            opcion = input("¿Que deseas hacer?: ")
            
            if opcion == "1":
                pass
                
            elif opcion == "2":
                pass
            
            elif opcion == "3":
                BADest = Actions.leerBADestinatario(ccuserdest)
                fechaENV = datetime.datetime.now().strftime("%d-%m-% %H:%M:%S")
                BADest.addFirst([fechaENV, "Ana Isabel", asuntomsm, mensaje])
                
                BADest.display()
                
            else:
                print("Opción no válida. Intente de nuevo.")