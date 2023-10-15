from StackList import StackList
import datetime


class borrador:
    def redactar_mensaje():
        while True:
            cedula_destinatario = input("Ingrese la cédula del destinatario: ")
            titulo = input("Ingrese el título del mensaje: ")
            mensaje = input("Ingrese el cuerpo del mensaje: ")
            fechaENV = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            nuevo_mensaje = [fechaENV,cedula_destinatario, titulo, mensaje]

            opcion = input("¿Guardar como borrador, descartar o enviar? (g/d/e): ")

            if opcion.lower() == 'g':
                borrador.guardar_como_borrador(nuevo_mensaje)
                
                
            elif opcion.lower() == 'd':
                descartar_borrador()
                
                
            elif opcion.lower() == 'e':
                nuevo_mensaje.enviar()
                print("Mensaje enviado con éxito!")

            continuar = input("¿Desea redactar otro mensaje? (s/n): ")
            if continuar.lower() != 's':
                break

    def guardar_como_borrador(mensaje):
        BD = StackList()
        
        BD.push(mensaje)
        print("Mensaje guardado como borrador.")


    def descartar_borrador(self):
        if self.borradores:
            
            
            
            
            borrador_descartado = self.borradores.pop()
            print(f"Borrador descartado:\nDestinatario: {borrador_descartado.cedula_destinatario}\nTítulo: {borrador_descartado.titulo}\nCuerpo: {borrador_descartado.cuerpo}")
        else:
            print("No hay borradores para descartar.")

    def enviar_borrador(self):
        if self.borradores:
            ultimo_borrador = self.borradores[-1]
            print(f"Último borrador:\nDestinatario: {ultimo_borrador.cedula_destinatario}\nTítulo: {ultimo_borrador.titulo}\nCuerpo: {ultimo_borrador.cuerpo}")

            decision = input("¿Desea descartar (d) o enviar (e) el último borrador? ")
            if decision.lower() == 'd':
                self.descartar_borrador()
            elif decision.lower() == 'e':
                ultimo_borrador.enviar()
        else:
            print("No hay mensajes en borrador.")

    def ver_borradores(self):
        if self.borradores:
            print("Mensajes en borrador:")
            for idx, borrador in enumerate(self.borradores, 1):
                print(f"{idx}. Destinatario: {borrador.cedula_destinatario}, Título: {borrador.titulo}, Cuerpo: {borrador.cuerpo}")
        else:
            print("No hay mensajes en borrador.")


    def obtener_ultimo_borrador(self):
        if self.borradores:
            return self.borradores[-1]
            decision = input("¿Desea descartar (d) o enviar (e) el último borrador? ")
            if decision.lower() == 'd':
                self.descartar_borrador()
            elif decision.lower() == 'e':
                ultimo_borrador.enviar()
            else:
                print("No hay mensajes en borrador.")

        else:
            print("No hay mensajes en borrador.")
            return None

# Uso del sistema
#empleado = Empleado()
borrador.redactar_mensaje()
#empleado.ver_borradores()

#ultimo_borrador = empleado.obtener_ultimo_borrador()