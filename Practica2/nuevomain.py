from Node import Node
from ListSimple import ListSimple
from DoubleNode import DoubleNode
from DoubleList import DoubleList


# Función para verificar las credenciales del usuario
def verificar_credenciales(identificacion, contraseña):
    with open("Practica2\Archivos proyecto\Password.txt", "r") as archivo:
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

# Llamada a la función principal
acceder_sistema()

# Datos existentes en forma de lista
data = [["Mike", 1105], ["Rob", 750], ["Paul", 720], ["Ana", 660], ["Rose", 500], ["Jack", 510]]

data2 = [1105,750,720,660,500,500,510,510]
data3 = [888, 100, 900, 500, 600, 200, 780, 100]

usuarios = [
    [69086825, "McLovin", "06-03-1981", "Hawaii", "Avenida Sur #10-75 Poblado Medellin", 1003291028, "mclovin.ejemplo@unal.edu.co"],
    [1000000000, "OVIDIO", "09-11-2000", "Colon", "Calle 2 #84b 63-11 robledo Medellin", 12345643, "marta.ejemplo@unal.edu.co"],
    [2345678901, "Fransisco", "18-12-1989", "Bucaramanga", "Avenida Norte #21-43 Barrio Granada Bucaramanga", 3210986312, "francisco.ejemplo@gmail.com"],
    [3210987654, "Cristian", "30-09-2003", "Barranquilla", "Carrera 7 #56-12 Barrio El Poblado Manizales", 3509087100, "cristian.ejemplo@gmail.com"],
    [4567890123, "Ximena", "12-05-1999", "Mocoa", "Calle 10 #45-32 Barrio El Prado Barranquilla", 3008871392, "ximena.ejemplo@gmail.com"],
    [5678901234, "Valentina", "03-11-1992", "Medellin", "Avenida 6 #78-90 Barrio La Floresta Cali", 3138209221, "valentina.ejemplo@gmail.com"],
    [8901234567, "Ana", "07-04-2002", "Manizales", "Calle 34 #65-21 Barrio El Bosque Cartagena", 3157628012, "ana.ejemplo@gmail.com"],
    [9876543210, "Sara", "22-07-2001", "Popayan", "Calle 45 #23-67 Barrio Los Alamos Medellin", 3118291091, "sara.ejemplo@gmail.com"]
]

# Crear una instancia de ListSimple
my_list = ListSimple()

# Agregar los elementos de data3 a la lista
for item in usuarios:
    my_list.addLast(item)
    
# Ordenar la lista utilizando Merge Sort, usando el segundo elemento como clave
sorted_list = my_list.merge_sort(key=lambda x: x[0])

# Imprimir la lista ordenada
sorted_list.display()






"""mylist.display()
print("------")
mylist.removeFirst()
mylist.display()
print(mylist.getSize())
"""
#newdata=["Jeni", 740]
#mylist.addFirst(newdata)

# Mostrar la lista enlazada
#print("----------------")
#mylist.display()  # Esto mostrará la lista enlazada en el orden en que se agregaron los datos

newdata= 730







