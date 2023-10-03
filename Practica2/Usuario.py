from Direccion import Direccion
from Fecha import Fecha

class Usuario:
    def __init__(self, id, nombre, fecha_nac, ciudad_nac, direccion, telefono, email):
        #Datos necesarios para identificar al usuario
        self._id = id
        self._nombre = nombre
        self._fechaNac = Fecha
        self._ciudadNac = ciudad_nac
        self._direccion = Direccion
        self._telefono = telefono
        self._email = email
    
    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getFechaNac(self):
        return self._fechaNac
    def setFechaNac(self, _fechaNac):
        self._fechaNac = fechaNac
    
    def setCiudadNac(self):
        return self.ciudadNac
    def setCiudadNac(self, ciudadNac):
        self._ciudadNac = ciudadNac
    
    def getDireccion(self):
        return self._direccion
    def setDireccion(self, direccion):
        self._direccion = direccion
    
    def getTelefono(self):
        return self._telefono
    def setTelefono(self, telefono):
        self._telefono = telefono
    
    def getEmail(self):
        return self._email
    def setEmail(self, email):
        self._email = email
    
    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Fecha de Nacimiento: {self._fechaNac}, Ciudad de Nacimiento: {self._ciudadNac}, Dirección: {self._direccion}, Teléfono: {self._telefono}, Email: {self._email}"

