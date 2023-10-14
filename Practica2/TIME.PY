import time

timestamp = time.time()
fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print("Fecha y Hora Formateadas:", fecha_hora)
